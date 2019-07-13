<template>
  <div>
    <h2>All Blogs</h2>
    <div v-for="blog in blogs">
      <h3>{{blog.title}}</h3>
      <article>{{blog.description}}</article>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      blogs: []
    };
  },
  created() {
    this.$http.get("http://127.0.0.1:8000/api/blog/").then(function(data) {
      this.blogs = data.body.slice(0, 10);
      console.log(data);
    });
  }
};
</script>

<style scoped>
h3,
h2,
article {
  text-align: center;
}
</style>
