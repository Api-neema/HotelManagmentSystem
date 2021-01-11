<template>
  <v-form ref="form">
    <v-container>
      <v-row>
        <v-col cols="12">
          <v-text-field
            @focusout="hnameFocus = true"
            v-model="hotelName"
            label="Hotel name"
          ></v-text-field>
          <span
            style="color: red"
            v-if="(!$v.hotelName.alpha || !$v.hotelName.required) && hnameFocus"
            >Please enter a valid hotel name</span
          >
        </v-col>

        <v-col cols="12">
          <v-text-field
            @focusout="addFocus = true"
            v-model="hotelAddress"
            label="Hotel Address"
          ></v-text-field>
          <span
            style="color: red"
            v-if="
              (!$v.hotelAddress.alphaNum || !$v.hotelAddress.required) &&
              addFocus
            "
            >Please enter a valid Address</span
          >
        </v-col>
        <v-col cols="4">
          <v-text-field
            @focusout="sroomFocus = true"
            v-model="singleRooms"
            label="Number of single rooms"
          ></v-text-field>
          <span
            style="color: red"
            v-if="
              (!$v.singleRooms.numeric || !$v.singleRooms.required) &&
              sroomFocus
            "
            >Please enter a valid room number</span
          >
        </v-col>
        <v-col cols="4">
          <v-text-field
            @focusout="droomFocus = true"
            v-model="doubleRooms"
            label="Number of double rooms"
          ></v-text-field>
          <span
            style="color: red"
            v-if="
              (!$v.doubleRooms.numeric || !$v.doubleRooms.required) &&
              droomFocus
            "
            >Please enter a valid room number</span
          >
        </v-col>

        <v-col cols="4">
          <v-text-field
            @focusout="troomFocus = true"
            v-model="tripleRooms"
            label="Number of triple rooms"
          ></v-text-field>
          <span
            style="color: red"
            v-if="
              (!$v.tripleRooms.numeric || !$v.tripleRooms.required) &&
              troomFocus
            "
            >Please enter a valid room number</span
          >
        </v-col>
        <v-col cols="12">
          <v-btn style="background-color: #4caf50" class="mr-4" @click="submit">
            Submit
          </v-btn>
        </v-col>
      </v-row>
    </v-container>
  </v-form>
</template>


<script>
import Axios from "axios";
import { required, alpha, alphaNum, numeric } from "vuelidate/lib/validators";

export default {
  data: () => ({
    hotelName: "",
    hotelAddress: "",
    singleRooms: "",
    doubleRooms: "",
    tripleRooms: "",
    hnameFocus: false,
    addFocus: false,
    sroomFocus: false,
    droomFocus: false,
    troomFocus: false,
  }),
  validations: {
    hotelName: {
      alpha,
      required,
    },
    hotelAddress: {
      alphaNum,
      required,
    },

    singleRooms: {
      required,
      numeric,
    },
    doubleRooms: {
      required,
      numeric,
    },
    tripleRooms: {
      required,
      numeric,
    },
  },

  methods: {
    submit: function () {
      let hotel = {
        hotelName: this.hotelName,
        hotelAddress: this.hotelAddress,
        singleRooms: this.singleRooms,
        doubleRooms: this.doubleRooms,
        tripleRooms: this.tripleRooms,
      };
      if (!this.$v.$invalid) {
        Axios.post("http://127.0.0.1:8000/api/user/", hotel)
          .then((response) => console.log(response))
          .catch((error) => console.log(error));
      } else {
        (this.hnameFocus = true),
          (this.addFocus = true),
          (this.sroomFocus = true),
          (this.droomFocus = true),
          (this.troomFocus = true);
      }
    },
  },
};
</script>