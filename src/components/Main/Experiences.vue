<template>
  <v-container>
    <v-row>
      <v-col cols="3">
        <div class="title1">Experience Something New</div>
        Close to home or across the world, Hilton is there for you with
        memorable offers and experiences. Check out what’s new.
      </v-col>
      <v-col cols="9">
        <v-row>
          <v-col v-for="item in Experiences" :key="item.name" cols="4">
            <v-card class="mx-auto" max-width="344">
              <v-img height="250" :src="item.img"
                ><v-card-title>{{ item.title }}</v-card-title>
                <v-expand-transition>
                  <v-card
                    v-if="item.reveal"
                    class="transition-fast-in-fast-out v-card--reveal"
                    style="height: 100%"
                  >
                    <v-card-text class="pb-0">
                      <p>
                        {{ item.description }}
                      </p>
                    </v-card-text>
                    <v-card-actions class="pt-0">
                      <v-btn
                        text
                        color="teal accent-4"
                        @click="item.reveal = false"
                      >
                        Close
                      </v-btn>
                    </v-card-actions>
                  </v-card>
                </v-expand-transition>
              </v-img>

              <v-card-actions>
                <v-btn
                  text
                  color="teal accent-4"
                  v-if="!item.reveal"
                  @click="item.reveal = true"
                >
                  Learn More
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-col>
        </v-row>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  data: () => ({
    Experiences: [
      {
        title: "test title",
        img: "https://cdn.vuetifyjs.com/images/cards/cooking.png",
        description: "test desciption",
        reveal: false,
      },
      {
        title: "test title",
        img: "https://cdn.vuetifyjs.com/images/cards/cooking.png",
        description: "test desciption",
        reveal: false,
      },
      {
        title: "test title",
        img: "https://cdn.vuetifyjs.com/images/cards/cooking.png",
        description: "test desciption",
        reveal: false,
      },
      {
        title: "test title",
        img: "https://cdn.vuetifyjs.com/images/cards/cooking.png",
        description: "test desciption",
        reveal: false,
      },
      {
        title: "test title",
        img: "https://cdn.vuetifyjs.com/images/cards/cooking.png",
        description: "test desciption",
        reveal: false,
      },
      {
        title: "test title",
        img: "https://cdn.vuetifyjs.com/images/cards/cooking.png",
        description: "test desciption",
        reveal: false,
      },
    ],
  }),
};
</script>

<style scoped>
.v-card--reveal {
  bottom: 0;
  opacity: 1 !important;
  position: absolute;
  width: 100%;
}
.title1 {
  font-weight: bold;
  font-size: 50px;
}
</style>