<template>
  <div class="header">
    <h1>{{blog_name}}</h1>
  </div>
</template>

<script>
export default {
  data() {
    return {
      blog_name: "avee blog"
    };
  }
};
</script>

<style scoped>
.header {
  background: lightgreen;
  padding: 10px;
}
h1 {
  text-align: center;
  color: black;
}
</style>
