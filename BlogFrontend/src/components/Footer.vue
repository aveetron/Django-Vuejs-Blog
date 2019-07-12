<template>
  <div class="footer">
    <p>{{formal_message}}</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      formal_message: "copy right"
    };
  }
};
</script>

<style scoped>
.footer {
  background: lightblue;
  padding: 10px;
}
p {
  color: black;
  text-align: center;
}
</style>
