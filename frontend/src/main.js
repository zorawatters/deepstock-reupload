import Vue from 'vue'
import App from './App.vue'
import router from './router'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

import axios from 'axios'
import { backendUrl } from './variables.js'
// export defualt {
//   name:"app",
//   components:{
//
//   }
// }
//
Vue.prototype.$http = axios
Vue.prototype.$backendUrl = backendUrl
Vue.config.productionTip = false

// Install BootstrapVue
Vue.use(BootstrapVue)
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin)

import './assets/bootstrap.css'
import './assets/bootstrap-vue.css'

new Vue({
  router,
  render: function (h) { return h(App) }
}).$mount('#app')
