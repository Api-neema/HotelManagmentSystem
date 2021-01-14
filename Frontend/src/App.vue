<template>
  <div>
    <Navbar />
    <router-view />
  </div>
</template>

<script>
import { store } from "./store";
import Navbar from "./components/Navbar";

export default {
  store: store,
  name: "App",
  components: {
    Navbar,
  },

  data: () => ({
    //
  }),
};
</script>
<style >
body {
  font-family: "calibri";
}
</style>
