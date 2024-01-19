<template>
  <div>
    <div class="allcategory">
      <editcategory
        :categoryname="categoryname"
        v-if="showComponent"
        @close="edit"
      />
      <!-- <editcategory :categoryname="categoryname"  v-if="ls===true"/> -->
      <div
        @click="item.id;"
        class="card"
        v-for="item in allcategories"
        :key="item.id"
        :todo="item"
        :id="`todo-${item.id}`"
      >
        <div class="categoryname">
          <h3>{{ item.name }}</h3>
        </div>
        <br />
        <div
          style="
            width: 100%;
            position: relative;
            display: flex;
            justify-content: center;
            align-items: center;
          "
        >
          <button
            class="btn btn-outline-primary"
            @click="navigateToadditem(item.name, item.id)"
          >
            <h3>ADD</h3>
          </button>
        </div>
        <button
          style="padding: 3px; margin: 8px; position: relative; "
          class="btn btn-outline-primary"
          @click="edit(item.name)"
        >
          <h4>Edit</h4>
        </button>
        <button
          style="padding: 3px; margin: 8px; position: relative;"
          class="btn btn-outline-primary"
          @click="remove(item.id)"
        >
          <h4>delete</h4>
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import newcategory from "@/components/managercreate/managercreate.vue"; // Adjust the import path as needed
import editcategory from "./editcategory.vue";
import refreshAccessToken from "../../utils/refresh_token.js";
console.log("additem");
localStorage.setItem("showComponent", false);

export default {
  name: "managercreate",

  components: {
    editcategory,
    newcategory,
  },
  data() {
    return {
      showComponent: false,
      allcategories: [],
      categoryname: "",
      categoryid: "",
      ls: "",
    };
  },
  mounted() {
    if (this.check()) {
      this.get_data();
    }
  },

  methods: {
    check() {
      const currentUrl = window.location.href;
        const urlSegments = currentUrl.split("/");
        this.lastSegment = urlSegments[urlSegments.length - 1];
      try {
        console.log(this.lastSegment)
        let access_token = localStorage.getItem(`access_token_${this.lastSegment}`);
        console.log(access_token);
        if (access_token === null) {
          console.log("it is false");
          // alert('Missing or invalid token')
          // this.$router.push('/login')
          return false;
        } else {
          axios.defaults.headers.common["Authorization"] =
            "Bearer " + access_token;
          console.log("it is not tru");
          return true;
        }
      } catch (error) {
        console.log("check error");
        console.log(error);

        if (error.response.status === 401) {
          console.log("refreshing...");
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
    navigateToadditem(name, id) {
      this.categoryid = id;
      this.$router.push(`/manager/${this.lastSegment}/${name}`);
      console.log(name);

      axios
        .get(`http://127.0.0.1:5000/manager/${name}`, { data: id })
        .then((response) => {
          console.log("item posted");
          if (response.data === "sucessful") {
            console.log(response.data);
            newCategory = this.newCategory;
            console.log("reloded");
          } else if (response.data === "duplicate") {
            console.log(response.data, "duplicate");
            alert("can't have duplicate catogery");
          } else {
            console.log("no response");
          }
        })
        .catch((error) => {
          console.log("error");
          console.error(error);
        });
    },
    edit(name) {
      this.categoryname = name;
      this.showComponent = !this.showComponent;
      localStorage.setItem("showComponent", this.showComponent);
      this.ls = localStorage.getItem("showComponent");
      console.log(
        "Button clicked, showComponent is now:",
        localStorage.getItem("showComponent")
      );
      // console.log(showComponent)
    },
    remove(id_) {
      // const id_ = id;
      // if(categoryValue != ""){
      // window.location.reload();
      console.log("Category id :", id_);
      console.log(localStorage.getItem("username"));
      axios
        .delete(
          `http://127.0.0.1:5000/manager/addcat/${id_}/${localStorage.getItem(
            "username"
          )}`
        )
        .then((response) => {
          console.log("deleted");
          console.log(response.data);
          if (response.data == "successful") {
            console.log(response.data);
            window.location.reload();
            console.log("reloded");
          } else if (response.data === "duplicate") {
            console.log(response.data, "duplicate");
            alert("Request already sent");
          } else if (response.data === "sent") {
            alert("request sent to admin");
          }
        })
        .catch((error) => {
          console.error(error);
        });
      // }
    },
    idExists(idToCheck) {
      return this.allcategories.some((item) => item.id === idToCheck);
    },
    handleButtonClick(clickedId) {
      console.log(`Button category_id-${clickedId}`);
    },
    get_data() {
      axios
        .get("http://127.0.0.1:5000/manager/addcat")
        .then((response) => {
          console.log("getting");
          this.allcategories = response.data;
        })
        .catch((error) => {
          console.error("Error fetching data:::", error);
        });
    },
  },
};
</script>

<style scoped>
@import url("https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css");

*,
*::before,
*::after {
  box-sizing: border-box;
}

* {
  font-family: Comic Sans MS;
  font-weight: 500;
  text-align: center;
}

body {
  text-align: center;
  background-color: #e2e1e0;
  overflow-x: hidden;
}

.categoryname {
  width: 250px;
  height: 35%;
}

.card {
  /* justify-content: center; */
  position: relative;
  display: inline-block;
  border-radius: 10px;
  padding: 2rem;
  /* width: 300px; */
  min-width: 25%;
  max-width: 80%;
  background: #040490e5;
  margin: 2rem;
  color: white;
  transition: all 0.4s ease;
  box-shadow: 0 1px 3px rgba(1, 1, 1, 0.12), 0 1px 2px rgba(0, 0, 0, 0.24);
}

.card:hover {
  transform: scale(103%);
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1), 0 10px 10px rgba(0, 0, 0);
}

.card i {
  font-size: 200%;
}

.card .card-title {
  font-size: 180%;
}

.card .card-text {
  font-size: 120%;
}

.card a {
  text-decoration: none;
  position: absolute;
  /* margin-bottom: 1.5rem; */
}

.card .btn-holder {
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
}

.btn {
  border: 1px solid transparent;
  background-image: none;
  display: inline-block;
  cursor: pointer;
  margin-bottom: 0;
  font-weight: 600;
  text-align: center;
  white-space: nowrap;
  vertical-align: middle;
  line-height: 1.42857143;
  touch-action: manipulation;
  user-select: none;
  -ms-user-select: none;
  -moz-user-select: none;
  -webkit-user-select: none;
  -ms-touch-action: manipulation;
}

.btn.btn-outline-primary {
  transition: 0.5s all ease;
  border: solid 1px #000066;
  padding: 0.2rem;
  color: #000066 !important;
  background-color: white;
  border-radius: 40px;
  width: 100px;
}

.btn.btn-outline-primary:hover {
  background-color: #000066;
  color: white !important;
}

/* .body{ */
/* width: 80%; */
/* } */
.allcategory {
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
  left: 10%;
  width: 80%;
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
}
</style>
