<template>
  <div id="chart">

  </div>
</template>
<script>
import FusionCharts from 'fusioncharts/core';
import TimeSeries from 'fusioncharts/viz/timeseries';
import DataStore from 'fusioncharts/datastore';

FusionCharts.addDep(TimeSeries);

let fusionDataStore = new DataStore();

let data = [
    [
        "United States",
        "1/4/2011",
        16.448
    ],
    [
        "United States",
        "1/5/2011",
        272.736
    ],
    [
        "United States",
        "1/5/2011",
        11.784
    ],
    [
        "India",
        "12/31/2014",
        364.59
    ],
    [
        "India",
        "12/31/2014",
        72
    ],
    [
        "India",
        "12/31/2014",
        39.42
    ]
]
let schema = [{
    "name": "Country",
    "type": "string"
}, {
    "name": "Time",
    "type": "date",
    "format": "%-m/%-d/%Y"
}, {
    "name": "Sales",
    "type": "number"
}]
let fusionTable = fusionDataStore.createDataTable(data, schema);
window.charInstance = new FusionCharts({
  type: 'timeseries',
  renderAt: 'chart',
  width: "90%",
  height: 650,
  dataSource: {
    data: fusionTable,
    chart: {
    },
    caption: {
      text: 'Online Sales of a SuperStore in India & the US'
    },
    yAxis: [{
      "plot": {
        "value": "Sales",
        "type": "line"
      }
    }],
    "series": "Country"
  }
});

export default{
  name: "stockCard",
  data() {
    return {

    }
  }
}

</script>
