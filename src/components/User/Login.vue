<template>
  <v-form v-model="valid">
    <v-container>
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
          <v-btn block depressed v-on:click="login">Login </v-btn>
        </v-col>
        <v-col cols="3"> </v-col>
      </v-row>
    </v-container>
  </v-form>
</template>
<script>
export default {
  data: () => ({
    valid: false,
    email: "",
    emailRules: [
      (v) => !!v || "E-mail is required",
      (v) => /.+@.+/.test(v) || "E-mail must be valid",
    ],
    password: "",
  }),
  methods: {
    login: function () {
      //send to server
      console.log(`email: ${this.email}`);
      console.log(`password: ${this.password}`);
      //server responds with user data
      //add user data to store
    },
  },
};
</script>