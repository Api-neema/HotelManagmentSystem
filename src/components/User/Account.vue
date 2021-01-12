<template>
  <v-container>
    <v-row v-if="feedback">
      <v-col cols="12">
        <p>Hello {{ user.firstName }}</p>
      </v-col>
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
            <v-col>{{ user.firstName }} {{ user.lastName }}</v-col>
          </v-row>

          <hr />
          <v-row justify="space-between">
            <v-col style="margin-left: 5px">Birthday</v-col>
            <v-col>{{ user.dateOfBirth }}</v-col>
          </v-row>

          <hr />
          <v-row justify="space-between">
            <v-col style="margin-left: 5px">Gender</v-col>
            <v-col>{{ user.gender }}</v-col>
          </v-row>
        </v-card>
      </v-col>
      <v-col style="" cols="6">
        <v-card shaped style="padding: 20px; margin-left: 15px" width="80%">
          <v-card-title> Contact Info</v-card-title>
          <hr />
          <v-row justify="space-between">
            <v-col style="margin-left: 5px">Email</v-col>
            <v-col>{{ user.email }}</v-col>
          </v-row>

          <hr />
          <v-row justify="space-between">
            <v-col style="margin-left: 5px">Mobile</v-col>
            <v-col>{{ user.mobileNumber }}</v-col>
          </v-row>
        </v-card>
      </v-col>
      <v-col style="" cols="6">
        <v-card shaped style="padding: 20px; margin-left: 15px" width="80%">
          <v-card-title>
            Payment info <v-spacer></v-spacer>
            <v-btn><router-link to="/add-card">Add card</router-link></v-btn>
          </v-card-title>
          <hr />
          <v-row justify="space-between">
            <v-col style="margin-left: 5px">Type</v-col>
            <v-col>{{ user.cardType }}</v-col>
          </v-row>

          <hr />
          <v-row justify="space-between">
            <v-col style="margin-left: 5px">Number</v-col>
            <v-col>{{ user.cardNumber }}</v-col>
          </v-row>

          <hr />
          <v-row justify="space-between">
            <v-col style="margin-left: 5px">Expiry Date</v-col>
            <v-col>{{ user.expiryDate }}</v-col>
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
              v-model="roomPrice"
              v-if="user.fees.length != 1"
              name="roomType"
            >
              <option selected hidden value="">Choose Room</option>
              <option
                v-for="room in user.fees"
                :key="room.room"
                :value="room.totalFees"
              >
                room: {{ room.room }}
              </option>
            </select>
          </v-card-title>
          <hr />
          <v-row justify="space-between">
            <v-col style="margin-left: 5px">Current Balance</v-col>
            <v-col>{{ roomPrice }}$</v-col>
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

                <v-card-text>
                  Are you sure you want to pay {{ roomPrice }}$?
                </v-card-text>

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
import Axios from "axios";
export default {
  data() {
    return {
      review: "",
      rating: 0,
      feedback: false,
      user: this.$store.state.user,
      roomPrice: this.$store.state.user.fees[0].totalFees,
    };
  },
  methods: {
    pay: function () {
      let userRoom = this.user.fees.filter((room) => {
        return room.totalFees == this.roomPrice;
      });
      Axios.put("http://127.0.0.1:8000/api/fee/1/", {
        user: this.user.id,
        room: userRoom[0].room,
        totalFees: -this.roomPrice,
      })
        .then(function (response) {})
        .catch(function (error) {
          console.log(error);
        });
    },

    submit: function () {
      Axios.post("http://127.0.0.1:8000/api/reviews/", {
        description: this.review,
        rating: this.rating,
      })
        .then(function (response) {
          console.log(response);
        })
        .catch(function (error) {
          console.log(error);
        });
      this.feedback = false;
    },
    test: function () {},
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

a {
  text-decoration: none;
  color: black;
}
</style>