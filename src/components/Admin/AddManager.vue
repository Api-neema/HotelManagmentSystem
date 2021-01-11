<template>
  <v-form>
    <v-container>
      <v-row>
        <v-col cols="3"> </v-col>
        <v-col cols="6">
          <v-text-field
            @focusout="fnameFocus = true"
            v-model="firstName"
            label="First name"
          ></v-text-field>
          <span
            style="color: red"
            v-if="(!$v.firstName.alpha || !$v.firstName.required) && fnameFocus"
            >Please enter a valid name</span
          >
        </v-col>
        <v-col cols="3"> </v-col>
      </v-row>
      <v-row>
        <v-col cols="3"> </v-col>
        <v-col cols="6">
          <v-text-field
            @focusout="lnameFocus = true"
            v-model="lastName"
            label="Last name"
          ></v-text-field>
          <span
            style="color: red"
            v-if="(!$v.lastName.alpha || !$v.lastName.required) && lnameFocus"
            >Please enter a valid name</span
          >
        </v-col>
        <v-col cols="3"> </v-col>
      </v-row>
      <v-row>
        <v-col cols="3"> </v-col>
        <v-col cols="6">
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
        </v-col>
        <v-col cols="3"> </v-col>
      </v-row>
      <v-row>
        <v-col cols="3"> </v-col>
        <v-col cols="6">
          <v-text-field
            @focusout="passFocus = true"
            v-model="password"
            label="Password"
          ></v-text-field>
          <span style="color: red" v-if="!$v.password.required && passFocus"
            >Please enter a valid password</span
          >
        </v-col>
        <v-col cols="3"> </v-col>
      </v-row>

      <v-row>
        <v-col cols="3"> </v-col>
        <v-col cols="6">
          <v-btn block depressed v-on:click="register">Register </v-btn>
        </v-col>
        <v-col cols="3"> </v-col>
      </v-row>
    </v-container>
  </v-form>
</template>
<script>
import Axios from "axios";
import { required, alpha, email, numeric } from "vuelidate/lib/validators";

export default {
  data() {
    return {
      firstName: "",
      lastName: "",
      email: "",
      password: "",

      fnameFocus: false,
      lnameFocus: false,
      emailFocus: false,
      passFocus: false,
    };
  },
  validations: {
    firstName: {
      alpha,
      required,
    },
    lastName: {
      alpha,
      required,
    },

    email: {
      required,
      email,
    },
    password: {
      required,
    },
  },
  methods: {
    register: function () {
      let user = {
        firstName: this.firstName,
        lastName: this.lastName,
        password: this.password,
        email: this.email,
        type: "manager",
      };
      if (!this.$v.$invalid) {
        Axios.post("http://127.0.0.1:8000/api/user/", user)
          .then((response) => console.log(response))
          .catch((error) => console.log(error));
      } else {
        (this.fnameFocus = true),
          (this.lnameFocus = true),
          (this.emailFocus = true),
          (this.passFocus = true);
      }
    },
  },
};
</script>
