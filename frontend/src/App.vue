<template>
  <router-view></router-view>
</template>

<script>
import HomeView from "@/views/HomeView.vue"
import ResultView from "@/views/ResultView.vue"

export default {
  name: "App",
  components: {
    HomeView,
    ResultView
  },
  mounted() {
    document.title = "NeuralStyle";
  }
}
</script>

<style>
* {
  margin: 0;
  padding: 0;
}

body {
  background: linear-gradient(100deg, #2b5876 , #4e4376);
}

#app {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #53789c;
}
</style>
