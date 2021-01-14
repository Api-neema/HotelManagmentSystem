<template>
  <v-container>
    <v-card style="margin-top: 15px" v-for="task in tasks" :key="task.id">
      <v-card-title>
        <p>
          {{ task.name }}
        </p>
      </v-card-title>
      <v-card-text>
        <p>{{ task.description }}</p>
        <v-btn @click="finish(task.id)"><v-icon>mdi-check</v-icon></v-btn>
      </v-card-text>
    </v-card>
  </v-container>
</template>
<script>
export default {
  data: () => ({
    tasks: [
      {
        name: "Task1",
        description:
          "Lorem ipsum dolor sit amet consectetur adipisicing elit. Ullam voluptate maxime cupiditate totam earum excepturi illo eius nam nostrum. Aut!",
        id: "1233",
      },
      {
        name: "Task1",
        description:
          "Lorem ipsum dolor sit amet consectetur adipisicing elit. Ullam voluptate maxime cupiditate totam earum excepturi illo eius nam nostrum. Aut!",
        id: "1243",
      },
      {
        name: "Task1",
        description:
          "Lorem ipsum dolor sit amet consectetur adipisicing elit. Ullam voluptate maxime cupiditate totam earum excepturi illo eius nam nostrum. Aut!",
        id: "1623",
      },
    ],
  }),
  methods: {
    finish: function (id) {
      this.tasks = this.tasks.filter(function (value, index, arr) {
        return value.id != id;
      });
      console.log(`Task finished`);
    },
  },
};
</script>