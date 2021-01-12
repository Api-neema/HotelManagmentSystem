<template>
  <v-form ref="form">
    <v-container>
      <v-row>
        <v-col cols="12">
          <v-text-field
            @focusout="snameFocus = true"
            v-model="serviceName"
            label="Service Name"
          ></v-text-field>
          <span
            style="color: red"
            v-if="
              (!$v.serviceName.required || !$v.serviceName.alpha) && snameFocus
            "
            >Please enter a valid service name</span
          >
        </v-col>

        <v-col cols="12">
          <v-text-field
            @focusout="sdescFocus = true"
            v-model="serviceDescription"
            label="Service Description"
          ></v-text-field>
          <span
            style="color: red"
            v-if="
              (!$v.serviceDescription.required ||
                !$v.serviceDescription.alpha) &&
              sdescFocus
            "
            >Please enter a valid service description</span
          >
        </v-col>
        <v-col cols="12">
          <v-text-field
            @focusout="simgFocus = true"
            v-model="serviceImg"
            label="Image URL"
          ></v-text-field>
          <span style="color: red" v-if="!$v.serviceImg.required && simgFocus"
            >Please enter a valid service img url</span
          >
        </v-col>
        <v-col cols="12">
          <v-text-field
            @focusout="feeFocus = true"
            v-model="fee"
            label="Fee"
          ></v-text-field>
          <span
            style="color: red"
            v-if="(!$v.fee.required || !$v.fee.numeric) && feeFocus"
            >Please enter a valid service fee</span
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
import { required, alpha, numeric } from "vuelidate/lib/validators";
export default {
  data: () => ({
    serviceName: "",
    serviceDescription: "",
    serviceImg: "",
    fee: "",
    snameFocus: false,
    sdescFocus: false,
    simgFocus: false,
  }),
  validations: {
    serviceName: {
      alpha,
      required,
    },
    serviceDescription: {
      alpha,
      required,
    },

    serviceImg: {
      required,
    },
    fee: {
      required,
      numeric,
    },
  },
  methods: {
    submit: function () {
      let service = {
        serviceName: this.serviceName,
        description: this.serviceDescription,
        image: this.serviceImg,
        fees: this.fee,
        type: this.serviceName,
      };
      if (!this.$v.$invalid) {
        Axios.post("http://127.0.0.1:8000/api/services/", service)
          .then((response) => console.log(response))
          .catch((error) => console.log(error));
      } else {
        (this.snameFocus = true),
          (this.sdescFocus = true),
          (this.simgFocus = true);
        this.feeFocus = true;
      }
    },
  },
};
</script>