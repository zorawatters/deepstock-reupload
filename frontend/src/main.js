import Vue from 'vue'
import App from './App.vue'
import router from './router'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

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