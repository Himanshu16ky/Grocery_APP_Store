import 'bootstrap/dist/css/bootstrap.css'
<script src="https://cdn.jsdelivr.net/gh/gitbrent/bootstrap4-toggle@3.6.1/js/bootstrap4-toggle.min.js"></script>

import { createRouter, createWebHashHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import UserDashbord from '../views/dashbord/userdashbord.vue'
import ManagerDashbord from '../views/dashbord/managerdashbord.vue'
import ca from '../components/managercreate/managercreate.vue'
import Login from '../views/login/login.vue'
import Rough from '../views/dashbord/rough.vue'
import Managercreate from '../components/managercreate/managercreate.vue'
import Manageritems from '../components/managercreate/manageritems.vue'
import Todo from '../views/dashbord/todo.vue'
import Cart from '../views/dashbord/cart.vue'
import Register from '../views/login/register.vue'
import Intro from '../components/intro.vue'


const routes = [
  {
    path: "/",
    component: Intro,
    props: true,
  },
  {
    // path: '/manager',
    path: "/manager/:username",
    component: ManagerDashbord,
    props: true,
  },
  {
    path: '/user/:username',
    name: 'userdashbord',
    component: UserDashbord
  },
  {
    path: '/login',
    name: 'login',
    component: Login
  },
  {
    path: '/register',
    name: 'register',
    component: Register
  },
  {
    path: '/rough',
    name: 'rough',
    component: Rough
  },
  {
    path: `/manager/:name/:item`,
    // path: `/manager`,
    name: 'managercreate',
    component: Manageritems
  },
  {
    path: '/:name',
    name: 'todo',
    component: Todo
  },
  {
    path: '/user/:name/cart',
    name: 'Cart',
    component: Cart,
    props:true,
    // props:(route) => ({
    //   data_for_cart: route.params.data_for_cart,
    // }),
  },

  // {
  //   path: '/api/receive_data',
  //   name: 'ca',
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  // }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
