//Loading data

const loadData = d3.json("stockDataExample.json",function(data) {
    // console.log(data);

    for (var i = 0; i < data.length; i++) {
       console.log(data[i].Volume);
       console.log(data[i].High);
   }

});

//   "Date":"2020-03-06T00:00:00.000Z",
  // "Open":162.61,
  // "High":163.11,
  // "Low":156.0,
  // "Close":161.57,
  // "Volume":72790000,
  // "Dividends":0,
  // "Stock Splits":0

// .then(data => {
//   const chartResultsData = data['chart']['result'][0];
//   const quoteData = chartResultsData['indicators']['quote'][0];
//   return chartResultsData['timestamp'].map((time, index) => ({
//     date: new Date(time * 1000),
//     high: quoteData['high'][index],
//     low: quoteData['low'][index],
//     open: quoteData['open'][index],
//     close: quoteData['close'][index],
//     volume: quoteData['volume'][index]
//   }));
// });
