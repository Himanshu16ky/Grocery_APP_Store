// import { createApp } from 'vue'
// import App from './App.vue'
// import router from './router'

// createApp(App).use(router).mount('#app')
// import "bootstrap4-toggle/js/bootstrap4-toggle.min.js";

import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle.min.js';
import '@popperjs/core/dist/umd/popper.min.js';
import "bootstrap4-toggle/css/bootstrap4-toggle.min.css";

import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap/dist/js/bootstrap.js';

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import LoadScript from "vue-plugin-load-script";

import 'bootstrap/dist/css/bootstrap.min.css';


import axios from 'axios'
import VueRouter from 'vue-router'
// import $ from 'jquery';
// window.$ = window.jQuery = $;


// Vue.use(VueRouter)
// const routes = [
//     {
//       path: '/carousel-new',
//       component: YourCarouselComponent, // Replace with the actual component you want to display
//     },
//     // Other routes...
//   ]
//   const router = new VueRouter({
//     routes,
//   })
  
//   export default router


// import Vue from 'vue';
// export const EventBus = new Vue();

// const managerData = {
//     username: res.data.username,
//     password: this.password,
//   };
//   EventBus.$emit('managerData', managerData);

window.$ = window.jQuery = require('jquery');
// window.bootstrap = require('bootstrap/dist/js/bootstrap.bundle.js');
window.bootstrap = require('bootstrap/dist/js/bootstrap.bundle.js');

const app = createApp(App);
app.use(LoadScript);
app.use(router);

app.mount("#app");