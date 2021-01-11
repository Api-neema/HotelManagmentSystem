<template>
  <v-container>
    <v-form>
      <v-row>
        <v-col cols="4"></v-col>
        <v-col cols="4"
          ><v-text-field
            @focusout="roomFocus = true"
            v-model="roomNumber"
            label="Room Number"
          ></v-text-field>
          <span
            style="color: red"
            v-if="
              (!$v.roomNumber.numeric || !$v.roomNumber.required) && roomFocus
            "
            >Please enter a valid room number</span
          ></v-col
        >
        <v-col cols="4"></v-col>
        <v-col cols="4"></v-col>
        <v-col cols="4"><v-btn @click="search" block>Search</v-btn></v-col>
        <v-col cols="4"></v-col>
      </v-row>
    </v-form>
    <v-form v-if="roomDetails">
      <v-row>
        <v-col cols="12" md="3">
          <v-text-field
            v-model="roomDetails.customerName"
            label="Customer Name"
            disabled
            required
          ></v-text-field>
        </v-col>

        <v-col cols="12" md="3">
          <v-text-field
            v-model="roomDetails.number"
            label="Room Number"
            disabled
            required
          ></v-text-field>
        </v-col>

        <v-col cols="12" md="3">
          <v-text-field
            v-model="roomDetails.type"
            disabled
            label="Room Type"
            required
          ></v-text-field>
        </v-col>
        <v-col cols="12" md="3">
          <v-text-field
            v-model="roomDetails.checkInStatus"
            disabled
            label="Status"
            required
          ></v-text-field>
        </v-col>
        <v-col cols="12">
          <v-text-field v-model="extra" label="Extras" required></v-text-field>
        </v-col>
        <v-col cols="12"><v-btn @click="checkIn" block>Check In</v-btn></v-col>
      </v-row>
    </v-form>
  </v-container>
</template>
<script>
import { required, numeric } from "vuelidate/lib/validators";
import Axios from "axios";
export default {
  data: () => ({
    roomNumber: "",
    roomDetails: "",
    extra: "",
    roomFocus: false,
  }),
  validations: {
    roomNumber: {
      required,
      numeric,
    },
  },
  methods: {
    search: function () {
      if (!this.$v.$invalid) {
        this.roomDetails = {
          number: 520,
          customerName: "Mohamed Raafat",
          type: "Double",
          checkInStatus: false,
          id: "25",
        };
      } else {
        this.roomFocus = true;
      }
      //send room number to server
      //retrieve room details from server
    },
    checkIn: function () {
      //send room id to server to change status to true
      //send extras to housekeeping
    },
  },
};
</script>