<template>
  <nav>
    <v-app-bar>
      <router-link to="/">Hotel</router-link>

      <v-spacer></v-spacer>
      <router-link
        v-if="$store.state.user.type == 'manager'"
        to="/manager/housekeeping"
        >Housekeeping Requests</router-link
      >
      <router-link v-if="false" to="/manager/schedule">Schedule</router-link>
      <router-link
        v-if="$store.state.user.type == 'manager'"
        to="/manager/check-out"
        >Check out</router-link
      >
      <router-link
        v-if="$store.state.user.type == 'manager'"
        to="/manager/check-in"
        >Check in</router-link
      >
      <router-link
        v-if="$store.state.user.type == 'admin'"
        to="/admin/add-manager"
        >Add Manager</router-link
      >
      <router-link
        v-if="$store.state.user.type == 'admin'"
        to="/admin/add-service"
        >Add Service</router-link
      >
      <router-link v-if="$store.state.user.type == 'admin'" to="/admin/requests"
        >Requests</router-link
      >
      <router-link
        v-if="$store.state.user.type == 'admin'"
        to="/admin/add-hotel"
        >Add Hotel</router-link
      >
      <router-link v-if="false" to="/admin/statistics">Statistics</router-link>
      <router-link
        v-if="$store.state.user.type == '' || $store.state.user.type == 'user'"
        to="/booking"
        >Book</router-link
      >
      <router-link
        v-if="$store.state.user.type == '' || $store.state.user.type == 'user'"
        to="/services"
        >Services</router-link
      >
      <router-link v-if="$store.state.user.type == ''" to="/register"
        >Register</router-link
      >
      <router-link v-if="$store.state.user.type == ''" to="/login"
        >Login</router-link
      >
      <router-link v-if="$store.state.user.type == 'user'" to="/profile"
        >Profile</router-link
      >
    </v-app-bar>
  </nav>
</template>
<style scoped>
a {
  text-decoration: none;
  margin-left: 20px;
  color: black;
}
</style>