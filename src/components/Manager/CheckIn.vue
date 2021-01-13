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
    <v-form v-if="room">
      <v-row>
        <v-col cols="12" md="3">
          <v-text-field
            v-model="room.roomNumber"
            label="Room Number"
            disabled
            required
          ></v-text-field>
        </v-col>

        <v-col cols="12" md="3">
          <v-text-field
            v-model="room.roomType"
            disabled
            label="Room Type"
            required
          ></v-text-field>
        </v-col>
        <v-col cols="12" md="3">
          <v-text-field
            v-model="room.checkIn"
            disabled
            label="Status"
            required
          ></v-text-field>
        </v-col>
        <v-col cols="12" md="3">
          <v-text-field
            v-model="room.accepted"
            disabled
            label="Accepted"
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
    room: "",
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
      let room = "";

      console.log(this.room);
      if (!this.$v.$invalid) {
        Axios.get("http://127.0.0.1:8000/api/book/")
          .then((response) => {
            room = response.data.results;
            console.log(room);
            room = room.filter((room) => {
              return room.roomNumber == this.roomNumber;
            });

            this.room = room[0];
            if (this.room.accepted == null) {
              this.room.accepted = "pending";
            }
          })
          .catch((error) => console.log(error));
      } else {
        this.roomFocus = true;
      }
      //send room number to server
      //retrieve room details from server
    },
    checkIn: function () {
      Axios.put(`http://127.0.0.1:8000/api/book/${this.room.id}/`, {
        user: this.room.user,
        checkIn: true,
      });
    },
  },
};
</script>