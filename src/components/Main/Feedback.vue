<template>
  <v-container>
    <v-row>
      <v-col cols="3">
        <div class="title1">GOT SOME FEEDBACK?</div>
      </v-col>
      <v-col cols="1"></v-col>
      <v-col cols="8">
        <v-form ref="form" v-model="valid" lazy-validation>
          <v-text-field
            v-model="name"
            :rules="nameRules"
            label="Name"
            required
          ></v-text-field>

          <v-text-field
            v-model="email"
            :rules="emailRules"
            label="E-mail"
            required
          ></v-text-field>
          <v-textarea
            style="margin-left: -12px"
            name="input-7-1"
            background-color="white"
            filled
            label="Feedback"
            auto-grow
            value=""
            v-model="feedback"
          ></v-textarea>

          <v-btn :disabled="!valid" color="success" class="mr-4" @click="send">
            Send
          </v-btn>
        </v-form>
      </v-col>
    </v-row>
  </v-container>
</template>
<style scoped>
.title1 {
  font-weight: bold;
  font-size: 50px;
}
</style>
<script>
export default {
  data: () => ({
    valid: true,
    feedback: "",
    name: "",
    nameRules: [(v) => !!v || "Name is required"],
    email: "",
    emailRules: [
      (v) => !!v || "E-mail is required",
      (v) => /.+@.+\..+/.test(v) || "E-mail must be valid",
    ],
    select: null,
    items: ["Item 1", "Item 2", "Item 3", "Item 4"],
    checkbox: false,
  }),

  methods: {
    send() {
      this.$refs.form.validate();
      console.log(this.feedback);
    },
  },
};
</script>