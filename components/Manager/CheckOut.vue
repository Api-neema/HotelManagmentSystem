<template>
  <v-container>
    <v-form>
      <v-row>
        <v-col cols="4"></v-col>
        <v-col cols="4"
          ><v-text-field
            v-model="roomNumber"
            label="Room Number"
            required
          ></v-text-field
        ></v-col>
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
            v-model="roomDetails.price"
            disabled
            label="Price"
            required
          ></v-text-field>
        </v-col>

        <v-col cols="12"><v-btn @click="checkIn" block>Check In</v-btn></v-col>
      </v-row>
    </v-form>
  </v-container>
</template>
<script>
export default {
  data: () => ({
    roomNumber: "",
    roomDetails: "",
    extra: "",
  }),
  methods: {
    search: function () {
      //send room number to server
      //retrieve room details from server
      this.roomDetails = {
        number: 520,
        customerName: "Mohamed Raafat",
        type: "Double",
        checkInStatus: false,
        id: "25",
        price: "500$",
      };
    },
    checkIn: function () {
      //send room id to server to change status to true
      //send extras to housekeeping
    },
  },
};
</script>