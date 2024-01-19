<template>
  <!-- @click.self="additem" -->
  <div>
    <div style="position: fixed; top: 30%; left: 40%">
      <div class="innerbox">
        <form @submit.prevent="addItem(itemname)">
          <img
            v-if="editMode"
            @click="cancelEdit"
            style="width: 30px; position: absolute; right: 0px; margin: 10px"
            src="../../assets/close1.png"
            alt="X"
          />
          <img
            v-else
            @click="close"
            style="width: 30px; position: absolute; right: 0px; margin: 10px"
            src="../../assets/close1.png"
            alt="X"
          />
          <div class="title-container">
            <!-- <h2> {{categoryname}} </h2> -->
            <!-- <img @click="edit(xxx)" style="width: 30px; " src="../../assets/close.png" alt="../../assets/search2.png"> -->
          </div>
          <div class="errors-container"></div>

          <div class="input-container">
            <label for="input-credit"> Item Name : </label>
            <input
              v-model="itemname"
              type="text"
              id="input-credit"
              name="input-credit"
              required
            />
          </div>
                    <!-- :placeholder="item_name" -->
          <div class="input-container">
            <label for="input-date">EXPdate : </label>
            <input
              v-model="expdate"
              type="date"
              id="input-date"
              name="input-date"
              required
            />
          </div>
          <div class="input-container">
            <label for="input-libelle">Unit : </label>
            <select v-model="unit" class="form-control"
            required
            >
              <option>Rs/Unit</option>
              <option>Rs/Kg</option>
              <option>Rs/Litre</option>
              <option>Rs/Dozen</option>
            </select>
          </div>
          <div class="input-container">
            <label for="input-debit"> Pack Size : </label>
            <input
              v-model="pack_size"
              type="number"
              id="input-debit"
              name="input-debit"
              required
            />
          </div>
          <div class="input-container">
            <label for="input-debit"> price/unit : </label>
            <input
              v-model="price"
              type="number"
              id="input-debit"
              name="input-debit"
              required
            />
          </div>
          <div class="input-container">
            <label for="input-debit"> Stock : </label>
            <!-- min="0.00" step="0.01" -->
            <input
              v-model="stock"
              type="number"
              id="input-debit"
              name="input-debit"
              required
            />
          </div>
          <div></div>
          <!-- type="submit" -->
          <div class="btn-container">
            <button
              v-if="editMode"

              @click.prevent="UpdateItem(item_name)"
              class="btn"
            >
              Edit ITEM
            </button>
            <button v-else type="submit">Add Item</button>
          </div>
        </form>
      </div>
    </div>

  </div>
</template>
<script>
import axios from "axios";

export default {
  data() {
    return {
      display: "none",
      allitems: [],
      itemname: "",
      expdate: "",
      price: 0,
      stock: 0,
      pack_size: 0,
      unit: "",
    };
  },
  props: {
    olditem: String,
    editMode: Boolean,
    categoryname: String,
    item_name: String,
    editItemName: String,
    editMode: false,
  },
  mounted() {
    if (this.editMode) {
      this.itemname = this.editItemName;
      this.expdate = localStorage.getItem("edit_expiry");
      this.price = localStorage.getItem("edit_price");
      this.stock = localStorage.getItem("edit_stock");
      this.pack_size = localStorage.getItem("edit_pack_size");
      this.unit = localStorage.getItem("edit_unit");
      console.log("editmode on");
    }
  },
  methods: {
    close() {
      this.$emit("close"); // Emit a close event to notify the parent component
    },
    cancelEdit() {
      this.$emit("cancel-edit");
      // Additional logic to clear or reset form fields if needed
    },
    async UpdateItem(categoryname) {
      if (this.item == "") {
        console.log("popopo");
        alert("Enter the item name.");
      } else {
        console.log(
          "...",
          this.editItemName,
          "....",
          this.itemname,
          this.expdate,
          this.price,
          this.stock,
          this.pack_size,
          this.unit
        );
        axios
          .put("http://127.0.0.1:5000/manager/additem", {
            editItemName: this.editItemName,
            item: this.itemname,
            expiry: this.expdate,
            price: this.price,
            pack_size: this.pack_size,
            stock: this.stock,
            unit: this.unit,
          })
          .then((response) => {
            // Handle the successful response data here
            this.alertMessage = response.data.alert;
            console.log("Response:", response.data);
            if (response.data === "duplicate") {
              alert("this item aready exists !!");
              // window.location.reload();
            } else if (response.data == "successful") {
              window.location.reload();
            } else if (response.data != "successful") {
              alert(this.alertMessage);
              categoryname.preventDefault();
              // Prevent the form from reloading the page
            }
          })
          .catch((error) => {
            console.log("in the catch");
          });
        // window.location.reload();
      }
    },

    addItem(item) {
      if (item === undefined) {
        console.log("addItem clicked");
        return "addItem clicked";
      }
      console.log(item, ".,.,.,.,.,.,", this.categoryname);
      axios
        .post("http://127.0.0.1:5000/manager/moi", {
          category: this.categoryname,
          item: this.itemname,
          expiry: this.expdate,
          price: this.price,
          pack_size: this.pack_size,
          stock: this.stock,
          unit: this.unit,
        })
        .then((response) => {
          console.log("posting...");
          console.log(response);
          console.log(response.data);
          if (response.data === "duplicate") {
            alert("can't have duplicate item");
          } else if (response.status == 200) {
            console.log(item)
            axios.post('http://127.0.0.1:5000/get_img', { name: item, }).then(
                                (res) => { 
                                  console.log(res,"jgEvrksbzfkubzskufbgkzushb")
                                  alert("image getting saved")
                                  console.log("image saving started") }
                            )
            console.log("posted");
            // this.allitems = response.data
            // this.$emit("childToParentEvent", response.data);
            // window.location.reload();
          } else {
            console.log("unable to post");
          }
        })
        .catch((error) => {
          console.error("error:::", error);
        });

    },
  },
};
</script>

<style scoped>
* {
  z-index: 1;

  /* position: absolute; */
  overflow-y: hidden;
  margin: 0;
  box-sizing: border-box;
}
/* body{
  display: flex;
  height: 100vh;
  justify-content: center;
  align-items: center;
  border: 2px solid red;
  background-color: rgba(171, 26, 26, 0.5);

} */
form {
  height: 400px;
  width: 400px;
  display: flex;
  flex-direction: column;
  gap: 1rem;
  padding: 0.75rem 1.5rem;
  background-color: #f0f0f0;
  border-radius: 10px;
  box-shadow: 1px 1px 10px rgba(0, 0, 0, 0.5);
  /*   min-width: 275px; */
  min-width: 50ch;
}
h3 {
  margin: 10px;
  font-size: 26px;
}
.title-container {
  margin: 10px;
  display: grid;
  grid-template-columns: 1fr 2rem;
  grid-template-rows: 1fr;
  /*   grid-template-areas:
    ". ."; */
  align-items: center;
}
.input-container {
  display: grid;
  grid-template-columns: 1fr 2fr;
  grid-template-rows: 1fr;
  gap: 1em 1em;
  grid-template-areas: ". .";
}

label {
  font-size: 1.05rem;
  letter-spacing: 0.95px;
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
.btn-container {
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
  box-shadow: 0px 0px 0px 0px rgba(0, 0, 0, 0.85);
  transition: box-shadow 0.2s linear;

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
  box-shadow: 1px 1px 5px rgba(0, 0, 0, 0.1);
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
