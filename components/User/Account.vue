<template>
  <v-container>
    <v-row v-if="feedback">
      <v-col cols="12"> <p>Hello Mohamed</p> </v-col>
      <v-col cols="12">
        <v-textarea
          v-model="review"
          color="white"
          label="Provide your review here"
          auto-grow
        ></v-textarea>
      </v-col>
      <v-col cols="12"
        ><v-rating
          v-model="rating"
          hover
          length="5"
          size="64"
          value="3"
        ></v-rating
      ></v-col>
      <v-col>
        <v-btn @click="submit">Submit</v-btn>
      </v-col>
    </v-row>
    <v-row v-if="!feedback">
      <v-col cols="6">
        <v-card shaped style="padding: 20px; margin-left: 15px" width="80%">
          <v-card-title> Personal Info</v-card-title>
          <hr />
          <v-row justify="space-between">
            <v-col style="margin-left: 5px">Name</v-col>
            <v-col>Mohamed Ahmed Raafat</v-col>
          </v-row>

          <hr />
          <v-row justify="space-between">
            <v-col style="margin-left: 5px">Birthday</v-col>
            <v-col>8/11/1997</v-col>
          </v-row>

          <hr />
          <v-row justify="space-between">
            <v-col style="margin-left: 5px">Gender</v-col>
            <v-col>Male</v-col>
          </v-row>
        </v-card>
      </v-col>
      <v-col style="" cols="6">
        <v-card shaped style="padding: 20px; margin-left: 15px" width="80%">
          <v-card-title> Contact Info</v-card-title>
          <hr />
          <v-row justify="space-between">
            <v-col style="margin-left: 5px">Email</v-col>
            <v-col>mohamedraafat060@gmail.com</v-col>
          </v-row>

          <hr />
          <v-row justify="space-between">
            <v-col style="margin-left: 5px">Mobile</v-col>
            <v-col>+201125731861</v-col>
          </v-row>
        </v-card>
      </v-col>
      <v-col style="" cols="6">
        <v-card shaped style="padding: 20px; margin-left: 15px" width="80%">
          <v-card-title> Payment info</v-card-title>
          <hr />
          <v-row justify="space-between">
            <v-col style="margin-left: 5px">Type</v-col>
            <v-col>Credit card</v-col>
          </v-row>

          <hr />
          <v-row justify="space-between">
            <v-col style="margin-left: 5px">Number</v-col>
            <v-col>1111 **** **** **** 0000</v-col>
          </v-row>

          <hr />
          <v-row justify="space-between">
            <v-col style="margin-left: 5px">Expiry Date</v-col>
            <v-col>01/01</v-col>
          </v-row>
        </v-card>
      </v-col>
      <v-col style="" cols="6">
        <v-card shaped style="padding: 20px; margin-left: 15px" width="80%">
          <v-card-title>
            Balance
            <v-spacer></v-spacer>
            <select
              @change="test()"
              v-model="roomNumber"
              v-if="userRooms.length != 0"
              name="roomType"
            >
              <option selected hidden value="">Choose Room</option>
              <option
                v-for="room in userRooms"
                :key="room.number"
                :value="room.number"
              >
                {{ room.number }}
              </option>
            </select>
          </v-card-title>
          <hr />
          <v-row justify="space-between">
            <v-col style="margin-left: 5px">Current Balance</v-col>
            <v-col>540$</v-col>
          </v-row>
          <hr />
          <v-card-actions>
            <v-dialog width="500">
              <template v-slot:activator="{ on, attrs }">
                <v-btn
                  data-app
                  color="red lighten-2"
                  dark
                  v-bind="attrs"
                  v-on="on"
                >
                  Pay
                </v-btn>
              </template>

              <v-card>
                <v-card-title class="headline grey lighten-2">
                  Privacy Policy
                </v-card-title>

                <v-card-text> Are you sure you want to pay 540$? </v-card-text>

                <v-divider></v-divider>

                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn color="primary" text @click="pay"> Pay </v-btn>
                </v-card-actions>
              </v-card>
            </v-dialog>
          </v-card-actions>
        </v-card>
      </v-col>
      <v-col style="padding-left: 30px" cols="12">
        <p>
          Would you like to provide a review?
          <v-btn style="margin-left: 10px" @click="feedback = true"
            >Click here</v-btn
          >
        </p>
      </v-col>
    </v-row>
  </v-container>
</template>
<script>
export default {
  data() {
    return {
      review: "",
      rating: 0,
      feedback: false,
      roomNumber: "",
      userRooms: [],
    };
  },
  methods: {
    pay: function () {
      console.log("payment complete");
    },
    submit: function () {
      console.log(this.review);
      console.log(this.rating);
      this.feedback = false;
    },
    test: function () {
      console.log(this.roomNumber);
    },
  },
};
</script>
<style scoped>
select {
  position: relative;
  padding: 5px;

  font-size: 1rem;
  font-family: monospace;

  border: 1px solid #8292a2;
  border-radius: 0.25rem;

  cursor: pointer;
}
select:focus {
  outline: none;
  border-color: #3acfff;
  box-shadow: 0 0 0 0.25rem rgba(0, 120, 250, 0.1);
}
</style>