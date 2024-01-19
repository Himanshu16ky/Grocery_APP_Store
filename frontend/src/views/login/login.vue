<template>
  <!-- <center>
    <div
      style="
        position: relative;
        top: 8rem;
        border: purple 2px solid;
        width: 25rem;
        height: 22rem;
        border-radius: 10px;
      "
    >
      <h3 style="font-size: 300%; color: purple; position: relative; top: 5%">
        Login
      </h3>
      <form
        @submit="validateInput"
        style="position: relative; top: 8%"
      >
        <div class="form-group" style="width: 50%">
          <label for="exampleInputEmail1">Username</label>
          <input
            v-model="username"
            style="border: 1px solid purple"
            name="username"
            type="text"
            class="form-control"
            id="username"
            @input="validateInput"
            aria-describedby="emailHelp"
            placeholder="Username"
            required
          />
        </div>
        <br />
        <div class="form-group" style="width: 50%">
          <label for="exampleInputPassword1">Password</label>
          <input
            v-model="password"
            style="border: 1px solid purple"
            name="password"
            type="password"
            class="form-control"
            id="password"
            placeholder="Password"
            @input="validateInput"
            required
          />
        </div>
        <br />
        <button
          type="submit"
          class="btn btn-primary"
          style="margin-right: 12%"
          @click.prevent="logging()"
        >
          Login
        </button>
        <a href="http://localhost:8080/#/register" type="submit" class="btn btn-primary">
          Register</a>
      </form>
    </div>
  </center> -->
  <center>
  <div class="container">
      <!-- <div class="col-md-6"> -->
        <div class="card">
          <form onsubmit="event.preventDefault()" class="box">
            <h1>Login</h1>
            <p style="color: white;">Please enter your login and password!</p>
            <input type="text" v-model="username"
             name="" placeholder="Username" 
             id="username"
            @input="validateInput"
            aria-describedby="emailHelp"
             />
            <input type="password" name="" 
            placeholder="Password" 
            v-model="password" id="password"
            @input="validateInput"
            required/>
            <input @click.prevent="logging()" type="submit" name="" value="Login" href="#" />New ?
            <a class="forgot " type="submit" href="http://localhost:8080/#/register">SignUp here </a>
          </form>
        </div>
      <!-- </div> -->
    </div>
    </center>
</template>

<style scoped>
/* Unset max-width and min-width */

/* .element {
  width: 100vw;
  max-width: none;
  min-width: none;
  box-sizing: none;
} */

.container {
  position: relative;
  top: -100px;
  margin: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    width: 10vw;

  /* background: #B8E1FC;
  background: radial-gradient(circle farthest-side at center center, #000000e9 0%, #341931 100%); */

  /* position: absolute; */
  /* top: 0;
  left: 0; */
  width: 100vw;
  height: 100vh;
  /* filter: blur(10px);  */
}

.container {
  /* background-color: rgb(196, 72, 72); */
  /* background-image: url('https://w0.peakpx.com/wallpaper/165/747/HD-wallpaper-beautiful-landscape-digital-art.jpg'); */
  /* background-size: cover; Make the background image cover the container */
  /* background-position: center; Center the background image */
  width: 100vw; /* Set the width of the container to 100% of its parent */
  height: 100vh; /* Set the height of the container to 100% of the viewport height */

  /* position: relative; Create a stacking context for child elements */
}
img{
  filter: blur(5px); /* Apply a background blur to the image */
  height: 100%;
  z-index: -100;
}
* {
  /* backdrop-filter: blur(10px); */
  /* background-image: url('https://w0.peakpx.com/wallpaper/165/747/HD-wallpaper-beautiful-landscape-digital-art.jpg');   */
  /* filter: blur(10px); */
  margin: 30px;
  padding: 0;
  font-family: sans-serif;
  /* background: linear-gradient(to right, #b92b27, #1565c0); */
}

.card {
  /* background: black; */
  /* position: absolute;
  left: 25%;
  margin-bottom: 20px;
  border: none; */
  width: 500px;
  height: 500px;
}

.box {
  border-radius: 1rem;
  background-image: url('https://w0.peakpx.com/wallpaper/165/747/HD-wallpaper-beautiful-landscape-digital-art.jpg'); 
  backdrop-filter: blur(10px);
  padding: 40px;
  position: relative;
  /* top: 0%; */
  /* left: 15%; */
  background: rgb(0, 0, 0);
  text-align: center;
  transition: 0.25s;
  /* height: 500px; */
  /* margin-top: 100px; */
}

.box input[type="text"],
.box input[type="password"] {
  border: 0;
  background: none;
  display: block;
  margin: 20px auto;
  text-align: center;
  border: 2px solid #3498db;
  padding: 10px 10px;
  width: 250px;
  outline: none;
  color: white;
  border-radius: 24px;
  transition: 0.25s;
}

.box h1 {
  color: white;
  text-transform: uppercase;
  font-weight: 500;
}

.box input[type="text"]:focus,
.box input[type="password"]:focus {
  width: 300px;
  border-color: #2ecc71;
}

.box input[type="submit"] {
  border: 0;
  background: none;
  display: block;
  margin: 20px auto;
  text-align: center;
  border: 2px solid #2ecc71;
  padding: 14px 40px;
  outline: none;
  color: white;
  border-radius: 24px;
  transition: 0.25s;
  cursor: pointer;
}

.box input[type="submit"]:hover {
  background: #2ecc71;
}

.forgot {
  text-decoration: underline;
}

</style>
<script>
import axios from "axios";
export default {
  name: "loginview",
  data() {
    return {
      username: "",
      password: "",
    };
  },
  // computed(){

    
  // },
  methods: {
    validateInput() {
      // Create a regex pattern for validation
      const pattern = /^[^/ ]{8,}$/;
      this.isValid = pattern.test(this.inputText);
    },
    logging() {
      console.log("loggin called")
      if (!this.username || !this.password){
        alert("enter both the credentials")
        
      }
      else{
      axios
        .post("http://127.0.0.1:5000/api/login", {
          username: this.username,
          password: this.password,
        })
        .then((res) => {
          if (res.data.status === "successful") {
            const token = res.data.token;
            // const username = res.data.username

            const access_token = res.data.access_token;
            const refresh_token = res.data.refresh_token;
            const username = res.data.username;

            localStorage.setItem(`access_token_${username}`, access_token);
            localStorage.setItem(`refresh_token_${username}`, refresh_token);
            localStorage.setItem("username", username);

            alert("Successfully Logged in !!");
            if (res.data.role === "manager") {
              console.log("pushing to manager");
              this.$router.push(`/manager/${username}`);
            } else if (res.data.role === "user") {
              this.$router.push(`/user/${username}`);
            } else if (res.data.role === "admin") {
              this.$router.push(`/${username}`);
            }

            // this.$router.push({
            //   name:"manager",
            //   params:{
            //     username: res.data.username,
            //     password: this.password,
            //   }
            // })
          } else {
            alert("Invalid credentials !!");
          }
        })
        .catch((error) => {
          console.error(error);
          alert("An error occurred while logging in !!");
        });
      }
    },
  },
};
</script>