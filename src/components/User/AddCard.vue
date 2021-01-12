<template>
  <v-form ref="form">
    <v-container>
      <v-row>
        <v-col cols="12">
          <v-text-field
            @focusout="ctypeRoom = true"
            v-model="cardType"
            label="Card type"
          ></v-text-field>
          <span
            style="color: red"
            v-if="(!$v.cardType.alpha || !$v.cardType.required) && ctypeRoom"
            >Please enter a valid card type</span
          >
        </v-col>

        <v-col cols="12">
          <v-text-field
            @focusout="cnumFocus = true"
            v-model="cardNumber"
            label="Card number"
            placeholder="xxxx-xxxx-xxxx-xxxx"
          ></v-text-field>
          <span
            style="color: red"
            v-if="
              (!$v.cardNumber.numeric ||
                !$v.cardNumber.required ||
                !$v.cardNumber.minLength) &&
              cnumFocus
            "
            >Please enter a valid card number</span
          >
        </v-col>

        <v-col cols="12">
          <v-text-field
            @focusout="expFocus = true"
            v-model="expiryDate"
            label="Expiry date"
            placeholder="mm/yy"
          ></v-text-field>
          <span style="color: red" v-if="!$v.expiryDate.required && expFocus"
            >Please enter a valid expiry date</span
          >
        </v-col>
        <v-col cols="12">
          <v-btn style="background-color: #4caf50" class="mr-4" @click="submit">
            Submit
          </v-btn>
        </v-col>
      </v-row>
    </v-container>
  </v-form>
</template>


<script>
import Axios from "axios";
import {
  required,
  alpha,
  alphaNum,
  numeric,
  minLength,
} from "vuelidate/lib/validators";

export default {
  data: () => ({
    cardId: "",
    cardNumber: "",
    expiryDate: "",
    cardType: "",
    cnumFocus: false,
    expFocus: false,
    ctypeRoom: false,
  }),
  validations: {
    cardNumber: {
      numeric,
      required,
      minLength: minLength(16),
    },
    expiryDate: {
      required,
    },

    cardType: {
      required,
      alpha,
    },
  },

  methods: {
    submit: function () {
      let card = {
        cardNumber: this.cardNumber,
        expiryDate: this.expiryDate,
        cardType: this.cardType,
      };
      if (!this.$v.$invalid) {
        Axios.post("http://127.0.0.1:8000/api/card/", card)
          .then((response) => {
            Axios.patch(
              `http://127.0.0.1:8000/api/user/${this.$store.state.user.id}/`,
              { card: response.data.id }
            )
              .then((response) => console.log(response))
              .catch((error) => console.log(error));
          })
          .catch((error) => console.log(error));
      } else {
        (this.cnumFocus = true),
          (this.expFocus = true),
          (this.ctypeRoom = true);
      }
    },
  },
};
</script>