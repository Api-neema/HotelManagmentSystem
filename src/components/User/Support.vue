<template>
  <v-form>
    <v-container>
      <p>Tell us your issue and we'll respond to you as soon as possible</p>
      <v-textarea
        v-model="query"
        name="input-7-1"
        label="Write your problem here"
      ></v-textarea>
      <v-btn @click="submit">Submit</v-btn>
    </v-container>
  </v-form>
</template>
<script>
export default {
  data: () => ({
    query: "",
  }),
  methods: {
    submit: function () {
      console.log(this.query);
      this.query = "";
    },
  },
};
</script>