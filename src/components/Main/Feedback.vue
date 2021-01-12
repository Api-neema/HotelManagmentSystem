<template>
  <v-container>
    <v-row>
      <v-col cols="3">
        <div class="title1">GOT SOME FEEDBACK?</div>
      </v-col>
      <v-col cols="1"></v-col>
      <v-col cols="8">
        <v-form ref="form" lazy-validation>
          <v-text-field
            @focusout="nameFocus = true"
            v-model="name"
            label="Name"
          ></v-text-field>
          <span style="color: red" v-if="!$v.name.required && nameFocus"
            >Please enter a valid name</span
          >

          <v-text-field
            @focusout="emailFocus = true"
            v-model="email"
            label="E-mail"
          ></v-text-field>
          <span
            style="color: red"
            v-if="(!$v.email.email || !$v.email.required) && emailFocus"
            >Please enter a valid email</span
          >
          <v-textarea
            @focusout="feedFocus = true"
            style="margin-left: -12px"
            name="input-7-1"
            background-color="white"
            filled
            label="Feedback"
            auto-grow
            value=""
            v-model="feedback"
          ></v-textarea>
          <span style="color: red" v-if="!$v.feedback.required && feedFocus"
            >Please enter a valid feedback</span
          >

          <v-btn color="success" class="mr-4" @click="send"> Send </v-btn>
        </v-form>
      </v-col>
    </v-row>
  </v-container>
</template>
<style scoped>
.title1 {
  font-weight: bold;
  font-size: 50px;
}
</style>
<script>
import { required, alpha, email } from "vuelidate/lib/validators";
import Axios from "axios";

export default {
  data: () => ({
    name: "",
    email: "",
    feedback: "",
    nameFocus: false,
    emailFocus: false,
    feedFocus: false,
  }),
  validations: {
    name: { required },
    email: {
      required,
      email,
    },
    feedback: {
      required,
    },
  },

  methods: {
    send() {
      if (!this.$v.$invalid) {
        let feedback = {
          userName: this.name,
          email: this.email,
          feedback: this.feedback,
        };
        Axios.post("http://127.0.0.1:8000/api/feedback/", feedback)
          .then((response) => {
            console.log(response);
          })
          .catch((error) => console.log(error));
      } else {
        (this.nameFocus = true)((this.emailFocus = true)),
          (this.feedFocus = true);
      }
    },
  },
};
</script>