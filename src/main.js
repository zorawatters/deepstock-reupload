import Vue from 'vue'
import Vuex from 'vuex'
import App from './App.vue'
import router from './router'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import axios from 'axios'
import { backendUrl } from './variables.js'
import VueFusionCharts from 'vue-fusioncharts';
import FusionCharts from 'fusioncharts';
import Column2D from 'fusioncharts/fusioncharts.charts';
import FusionTheme from 'fusioncharts/themes/fusioncharts.theme.fusion';
import Charts from "fusioncharts/fusioncharts.charts";
import { FCComponent } from "vue-fusioncharts";


Vue.use(VueFusionCharts, FusionCharts, Column2D, FusionTheme, Charts);

Vue.prototype.$http = axios
Vue.prototype.$backendUrl = backendUrl
Vue.config.productionTip = false
//Install Vuex
Vue.use(Vuex)
// Install BootstrapVue
Vue.use(BootstrapVue)
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin)

import './assets/bootstrap.css'
import './assets/bootstrap-vue.css'
import { mapGetters } from 'vuex';

const store = new Vuex.Store({
  state: {
       companies: [
           { id: 1, ticker: 'TWTR', name: 'Twitter', selected: true, high: 164, low: 154},
           { id: 2, ticker: 'GOOGL', name: 'Google', selected: false, high: 145, low: 112},
           { id: 3, ticker: 'SPLK', name: 'Splunk', selected: false, high: 190, low: 163 },
           { id: 4, ticker: 'TSLA', name: 'Tesla', selected: false, high: 189, low: 176 }
       ]
   },
   getters: {
       selectedCompany: state => {
           return state.companies.filter(companies => companies.selected);
       },
       getCompanyId: (state) => (id) => {
           return state.companies.find(companies => companies.id === id)
       }
   }
});

console.log(store.getters.selectedCompany)

new Vue({
  router,
  store,
  data: {
    },
    computed: mapGetters([
      'selectedCompany', 'getCompanyId'
    ]),
  render: function (h) { return h(App) }
}).$mount('#app')
