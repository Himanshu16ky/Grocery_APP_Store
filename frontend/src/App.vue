<template>
  <div>
    <router-view />
    <!-- <Intro/> -->
  </div>
</template>

<script>
import UserNavbar from "./components/navbar/usernavbar.vue";
import Intro from "./components/intro.vue";

export default {
  name: "App",
  components: {
    UserNavbar,
    Intro,
  },
};
</script>
