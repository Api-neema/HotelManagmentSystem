<template>
  <v-form ref="form">
    <v-container>
      <v-row>
        <v-col cols="12">
          <v-text-field
            v-model="hotelName"
            label="Hotel name"
            required
            :rules="nameRules"
          ></v-text-field>
        </v-col>

        <v-col cols="12">
          <v-text-field
            v-model="hotelAddress"
            label="Hotel Address"
            required
            :rules="nameRules"
          ></v-text-field>
        </v-col>
        <v-col cols="4">
          <v-text-field
            v-model="singleRooms"
            label="Number of single rooms"
            required
          ></v-text-field>
        </v-col>
        <v-col cols="4">
          <v-text-field
            v-model="doubleRooms"
            label="Number of double rooms"
            required
          ></v-text-field>
        </v-col>

        <v-col cols="4">
          <v-text-field
            v-model="tripleRooms"
            label="Number of triple rooms"
            required
          ></v-text-field>
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
export default {
  data: () => ({
    hotelName: "",
    hotelAddress: "",
    singleRooms: "",
    doubleRooms: "",
    tripleRooms: "",
    nameRules: [
      (v) => !!v || "Name is required",
      (v) => v.length <= 10 || "Name must be less than 10 characters",
    ],
    valid: false,
  }),
  methods: {
    submit: function () {
      let hotel = {
        hotelName: this.hotelName,
        hotelAddress: this.hotelAddress,
        singleRooms: this.singleRooms,
        doubleRooms: this.doubleRooms,
        tripleRooms: this.tripleRooms,
      };
      this.$refs.form.validate();
      console.log(hotel);
    },
  },
};
</script>