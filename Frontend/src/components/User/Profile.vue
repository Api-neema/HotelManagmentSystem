<template>
  <v-card height="100vh">
    <v-row>
      <v-col cols="2">
        <v-navigation-drawer absolute permanent>
          <template v-slot:prepend>
            <v-list-item two-line>
              <v-list-item-avatar>
                <img src="https://randomuser.me/api/portraits/women/81.jpg" />
              </v-list-item-avatar>

              <v-list-item-content>
                <v-list-item-title>Jane Smith</v-list-item-title>
                <v-list-item-subtitle>Logged In</v-list-item-subtitle>
              </v-list-item-content>
            </v-list-item>
          </template>

          <v-divider></v-divider>

          <v-list dense>
            <v-list-item>
              <v-list-item-icon>
                <v-icon>mdi-account</v-icon>
              </v-list-item-icon>

              <v-list-item-content>
                <v-list-item-title @click="showAccount"
                  >My Account</v-list-item-title
                >
              </v-list-item-content>
            </v-list-item>

            <v-list-item>
              <v-list-item-icon>
                <v-icon>mdi-email</v-icon>
              </v-list-item-icon>

              <v-list-item-content>
                <v-list-item-title @click="showSupport"
                  >Support</v-list-item-title
                >
              </v-list-item-content>
            </v-list-item>
          </v-list>
        </v-navigation-drawer>
      </v-col>
      <v-col cols="10">
        <Account v-if="account" />
        <Services v-if="services" />
        <Support v-if="support" />
      </v-col>
    </v-row>
  </v-card>
</template>
<script>
import Account from "./Account";
import Support from "./Support";

export default {
  components: {
    Account,
    Support,
  },
  data() {
    return {
      account: true,
      services: false,
      support: false,
    };
  },
  methods: {
    showAccount: function () {
      this.account = true;
      this.services = false;
      this.support = false;
    },
    showServices: function () {
      this.account = false;
      this.services = true;
      this.support = false;
    },
    showSupport: function () {
      this.account = false;
      this.services = false;
      this.support = true;
    },
  },
};
</script>
<style  scoped>
.v-list-item__title {
  margin-left: 10px;
  cursor: pointer;
}
</style>