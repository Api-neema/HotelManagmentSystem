<template>
  <v-form v-model="valid">
    <v-container>
      <v-row>
        <v-col cols="3"> </v-col>
        <v-col cols="6">
          <v-text-field
            v-model="firstName"
            :rules="nameRules"
            label="First name"
            required
          ></v-text-field>
        </v-col>
        <v-col cols="3"> </v-col>
      </v-row>
      <v-row>
        <v-col cols="3"> </v-col>
        <v-col cols="6">
          <v-text-field
            v-model="lastName"
            :rules="nameRules"
            label="Last name"
            required
          ></v-text-field>
        </v-col>
        <v-col cols="3"> </v-col>
      </v-row>
      <v-row>
        <v-col cols="3"> </v-col>
        <v-col cols="6">
          <v-text-field
            v-model="password"
            label="Password"
            required
          ></v-text-field>
        </v-col>
        <v-col cols="3"> </v-col>
      </v-row>
      <v-row>
        <v-col cols="3"> </v-col>
        <v-col cols="6">
          <v-text-field
            v-model="email"
            :rules="emailRules"
            label="E-mail"
            required
          ></v-text-field>
        </v-col>
        <v-col cols="3"> </v-col>
      </v-row>
      <v-row>
        <v-col cols="3"> </v-col>
        <v-col cols="6">
          <v-text-field
            v-model="mobileNumber"
            label="Mobile Number"
            required
          ></v-text-field>
        </v-col>
        <v-col cols="3"> </v-col>
      </v-row>
      <v-row>
        <v-col cols="3"> </v-col>
        <v-col cols="6">
          <v-text-field
            v-model="gender"
            label="Gender"
            placeholder="Male/Female"
            required
          ></v-text-field>
        </v-col>
        <v-col cols="3"> </v-col>
      </v-row>
      <v-row>
        <v-col cols="3"> </v-col>
        <v-col cols="6">
          <v-text-field
            v-model="dob"
            label="Date of Birth"
            placeholder="dd/mm/yyy"
            required
          ></v-text-field>
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
export default {
  data() {
    return {
      valid: false,
      firstName: "",
      lastName: "",
      userType: "customer",
      nameRules: [
        (v) => !!v || "Name is required",
        (v) => v.length <= 10 || "Name must be less than 10 characters",
      ],
      email: "",
      emailRules: [
        (v) => !!v || "E-mail is required",
        (v) => /.+@.+/.test(v) || "E-mail must be valid",
      ],
      password: "",
      gender: "",
      mobileNumber: "",
      dob: "",
    };
  },
  methods: {
    register: function () {
      let user = {
        frist_name: this.firstName,
        last_name: this.lastName,
        password: this.password,
        mobileNumbe: this.mobileNumber,
        gender: this.gender,
        email: this.email,
        dateOfBirth: `${this.dob}T00:00:00Z`,
      };
      console.log(user);
      Axios.post("http://127.0.0.1:8000/api/user/", user)
        .then((response) => console.log(response))
        .catch((error) => console.log(error));
    },
  },
};
</script>
