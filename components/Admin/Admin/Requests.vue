<template>
  <v-container>
    <v-card
      style="margin-top: 15px"
      v-for="request in requests"
      :key="request.id"
    >
      <v-card-title>
        <p>
          {{ request.customerName }} requested a {{ request.roomType }} room
          from {{ request.startDate }} to {{ request.endDate }}
        </p>
        <v-spacer></v-spacer>
        <v-btn @click="accept(request.id)">Accept</v-btn>
        <v-btn @click="reject(request.id)">Reject</v-btn>
      </v-card-title>
    </v-card>
  </v-container>
</template>
<script>
export default {
  data: () => ({
    requests: [
      {
        id: "123",
        customerName: "Mohamed Raafat",
        roomType: "triple",
        startDate: "21/12/2020",
        endDate: "28/12/2020",
      },
      {
        id: "4124",
        customerName: "Mohamed Raafat",
        roomType: "triple",
        startDate: "21/12/2020",
        endDate: "28/12/2020",
      },
      {
        id: "41",
        customerName: "Mohamed Raafat",
        roomType: "triple",
        startDate: "21/12/2020",
        endDate: "28/12/2020",
      },
      {
        id: "123224",
        customerName: "Mohamed Raafat",
        roomType: "triple",
        startDate: "21/12/2020",
        endDate: "28/12/2020",
      },
      {
        id: "1523",
        customerName: "Mohamed Raafat",
        roomType: "triple",
        startDate: "21/12/2020",
        endDate: "28/12/2020",
      },
      {
        id: "12663",
        customerName: "Mohamed Raafat",
        roomType: "triple",
        startDate: "21/12/2020",
        endDate: "28/12/2020",
      },
    ],
  }),
  methods: {
    accept: function (id) {
      this.requests = this.requests.filter(function (value, index, arr) {
        return value.id != id;
      });
      console.log(`accepted request number ${id}`);
    },
    reject: function (id) {
      this.requests = this.requests.filter(function (value, index, arr) {
        return value.id != id;
      });
      console.log(`rejected request number ${id}`);
    },
  },
};
</script>