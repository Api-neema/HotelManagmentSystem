import Vue from 'vue'
import { email } from 'vuelidate/lib/validators';
import Vuex from 'vuex'
Vue.use(Vuex);
export const store = new Vuex.Store({
    state: {
        user: {
            type:''
        },
    },

})