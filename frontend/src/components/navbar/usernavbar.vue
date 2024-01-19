<template>
  <div style="background-color: red">
    <nav class="navbar navbar-light bg-light">
      <div class="container-fluid">
        <a class="navbar-brand" style="margin-left: 10px"
          ><strong><h1>SnapShop</h1></strong></a
        >
        <div class="mx-auto">
          <form class="d-flex align-items-center">
            <div
              class="input-group"
              style="background: #15928a;
              border: 2px solid black; border-radius: 30px
              "
            >
              <!-- <input
                class="form-control me-2 search-bar"
                type="search"
                placeholder="Search"
                aria-label="Search"
                style="border: none"
              /> -->
              <input
                v-model="searchQuery"
                class="form-control me-2 search-bar"
                type="search"
                placeholder="Search"
                aria-label="Search"
                style="border: none"
              />
              <button
                class="searchbutton"
                style="
                  border: none;
                  border-radius: 50px;
                  width: 52px;
                "
                @click="performSearch"
              >
                <img
                  style="border-radius: 0px;
                  width:40px;
                  height:40px;
                  position: relative;
                  "
                  src="../../assets/logo.png"
                  alt="../../assets/logo.png"
                  
                  class="d-inline-block align-text-top"
                />
              </button>
            </div>
          </form>
        </div>
        <div
          class="d-flex justify-content-end align-items-center ml-auto bntholder"
        >
          <button
            style="margin: 10px"
            class="btn btn-outline-success"
            type="submit"
            @click="logout()"
          >
            <img style="height: 30px" src="../../assets/profile.png" alt="" />
            Logout
          </button>
          <button
            style="margin: 10px; display: flex"
            class="btn btn-outline-success"
            type="submit"
            @click="toCart"
          >
            <!--  @custom-event="handleChildData" -->
            <img src="../../assets/trolley.png" alt="" width="35" height="34" />
            <div style="text-align: center; font-size: 12px" type="submit">
              {{ total_items }} items <br />
              {{ total_price }} ₹
            </div>
            <br />
          </button>

          <!-- Example split danger button -->
          <div class="btn-group">
            <button
              type="button"
              class="btn btn-success dropdown-toggle"
              data-bs-toggle="dropdown"
              aria-haspopup="true"
              aria-expanded="false"
            >
              {{ selectedFilter }}
            </button>
            <ul class="dropdown-menu">
              <li><a class="dropdown-item" @click="selectPriceRange('10')">{{'< 10'}}</a></li>
              <li><a class="dropdown-item" @click="selectPriceRange('50')">{{'< 50'}}</a></li>
              <li><a class="dropdown-item" @click="selectPriceRange('100')">{{'< 100'}}</a></li>
              <li><hr class="dropdown-divider" /></li>
              <li><a class="dropdown-item" @click="selectPriceRange('0')">None</a></li>
            </ul>
          </div>

        </div>
      </div>
    </nav>
  </div>
</template>

<script>
export default {
  name: "UserNavbar",
  props: {
    total_items: Number,
    total_price: Number,
    // cart_items:[],
  },
  data() {
    return {
      searchQuery: "",
      suggestions: [],
      selectedFilter: 'Filter',
    };
  },  
  computed: {
    // intersection() {
    //   if(this.selectedFilter != 'Filter'){
    //     this.searchQuery= "";
    //   }
    //   if(this.searchQuery != ''){
    //     this.selectedFilter= "Filter";
    //   }
      
    // },
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
    toCart() {
      this.$emit("toCart");
    },
    selectPriceRange(range) {
      if(this.searchQuery != ''){
        this.searchQuery= "";
        
      }
      this.selectedFilter = "<"+range;
      if (range == 0){
        this.selectedFilter = "Filter"
      }
      this.$emit("selectPriceRange", range);
    },
    performSearch() {
      if(this.selectedFilter != 'Filter'){
        this.selectedFilter = 'Filter';
      }
      console.log("from navbar", this.searchQuery)
      this.searchQuery = this.searchQuery.trim();
      // if (this.searchQuery != null && this.searchQuery != ""){
        this.$emit("search", this.searchQuery);
      // }
    },
  },
};
</script>
<style scoped>
* {
  font-family: Comic Sans MS;
  font-weight: bolder;
}
.btn{
  border: 2px solid #15928a;
}
.mx-auto {
  max-width: 500px;
  flex-grow: 1;
}
.navbar-brand {
  font-size: 250%;
}
.container-fluid{
  background-color:#d0f0ee;
}
.search-bar {
  background: #15928a;
  flex: 1;
  height: 20px;
  /* border: 2px solid black; */
  border-radius: 30px;
  padding: 24px 20px;
  font-size: 20px;
  /* color: #cccc; */
}
input:focus {
  outline: none;
}
.bntholder {
  margin-right: 10px;
}
img {
  padding: 2px;
  margin-right: 10px;
}
</style>
