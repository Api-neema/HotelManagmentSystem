<template>
  <v-form ref="form">
    <v-container>
      <v-row>
        <v-col cols="12">
          <v-text-field
            v-model="serviceName"
            label="Service Name"
            required
            :rules="nameRules"
          ></v-text-field>
        </v-col>

        <v-col cols="12">
          <v-text-field
            v-model="serviceDescription"
            label="Service Description"
            required
            :rules="nameRules"
          ></v-text-field>
        </v-col>
        <v-col cols="12">
          <v-text-field
            v-model="serviceImg"
            label="Image URL"
            required
            :rules="nameRules"
          ></v-text-field>
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
export default {
  data: () => ({
    serviceName: "",
    serviceDescription: "",
    serviceImg: "",
    nameRules: [
      (v) => !!v || "Name is required",
      (v) => v.length <= 10 || "Name must be less than 10 characters",
    ],
    valid: false,
  }),
  methods: {
    submit: function () {
      let service = {
        serviceName: this.serviceName,
        description: this.serviceDescription,
        serviceImg: this.serviceImg,
      };
      Axios.post("http://127.0.0.1:8000/api/services/", service)
        .then((response) => console.log(response))
        .catch((error) => console.log(error));
      console.log(service);
    },
  },
};
</script>