import Vue from 'vue'
import Vuex from 'vuex'
import App from './App.vue'
import router from './router'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import axios from 'axios'
import { backendUrl } from './variables.js'
import VueFusionCharts from 'vue-fusioncharts';
import FusionCharts from 'fusioncharts';
import TimeSeries from 'fusioncharts/fusioncharts.timeseries';
import FusionTheme from 'fusioncharts/themes/fusioncharts.theme.fusion';

Vue.use(VueFusionCharts, FusionCharts, TimeSeries, FusionTheme);
Vue.use(Vuex);

Vue.prototype.$http = axios
Vue.prototype.$backendUrl = backendUrl
Vue.config.productionTip = false
// Install BootstrapVue
Vue.use(BootstrapVue)
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin)

import './assets/bootstrap.css'
import './assets/bootstrap-vue.css'

var store = new Vuex.Store({
  state: {
    ticker: "TSLA"
  },
  getters:{
    getTicker(state){
      return state.ticker
    }
  },
  mutations:{
    setTicker(state, t) {
      console.log(state)
      state = t
      console.log(state)
    },
  }
});
new Vue({
  router,
  store,
  render: function (h) { return h(App) }
}).$mount('#app')
