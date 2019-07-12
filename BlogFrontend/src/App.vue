<template>
  <div>
    <app-header></app-header>
    <app-blog></app-blog>
    <app-footer></app-footer>
  </div>
</template>

<script>
import Header from "./components/Header.vue";
import Footer from "./components/Footer.vue";
import ShowBlog from "./components/ShowBlog.vue";

export default {
  components: {
    "app-header": Header,
    "app-footer": Footer,
    "app-blog": ShowBlog
  },
  data() {
    return {};
  }
};
</script>

<style>
</style>
