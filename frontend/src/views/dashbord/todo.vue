<template>
  <section>
    <!-- <div v-for="item in all_requests"
  :key="item.details"
  style="z-index: 100; height: 100px; width: 100px; background-color: red;">
  {{ item.name }}
</div> -->
<nav class="navbar navbar-light bg-light">
      <div class="container-fluid"
      style="background-color: rgba(128, 204, 255, 0.827) 112, 238, 0.898);
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
        </div>
      </div>
    </nav>
    <div class="container py-5 h-100">
      <div class="row d-flex justify-content-center align-items-center h-100">
        <div class="col-md-12 col-xl-10">
          <div class="card">
            <div class="card-header p-3">
              <h5 class="mb-0">
                <i class="fas fa-tasks me-2"></i> Joining Requests
              </h5>
            </div>
            <div class="card-body" data-mdb-perfect-scrollbar="true">
              <table class="table mb-0">
                <thead>
                  <tr>
                    <th scope="col">Serial n.o</th>
                    <th scope="col">Name</th>
                    <!-- <th scope="col">role</th> -->
                    <th scope="col">Email id</th>
                    <th scope="col">Actions</th>
                  </tr>
                </thead>
                <tbody>
                  <tr
                    class="fw-normal"
                    v-for="(item, index) in joining_requests"
                    :key="index"
                  >
                    <td class="align-middle">
                      <span>{{ index + 1 }}</span>
                    </td>
                    <th>
                      <!-- <img src="https://mdbcdn.b-cdn.net/img/Photos/Avatars/avatar-5.webp"
                      class="shadow-1-strong rounded-circle" alt="avatar 1"
                      style="width: 55px; height: auto;"> -->
                      <span class="ms-2">{{ item.name }}</span>
                    </th>
                    <!-- <td class="align-middle">
                      <span>Manager</span>
                    </td> -->
                    <td class="align-middle">
                      <span>{{item.details}}</span>
                    </td>
                    <td class="align-middle">
                      <a
                        @click="join(item.req_id,index)"
                        data-mdb-toggle="tooltip"
                        title="Done"
                        ><i
                          class="fas fa-check text-success me-3"
                          style="margin-right: 10px"
                        ></i></a
                      >|
                      <a 
                      @click="remove(item.req_id,index)"
                       data-mdb-toggle="tooltip" title="Remove"
                        ><i
                          class="fas fa-trash-alt text-danger"
                          style="margin-left: 10px"
                        ></i
                      ></a>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
          <div class="card">
            <div class="card-header p-3">
              <h5 class="mb-0">
                <i class="fas fa-tasks me-2"></i> Adding Categories
              </h5>
            </div>
            <div class="card-body" data-mdb-perfect-scrollbar="true">
              <table class="table mb-0">
                <thead>
                  <tr>
                    <th scope="col">Serial n.o</th>
                    <th scope="col">Name</th>
                    <th scope="col">Category</th>
                    <th scope="col">Actions</th>
                  </tr>
                </thead>
                <tbody>
                  <tr
                    class="fw-normal"
                    v-for="(item, index) in add_category"
                    :key="index"
                  >
                    <td class="align-middle">
                      <span>{{ index + 1 }}</span>
                    </td>
                    <th>
                      <!-- <img src="https://mdbcdn.b-cdn.net/img/Photos/Avatars/avatar-5.webp"
                      class="shadow-1-strong rounded-circle" alt="avatar 1"
                      style="width: 55px; height: auto;"> -->
                      <span class="ms-2">{{ item.name }}</span>
                    </th>
                    <td class="align-middle">
                      <span>{{ item.details }}</span>
                    </td>
                    <td class="align-middle">
                      <a
                        @click="add_req(item.details, index)"
                        data-mdb-toggle="tooltip"
                        title="Done"
                        ><i
                          class="fas fa-check text-success me-3"
                          style="margin-right: 10px"
                        ></i></a
                      >|
                      <a 
                      @click="remove(item.req_id)"
                       data-mdb-toggle="tooltip" title="Remove"
                        ><i
                          class="fas fa-trash-alt text-danger"
                          style="margin-left: 10px"
                        ></i
                      ></a>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
          <div class="card">
            <div class="card-header p-3">
              <h5 class="mb-0">
                <i class="fas fa-tasks me-2"></i> Editing Categories
              </h5>
            </div>
            <div class="card-body" data-mdb-perfect-scrollbar="true">
              <table class="table mb-0">
                <thead>
                  <tr>
                    <th scope="col">Serial n.o</th>
                    <th scope="col">Name</th>
                    <th scope="col">Change Name</th>
                    <th scope="col">Actions</th>
                  </tr>
                </thead>
                <tbody>
                  <tr
                    class="fw-normal"
                    v-for="(item, index) in edit_category"
                    :key="index"
                  >
                    <td class="align-middle">
                      <span>{{ index + 1 }}</span>
                    </td>
                    <th>
                      <span class="ms-2">{{ item.name }}</span>
                    </th>
                    <td class="align-middle">
                      <span>{{ item.details }}</span>
                    </td>
                    <td class="align-middle">
                      <a data-mdb-toggle="tooltip" title="Done"
                        ><i
                          @click="edit_req(item.details, index)"
                          class="fas fa-check text-success me-3"
                          style="margin-right: 10px"
                        ></i></a
                      >|
                      <a @click="remove(item.req_id)" data-mdb-toggle="tooltip" title="Remove"
                        ><i
                          class="fas fa-trash-alt text-danger"
                          style="margin-left: 10px"
                        ></i
                      ></a>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
          <div class="card">
            <div class="card-header p-3">
              <h5 class="mb-0">
                <i class="fas fa-tasks me-2"></i> Deleting Categories
              </h5>
            </div>
            <div class="card-body" data-mdb-perfect-scrollbar="true">
              <table class="table mb-0">
                <thead>
                  <tr>
                    <th scope="col">Serial n.o</th>
                    <th scope="col">Name</th>
                    <th scope="col">Category</th>
                    <th scope="col">Actions</th>
                  </tr>
                </thead>
                <tbody>
                  <tr
                    class="fw-normal"
                    v-for="(item, index) in delete_category"
                    :key="index"
                  >
                    <td class="align-middle">
                      <span>{{ index + 1 }}</span>
                    </td>
                    <th>
                      <span class="ms-2">{{ item.name }}</span>
                    </th>
                    <td class="align-middle">
                      <span>{{ item.details }}</span>
                       </td>
                    <td class="align-middle">
                      <a
                        @click="delete_req(item.details, index)"
                        data-mdb-toggle="tooltip"
                        title="Done"
                        ><i
                          class="fas fa-check text-success me-3"
                          style="margin-right: 10px"
                        ></i></a
                      >|
                      <!-- <button
                      @click="delete_req(item.details,index)"
                        type="button"
                        class="btn btn-success btn-sm"
                        style="margin-left: 10px; padding: 5px 15px 5px 15px"
                      >
                        Approve
                      </button> -->
                      <a @click="remove(item.req_id)"
                       data-mdb-toggle="tooltip" title="Remove"
                        ><i
                          class="fas fa-trash-alt text-danger"
                          style="margin-left: 10px"
                        ></i
                      ></a>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import axios from "axios";
import refreshAccessToken from "../../utils/refresh_token.js";

export default {
  name: "TodoApp",
  props: {
    msg: String,
  },
  computed: {
    // serialNumbers() {
    //   return this.add_category.map((_, index) => index + 1);
    // },
  },

  data() {
    return {
      num: 0,
      task: "",
      sno1: 1,
      sno2: 1,
      sno3: 1,
      editTask: null,
      all_requests: [],
      add_category: [],
      delete_category: [],
      edit_category: [],
      joining_requests:[],
    };
  },

  mounted(){
    if(this.check()){
     this.get_itms()
    }
  },

  methods: {
    logout(){
      const currentUrl = window.location.href;
      const urlSegments = currentUrl.split("/");
      this.lastSegment = urlSegments[urlSegments.length - 1];
      localStorage.removeItem(`refresh_token_${this.lastSegment}`)
      localStorage.removeItem(`access_token_${this.lastSegment}`)
      this.$router.push(`/login`);
    },
    join(req_id,index){
      console.log(req_id,index)
      axios .post(`http://127.0.0.1:5000/remove/${req_id}`)
      .then((response) => {
        if (response.data =="successful"){
          console.log(this.joining_requests.splice(index, 1));
        }
        else{
          alert("invalid request !!")
          console.log("error : ", response)
        }
      })
        .catch((error) => {
          console.error("Error fetching data:", error);
        });
    },
    remove(reqId){
      axios .delete(`http://127.0.0.1:5000/remove/${reqId}`)
      .then((response) => {
          console.log("removing request : ",response.data);
    const addCategoryIndex = this.add_category.findIndex(item => item.req_id === reqId);
    const deleteCategoryIndex = this.delete_category.findIndex(item => item.req_id === reqId);
    const editCategoryIndex = this.edit_category.findIndex(item => item.req_id === reqId);
    const joiningRequestsIndex = this.joining_requests.findIndex(item => item.req_id === reqId);

    // Remove the item from each array if found
    if (addCategoryIndex !== -1) {
      this.add_category.splice(addCategoryIndex, 1);
    }

    if (deleteCategoryIndex !== -1) {
      this.delete_category.splice(deleteCategoryIndex, 1);
    }

    if (editCategoryIndex !== -1) {
      this.edit_category.splice(editCategoryIndex, 1);
    }

    if (joiningRequestsIndex !== -1) {
      this.joining_requests.splice(joiningRequestsIndex, 1);
    }
        })
        .catch((error) => {
          console.error("Error fetching data:", error);
        });
    },

    async get_itms(){
      await axios
      .get("http://127.0.0.1:5000/todo")
      .then((response) => {
        console.log("response111 ::: ", response.data);
        // console.log("response:::", response.data[3][0]["name"]);
        this.add_category = response.data[0];
        this.delete_category = response.data[1];
        this.edit_category = response.data[2];
        this.joining_requests = response.data[3];
        // [this.add_category,this.delete_category,this.edit_category] = [response.data]

        // console.log(this.all_requests)
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
      });
    this.all_requests.forEach((req) => {
      // this.add_category = req.data[0]
      // this.delete_category = req.data[1]
      // this.edit_category = req.data[2]
      // if (req.type ==="add category"){
      //   this.add_category.push(req)
      // }
      // else if (req.type ==="delete category"){
      //   this.delete_category.push(req)
      // }
      // else if (req.type ==="edit category"){
      //   this.edit_category.push(req)
      // }
      // else{
      //   console.log("unknown request")
      // }
    });
    },

    check() {
      try {
        const currentUrl = window.location.href;
        const urlSegments = currentUrl.split("/");
        this.lastSegment = urlSegments[urlSegments.length - 1];
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
    // delete task
    delete_req(category, index) {
      axios
        .delete(`http://127.0.0.1:5000/todo/${category}`)
        .then((response) => {
          if (response.data === "successful"){
            console.log("action successful")
          }
          else if (response.data === "duplicate") {
            console.log("can't");
            console.log(response.data);
            alert("command not possible");
          }
          else {
            alert("Completed")
          }
          console.log(this.delete_category.splice(index, 1));
          console.log("request deleted 1");
        })
        .catch((error) => {
          console.error("Error fetching data:", error);
        });
    },
    add_req(category, index) {
      axios
        .post(`http://127.0.0.1:5000/todo/${category}`)
        .then((response) => {
          if (response.data === "successful"){
            console.log("action successful")
          }
          else if (response.data == "duplicate") {
            console.log("can't");
            console.log(response.data);
            alert("command not possible");
          }
          else {
            alert("invalid request")
          }
          console.log(this.add_category.splice(index, 1));
          console.log("request deleted 1");
        })
        .catch((error) => {
          console.error("Error fetching data:", error);
        });
    },
    edit_req(category, index) {
      axios
        .put(`http://127.0.0.1:5000/todo/${category}`)
        .then((response) => {
          if (response.data == "successful"){
            console.log("action successful")
          }
          else if (response.data === "duplicate") {
            console.log("can't");
            console.log(response.data);
            alert("command not possible");
          }
          else {
            alert("invalid request")
          }
          // this.edit_category.forEach((item)=>{
          //   console.log(item)
          //   if item["deta"]
          // })
          // this.edit_category = this.edit_category.filter((item) => !item.details.includes(response.data[2]));
          this.edit_category.splice(index, 1);
          console.log("request deleted 2");
        })
        .catch((error) => {
          console.error("Error fetching data:", error);
        });
    },

    // edit task
    EditTask(index) {
      (this.task = this.tasks[index].name), (this.editTask = index);
    },
  },
};
</script>

<style scoped>
.caintaner {
  width: 80%;
  margin: auto;
}

.card {
  height: auto;
  width: 100%;
  margin-bottom: 100px;
  border: 1px solid green;
}

element.style {
  position: relative;
  height: auto;
}

.card-body {
  height: auto;
  /* overflow-y: visible; */
}

table {
  border-radius: 5px;
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width: 100%;
  margin-top: 20px;
}

td,
th {
  border: 1px solid #a8cddf;
  text-align: center;
  padding: 8px;
}

tr:nth-child(even) {
  background-color: #dddddd;
}

/* .add-btn {
        border: none;
        width: 100px;
        height: 30px;
        padding: 2px;
        background-color: teal;
        color: white;
    }
    
    .del-btn {
        margin: 5px;
        border-radius: 5px;
        border: none;
        background-color: red;
        color: white;
    }
    
    .edit-btn {
        margin: 5px;
        border: none;
        border-radius: 5px;
        background-color: #77b631;
        color: white;
    
    } */
</style>
