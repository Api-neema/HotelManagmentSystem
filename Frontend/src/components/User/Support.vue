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
        let feedback = {
          userName:
            this.$store.state.user.firstName + this.$store.state.user.lastName,
          email: this.$store.state.user.email,
          feedback: this.query,
        };
        Axios.post("http://127.0.0.1:8000/api/feedback/", feedback)
          .then((response) => {
            alert("Request submitted successfully");
          })
          .catch((error) => console.log(error));
      } else {
        this.queryFocus = true;
      }
    },
  },
};
</script>