<template>
  <v-container>
    <v-row v-if="Services.length == 0">
      <v-col cols="6"> <p>You haven't subscribed to any services</p> </v-col>
    </v-row>
    <v-row>
      <v-col v-for="item in Services" :key="item.name" cols="4">
        <v-card class="mx-auto" max-width="400">
          <v-img class="white--text align-end" height="200px" :src="item.image">
          </v-img>

          <v-card-subtitle class="pb-0"> {{ item.name }} </v-card-subtitle>

          <v-card-text class="text--primary">
            <div>{{ item.description }}</div>
          </v-card-text>

          <v-card-actions>
            <v-btn color="primary" style="color: green" text>
              Cancel Subscription
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>
<script>
export default {
  data: () => ({
    Services: [
      {
        name: "HouseKeeping",
        description: "HouseKeeping",
        image: "https://cdn.vuetifyjs.com/images/cards/docks.jpg",
      },
    ],
  }),
  methods: {},
};
</script>