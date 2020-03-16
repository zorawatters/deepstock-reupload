//Loading data

const loadData = d3.json("stockDataExample.json", function(data){console.log(data);});

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
