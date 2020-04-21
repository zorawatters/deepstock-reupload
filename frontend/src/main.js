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
    companies: ['AMD', 'AAPL', 'TSLA', 'SPLK'],	
    ticker: "TSLA",
  	stockData: {},
  },
  getters:{
    getTicker: state => {
      return state.ticker
      //return lodash.cloneDeep(state.ticker)
    },
    getMetadata: state => {
    	if(!state.stockData[state.ticker]){
				state.stockData[state.ticker] = {}
			}
    	return state.stockData[state.ticker]['metadata']
    },
    getChartData: (state, getters) => {
    	if(!state.stockData[getters.getTicker]){
				state.stockData[getters.getTicker] = {}
			}
			return (getters.getStockData[getters.getTicker]['chartData'])
    },
    getStockData: (state) => {
    	return (state.stockData)
    },
  },
  mutations:{
    setTicker(state, t) {
      state.ticker = t
    },
    setChartData(state, payload){
    	if(!state.stockData[payload.company]){
				state.stockData[payload.company] = {}
			}
			state.stockData[payload.company]['chartData'] = payload.chartData
    },
    setMetadata(state, payload){
    	if(!state.stockData[payload.company]){
				state.stockData[payload.company] = {}
			}
			state.stockData[payload.company]['metadata'] = payload.metadata
    },
    init(state){
    	state.companies.forEach(company => {
    		state.stockData[company] = {
    			metadata: {},
    			chartData: []
    		}
    	})
    }
  },
  actions:{
  	updateIntraday({commit, state}){
  		var update = () => {
  			var counter = 100
  			state.companies.forEach(company => {
					//axios.get(backendUrl + '/' + state.ticker + '/intraday').then(response => {
						var cd = []

						cd = [['2020-04-17 10:05:00', counter],
								  ['2020-04-17 13:25:00', 500],
								  ['2020-04-17 14:30:00', 600],
								  ['2020-04-17 15:30:00', 740]]
						counter += 100
						//for(var datetime in response.data){
						//	cd.push([datetime, Number(response.data[datetime][0]['4. close'])])
						//}
						commit('setChartData', {company:company, chartData: cd})
					//})
	  		})
  		}
  		update()
  		setInterval(update, 300000)
	  		
  	},
  	updateMetadata({commit, state}){
  		state.companies.forEach(company => {
  			axios.get(backendUrl + '/' + state.ticker + '/metadata').then(response => {
  				commit('setMetadata', {company: company, metadata: response.data})
  			})
  		})
  	},


  }
});

store.commit('init')
store.dispatch('updateIntraday')
//store.dispatch('updateMetadata')

new Vue({
  router,
  store,
  render: function (h) { return h(App) }
}).$mount('#app')
