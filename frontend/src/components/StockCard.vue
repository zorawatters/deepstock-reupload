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


// STEP 3: Configure your chart
const dataSource = {
  chart: {
    caption: "Intraday movements",
    subcaption: "In MMbbl = One Million barrels",
    xaxisname: "Country",
    yaxisname: "Reserves (MMbbl)",
    numbersuffix: "K",
    theme: "fusion"
  },
  data: chartData
};

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
}

</script>
