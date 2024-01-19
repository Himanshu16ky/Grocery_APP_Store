<template>
  <div class="boss">
    <UserNavbar
      :total_items="total_item"
      :total_price="price"
      @toCart="toCart"
      @search="handleSearch"
      @selectPriceRange="handlePriceRangeSelection"
    />

    <!-- <Cart
  :is-open="isCartOpen"
  :cart_items="userData"
  @remove="removeItemFromCart"
  @purchase="handlePurchase"
  @close="toggleCart"
/> -->
    <!-- :dataProp="dataToSend" -->
    <!-- {{ localStorage.getItem("total_item") }} -->
    <!-- <div
      class="category-card"
      v-for="(category, categoryName) in all_products"
      :key="categoryName"
    > -->
    <div
      class="category-card"
      v-for="(category, categoryName) in (searchQuery || prrr ? filteredProducts : all_products)"
      :key="categoryName"
    >
      <h1 style="font-family: Comic Sans MS;
    font-weight: bolder;
      position: -webkit-sticky;
      position: sticky; ">
        {{ categoryName }}
      </h1>
      <div class="product-list"       
>
        <div
          class="product-card"
          v-for="product in category"
          :key="product.item"
        >
          <div
            class="product-img"
            style="
              justify-content: center;
              height: 180px;
              width: 190px;
              background-color: white;
              position: relative;
              border: 12px sold green;
              border-radius: 5px;
              top: -9px;
            "
          >
            <img class="image"
              style="
                height: 100%;
                width: 100%;
                border-radius: 10px;
                display: block;
                margin-left: auto;
                margin-right: auto;
              "
              :src="`${publicPath}${product['image']}`" :alt="`${product['item']}`"
            />
          </div>
          <div class="product-info" style="">
            <strong >{{ product.item }}</strong>
            <div style="
            position: relative;
            top: 8px;
            display: flex;
      justify-content: space-between;">
              <p style="width: 40%;">
              {{ product.pack_size }}
              <span style="font-size: small; text-align: left">{{
                product.unit.slice(3)
              }}</span>
            </p>
            <p style="width: 40%;">
              ₹ {{ product.price }}
              <span style="font-size: small; text-align: left">{{
                product.unit.slice(2)
              }}</span>
            </p>
            </div>
          </div>
          
          <div v-if=" product.stock != 0 && product.stock + 1  - product.quantity > 0">
            <form @submit="addItem(product)">
              <div class="button-holder">
                <div
                  style="position: relative; right: 100px"
                  v-if="product.added"
                >
                  <div class="quantity-control">
                    <button
                      type="submit"
                      @click="decrement(product)"
                      style="width: 30px; background-color: rgb(243, 32, 13)"
                    >
                      -
                    </button>
                    <span style="position: relative; top: -50px; left: 100px">{{
                      product.quantity
                    }}</span>
                    <button
                      type="submit"
                      @click="increment(product)"
                      style="width: 30px"
                    >
                      +
                    </button>
                  </div>
                </div>
                <button style="color: white;"
                 v-if=" ! product.added && product.stock>0" @click="addToCart(product)" >
                  ADD
                </button>
                <!-- remove above second condition to show add -->
              </div>
            </form>
          </div>
          <div
          v-else
            class="out_of_stock"
          >
            OUT OF STOCK
          </div>
          
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import UserNavbar from "../../components/navbar/usernavbar.vue";
// import Cart from "./cart.vue";
import { computed } from "vue";
import Vue from 'vue';
import { ref } from 'vue';

export default {
  name: "userdashbord",
  data() {
    return {
      cart_display: false,
      cartItems: [],
      all_products: {},
      total_item: 0,
      price: 0,
      prrr: "",
      publicPath: process.env.BASE_URL,
      lastSegment: "",
      data_for_cart: null,
      searchQuery: "",
    filteredProducts: {},
    selectedPriceRange: null,
      // for_cart:Object,
    };
  },
  computed: {},
  components: {
    UserNavbar,
  },
  // watch: {
  // selectedPriceRange(newValue) {
  //   console.log("4we")
  //   // Handle the selected price range change
  //   this.filterItemsByPrice(newValue);
  // },
// },
  mounted() {
    if(this.check()){
     this.get_itms()
     console.log("data got from server")
    }
  },

  methods: {
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
    get_itms(){
      var username = localStorage.getItem("username");
    var total_items = localStorage.getItem("total_item");

    const currentUrl = window.location.href;
    const urlSegments = currentUrl.split("/");
    this.lastSegment = urlSegments[urlSegments.length - 1];

    axios
      .get(`http://127.0.0.1:5000/user/${this.lastSegment}`)
      .then((response) => {
        const shopData = response.data[0];
        const userData = response.data[1];
        this.data_for_cart = userData;
        // console.log("shop data  :::",shopData)
        // console.log("user data  :::", userData);
        // console.log("shop data  :::", shopData);
        // const user_list = userData.split(',');
        // const count = 0;
        // for (const u in user_list){
        //   localStorage.setItem(u,) 
        // }
        // var count = 0
        // for (const i in shopData){
        // count+=1
        //   console.log(shopData)
        // }
        for (const category in shopData) {
          this.all_products[category] = shopData[category].map((product) => {
            // console.log(shopData[category])
            // shopData[category].forEach(item=>{
            // localStorage.setItem(item.item,item.stock)
            //   count+=1
            // console.log(item,count)
            // })
            localStorage.setItem(product["item"], product["stock"]);
            // console.log(product["item"], product["stock"]);
            const userDataProduct = userData.find(
              (item) => item.item_id === product.item_id
            );
            this.price += userDataProduct
              ? userDataProduct.price * userDataProduct.item_count
              : 0;
            this.total_item += userDataProduct ? userDataProduct.item_count : 0;
            return {
              ...product,
              added: userDataProduct ? true : false,
              // total_item_price: userDataProduct ? userDataProduct.price * userDataProduct.item_count : 0,
              quantity: userDataProduct ? userDataProduct.item_count : 0,
            };
          });
          // console.log(category,"-------",this.all_products.category.quantity)
        }
        console.log("all_products",this.all_products);
        // this.total_item = product.total_item_price
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
      });
    },
    handlePriceRangeSelection(range) {
      // range = range.slice(1)
    console.log('Selected Price Range:', range);
    this.filterItemsByPrice(range);
    
    // Implement your logic to filter items based on the selected price range
    // You may need to update the 'all_products' and 'filteredProducts' accordingly
  },
  filterItemsByPrice(priceRange) {
    // Implement your logic to filter items based on the selected price range
    // Update 'filteredProducts' accordingly
    if (priceRange > 0) {
      // this.searchQuery =  " ";
      this.prrr = " ";
      this.filteredProducts = {};
      console.log(priceRange)
      for (const category in this.all_products) {
        const filteredCategory = this.all_products[category].filter(
          (product) => product.price <  parseInt(priceRange)
        );

        if (filteredCategory.length > 0) {
          this.filteredProducts[category] = filteredCategory;
        }
      }
    } else {
      this.filteredProducts = { ...this.all_products };
    }
    console.log('All Products:', this.all_products);
console.log('Filtered Products:', this.filteredProducts);
// this.searchQuery =  "";

  },
  
    handleSearch(query) {
      if(query == null || query ==""){
        console.log("null returned")
        this.searchQuery = "";
        return "xdf"
      }
      else{
        console.log("handelSearch query = ",query);
      this.searchQuery = query;
      this.performSearch();
      }
    },
    //the new code  start
    performSearch() {
      try{
        this.filteredProducts = {};
    this.searchQuery = this.searchQuery.toLowerCase()
    for (const category in this.all_products) {
      const filteredCategory = this.all_products[category].filter((product) => {
        const lowercaseItem = (product.item || "").toLowerCase();
      const lowercaseCategory = (category || "").toLowerCase();
      //   console.log('Item:', product.item.toLowerCase());
      // console.log('Category:', category.toLowerCase());
      // console.log('Match:', product.item.toLowerCase().includes(this.lowercaseSearchQuery) || category.toLowerCase().includes(this.lowercaseSearchQuery));
        return (
          lowercaseItem.includes(this.searchQuery) ||
          lowercaseCategory.includes(this.searchQuery)
        );
      });

      if (filteredCategory.length > 0) {
        this.filteredProducts[category] = filteredCategory;
      }
      // else{
      //   this.filteredProducts = { ...this.all_products };
      // }
    }
    console.log('Filtered Products:', this.filteredProducts);
    if (this.searchQuery) {
      this.suggestions = this.findSuggestions();
    } else {
      this.suggestions = [];
    }

      }
      catch{
        this.performSearch()
      }
      
    // console.log('Search Query:', this.lowercaseSearchQuery);
    // const lowercaseSearchQuery = (this.searchQuery || "").toLowerCase(); 

  },
  findSuggestions() {
    const suggestions = [];

    // Iterate over your data to find suggestions
    for (const category in this.all_products) {
      const categoryMatches = this.all_products[category].some((product) =>
        product.item.toLowerCase().includes(this.searchQuery)
      );

      if (categoryMatches) {
        suggestions.push(category);
      }

      const productMatches = this.all_products[category].filter((product) =>
        product.item.toLowerCase().includes(this.searchQuery)
      );

      suggestions.push(...productMatches.map((product) => product.item));
    }

    return suggestions;
  },

  // the new code end
    toCart() {
      console.log(this.lastSegment);
      //   const currentUrl = window.location.href;
      // const urlSegments = currentUrl.split("/");
      // this.lastSegment = urlSegments[urlSegments.length - 1];
      //   this.$router.push({path : `/user/${this.lastSegment}/cart`,
      //   params:{name:this.lastSegment},
      // })
      this.$router.push({
        name: "Cart",
        params: { name: this.lastSegment },
        props: { data_for_cart: this.data_for_cart },
      });
    },
    addItemToCart(product) {
      this.cartItems.push(product);
      this.price += product.price;
    },

    removeItemFromCart(index) {
      this.price -= this.cartItems[index].price;
      this.cartItems.splice(index, 1);
    },

    // Method to toggle the cart visibility
    toggleCart() {
      this.isCartOpen = !this.isCartOpen;
    },
    async addItem(product) {
    console.log("search for item _ id",product);
      var username = this.lastSegment;
      await axios
        .post(`http://127.0.0.1:5000/user/${username}`, {
          item: product,
        })
        .then((response) => {
          // this.for_cart.push(product)
        })
        .catch((error) => {
          console.error("Error fetching data:", error);
        });
      console.log(this.lastSegment, " added ", product);
    },
    // async removeItem(product){
    //   var username = localStorage.getItem("username");
    //   await axios.delete(`http://127.0.0.1:5000/user/${username}/${product.item}`)
    //   .then(response =>{
    //     // this.for_cart.push(product)
    //     console.log(response.data,"removed")
    //   })
    //   .catch((error) => {
    //     console.error("Error fetching data:", error);
    //   });
    // },
    addToCart(product) {
      // console.log(product)
      console.log("user data : ",this.userData);
      
      
      // localStorage.setItem(product.item,product.quantity)
      this.addItem(product);
      product.added = true;
      product.quantity += 1;
      console.log("product.quantity",product.quantity)
      this.price += product.price;
      this.total_item += product.quantity;

      // localStorage.setItem("total_item",this.total_item)
      // this.$emit('customEvent',this.total_item);
      console.log("total_item",this.total_item);
      var username = this.lastSegment;
      axios
        .post(`http://127.0.0.1:5000/user/${username}`, {
          item: product,
        })
        .then((response) => {
          // this.for_cart.push(product)
        })
        .catch((error) => {
          console.error("Error fetching data:", error);
        });
      console.log(this.lastSegment, " added ", product);
    },
    increment(product) {
      if (product.stock   - product.quantity > 0){
        
      this.total_item += 1;
      this.price += product.price;
      }
      product.quantity += 1;
      // localStorage.setItem(product.item,product.quantity)
      // localStorage.setItem("total_item",this.total_item)
      // this.$emit('customEvent',this.total_item);
    },
    decrement(product) {
      if (product.quantity > 1) {
        product.quantity -= 1;
        this.price -= product.price;
        this.total_item -= 1;
        // localStorage.setItem(product.item,product.quantity)
        // localStorage.setItem("total_item",this.total_item)
        // this.$emit('customEvent',this.total_item);
      } 
      else {
        this.total_item -= 1;
        this.price -= product.price;
        // localStorage.setItem(product.item,product.quantity)
        // localStorage.setItem("total_item",this.total_item)
        product.added = false;
        product.quantity = 0;
        this.addItem(product);
        // this.$emit('customEvent',this.total_item);
      }
    },
  },
};
</script>

<style scoped>
body{
  background-color: grey;
  margin: 0;
  padding: 0;
}
.category-card[data-v-fa69a920] {
    border-color: rgb(0, 0, 0);
    background-color: rgb(12, 61, 50);
}
/* .image {
transition: 1s ease;
}

.image :hover{
-webkit-transform: scale(0.8);
-ms-transform: scale(0.8);
transform: scale(0.8);
transition: 1s ease;
} */
.out_of_stock {
  position: relative;
  top: -2px;
  text-align: center;
  font: sans-serif;
  background-color: rgba(255, 0, 0, 0.853);
  border-radius: 10px;
  width: 100%;
  height: 120%;
  /* border: 2px solid rgb(3, 0, 11); */
}
.out_of_stock:hover {
  cursor: pointer;
  position: relative;
}
.button-holder {
  position: relative;
  top: 50px;
}
</style>

<style scoped>
/* h1{
  size: 100px;
} */

::-webkit-scrollbar {
  display: none;
}
.boss {
  width: 94%;
  position: relative;
  left: 3%;
}
.category-card {
  height: 470px;
  border: 1px solid #ccc;
  padding: 10px;
  margin: 10px;
  border-radius: 30px;
  overflow: auto;
  white-space: nowrap;
}

.product-list {
  display: flex;
  flex-direction: row;
  position: relative;
  top: 20px;
}

.product-card {
  /* width: 25rem; */
  border-radius: 10px;
  border: 1px solid #ccc;
  padding: 5px;
  margin: 5px;
  margin-top: 20px;
  width: 200px;
  text-align: center;
  display: grid;
  place-content: center;
  color: #ffffff;
  background-color: #15928a;
  background-color: #018b7e;
  /* color: #15928a; */
  font-size: 1.2rem;
  height: 20rem;
  min-width: 13rem;
}
button {
  position: relative;
  top: -50px;
  font-size: 15px;
  height: 30px;
  width: 45px;
  background-color: #00cc00;
  border-radius: 5px;
  border: none;
  /* display: flex; */
  /* flex-direction: column; */
}
.quantity-control {
  /* display: flex; */
  
  align-items: center;
}

.quantity-control button {
  font-size: 15px;
  height: 30px;
  width: 45px;
  /* top: -40px; */
  left: 100px;
  display: inline-block;
  margin: 0 5px;
}
.product-info {
  position: relative; 
  /* top: 22px; */
  /* display: flex; */
  /* position: relative;
  top: -10px; */
  /* margin-bottom: 10px; */
}
p,
span {
  text-align: left;
  position: relative;
  /* top: 5px; */
}
</style>
