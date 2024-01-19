<template>
    <div v-if="showComponent" class="outerbox">
        <div class="innerbox" >
            <form type="submit" style="position: fixed;z-index: 1;">
  
  <div class="title-container" >
    <h2> {{categoryname}} </h2>
    <img @click="close" style="width: 30px; " src="../../assets/close1.png" alt="../../assets/search2.png">

  </div>
  <div class='errors-container'></div>
  <div  class='input-container'>
      <label  for="input-credit"> Category Name : </label>
    <input v-model="newname" type="text" id="input-credit" name="input-credit"  required>
  </div>
  <div class='btn-container'>
    <button type="submit"  @click.prevent="checking(categoryname)" >Save</button>
  </div>
</form>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import categoryname from "./managercreate.vue"
import showComponent from "./managercreate.vue"
export default{
    name:"editcategory",
    data(){
        return{
          person:"",
          showComponent:true,
          newname:"",
          alertMessage:"thie is from vue",
          ls:"",
        }
    },
    props:{
        functionEnabled: Boolean,
        gg:showComponent,
        categoryname:categoryname
    },
    methods:{
      close() {
      this.$emit('close'); // Emit a close event to notify the parent component
    },
        checking(oldname){
            if(this.newname !=""){
            console.log(oldname,"->",this.newname)
            console.log(localStorage.getItem("username"))
            // Sending a PUT request with data
            axios.put('http://127.0.0.1:5000/manager/addcat', {
            oldname: oldname,
            newname:this.newname,
            person: localStorage.getItem("username")
            })
            .then(response => {
                // Handle the successful response data here
                // this.alertMessage = response.data.alert;
                console.log('Response:', response.data);
                if(response.data == "sent"){
                    alert("request sent to admin ")
                     // Prevent the form from reloading the page
                }
                else if (response.data == "duplicate"){
                  alert("category already exists !!")
                }
                else {
                  
      this.$emit("close"); // Emit a close event to notify the parent component

                    // window.location.reload();

                }
            })
            .catch(error => {
                console.log("in the catch")
                // Handle errors here
            //     if (error.response) {
            // // The request was made, but the server responded with an error status
            //         this.alertMessage = response.data.alert;
            //         alert(this.alertMessage)
            //     } else {
            //         // The request was not made, or there was no response from the server
            //         console.error('Request Error:', error.message);
            //         this.alertMessage = response.data.alert;
            //         alert(this.alertMessage)
            //     }
            });
        }
    }}
}

</script>

<style scoped>

* {
    overflow-y:hidden;
  margin: 0;
  box-sizing: border-box;
}
body{
  display: flex;
  height: 100vh;
  justify-content: center;
  align-items: center;
  border: 2px solid red;
  background-color: rgba(171, 26, 26, 0.5);

}
.outerbox{
  position: relative;
  left: 30%;
}
form {
    
  display: flex;
  flex-direction: column;
  gap: 1rem;
  padding: 0.75rem 1.5rem;
  background-color: #f0f0f0;
  border-radius: 10px;
  box-shadow: 1px 1px 10px rgba(0,0,0,0.5);
/*   min-width: 275px; */
  min-width: 50ch;
}
h3{
  margin: 10px;
  font-size: 26px;
}
.title-container{
  display: grid; 
  grid-template-columns: 1fr 2rem; 
  grid-template-rows: 1fr; 
/*   grid-template-areas:
    ". ."; */
  align-items: center;
}
.input-container{
  display: grid; 
  grid-template-columns: 1fr 2fr; 
  grid-template-rows: 1fr; 
  gap: 1em 1em; 
  grid-template-areas: 
    ". ."; 
}

label {
  font-size: 1.05rem;
  letter-spacing: 0.95px
}

input[type="text"],
select,
input[type="number"] {
/*   width: 100px; */
  padding: 0.25rem;
  border: 1px solid #ccc;
  border-radius: 5px;
  font-weight: normal;
}
/* select{ */
/*   width: 110px; */
/* } */

button[type="submit"] {
  background-color: #007bff;
  color: #fff;
  padding: 0.5rem 1rem;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 1rem;
  width: 175px;
  transition: background-color 0.2s ease-in-out;
}
.btn-container{
  text-align: center;
}

button[type="submit"]:hover {
  background-color: #0062cc;
}
.close {
  --size: 1.5rem;
  display: inline-grid;
  align-items: center;
  height: var(--size);
  width: var(--size);
/*   border: 1px solid transparent; */
/*   border-radius: .5rem; */
  box-shadow: 0px 0px 0px 0px rgba(0,0,0, 0.85);
  transition: box-shadow .2s linear;
  
  /* & svg {
    user-select: none;
    pointer-events: auto;
  }
  
  &:active ,
  &:hover ,
  &:focus {
    box-shadow: 0px 0px 5px 1px rgba(0,0,0, 0.85);
  } */
}

.error-message {
  background-color: #fcf4a3;
  color: black;
  padding: 0.25rem 0.65rem;
  border-radius: 12px;
  margin-bottom: 0.75rem;
  font-size: 14px;
  box-shadow: 1px 1px 5px rgba(0,0,0, 0.1);
}

</style>

<!-- <style scoped>

*{ 

    position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background: rgb(43, 170, 189);
  padding: 20px;
  /* height: 100vh;
  width: 100vw; */
z-index: 1;
}

.outerbox{
    background-color: brown; 
    width: 400px;
    height: 440px;
}
.innerbox{
    background-color: rgb(42, 165, 99); 
    width: 380px;
    height: 380px;
    z-index: 100;
}
</style> -->