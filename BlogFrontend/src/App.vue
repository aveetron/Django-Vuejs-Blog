<template>
  <div>
    <app-header></app-header>
    <app-topic></app-topic>
    <app-footer></app-footer>
  </div>
</template>

<script>
import Header from "./components/Header.vue";
import Footer from "./components/Footer.vue";
import topic from "./components/topic.vue";

export default {
  components: {
    "app-header": Header,
    "app-footer": Footer,
    "app-topic": topic
  },
  data() {
    return {};
  }
};
</script>

<style>
</style>
