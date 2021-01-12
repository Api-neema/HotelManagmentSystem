<template>
  <v-container>
    <v-row>
      <v-col cols="3">
        <div class="title1">Experience Something New</div>
        Close to home or across the world, we are there for you with memorable
        offers and experiences. Check out what’s new.
      </v-col>
      <v-col cols="9">
        <v-row>
          <v-col v-for="item in Experiences" :key="item.name" cols="4">
            <v-card class="mx-auto" max-width="344">
              <v-img height="250" :src="item.img"
                ><v-card-title style="color: white">{{
                  item.title
                }}</v-card-title>
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
        title: "Big Dreams, Big Savings",
        img:
          "https://www.hilton.com/im/en/RKTWAWA/1337027/waldorf-astoria-ras-al-khaimah-cabana-may-2014.jpg?impolicy=crop&cw=5367&ch=3670&gravity=NorthWest&xposition=66&yposition=0&rw=547&rh=374",
        description:
          "Save on your next memory-making getaway and enjoy even more flexibility like early check-in and late check-out, where available.",
        reveal: false,
      },
      {
        title: "WorkSpaces by us",
        img:
          "https://www.hilton.com/im/en/NoHotel/14717785/hero-room-image.jpg?impolicy=crop&cw=2919&ch=1996&gravity=NorthWest&xposition=313&yposition=0&rw=547&rh=374",
        description:
          "Try WorkSpaces by us for the first time and earn 10,000 Bonus Points at participating hotels. Our day-use rooms offer you a clean, flexible, and distraction-free environment for productive remote working.",
        reveal: false,
      },
      {
        title: "Get Back  Get Away Offer",
        img:
          "https://www.hilton.com/im/en/NoHotel/14845230/518-hho-cb-accelerator-base-featuredoffer-2000x1333px.png?impolicy=crop&cw=1949&ch=1333&gravity=NorthWest&xposition=25&yposition=0&rw=547&rh=374",
        description:
          "to spend now and 75K Bonus Points to travel later with the Honor American Express Card. Terms Apply.",
        reveal: false,
      },
      {
        title: "Earn 2X Points",
        img:
          "https://www.hilton.com/im/en/NoHotel/14807975/545-por-winter-image-for-web-licensed-shutterstock-1533974810-4500x3000.jpg?impolicy=crop&cw=4387&ch=3000&gravity=NorthWest&xposition=56&yposition=0&rw=547&rh=374",
        description:
          "Your next trip could be twice as rewarding with the 2X Points Package. Receive double the Honor Points each night of your stay at any participating property within our  Portfolio.",
        reveal: false,
      },
      {
        title: "Europe & More: Up to 25% Off",
        img:
          "https://www.hilton.com/im/en/NoHotel/14942184/emea-phase-2-bikes-on-beach.jpg?impolicy=crop&cw=4874&ch=3333&gravity=NorthWest&xposition=62&yposition=0&rw=547&rh=374",
        description:
          "Head to Europe, the Middle East, or Africa and make new memories. From now through January 31, book one of our flexible stay options with free cancellations for up to 25% off*. All stays must be completed by March 31, 2021.",
        reveal: false,
      },
      {
        title: "Earn Unlimited Points",
        img:
          "https://www.hilton.com/im/en/GOISHHI/14238241/loungers-and-leisure-pool.jpg?impolicy=crop&cw=8471&ch=5792&gravity=NorthWest&xposition=108&yposition=0&rw=547&rh=374",
        description:
          "Enjoy unlimited Points to make unforgettable memories. Earn 2,000 Points every stay, PLUS 5,000 Points every 5 nights through May 2.",
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