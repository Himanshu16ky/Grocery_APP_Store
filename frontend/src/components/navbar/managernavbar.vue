<template>
  <div style="background-color: rgb(0, 0, 0)">
    <nav class="navbar navbar-light bg-light">
      <div class="container-fluid"
      style="background-color: rgba(128, 204, 255, 0.827);
      width: 90%;
      position: sticky;
      
      "
      >
        <a class="navbar-brand" style="margin-left: 10px"
          ><strong><h1 >SnapShop</h1></strong></a
        >

        <div
          class="d-flex justify-content-end align-items-center ml-auto bntholder"
        >
          <button
            style="margin: 10px;border-color: #040490e5;"
            class="btn btn-outline-success red-hover"
            type="submit"
            @click="logout()"
          >
            <img style="height: 30px" src="../../assets/profile.png" alt="" />
            Logout
          </button>

          <!-- Example split danger button -->

          <button class="btn btn-outline-success red-hover"
          @click="exportPostsCSV()" 
          style="border-color: #040490e5;margin: 10px">
            Export
          </button>
        </div>
      </div>
    </nav>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "ManagerNavbar",

  methods: {
    logout(){
      localStorage.clear();
      this.$router.push(`/login`);
    },
    async exportPostsCSV() {
      try {
        let access_token = localStorage.getItem("access_token");
        axios.defaults.headers.common["Authorization"] =
          "Bearer " + access_token;

        const response = await axios.get(
          `http://127.0.0.1:5000/export/report`,
          { responseType: "arraybuffer" }
        );
        console.log(response);

        const url = window.URL.createObjectURL(new Blob([response.data]));
        const link = document.createElement("a");

        // setting filenames.
        const now = new Date()
          .toLocaleString()
          .replace(/[^\w\s]/gi, "")
          .replace(/ /g, "_");
        const post_filename = `posts_${now}.csv`;

        link.href = url;
        link.setAttribute("download", post_filename);
        document.body.appendChild(link);
        link.click();

        // code to : Save the file to a custom location.
        // const fileSaver = new FileSaver(url);
        // fileSaver.save(post_filename, {
        //     type: 'text/csv',
        // });
      } catch (error) {
        if (error.response && error.response.status === 401) {
          await refreshAccessToken();
          await this.exportPostsCSV();
        } else {
          console.log(error);
          alert("An error occurred while exporting CSV files.");
        }
      }
    },
  },
};
</script>

<style scoped>
.red-hover:hover {
  background-color: #040490e5 !important;
  border-color: rgb(0, 170, 255) !important;
}
* {
  font-family: Comic Sans MS;
  font-weight: bolder;
  color: #040490e5;
}
.navbar-brand {
  font-size: 250%;
}
.navbar {
  --bs-navbar-padding-y: 0rem;
}
.form-control {
  position: relative;
  left: 10%;
}
</style>
<style scoped>
.d-flex[data-v-2da3e2a0] {
  width: 55rem;
}
.searchbutton {
  background-color: inherit;
  border: none;
  position: relative;
  right: -4%;
  bottom: 3px;
}
.search-bar {
  background: rgb(139, 216, 255);
  flex: 1;
  height: 20px;
  border: 0;
  width: 50rem;
  border-radius: 30px;
  padding: 24px 20px;
  font-size: 20px;
  color: #cccc;
}
.align-text-top {
  vertical-align: text-top !important;
  left: -0.7rem;
  position: relative;
  top: 0.2rem;
  border-radius: 50%;
}
.btn[data-v-6f9f021a] {
  /* border-color: #040490e5; */
  border: 1px solid #040490e5;
  font-weight: bolder;
  font-size: larger;
  position: relative;
  left: 10%;
  margin-left: 3%;
  --bs-btn-padding-x: 1.3rem;
}
.d-flex[data-v-6f9f021a] {
  width: 60%;
  position: relative;
  float: right;
  left: 20%;
}
.btn-primary, .btn-primary:hover, .btn-primary:active, .btn-primary:visited {
    background-color: #6d3ea6 !important;
}
.d-flex {
  width: 50rem;
}
.container,
.container-fluid,
.container-xxl,
.container-xl,
.container-lg,
.container-md,
.container-sm {
  --bs-gutter-x: 10.5rem;
  --bs-gutter-y: 0;
}
.me-2 {
  margin-right: 55.5rem;
  /* margin:100px 100px 200px 200px; */
}
.btn {
  --bs-btn-padding-x: 1.3rem;
}
/* .btn-outline-success{
  margin:100px 100px 200px 200px;
} */
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
