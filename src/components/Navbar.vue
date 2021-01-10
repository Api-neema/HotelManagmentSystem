<template>
  <nav>
    <v-app-bar>
      <router-link to="/">Hotel</router-link>

      <v-spacer></v-spacer>
      <router-link to="/manager/housekeeping"
        >Housekeeping Requests</router-link
      >
      <router-link to="/manager/schedule">Schedule</router-link>
      <router-link to="/manager/check-out">Check out</router-link>
      <router-link to="/manager/check-in">Check in</router-link>
      <router-link to="/admin/add-manager">Add Manager</router-link>
      <router-link to="/admin/add-service">Add Service</router-link>
      <router-link to="/admin/requests">Requests</router-link>
      <router-link to="/admin/add-hotel">Add Hotel</router-link>
      <router-link to="/admin/statistics">Statistics</router-link>
      <router-link to="/booking">Book</router-link>
      <router-link to="/services">Services</router-link>
      <router-link to="/register">Register</router-link>
      <router-link to="/login">Login</router-link>
      <router-link to="/profile">Profile</router-link>
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