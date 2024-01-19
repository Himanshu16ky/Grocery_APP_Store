<template>
  <center>
    <div class="container">
      <div class="row">
        <div class="col-md-6">
          <div class="card">
            <form @submit.prevent="register" class="box">
              <h1>Register</h1>
              <span style="color: white;">Registering as : 
                <button
                style="background-color: #2ecc71;
                border-color:#3498db"
                 class="toggler" v-if="isuser" @click="toggel()">
                 <span>User</span></button>

                <button 
                style="background-color: #3498db;
                border-color: #2ecc71;"
                class="toggler" v-else @click="toggel()">
                <span>Manager</span></button>
              </span>
              <input
                type="text"
                v-model="username"
                placeholder="Username"
                @input="validateUsername"
              />
              <div v-if="usernameError" class="error-message">{{ usernameError }}</div>
              <form action="">
              <input
                type="email"
                required
                class="blue_border"
                v-model="email"
                placeholder="Email"
                @input="updateEmailVerificationStatus"
              />
              <span style=" 
              background-color: #000000;
              color: white;
              cursor: pointer;
              border: none;
              border-radius: 10px;"
              v-if="!isEmailVerified && !processing" 
              type = "submit"
              @click.prevent="email ? verifyEmail(email) : null">
                Verify Email
            </span>
            
          
            <span style=" 
              background-color: #000000;
              color: rgb(251, 134, 0);
              cursor: pointer;
              border: none;
              mask-type: submit;
              border-radius: 10px;" 
              v-else-if="processing" 
              >
                Click on the link sent to this Email.
            </span>
            
              <span v-else-if="isEmailVerified"  style="color: green">Email Verified ✓</span>
              <input
                type="password"
                v-model="password"
                placeholder="Password"
                required
                @input="validatePassword"
              />
            </form>
              <div v-if="passwordError" class="error-message">{{ passwordError }}</div>
              <input
                type="password"
                v-model="confirmPassword"
                placeholder="Confirm Password"
                required
              />
              <input type="submit" value="Register" />
              <span
              style="color: white;"
              >Already have an account? </span>
              <a class="forgot " href="http://localhost:8080/#/login"
                > Login here</a
              >
            </form>
          </div>
        </div>
      </div>
    </div>
  </center>
</template>

<script>
import axios from "axios";
export default {
  name: "registerView",
  data() {
    return {
      username: "",
      isuser:true,
      ismanager:false,
      email: "",
      message: '',
      isEmailVerified: false,
      password: "",
      confirmPassword: "",
      isSuccess: false,
      usernameError: '',
      passwordError: '',
      passwordStrength: -1,
      processing:false,
    };
  },
  mounted() {
    // Initialize Bootstrap Toggle on the checkbox
    // $(this.$el).find('[data-toggle="toggle"]').bootstrapToggle();
  },
  
  methods: {
    updateEmailVerificationStatus(){
      this.isEmailVerified = false;
    },
    validatePassword() {
      // Password validation logic
      const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;
      if (!passwordRegex.test(this.password)) {
        this.passwordError = 'Password must be at least 8 characters and contain at least 1 lowercase, 1 uppercase, 1 digit, and 1 special character.';
      } else {
        this.passwordError = '';
      }

      // Password strength calculation (for the sake of example)
      const strength = this.password.length >= 8 ? 5 : 0;
      this.passwordStrength = strength;
    },
    toggel(){
      this.isuser = !this.isuser
      this.ismanager = !this.ismanager
    },
    validateUsername() {
      // Username validation logic
      const usernameRegex = /^\S+$/; // No whitespace allowed
      if (this.username.length < 6 || !usernameRegex.test(this.username)) {
        this.usernameError = 'Username must be at least 6 characters and cannot have blank spaces.';
      } else {
        this.usernameError = '';
      }
    },
    // validateEmail() {
    //   // Add any additional email validation logic
    //   // This is a basic example
    //   this.isEmailVerified = false;
    // },
    verifyEmail(email) {
      if (this.email != "" || this.email != null){
        console.log(email)
      this.processing = true;
      console.log(email)
      const axios = require('axios');
              axios.get(`http://127.0.0.1:5000/api/register/${email}`)
                  .then(response => {
                      console.log(response);
                      if (response.data == true){
                        console.log("Email Verified")
                        this.processing = false;
                        this.isEmailVerified = true;
                      }
                      else{
                        alert("email verification failed please check it.")
                      }
                  })
                  .catch(error => {
                      console.log(error);
                  });
                }

      // setTimeout(() => {
      //   //code to verift email
        
      //  }, 2000);
      
      
    },
    register() {
      // Perform registration logic here
      // This is a basic example; you may want to add more checks and validations
      this.validateUsername();
      this.validatePassword();
      console.log(this.usernameError ,this.passwordError , this.isEmailVerified)
      // this.verifyEmail();

      if (!this.usernameError && !this.passwordError && this.isEmailVerified) {
        // Implement your registration logic here
        // For simplicity, just displaying a message
        this.message = 'Account created successfully!';
        this.isSuccess = true;
        console.log("inside if")
      
      axios
        .post("http://127.0.0.1:5000/api/register", {
          username: this.username,
          email: this.email,
          password: this.password,
          role: this.isuser ? "user":"manager"
        })
        .then((res) => {
          const response = res.data;
          console.log("registeration response : ",response)
          if (res.data == "pending"){
            alert("Registration request sent to Admin.");
            this.$router.push("/login");
          }
          // Handle registration success
          else if(res.data == "username_exist"){
            alert("Username already exists please try a new one.");
          }
          else if(res.data == "email_exist"){
            alert("Email ID already Register please try a new one.");
          }
          else{
            alert("Regeisteration successful");
            this.$router.push("/login");
          }
          
        })
        .catch((error) => {
          // Handle registration failure
          console.error(error);
          alert("An error occurred during Registration");
        });
    }
  },
  },
};
</script>


<style scoped>
.error-message {
  color: red;
  margin-top: 5px;
  font-size: 13px;
}

.success-message {
  color: green;
  margin-top: 10px;
}

.password-strength {
  margin-top: 10px;
  font-size: 14px;
}

.password-bar {
  height: 10px;
  background-color: #4caf50;
}
.toggler{
  border: 2px solid ;
  border-radius: 10px;
}

/* .toggleSwitch span span {
  display: none;
} */

@media only screen {
  .toggleSwitch {
    display: inline-block;
    height: 18px;
    position: relative;
    overflow: visible;
    padding: 0;
    margin-left: 50px;
    cursor: pointer;
    width: 60px
  }
  .toggleSwitch * {
    -webkit-box-sizing: border-box;
    -moz-box-sizing: border-box;
    box-sizing: border-box;
  }
  .toggleSwitch label,
  .toggleSwitch > span {
    line-height: 20px;
    height: 20px;
    vertical-align: middle;
  }
  .toggleSwitch input:focus ~ a,
  .toggleSwitch input:focus + label {
    outline: none;
  }
  .toggleSwitch label {
    position: relative;
    z-index: 3;
    display: block;
    width: 100%;
  }
  .toggleSwitch input {
    position: absolute;
    opacity: 0;
    z-index: 5;
  }
  .toggleSwitch > span {
    position: absolute;
    left: -50px;
    width: 100%;
    margin: 0;
    padding-right: 50px;
    text-align: left;
    white-space: nowrap;
  }
  .toggleSwitch > span span {
    position: absolute;
    top: 0;
    left: 0;
    z-index: 5;
    display: block;
    width: 50%;
    margin-left: 50px;
    text-align: left;
    font-size: 0.9em;
    width: 100%;
    left: 15%;
    top: -1px;
    opacity: 0;
  }
  /* .toggleSwitch a {
    position: absolute;
    right: 50%;
    z-index: 4;
    display: block;
    height: 100%;
    padding: 0;
    left: 2px;
    width: 18px;
    background-color: #b71616;
    border: 1px solid #CCC;
    border-radius: 100%;
    -webkit-transition: all 0.2s ease-out;
    -moz-transition: all 0.2s ease-out;
    transition: all 0.2s ease-out;
    box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
  } */
  .toggleSwitch > span span:first-of-type {
    color: #d31717;
    opacity: 1;
    left: 45%;
  }
  .toggleSwitch > span:before {
    content: '';
    display: block;
    width: 100%;
    height: 100%;
    position: absolute;
    left: 50px;
    top: -2px;
    background-color: #ffffff;
    border: 1px solid #ccc;
    border-radius: 30px;
    -webkit-transition: all 0.2s ease-out;
    -moz-transition: all 0.2s ease-out;
    transition: all 0.2s ease-out;
  }
  .toggleSwitch input:checked ~ a {
    border-color: #fff;
    left: 100%;
    margin-left: -8px;
  }
  .toggleSwitch input:checked ~ span:before {
    border-color: #0097D1;
    box-shadow: inset 0 0 0 30px #0097D1;
  }
  .toggleSwitch input:checked ~ span span:first-of-type {
    opacity: 0;
  }
  .toggleSwitch input:checked ~ span span:last-of-type {
    opacity: 1;
    color: #fff;
  }
  /* Switch Sizes */
  .toggleSwitch.large {
    width: 60px;
    height: 27px;
  }
  .toggleSwitch.large a {
    width: 27px;
  }
  .toggleSwitch.large > span {
    height: 29px;
    line-height: 28px;
  }
  .toggleSwitch.large input:checked ~ a {
    left: 41px;
  }
  .toggleSwitch.large > span span {
    font-size: 1.1em;
  }
  .toggleSwitch.large > span span:first-of-type {
    left: 50%;
  }
  .toggleSwitch.xlarge {
    width: 80px;
    height: 36px;
  }
  .toggleSwitch.xlarge a {
    width: 36px;
  }
  .toggleSwitch.xlarge > span {
    height: 38px;
    line-height: 37px;
  }
  .toggleSwitch.xlarge input:checked ~ a {
    left: 52px;
  }
  .toggleSwitch.xlarge > span span {
    font-size: 1.4em;
  }
  .toggleSwitch.xlarge > span span:first-of-type {
    left: 50%;
  }
}

/* Unset max-width and min-width */
.element {
  width: 100vw;
  max-width: none;
  min-width: none;
  box-sizing: none;
}

.container {

  /* background: #B8E1FC; */
  /* background: radial-gradient(circle farthest-side at center center, #000000e9 0%, #341931 100%); */

  position: absolute;
  left: 27%;
  /* top: 0;
  left: 0; */
  width: 100vw;
  height: 100vh;
  /* filter: blur(10px); Adjust the blur intensity as needed */
}

.container {
  /* background-color: red; */
  /* background-image: url('https://w0.peakpx.com/wallpaper/165/747/HD-wallpaper-beautiful-landscape-digital-art.jpg'); Replace 'your-image.jpg' with the URL of your background image */
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
body {
  /* backdrop-filter: blur(10px); */
  /* background-image: url('https://w0.peakpx.com/wallpaper/165/747/HD-wallpaper-beautiful-landscape-digital-art.jpg'); */
  filter: blur(10px);
  margin: 0;
  padding: 0;
  font-family: sans-serif;
  background: linear-gradient(to right, #b92b27, #1565c0);
}

/* .card {
  position: absolute;
  left: 25%;
  margin-bottom: 20px;
  border: none;
} */

.box {border-radius: 1rem;
  background-image: url('https://w0.peakpx.com/wallpaper/165/747/HD-wallpaper-beautiful-landscape-digital-art.jpg'); 
  backdrop-filter: blur(10px);
  width: 500px;
  padding: 40px;
  position: absolute;
  top: 50%;
  left: 15%;
  background: rgb(0, 0, 0);
  text-align: center;
  transition: 0.25s;
  margin-top: 100px;
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
.blue_border
{
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
.box input[type="email"]:focus,
.box input[type="tel"]:focus ,
.box input[type="password"]:focus,
.box input[type="text"]:focus {
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


