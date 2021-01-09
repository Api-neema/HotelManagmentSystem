<template>
  <v-app>
    <Carousel />
    <Description />
    <Experiences />
    <Reviews />
    <Feedback />
    <Footer />
  </v-app>
</template>
<script>
import Carousel from "./Carousel";
import Description from "./Description";
import Experiences from "./Experiences";
import Reviews from "./Reviews";
import Feedback from "./Feedback";
import Footer from "./Footer";

export default {
  components: {
    Carousel,
    Description,
    Experiences,
    Reviews,
    Feedback,
    Footer,
  },
  data: () => ({
    //
  }),
};
</script>