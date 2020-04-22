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
    ticker: "AMD",
  	stockData: {},
  },
  getters:{
    getTicker: state => {
      return state.ticker
    },
    getMetadata: state => {
    	return state.stockData[state.ticker]['metadata']
    },
    getChartData: (state, getters) => {
			return (getters.getStockData(getters.getTicker)['chartData'])
			//return (getters.getStockData[getters.getTicker]['chartData'])
    },
    getStockData: (state) => {
    	return company => state.stockData[company]
    },
    getPrediction: (state, getters) => {
      var p = (getters.getStockData(getters.getTicker)['prediction'])
      console.log('got', p)
      return p
    }
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
      //console.log(state.stockData[payload.company])
    },
    setMetadata(state, payload){
    	if(!state.stockData[payload.company]){
				state.stockData[payload.company] = {}
			}
			state.stockData[payload.company]['metadata'] = payload.metadata
    },
    setPrediction(state, payload){
      if(!state.stockData[payload.company]){
        state.stockData[payload.company] = {}
      }
      console.log('pred', payload)
      state.stockData[payload.company]['prediction'] = payload.prediction
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
        var proms = []
  			state.companies.forEach(async company => {
					proms.push(new Promise(async (resolve, reject) => {
            var c = company
            //var response = await axios.get(backendUrl + '/' + company + '/intraday')
            var cd = []
            cd = cd = [['2020-04-17 10:05:00', 400],
                  ['2020-04-17 13:25:00', counter],
                  ['2020-04-17 14:30:00', 600],
                  ['2020-04-17 15:30:00', counter*2]]
            counter+=100
            //for(var datetime in response.data){
            //  cd.push([datetime, Number(response.data[datetime][0]['4. close'])])
            //}
            resolve({company: c, chartData: cd})
          }))
				})
	  		Promise.all(proms).then(values => {
          values.forEach(value => commit('setChartData', value))
  		  })
      }
  		update()
  		setInterval(update, 300000)
	  		
  	},
  	updateMetadata({commit, state}){
  		state.companies.forEach(company => {
  			axios.get(backendUrl + '/' + company + '/metadata').then(response => {
  				commit('setMetadata', {company: company, metadata: response.data})
  			})
  		})
  	},
    updatePredictions({commit, state}){
      state.companies.forEach(company => {
        console.log('called for', company)
        axios.get(backendUrl + '/' + company + '/make_prediction').then(response => {
          commit('setPrediction', {company: company, prediction: response.data[0]['dense']})
        })
      })
    }

  }
});

store.commit('init')
store.dispatch('updateIntraday')
store.dispatch('updateMetadata')
store.dispatch('updatePredictions')

new Vue({
  router,
  store,
  render: function (h) { return h(App) }
}).$mount('#app')
