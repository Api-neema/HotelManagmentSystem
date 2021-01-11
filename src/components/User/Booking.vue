<template>
  <v-container>
    <v-row>
      <v-col v-for="item in Rooms" :key="item.name" cols="4">
        <v-card min-height="415" class="mx-auto" max-width="400">
          <v-img class="white--text align-end" height="200px" :src="item.image">
          </v-img>

          <v-card-subtitle class="pb-0"> {{ item.name }} </v-card-subtitle>

          <v-card-text class="text--primary">
            <div>{{ item.description }}</div>
          </v-card-text>

          <v-card-actions>
            <div>
              <p>Price per night per person: {{ item.price }}</p>
            </div>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>

    <v-row v-if="$store.state.user.type == 'user'">
      <v-form>
        <v-row>
          <v-col>
            <label for="hotels">Hotel</label>

            <select @focusout="hnameFocus = true" v-model="hotel" name="hotels">
              <option selected hidden value="">Choose Hotel</option>
              <option value="hotel1">hotel1</option>
              <option value="hotel2">hotel2</option>
              <option value="hotel3">hotel3</option>
            </select>

            <span style="color: red" v-if="!$v.hotel.required && hnameFocus"
              >Please choose a hotel</span
            >
          </v-col>

          <v-col>
            <label for="start">Start</label>
            <input
              @focusout="sdateFocus = true"
              v-model="startDate"
              name="start"
              type="date"
              min="2019-01-01"
              max="2022-01-01"
            />
            <span style="color: red" v-if="!$v.startDate.required && sdateFocus"
              >Please choose a start date</span
            >
          </v-col>
          <v-col>
            <label for="end">End</label>

            <input
              @focusout="edateFocus = true"
              v-model="endDate"
              name="end"
              type="date"
              min="2019-01-01"
              max="2022-01-01"
            />
            <span style="color: red" v-if="!$v.endDate.required && edateFocus"
              >Please choose an end date</span
            >
          </v-col>
          <v-col>
            <label for="roomCapacity">Room Capacity</label>

            <select
              @focusout="roomCapacityFocus = true"
              v-model="roomCapacity"
              name="roomCapacity"
            >
              <option selected hidden value="">Room Capacity</option>
              <option value="single">Single</option>
              <option value="double">Double</option>
              <option value="triple">Triple</option>
            </select>
            <span
              style="color: red"
              v-if="!$v.roomCapacity.required && roomCapacityFocus"
              >Please choose a room capacity</span
            >
          </v-col>
          <v-col>
            <label for="roomType">Room Type</label>

            <select
              @focusout="roomTypeFocus = true"
              v-model="roomType"
              name="roomType"
            >
              <option selected hidden value="">Room Type</option>
              <option value="standard">Standard Room</option>
              <option value="deluxe">Deluxe Suite</option>
              <option value="presidential">Presidential Suite</option>
            </select>
            <span
              style="color: red"
              v-if="!$v.roomType.required && roomTypeFocus"
              >Please choose a room type</span
            >
          </v-col>

          <v-col>
            <label for=""></label>

            <v-btn
              @click="book"
              block
              depressed
              style="
                height: 69%;
                background: rgb(24, 103, 192);
                border: 1px solid rgb(130, 146, 162);
                color: white;
                margin-top: 14%;
              "
              >Book</v-btn
            >
          </v-col>
        </v-row>
      </v-form>
    </v-row>
  </v-container>
</template>
<script>
import Axios from "axios";
import { required, alpha, email, numeric } from "vuelidate/lib/validators";
export default {
  data: () => ({
    hotel: "",
    startDate: "",
    endDate: "",
    roomType: "",
    roomCapacity: "",
    hnameFocus: false,
    sdateFocus: false,
    edateFocus: false,
    roomTypeFocus: false,
    roomCapacityFocus: false,
    Rooms: [
      {
        name: "Standard Room",
        description:
          "Featuring a balcony, this air conditioned double room offers a seating area with satellite/cable TV and a work desk. The bathroom offers a shower and a bath and complimentary toiletries.",
        image:
          "https://cf.bstatic.com/xdata/images/hotel/max1024x768/203567707.jpg?k=01157cd143bed0215af2a58347fdbcbfe1c1305e24caf20688b2ba5e54230f09&o=",
        price: "300$",
      },
      {
        name: "Deluxe Suite",
        description:
          "Featuring a balcony with partial view of the Nile, this spacious, air-conditioned suite offers a blend of French and Oriental décor. It includes a separate living room with a flat-screen TV, a mini-bar and free WiFi .",
        image:
          "https://cf.bstatic.com/xdata/images/hotel/max1024x768/42173392.jpg?k=ba100501be29fc6ec21ddd8039b14aa55b87cf202365ddb34fc8ba9bd901ca14&o=",
        price: "500$",
      },
      {
        name: "Presidential Suite",
        description:
          "Featuring a balcony with a view, this spacious air conditioned Presidential Suite offers a seating area with cable TV, mini bar and a work desk. The bathroom offers a shower and a bath and complimentary toiletries.",
        image:
          "https://cf.bstatic.com/xdata/images/hotel/max1024x768/7857097.jpg?k=3e5ab613492778e32171b7f786f85542fcdad63f2801e813de5a990023908fa8&o=  ",
        price: "800$",
      },
    ],
  }),
  validations: {
    hotel: {
      required,
    },
    startDate: {
      required,
    },

    endDate: {
      required,
    },
    roomType: {
      required,
    },
    roomCapacity: {
      required,
    },
  },

  methods: {
    book: function () {
      let book = {
        hotel: this.hotel,
        startDate: this.startDate,
        endDate: this.endDate,
        roomType: this.roomType,
        roomCapacity: this.roomCapacity,
      };
      if (!this.$v.$invalid) {
        Axios.post("http://127.0.0.1:8000/api/user/", book)
          .then((response) => console.log(response))
          .catch((error) => console.log(error));
      } else {
        (this.hnameFocus = true),
          (this.sdateFocus = true),
          (this.edateFocus = true),
          (this.roomTypeFocus = true),
          (this.roomCapacityFocus = true);
      }
    },
  },
};
</script>
<style  scoped>
input[type="date"] {
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
select {
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