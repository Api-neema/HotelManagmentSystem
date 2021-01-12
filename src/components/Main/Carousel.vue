<template>
  <v-carousel cycle hide-delimiters :show-arrows="false">
    <v-carousel-item
      v-for="(item, i) in items"
      :key="i"
      :src="item.src"
    ></v-carousel-item>
  </v-carousel>
</template>
<script>
export default {
  data() {
    return {
      items: [
        {
          src:
            "https://www.hilton.com/im/en/NoHotel/14808086/545-por-winter-image-for-web-licensed-shutterstock-1277023897.jpg?impolicy=crop&cw=5000&ch=1315&gravity=NorthWest&xposition=0&yposition=1268&rw=1920&rh=505",
        },
        {
          src:
            "https://www.hilton.com/im/en/KHNLSQQ/14342285/curio-lushan-1809.jpg?impolicy=crop&cw=4574&ch=1203&gravity=NorthWest&xposition=0&yposition=898&rw=1920&rh=505",
        },

        {
          src:
            "https://media.kempinski.com/34397312/mow_1920x1080px.jpg;width=1905;height=794;mode=crop;anchor=middlecenter;autorotate=true;quality=85;scale=both;progressive=true;encoder=freeimage;format=jpg",
        },
      ],
    };
  },
};
</script>-