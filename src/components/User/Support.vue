<template>
  <v-form>
    <v-container>
      <p>Tell us your issue and we'll respond to you as soon as possible</p>
      <v-textarea
        @focusout="queryFocus = true"
        v-model="query"
        name="input-7-1"
        label="Write your problem here"
      ></v-textarea>
      <span style="color: red" v-if="!$v.query.required && queryFocus"
        >Please enter a valid query</span
      >
      <v-btn @click="submit">Submit</v-btn>
    </v-container>
  </v-form>
</template>
<script>
import { required } from "vuelidate/lib/validators";
import Axios from "axios";

export default {
  data: () => ({
    query: "",
    queryFocus: false,
  }),
  validations: {
    query: {
      required,
    },
  },
  methods: {
    submit: function () {
      if (!this.$v.$invalid) {
        Axios.post("http://127.0.0.1:8000/api/user/loginCheck/", {})
          .then((response) => {
            this.user = response.data;
            console.log(response);
            this.$store.state.user = this.user;
          })
          .catch((error) => console.log(error));
      } else {
        this.queryFocus = true;
      }
    },
  },
};
</script>