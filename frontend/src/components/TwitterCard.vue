<template>
  <div>
    <div class="card text-center">

      <div class="card-body">
        <h5 class="card-title">Company Tweets</h5>
        <p class="card-text">INSERT TWEET HERE</p>
        <a href="#" class="btn btn-info">Link to tweet/bio?</a>
      </div>
      <div class="card-footer text-muted">
        Display how recent tweet was posted
      </div>
    </div>

    <div :class = "custom">
      <fusioncharts
      :type="type"
      :width="width"
      :height="height"
      :dataFormat="dataFormat"
      :dataSource="dataSource"
      ></fusioncharts>
  </div>
  </div>
</template>
<script>
export default {
  name: 'twitter-card',
  props: {
    custom: {
      type: String,
      default: ''
    },
    ticker: {
      type: String,
      default: ''
    }
  },
  data(){
    return {
    {
  "chart": {
    "caption": "Countries With Most Oil Reserves [2017-18]",
    "subCaption": "In MMbbl = One Million barrels",
    "xAxisName": "Country",
    "yAxisName": "Reserves (MMbbl)",
    "numberSuffix": "K",
    "theme": "candy"
  },
  "data": [
    {
      "label": "Venezuela",
      "value": "290"
    },
    {
      "label": "Saudi",
      "value": "260"
    },
    {
      "label": "Canada",
      "value": "180"
    },
    {
      "label": "Iran",
      "value": "140"
    },
    {
      "label": "Russia",
      "value": "115"
    },
    {
      "label": "UAE",
      "value": "100"
    },
    {
      "label": "US",
      "value": "30"
    },
    {
      "label": "China",
      "value": "30"
    }
  ]
}
    }
  }
}
</script>
