<template>
  <v-container>
    <v-card
      style="margin-top: 15px"
      v-for="request in requests"
      :key="request.id"
    >
      <v-card-title>
        <p>
          {{ request.userName }} requested a {{ request.roomType }} room from
          {{ request.startDate }} to {{ request.endDate }}
        </p>
        <v-spacer></v-spacer>
        <v-btn @click="accept(request.id, request.user)">Accept</v-btn>
        <v-btn @click="reject(request.id, request.user)">Reject</v-btn>
      </v-card-title>
    </v-card>
  </v-container>
</template>
<script>
import Axios from "axios";
export default {
  created: function () {
    let requests = [];
    Axios.get("http://127.0.0.1:8000/api/book/", {})
      .then((response) => {
        requests = response.data.results;
        requests = requests.map(function (request) {
          let req = request;
          Axios.get(`http://127.0.0.1:8000/api/user/${request.user}/`, {}).then(
            function (response) {
              req.userName =
                response.data.firstName + " " + response.data.lastName;
            }
          );
          return req;
        });
        requests = requests.filter(function (request) {
          return request.accepted == null && request.bookingType == true;
        });
        this.requests = requests;
        console.log(this.requests);
      })
      .catch(function (error) {
        console.log(error);
      });
  },
  data: () => ({
    requests: "",
  }),
  methods: {
    accept: function (id, userId) {
      Axios.put(`http://127.0.0.1:8000/api/book/${id}/`, {
        user: userId,
        accepted: true,
      })
        .then(function (response) {
          console.log(response);
        })
        .catch(function (error) {
          console.log(error);
        });
      this.requests = this.requests.filter(function (value, index, arr) {
        return value.id != id;
      });
      console.log(`accepted request number ${id}`);
    },
    reject: function (id, userId) {
      Axios.put(`http://127.0.0.1:8000/api/book/${id}/`, {
        user: userId,
        accepted: false,
      })
        .then(function (response) {
          console.log(response);
        })
        .catch(function (error) {
          console.log(error);
        });
      this.requests = this.requests.filter(function (value, index, arr) {
        return value.id != id;
      });
      console.log(`rejected request number ${id}`);
    },
  },
};
</script>