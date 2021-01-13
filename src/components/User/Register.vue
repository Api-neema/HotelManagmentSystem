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
          <v-text-field
            @focusout="numberFocus = true"
            v-model="mobileNumber"
            label="Mobile Number"
          ></v-text-field>
          <span
            style="color: red"
            v-if="
              (!$v.mobileNumber.numeric || !$v.mobileNumber.required) &&
              numberFocus
            "
            >Please enter a valid mobile number</span
          >
        </v-col>
        <v-col cols="3"> </v-col>
      </v-row>
      <v-row>
        <v-col cols="3"> </v-col>
        <v-col cols="6">
          <v-text-field
            @focusout="genderFocus = true"
            v-model="gender"
            label="Gender"
            placeholder="Male/Female"
          ></v-text-field>
          <span
            style="color: red"
            v-if="(!$v.gender.required || !$v.gender.alpha) && genderFocus"
            >Please enter a valid gender</span
          >
        </v-col>
        <v-col cols="3"> </v-col>
      </v-row>
      <v-row>
        <v-col cols="3"> </v-col>
        <v-col cols="6">
          <v-text-field
            @focusout="dobFocus = true"
            v-model="dateOfBirth"
            label="Date of Birth"
            placeholder="dd/mm/yyyy"
          ></v-text-field>
          <span style="color: red" v-if="!$v.dateOfBirth.required && dobFocus"
            >Please enter a valid date of birth</span
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
      gender: "",
      mobileNumber: "",
      dateOfBirth: "",
      emailFocus: false,
      fnameFocus: false,
      lnameFocus: false,
      passFocus: false,
      genderFocus: false,
      numberFocus: false,
      dobFocus: false,
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
    gender: {
      required,
      alpha,
    },
    mobileNumber: {
      required,
      numeric,
    },
    dateOfBirth: {
      required,
    },
  },
  methods: {
    register: function () {
      let user = {
        firstName: this.firstName,
        lastName: this.lastName,
        password: this.password,
        mobileNumber: this.mobileNumber,
        gender: this.gender,
        email: this.email,
        dateOfBirth: `${this.dateOfBirth}`,
        type: "user",
      };

      if (!this.$v.$invalid) {
        Axios.post("http://127.0.0.1:8000/api/user/", user)
          .then((response) => {
            console.log(response.data);
            let fee = {
              user: response.data.id,
              room: 0,
              totalFees: 0,
              adminFees: 0,
            };
            Axios.post("http://127.0.0.1:8000/api/fee/", fee)
              .then((response) => console.log(response))
              .catch((error) => console.log(error));
          })
          .catch((error) => console.log(error));
        this.$router.push({ path: "/" });
      } else {
        (this.emailFocus = true),
          (this.fnameFocus = true),
          (this.lnameFocus = true),
          (this.passFocus = true),
          (this.genderFocus = true),
          (this.numberFocus = true),
          (this.dobFocus = true);
      }
    },
  },
};
</script>
