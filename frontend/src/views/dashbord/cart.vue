<template>
  <div class="cart_holder">
    <div class="card">
      <div class="card-header p-3">
        <h1 class="mb-0">
          <i class="fas fa-tasks me-2"></i> Your Cart
          <i  style="position: absolute;right: 5%;"><button class="button-62" @click="goback()">GO Back</button></i>
        </h1>
      </div >
      <div v-if="! empty_cart" class="card-body" data-mdb-perfect-scrollbar="true">
        <table class="table mb-0">
          <thead>
            <tr>
              <th scope="col">Serial n.o</th>
              <th scope="col">Name</th>
              <!-- <th scope="col">Quantity</th> -->
              <th scope="col">Units</th>
              <th scope="col">Price/Unit</th>
              <th scope="col">NetPrice</th>
              <th scope="col">Action</th>
            </tr>
          </thead>
          <!-- <tbody>
            <tr v-for="(data, index) in cart" :key="index">
              <td>{{ index + 1 }}</td>
              <td>{{ data.product_name }}</td>
              <td>{{ data.item_count }}</td>
              <td>{{ data.units }}</td>
              <td>{{ data.price }}</td>
              <td>{{ data.netPrice }}</td>
              <td>
                <button @click="removeItem(index)">Remove</button>
              </td>
            </tr>
          </tbody> -->

          <tbody>
            <tr
              class="fw-normal"
              v-for="(data, index) in this.cart"
              :key="index"
            >
              <td class="align-middle">
                <span>{{ index + 1 }}</span>
              </td>
              <th>
                <span class="ms-2">{{ data.product_name }}</span>
              </th>
              <!-- <td class="align-middle">
                <span>{{ data.pack_size }}</span>
              </td> -->
              <td class="align-middle">
                <span>{{ data.item_count }}</span>
              </td>
              <td class="align-middle">
                <span>{{ data.price }}</span>
              </td>
              <td style="z-index: 10;" class="align-middle">
                <span>{{ data.item_count * data.price }}</span>
              </td>
              <td class="align-middle">
                <!-- @submit="addItem(data)" -->
                <form style=" display: flex;
                position: relative;
                left: 35%;
                "
                >
                  <div class="button-holder">
                    <div
                    >

                      <div class="quantity-control">
                        
                        <button
                          type="submit"
                          @click="decrement(data)"
                          style="border: none; border-radius: 5px;
                            width: 30px;
                            background-color: rgb(243, 32, 13);"
                          v-if="data.item_count -1>=0"
                        >
                        
                          -    </button>
                        <span style="margin: 5px;"
                          >{{ data.item_count }}</span
                        >
                        <button 
                          type="submit"
                          @click="increment(data)"
                          style="border: none; border-radius: 5px;
                          width: 30px; background-color:green;"
                          v-if="data.stock-data.item_count >0"
                        >
                        
                          +    </button>
                      </div>
                      
                    </div>
                  </div>
                  <div 
                  style=" cursor: pointer; 
                   font-size: 30px; color: orange;
                  display: flex; margin-left: 8px; margin-bottom:-8px;margin-top:-8px;"
                      v-if="data.stock<data.item_count" 
                      :class="{ 'warning': data.stock<data.item_count }"
                      ref="myElement"
                       title="this item is out of stock please remove some items befor purchase !!" >
                       !
                      </div>
                </form>
              </td>
            </tr>
          </tbody>
        </table>
        <div class = "to_purchase"  >
          <div class="total">
            <h4>TOTAL PAYABLE AMOUNT : ₹  {{ totalPrice }}</h4>
          </div>
          <div class="buy">
            <button @click="purchase" class="button-77"
            :disabled="isPurchaseDisabled">
              Proceed to Pay
            </button>
          </div>
        </div>
      </div>
      <div v-else style="text-align: center; font-size: 50px; ">
        Nothing to show
      </div>
    </div>
  </div>
</template>


<script>
import axios from "axios";
export default {
  name: "Cart",
  data() {
    return {
      task: "",
      editTask: null,
      all_items: Object,
      cart:[],
      empty_cart : false,
    };
    
  },
  computed: {
    isPurchaseDisabled() {
    // Check if any item is out of stock
    return this.cart.some((data) => data.stock < data.item_count);
  },
    totalPrice() {
      // Calculate the total price using a computed property
      return this.cart.reduce((total, item) => {
        return total + item.price * item.item_count;
      }, 0);
    },
  },
  props:{
    cart_items:Array,
    userData:Object,
    data_for_cart:Object,
        // cart_items:[],
        // cartItems:[],
    },
//     created() {
//         const name  = this.$route.params.name;
        
//     console.log("Name parameter from route:", name);
// },

  mounted() {
    var count = 0
    console.log("aegf")

    const username = this.$route.params.name;
    axios.get(`http://127.0.0.1:5000/user/${username}/cart`)
      .then((response) => {
                
        if  (response.data == "empty"){
        this.empty_cart = true
        console.log(this.empty_cart)
        }
        else{
          this.cart = response.data
          console.log("response:::", this.cart);
          // for (var e in this.cart){
          //   count+=1
          //   // console.log(this.cart[e]["stock"],"stockkk")
          //   this.cart[e]["stock"] = localStorage.getItem(this.cart[e]["product_name"])
          //   console.log(this.cart[e]["stock"],localStorage.getItem(this.cart[e]["product_name"]))
          // }
          // console.log("response:::", this.cart);
        }
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
      });
  },
  methods:{
    async purchase(){
      const username = this.$route.params.name;
      const purchasing = this.cart
      console.log("cart",this.cart)
      axios.post(`http://127.0.0.1:5000/user/${username}/purchase`,{
            purchasing
        }).then((response) => {
          if (response.data == "out_of_stock"){
            alert("some items are out of stock !!")
            this.$router.push(`/user/${username}`)
          }
          else if (response.data=="successful"){
            const sucess = true
            console.log("payment sucess",sucess)
            alert("payment Successful")
            window.location.reload();
          }
        }).catch((error) => {
        console.error("Error fetching data:", error);
      });

    },
    addItem(data){
        const username = this.$route.params.name;
        console.log(data.item_count)
        axios.post(`http://127.0.0.1:5000/user/${username}/cart`,{
            data
        })
        if (data["item_count"] == 0){
          console.log(data["item_count"],"coiunijifjn")
          window.location.reload();

      }
    },
    goback(){
      this.$router.push(`/user/${this.$route.params.name}`)
    },
    decrement(data){
        data.item_count -=1 ;
        this.addItem(data)
    },
    increment(data){
        data.item_count +=1 ;
        this.addItem(data)
    },
    // decrement(data) {
    //   if (data.item_count > 1) {
    //     data.quantity -= 1;
    //     this.price -= data.price;
    //     // localStorage.setItem(product.item,product.quantity)
    //     // localStorage.setItem("total_item",this.total_item)
    //     // this.$emit('customEvent',this.total_item);
    //   }
  }
};
</script>

<style scoped>

.button-62 {
  background: linear-gradient(to bottom right, #EF4765, #FF9A5A);
  border: 0;
  border-radius: 12px;
  color: #FFFFFF;
  cursor: pointer;
  display: inline-block;
  font-family: -apple-system,system-ui,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
  font-size: 16px;
  font-weight: 500;
  line-height: 2.5;
  outline: transparent;
  padding: 0 1rem;
  text-align: center;
  text-decoration: none;
  transition: box-shadow .2s ease-in-out;
  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
  white-space: nowrap;
}

.button-62:not([disabled]):focus {
  box-shadow: 0 0 .25rem rgba(0, 0, 0, 0.5), -.125rem -.125rem 1rem rgba(239, 71, 101, 0.5), .125rem .125rem 1rem rgba(255, 154, 90, 0.5);
}

.button-62:not([disabled]):hover {
  box-shadow: 0 0 .25rem rgba(0, 0, 0, 0.5), -.125rem -.125rem 1rem rgba(239, 71, 101, 0.5), .125rem .125rem 1rem rgba(255, 154, 90, 0.5);
}
.cart_holder{
    padding: 3%;
}
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
</style>
<style scoped>
.to_purchase{
  margin: 30px;
  display: flex;
  justify-content: center; 
  text-align: center;
}
.total{
  position: relative;
  top: 17px;
  margin-right: 30px;
  font: bolder;
  font-family: cursive;
}

/* CSS */
.button-77 {
  align-items: center;
  appearance: none;
  background-clip: padding-box;
  background-color: initial;
  background-image: none;
  border-style: none;
  box-sizing: border-box;
  color: #000000;
  cursor: pointer;
  display: inline-block;
  flex-direction: row;
  flex-shrink: 0;
  font-family: Eina01,sans-serif;
  font-size: 18px;
  font-weight: 800;
  justify-content: center;
  line-height: 24px;
  margin: 0;
  min-height: 64px;
  outline: none;
  overflow: visible;
  padding: 15px 22px;
  pointer-events: auto;
  position: relative;
  text-align: center;
  text-decoration: none;
  text-transform: none;
  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
  vertical-align: middle;
  width: auto;
  word-break: keep-all;
  z-index: 0;
}

@media (min-width: 768px) {
  .button-77 {
    padding: 19px 32px;
  }
}

.button-77:before,
.button-77:after {
  border-radius: 80px;
}

.button-77:before {
  background-color: rgb(12, 113, 34);
  content: "";
  display: block;
  height: 100%;
  left: 0;
  overflow: hidden;
  position: absolute;
  top: 0;
  width: 100%;
  z-index: -2;
}

.button-77:after {
  background-color: initial;
  background-image: linear-gradient(92.83deg, #9aff26 0, #22b538 100%);
  bottom: 4px;
  content: "";
  display: block;
  left: 4px;
  overflow: hidden;
  position: absolute;
  right: 4px;
  top: 4px;
  transition: all 100ms ease-out;
  z-index: -1;
}

.button-77:hover:not(:disabled):after {
  bottom: 0;
  left: 0;
  right: 0;
  top: 0;
  transition-timing-function: ease-in;
}

.button-77:active:not(:disabled) {
  color: #000000;
}

/* .button-77:active:not(:disabled):after {
  background-image: linear-gradient(0deg, rgb(71, 107, 224), rgba(19, 19, 239, 0.2)), linear-gradient(92.83deg, #ff7426 0, #f93a13 100%);
  bottom: 4px;
  left: 4px;
  right: 4px;
  top: 4px;
} */

.button-77:disabled {
  cursor: default;
  opacity: .24;
}
</style>
