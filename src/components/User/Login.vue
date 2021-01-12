<template>
  <v-form>
    <v-container>
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
          <span v-if="!$v.password.required && passFocus" style="color: red"
            >Please enter a password</span
          >
        </v-col>
        <v-col cols="3"> </v-col>
      </v-row>

      <v-row>
        <v-col cols="3"> </v-col>
        <v-col cols="6">
          <v-btn block depressed v-on:click="login">Login </v-btn>
        </v-col>
        <v-col cols="3"> </v-col>
      </v-row>
    </v-container>
  </v-form>
</template>
<script>
import { required, minLength, email } from "vuelidate/lib/validators";
import Axios from "axios";

export default {
  data: () => ({
    user: "",
    email: "",
    password: "",
    emailFocus: false,
    passFocus: false,
  }),
  validations: {
    email: {
      required,
      email,
    },
    password: {
      required,
    },
  },
  methods: {
    login: function () {
      if (!this.$v.$invalid) {
        Axios.post("http://127.0.0.1:8000/api/user/loginCheck/", {
          email: this.email,
          password: this.password,
        })
          .then((response) => {
            this.user = response.data;
            Axios.get(`http://127.0.0.1:8000/api/fee/`, {}).then((response) => {
              let user1 = this.user;

              this.user.fees = response.data.results.filter(function (fee) {
                return fee.user == user1.id && fee.totalFees != 0;
              });
            });

            Axios.get(
              `http://127.0.0.1:8000/api/card/${this.user.card}/`,
              {}
            ).then((response) => {
              this.user.cardNumber = response.data.cardNumber;
              this.user.cardType = response.data.cardType;
              this.user.expiryDate = response.data.expiryDate;
              this.$store.state.user = this.user;
            });
          })
          .catch((error) => console.log(error));

        this.$router.push({ path: "/" });
      } else {
        (this.emailFocus = true), (this.passFocus = true);
      }
    },
  },
};
</script>