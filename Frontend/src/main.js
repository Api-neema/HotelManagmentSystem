import Vue from 'vue'
import App from './App.vue'
import vueRouter from 'vue-router'
import Routes from './routes.js'
import vuetify from './plugins/vuetify';
import Vuelidate from 'vuelidate'

Vue.config.productionTip = false
Vue.use(vueRouter);
Vue.use(Vuelidate)
const router = new vueRouter({
  routes: Routes,
  mode: 'history'
})

new Vue({
  render: h => h(App),
  vuetify,
  router: router
}).$mount('#app')
