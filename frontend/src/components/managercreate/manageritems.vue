<template>
            <!-- <div class="imgcontainer"><img src="../../assets/grocery.png" alt=""></div> -->

  <div style="overflow-x: hidden;
  ">
    <ManagerNavbar />
    <div style="position: relative; left: 10%;">
    <div class="card-container"
    style="left: 10%;">
      <div class="header">
        <h1 class="page-title" 
        style="font-family: Comic Sans MS;
  font-weight: bolder;
  position: relative;
  margin: 20px;
  top: -10%;"
        >{{ $route.params.item }}</h1>
        <button
          @click="goback()"
          class="btn btn-primary btn-lg"
        >
          Go Back
        </button>
      </div>
      <AddItem
        :categoryname="lastSegment"
        :editItemName="editItemName"
        :editMode="editMode"
        @cancel-edit="cancelEdit"
        @close="closeItemForm"
        :itemname="olditem"
        v-if="showItem || editMode"
      />
      <!-- <EditItem  :item_name = "this.item_name" @close="edit" v-if="showItem" /> -->
      <!-- ////////////////..............b......,,,,,,,,,,,,,,,,,,,,,,,dddddddddddddddddddddddddd777777777777777777777777777777773333333333333333333333333333333333333333333330000000000000000000000000000000000;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzb -->
      


      <table class="table mb-0">
          <thead>
            <tr>
              <!-- <th scope="col">Serial n.o</th> -->
              <th scope="col">S.no</th>
              <th scope="col">Name</th>
              <th scope="col">Size</th>
              <th scope="col">Stock</th>
              <th scope="col">Price</th>
              <th scope="col">Action</th>
            </tr>
          </thead>

          <tbody>
            <tr
              class="fw-normal"
              v-for="(item,index) in items" :key="item.id"
            >
            
            <!-- <div v-if="item.category_name == lastSegment" > -->

              <td class="align-middle" 
              >
                <span>{{ index + 1 }}</span>
              </td>
              <th >
                <span class="ms-2">{{ item.item }}</span>
              </th>
              <td class="align-middle">
                <span>{{ item.pack_size }}</span>
              </td>
              <td class="align-middle">
                <span>{{ item.stock }}</span>
              </td>
              <td class="align-middle">
                <span>{{ item.price }}</span>
              </td>
              <td class="align-middle">
                <!-- @submit="addItem(data)" -->
                <form style=" display: flex;"
                >
                  <div class="button-holder">
                    <div
                    >
                    <button class="btn btn-primary " @click="editItem(item.item,item.size,item.stock,item.price,item.unit,item.expiry)">Edit</button>
                    <button class="btn btn-outline-danger" @click="dele(item.item)">Delete</button>
                      
                    </div>
                  </div>
                </form>
              </td>
            <!-- </div> -->

            </tr>
          </tbody>
          
        </table>
        <div style="position: relative;
        margin: 30px;">
          <button
          @click="additem(lastSegment)"
          class="btn btn-primary btn-lg"
        >
         <h4>+ Add Item</h4>
        </button>
        </div>
    </div>
  </div>
</div>
</template>

<script>
import axios from "axios";
import AddItem from "./Additem.vue";
import EditItem from "./Additem.vue";

import ManagerNavbar from "../navbar/managernavbar.vue";
export default {
  data() {
    return {
      lastSegment: "",
      categoryname: "",
      item_name: "",
      showItem: false,
      add_item_menue:false,
      items: [],
      editItemName: "", // For storing the item name being edited
      editMode: false, // Flag for edit mode
    };
  },
  // name: "Manageritems",
  components: {
    EditItem,
    ManagerNavbar,
    AddItem,
  },
  mounted() {

    const currentUrl = window.location.href;
    const urlSegments = currentUrl.split("/");
    this.lastSegment = urlSegments[urlSegments.length - 1];
    console.log("lastsegment:", this.lastSegment);
    console.log("categoryname:", this.categoryname);
    axios
      .get(`http://127.0.0.1:5000/manager/${this.lastSegment}`)
      .then((response) => {
        this.items = response.data;
        console.log("response : ",response)
      })
      .catch((error) => {
        console.log("at admititems", error);
      });

    // for edititem menue
    localStorage.removeItem("edit_item");
    localStorage.removeItem("edit_pack_size");
    localStorage.removeItem("edit_stock");
    localStorage.removeItem("edit_price");
    localStorage.removeItem("edit_unit");
    localStorage.removeItem("edit_expiry");
  },
  methods: {
    
    editItem(item,pack_size,stock,price,unit,expiry) {
      this.editItemName = item;
      console.log(expiry)
      localStorage.setItem("edit_item",item)
      localStorage.setItem("edit_pack_size",pack_size)
      localStorage.setItem("edit_stock",stock)
      localStorage.setItem("edit_price",price)
      localStorage.setItem("edit_unit",unit)
      localStorage.setItem("edit_expiry",expiry)
      this.editMode = true;
      this.showItem = true;
      // this.olditem =
    },
    goback(){
      const currentUrl = window.location.href;
      const urlSegments = currentUrl.split("/");
      this.lastSegment = urlSegments[urlSegments.length - 2];
      this.$router.push(`/manager/${this.lastSegment}`)
    },
    closeItemForm() {
      this.editItemName = "";
      this.editMode = false;
      this.showItem = false;
    },
    //   handleChildData(data) {
    //   this.items = data;
    // }
    dele(itemname) {
      console.log(itemname);

      const isConfirmed = window.confirm(`Are you sure you want to Delete ${itemname}`);
      if (isConfirmed) {
        // Logic to execute when the user clicks "OK"
        axios
        .delete(`http://127.0.0.1:5000/manager/additem/${itemname}`)
        .then((response) => {
          console.log("delete response : ", response.data);
          window.location.reload();
        });
        console.log("Confirmed!");
      } else {
        console.log("Canceled!");
      }

    },
    additem() {
      this.categoryname = this.lastSegment;
      this.showItem = !this.showItem;
      console.log(this.showItem);
      console.log(this.editMode);
    },
    cancelEdit() {
      this.editMode = false; // Update the editMode state in the parent component
      // this.editMode =
      // window.location.reload();
      this.showItem = !this.showItem
    },
    edit(item_name) {
      this.item_name = item_name;
      this.showItem = !this.showItem;
      console.log(this.showItem);
    },
  },
};
</script>

<style scoped>
.button-wrapper {
  margin-top: 10px;
}

/* .btn {
  border: none;
  padding: 4px 6px;
  border-radius: 24px;
  font-size: 12px;
  font-size: 0.8rem;
  letter-spacing: 2px;
  cursor: pointer;
} */

.btn + .btn {
  margin-left: 10px;
}

.outline {
  background: transparent;
  color: rgba(0, 212, 255, 0.9);
  border: 1px solid rgba(0, 212, 255, 0.6);
  transition: all 0.3s ease;
}

.outline:hover {
  transform: scale(1.125);
  color: rgba(255, 255, 255, 0.9);
  border-color: rgba(255, 255, 255, 0.9);
  transition: all 0.3s ease;
}

.fill {
  background: rgba(0, 212, 255, 0.9);
  color: rgba(255, 255, 255, 0.95);
  filter: drop-shadow(0);
  font-weight: bold;
  transition: all 0.3s ease;
}

.fill:hover {
  transform: scale(1.125);
  border-color: rgba(255, 255, 255, 0.9);
  filter: drop-shadow(0 10px 5px rgba(0, 0, 0, 0.125));
  transition: all 0.3s ease;
}
/* .imgcontainer{
  height: 100px;
  width: 118px;
}
.imgcontainer img {
  position: relative;
  top: 0px;
  height: 100%;
  width: 100%;
} */

.header {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  /* background-color: #60b0fa; */
  height: 200px;
  width: 50%;
  /* position: relative; */
  left: 25%;
}
h1 {
  bottom: 30%;
  font-size: 70px;
  font-weight: 600;
  color: #040490e5;;
  /* background-image: linear-gradient(to left, #553c9a, #b393d3); */
  background-clip: text;
  -webkit-background-clip: text;
}
/* .page-title {
  font-size: 36px; 
  color: #333; 
  text-align: center;
  padding: 20px;
  border-bottom: 2px solid #333;
  margin-bottom: 20px;
  text-transform: uppercase; 
  letter-spacing: 2px; 
  font-weight: bold; 
} */
.card-container {
  display: flex;
  width: 80%;
  left: 10%;
  padding: 50px;
  flex-wrap: wrap; /* Allow cards to wrap to the next line */
  justify-content: center; /* Distribute cards evenly */
}
.cards-wrapper {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  width: 100%; /* Ensure it takes full available width */
}
.card {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  height: 220px;
  width: 160px;
  margin: 10px;
  /* padding: 20px; */
  background-color: bisque;
  border: 1px solid green;
  /* Add additional styling for cards as needed */
}
/* .card {
    height: 300px;
    width: 250px;
  margin-bottom: 50px;
  margin: 20px;
  padding: 20px;
  background-color: bisque;
  border: 1px solid green;
} */
.card-button {
  width: 100%; /* This will cause the button to expand to the card's width */
}
/* .container{
    padding: 1rem;
    display: flex-box;
    position: relative;
  display: inline-block;
}
.box{
    position: relative;
    margin: 10px;
    height: 300px;
    width: 250px;
    background-color: bisque;
    border: 1px solid green;
} */
</style>
