<template>
<div :class = "custom" id="chart-container">
      <fusioncharts
      :type="type"
      :width="width"
      :height="height"
      :dataformat="dataFormat"
      :dataSource="dataSource"
      >
      </fusioncharts>
</div>
</template>
<script>
// STEP 2: Prepare the data
const chartData = [
    {
      label: "Venezuela",
      value: "290"
    },
    {
      label: "Saudi",
      value: "260"
    },
    {
      label: "Canada",
      value: "180"
    },
    {
      label: "Iran",
      value: "140"
    },
    {
      label: "Russia",
      value: "115"
    },
    {
      label: "UAE",
      value: "100"
    },
    {
      label: "US",
      value: "30"
    },
    {
      label: "China",
      value: "30"
    }
  ];

// STEP 3: Configure your chart
const dataSource = {
  chart: {
    caption: "Countries With Most Oil Reserves [2017-18]",
    subcaption: "In MMbbl = One Million barrels",
    xaxisname: "Country",
    yaxisname: "Reserves (MMbbl)",
    numbersuffix: "K",
    theme: "fusion"
  },
  data: chartData
  };
  <div :class = "custom">
    <fusioncharts
    :type="type"
    :width="width"
    :height="height"
    :dataFormat="dataFormat"
    :dataSource="dataSource"
    ></fusioncharts>

  </div>
</template>
<script>

import { mapGetters } from 'vuex';

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
      "type": "column2d",
      "renderAt": "chart-container",
      "width": "550",
      "height": "350",
      "dataFormat": "json",
      dataSource
    }
  }
      type: "timeseries",
      width: "100%",
      height: "85%",
      dataFormat: "json",
      dataStore: new FusionCharts.DataStore(),
      schema: [{
        name: "Time",
        type: "date",
        format: "%Y-%m-%d %-H:%M:%S"
      }, {
        name: "Price",
        type: "number"
      }],
    }
  },

  computed:{
    dataSource(){
      this.dataStore.dispose()
      this.dataStore = new FusionCharts.DataStore()
      return ({
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
      })
    },
    ...mapGetters({
      ticker:'getTicker',
      chartData: 'getChartData'
    })
  },
}

</script>
