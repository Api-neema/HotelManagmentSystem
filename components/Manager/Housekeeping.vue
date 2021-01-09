<template>
  <v-container>
    <v-card
      style="margin-top: 15px"
      v-for="request in requests"
      :key="request.id"
    >
      <v-card-title>
        <p>
          {{ request.customerName }} requested housekeeping at room number
          {{ request.roomNumber }}
        </p>
        <v-spacer></v-spacer>
        <v-btn @click="done(request.id)">Done</v-btn>
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
        roomNumber: "30",
      },
      {
        id: "4124",
        customerName: "Mohamed Raafat",
        roomNumber: "30",
      },
      {
        id: "41",
        customerName: "Mohamed Raafat",
        roomNumber: "30",
      },
      {
        id: "123224",
        customerName: "Mohamed Raafat",
        roomNumber: "30",
      },
      {
        id: "1523",
        customerName: "Mohamed Raafat",
        roomNumber: "30",
      },
      {
        id: "12663",
        customerName: "Mohamed Raafat",
        roomNumber: "30",
      },
    ],
  }),
  methods: {
    done: function (id) {
      this.requests = this.requests.filter(function (value, index, arr) {
        return value.id != id;
      });
      console.log(`finished request number ${id}`);
    },
  },
};
</script>