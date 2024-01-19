<template>
    <ManagerNavbar />
    <div class="enter">
        
        <!-- <form action="/manager" method="POST"> -->
        <form @submit.prevent="submitForm" class="form1">
            <input v-model="newCategory" type="text" name="data" required placeholder="Add new Category">
            <button class="btn btn-primary mb-2" @click.prevent="addCategory()" type="submit">Submit</button>
        </form>
        
    </div>
    <managercreate />
</template>

<script>
console.log("heyyyy")
import axios from 'axios';
import ManagerNavbar from '../../components/navbar/managernavbar.vue'
import Managercreate from '@/components/managercreate/managercreate.vue';
// import editcategory from '@/components/managercreate/editcategory.vue';
// import Rough from 'rough.vue'


export default {
    name: 'Managerdashbord',
    showComponent : false,
    // props: ['username', 'password'], 
    components:{
        ManagerNavbar,
        Managercreate,
        // Rough
    },
    computed:{
        localmanager(){
            console.log(localStorage.getItem('username'))
            return localStorage.getItem('username')
        }
    },
    data() {
    return {
      newCategory: '',

    };
  },
  methods: {
    check() {
        const currentUrl = window.location.href;
        const urlSegments = currentUrl.split("/");
        this.lastSegment = urlSegments[urlSegments.length - 1];
      try {
        let access_token = localStorage.getItem(`access_token_${this.lastSegment}`);
        if (access_token === null) {
          alert('Missing or invalid token')
          this.$router.push('/login')
          return false;
        } else {
          axios.defaults.headers.common["Authorization"] =
            "Bearer " + access_token;
          return true;
        }
      } catch (error) {
        console.log(error);

        if (error.response.status === 401) {
          console.log("refreshing....");
          refreshAccessToken(this.lastSegment).then((result) => {
            if (result == "success") {
              this.check();
            } else {
              return false;
              //  this.$router.push('/login')
            }
          });
        } else if (error.response) {
          console.error(error);
          alert("An error occurred while fetching the followers data.");
        }
      }
    },
    addCategory() {
      const categoryValue = this.newCategory;
      if(categoryValue != ""){
        // window.location.reload();
        console.log('New Category:',categoryValue );
        axios.post('http://127.0.0.1:5000/manager/addcat',{
            data:categoryValue,
            person:localStorage.getItem('username')
        })
        .then(response => {
            // if (response === "pending"){
            //     console.log("request sent to admin")
            //     alert("request sent to admin")
            //     // newCategory = this.newCategory
            // }
            if (response.data === "sent"){
                console.log(response.data);
                // newCategory = this.newCategory
                // window.location.reload();
                alert("request sent to admin")
            }
            else if(response.data === "duplicate"){
                // e.preventDefault();
                console.log(response.data,"duplicate");
                alert("can't have duplicate catogery")
            }            
            console.log("posted")
            this.newCategory = '';

        })
        .catch(error => {
            console.error(error);
        });
    }
    }
}
};
</script>

<style scoped>
*{
    overflow-x: hidden;
}
* {
  font-family: Comic Sans MS;
  font-weight: bolder;
}
.enter{
    display: flex;
  justify-content: center;
  align-items: center;
}
.form1{
    justify-content: center;
  align-items: center;
    display: flex;
    width: 80%;
}
input{
    width: 50%;
    resize: vertical;
    padding:15px;
    border-radius:15px;
    border:0;
    margin: 10px;
    box-shadow:4px 4px 10px rgb(55, 54, 54);
}
button{
    position: relative;
    top: 5px;
    height: 50px;
    background-color: #040490e5;
    box-shadow:4px 4px 10px rgb(55, 54, 54);
}
</style>