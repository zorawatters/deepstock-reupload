<template>
  <div :class = "custom">
    <fusioncharts
    :type="type"
    :width="width"
    :height="height"
    :dataformat="dataFormat"
    :dataSource="dataSource"
    ></fusioncharts>
  </div>
</template>
<script>
const d = [
  ['2020-04-17 10:05:00', 700],
  ['2020-04-17 13:25:00', 500],
  ['2020-04-17 14:30:00', 600],
  ['2020-04-17 15:30:00', 740]
]

import { mapState } from 'vuex';

export default {
  name: 'stock-card',
  props: {
    custom: {
      type: String,
      default: ''
    }
  },
  data() {
    return {
      type: "timeseries",
      width: "100%",
      height: "85%",
      dataFormat: "json",
      chartData: [],
      dataStore: new FusionCharts.DataStore(),
      schema: [{
        name: "Time",
        type: "date",
        format: "%Y-%m-%d %-H:%M:%S"
      }, {
        name: "Price",
        type: "number"
      }]
    }
  },
  async mounted(){
    this.getIntraday()
    setInterval(this.getIntraday, 600000)
  },
  methods:{
    getIntraday: async function(){
      console.log("Getting it for this.ticker")
      var response = await this.$http.get(this.$backendUrl + '/' + this.ticker + '/intraday')
      var data = response.data
      this.chartData = []

      for(var datetime in data){
        this.chartData.push([datetime, Number(data[datetime][0]['4. close'])])

      }
    }
  },
  computed:{
    dataSource(){

      var r =  {
        chart: {},
        navigator: {
          enabled: 0
        },
        caption: {
          text: "Intraday movements of " + this.ticker
        },
        yaxis: [
          {
            plot: [
              {
                value: "Price",
                //type: 'line',
                connectnulldata: true,
                style: {
                  "plot.null": {
                    "stroke-dasharray": "none",
                  }
                }
              }
            ]
          }
        ],
        //numbersuffix: "K",
        theme: "fusion",
        data: this.dataStore.createDataTable(this.chartData, this.schema)
      }
      console.log(r)
      return r
    },
    ...mapState(['ticker'])
    // ticker:
    //   {
    //     console.log("Computer Called")
    //     return this.$store.getters.getTicker
    //   }
  },

  created(){
    this.$store.watch(
      (state)=>{
        return this.$store.state.ticker // could also put a Getter here
      },
      (newValue, oldValue)=>{
        //something changed do something
        console.log(oldValue)
        console.log(newValue)
        this.getIntraday()
      }
    )
  },

}

</script>
