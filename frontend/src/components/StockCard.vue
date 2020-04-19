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
export default {
  name: 'stock-card',
  props: {
    custom: {
      type: String,
      default: ''
    },
    ticker: {
      type: String,
      default: 'TSLA'
    }
  },
  data() {
    return {
      type: "timeseries",
      width: "550",
      height: "350",
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
      var response = await this.$http.get(this.$backendUrl + '/' + this.ticker + '/intraday')
      var data = response.data
      this.chartData = []

      for(var datetime in data){
        this.chartData.push([datetime, Number(data[datetime][0]['4. close'])])

      }
    }
  },
  computed:{
    dataSource: function(){
      
      var r =  {
        chart: {
          caption: "Intraday movements of " + this.ticker,
          //subcaption: "In MMbbl = One Million barrels",
          xaxisname: "Time",
          yaxis: [
            {
              plot: [
                {
                  value: "Price",
                  type: 'line',
                  style: {
                    plot: {
                      "stroke-dasharray": "5 2"
                    }
                  }
                }
              ]
            }
          ],
          //numbersuffix: "K",
          theme: "fusion"
        },
        data: this.dataStore.createDataTable(this.chartData, this.schema)
      }
      console.log(r)
      return r
    }
  },
  watch:{
  	ticker: function(newVal){
  		this.getIntraday()
  	}
  }
}

</script>
