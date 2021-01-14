<template>
  <div class="dialogContainer">
    <!-- Dialog title and body -->
    <div class="dialogContent">
      <div class="dialogContentTitle">Book a Restaurant</div>
      <div class="dialogContentBody">
        <v-row>
          <v-col cols="12">
            <label for="restaurant">Restaurant Name</label>

            <select v-model="restaurantName" name="restaurant">
              <option selected hidden value="">Restaurant Name</option>
              <option value="single">Single</option>
              <option value="double">Double</option>
              <option value="triple">Triple</option>
            </select>
          </v-col>
          <v-col cols="12" c>
            <label for="table">Table Size</label>

            <select v-model="tableSize" name="table">
              <option selected hidden value="">Table Size</option>
              <option value="single">Single</option>
              <option value="double">Double</option>
              <option value="triple">Triple</option>
            </select>
          </v-col>
          <v-col>
            <label for="date">date</label>

            <input
              v-model="date"
              name="end"
              type="date"
              min="2019-01-01"
              max="2022-01-01"
            />
          </v-col>
          <v-col cols="12" class="bottom">
            <label for="appt">Select a time:</label>
            <input v-model="time" type="time" id="appt" name="appt" />
          </v-col>
        </v-row>
      </div>
    </div>
    <!-- Dialog action bar -->
    <div class="dialogActionBar">
      <!-- Buttons -->
      <a class="buttonTouchTarget" id="buttonOneTouchTarget" href="#">
        <v-btn depressed class="buttonFlat" id="buttonOne" @click="close()" fit>
          Close
        </v-btn> </a
      ><!-- This comment removes 4px gap between buttons
					--><a class="buttonTouchTarget" id="buttonTwoTouchTarget" href="#">
        <v-btn depressed class="buttonFlat" id="buttonTwo" @click="book"
          >AGREE</v-btn
        >
      </a>
    </div>
  </div>
</template>
<script>
export default {
  data: () => ({
    restaurantName: "",
    tableSize: "",
    time: "",
    date: "",
  }),
  methods: {
    close: function () {
      this.$emit("hide");
    },
    book: function () {
      let restaurant = {
        restaurantName: this.restaurantName,
        tableSize: this.tableSize,
        time: this.time,
        date: this.date,
      };
      alert("Request submitted successfully");

      this.close();
    },
  },
};
</script>
<style scoped>
.bottom {
  margin-top: -5%;
}
label {
  display: block;
}
select {
  width: 100%;
  position: relative;
  padding: 1rem 3.5rem 1rem 0.75rem;

  font-size: 1rem;
  font-family: monospace;

  border: 1px solid #8292a2;
  border-radius: 0.25rem;

  cursor: pointer;
}
select:focus {
  outline: none;
  border-color: #3acfff;
  box-shadow: 0 0 0 0.25rem rgba(0, 120, 250, 0.1);
}

div {
  -webkit-transition-property: all;
  -webkit-transition-duration: 0.2s;
  -webkit-transition-timing-function: ease;
  -webkit-transition-delay: 0s;
}
.dialogContainer {
  /* Form */
  position: absolute;
  top: 25%;
  left: 25%;

  width: auto;
  height: auto;
  /*
  Drop Shadow
  a. Horizontal shadow
  b. Vertical shadow
  c. Blur
  d. Spread
  e. Color
  */
  -webkit-box-shadow: 0 -2px 25px 0 rgba(0, 0, 0, 0.15),
    0 13px 25px 0 rgba(0, 0, 0, 0.3);
  background-color: #ffffff;
  /* Internal padding */
  padding-top: 0;
  padding-left: 0;
  padding-right: 0;
  padding-bottom: 0;
  /* External padding */
  margin-top: 0;
  margin-left: auto;
  margin-right: auto;
  margin-bottom: 0;
}

.dialogContent {
  /* Form */
  width: auto;
  height: auto;
  background-color: #ffffff;
  /* Corner radius */
  border-top-left-radius: 2px;
  border-top-right-radius: 2px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
  /* Internal padding */
  padding-top: 21px;
  padding-left: 24px;
  padding-right: 24px;
  padding-bottom: 12px;
  /* External padding */
  margin-top: 0;
  margin-left: 0;
  margin-right: 0;
  margin-bottom: 0;
}

.dialogContentTitle {
  /* Form */
  background-color: #ffffff;
  /* Typography */
  font-family: "Roboto", sans-serif;
  font-weight: 500;
  font-size: 20px;
  color: rgba(0, 0, 0, 0.8);
  line-height: 24px;
  text-align: left;
  letter-spacing: 0.03px;
  /* Internal padding */
  padding-top: 0;
  padding-left: 0;
  padding-right: 0;
  padding-bottom: 0;
  /* External padding */
  margin-top: 0;
  margin-left: 0;
  margin-right: 0;
  margin-bottom: 0;
}

.dialogContentBody {
  /* Typography */
  font-family: "Roboto", sans-serif;
  font-weight: 400;
  font-size: 16px;
  color: rgba(0, 0, 0, 0.5);
  line-height: 24px;
  text-align: left;
  letter-spacing: 0.03px;
  /* Internal padding */
  padding-top: 14px;
  padding-left: 0;
  padding-right: 0;
  padding-bottom: 0;
  /* External padding */
  margin-top: 0;
  margin-left: 0;
  margin-right: 0;
  margin-bottom: 0;
}

.dialogActionBar {
  /* Form */
  width: auto;
  height: 48px;
  background-color: #ffffff;
  text-align: right;
  /* Corner radius */
  border-top-left-radius: 0;
  border-top-right-radius: 0;
  border-bottom-right-radius: 2px;
  border-bottom-left-radius: 2px;
  /* Internal padding */
  padding-top: 0;
  padding-left: 16px;
  padding-right: 15px;
  padding-bottom: 8px;
  /* External padding */
  margin-top: 0;
  margin-left: 0;
  margin-right: 0;
  margin-bottom: 0;
}

/*
The attributes below style the
hit target.
*/

.buttonTouchTarget {
  display: inline-block;
  background-color: rgba(0, 0, 0, 0);
  /* Remove grey background on link clicked in ios safari */
  -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
}

/*
The attributes below style the
flat button based on the Google
material design language.
*/

.buttonFlat {
  /* Form */
  display: inline-block;
  height: 36px;
  background-color: rgba(9, 9, 9, 0);
  /* Typography */
  font-family: "Roboto", sans-serif;
  font-weight: 500;
  font-size: 14px;
  color: rgba(33, 150, 243, 0.9);
  line-height: 36px;
  text-align: center;
  letter-spacing: 0.4px;
  /* Internal padding */
  padding-top: 0;
  padding-left: 8px;
  padding-right: 8px;
  padding-bottom: 0;
  /* External padding – Touch target size */
  margin-top: 6px;
  margin-left: 4px;
  margin-right: 4px;
  margin-bottom: 6px;
}
input[type="time"] {
  height: 10%;
  position: relative;
  padding: 1rem 3.5rem 1rem 0.75rem;

  font-size: 1rem;
  font-family: monospace;

  border: 1px solid #8292a2;
  border-radius: 0.25rem;
  background: white
    url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='20' height='22' viewBox='0 0 20 22'%3E%3Cg fill='none' fill-rule='evenodd' stroke='%23688EBB' stroke-linecap='round' stroke-linejoin='round' stroke-width='2' transform='translate(1 1)'%3E%3Crect width='18' height='18' y='2' rx='2'/%3E%3Cpath d='M13 0L13 4M5 0L5 4M0 8L18 8'/%3E%3C/g%3E%3C/svg%3E")
    right 1rem center no-repeat;

  cursor: pointer;
}
input[type="time"]:focus {
  outline: none;
  border-color: #3acfff;
  box-shadow: 0 0 0 0.25rem rgba(0, 120, 250, 0.1);
}

input[type="date"] {
  height: 10%;
  position: relative;
  padding: 1rem 3.5rem 1rem 0.75rem;

  font-size: 1rem;
  font-family: monospace;

  border: 1px solid #8292a2;
  border-radius: 0.25rem;
  background: white
    url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='20' height='22' viewBox='0 0 20 22'%3E%3Cg fill='none' fill-rule='evenodd' stroke='%23688EBB' stroke-linecap='round' stroke-linejoin='round' stroke-width='2' transform='translate(1 1)'%3E%3Crect width='18' height='18' y='2' rx='2'/%3E%3Cpath d='M13 0L13 4M5 0L5 4M0 8L18 8'/%3E%3C/g%3E%3C/svg%3E")
    right 1rem center no-repeat;

  cursor: pointer;
}
input[type="date"]:focus {
  outline: none;
  border-color: #3acfff;
  box-shadow: 0 0 0 0.25rem rgba(0, 120, 250, 0.1);
}
::-webkit-datetime-edit-month-field:hover,
::-webkit-datetime-edit-day-field:hover,
::-webkit-datetime-edit-year-field:hover {
  background: rgba(0, 120, 250, 0.1);
}
::-webkit-datetime-edit-text {
  opacity: 0;
}
::-webkit-clear-button,
::-webkit-inner-spin-button {
  display: none;
}
::-webkit-calendar-picker-indicator {
  position: absolute;
  width: 2.5rem;
  height: 100%;
  top: 0;
  right: 0;
  bottom: 0;

  opacity: 0;
  cursor: pointer;

  color: rgba(0, 120, 250, 1);
  background: rgba(0, 120, 250, 1);
}

input[type="date"]:hover::-webkit-calendar-picker-indicator {
  opacity: 0.05;
}
input[type="date"]:hover::-webkit-calendar-picker-indicator:hover {
  opacity: 0.15;
}
</style>