<template>
  <v-carousel cycle hide-delimiters>
    <v-carousel-item v-for="(review, i) in Reviews" :key="i">
      <v-sheet height="100%" tile>
        <v-row class="fill-height" align="center" justify="center">
          <div class="rating">
            <v-rating
              readonly
              :value="review.rating"
              background-color="white"
              color="white"
              large
            ></v-rating>
          </div>
          <div>
            <q>{{ review.review }}</q>
          </div>
          <span class="author">{{ review.author }}</span>
        </v-row>
      </v-sheet>
    </v-carousel-item>
  </v-carousel>
</template>
<script>
export default {
  data: () => ({
    Reviews: [
      {
        review: " dont forget form validation ",
        author: "Mohamed Raafat",
        rating: 3,
      },
      {
        review: " dont forget form validation ",
        author: "Mohamed Raafat",
        rating: 3,
      },
      {
        review: " dont forget form validation ",
        author: "Mohamed Raafat",
        rating: 3,
      },
      {
        review: " dont forget form validation ",
        author: "Mohamed Raafat",
        rating: 3,
      },
    ],
  }),
};
</script>
<style scoped>
.author {
  position: absolute;
  top: 55%;
  right: 20%;
  font-style: italic;
}
.rating {
  position: absolute;
  top: 36%;
}
</style>