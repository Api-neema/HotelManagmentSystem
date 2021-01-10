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
            <q>{{ review.description }}</q>
          </div>
          <span class="author">{{ review.author }}</span>
        </v-row>
      </v-sheet>
    </v-carousel-item>
  </v-carousel>
</template>
<script>
import Axios from "axios";
export default {
  created: function () {
    Axios.get("http://127.0.0.1:8000/api/reviews/")
      .then((response) => {
        let reviews = response.data.results.map(function (review) {
          review.rating = Number(review.rating);
        });
        this.Reviews = response.data.results;
      })
      .catch(function (error) {
        console.log(error);
      });
  },
  data: () => ({
    Reviews: [],
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