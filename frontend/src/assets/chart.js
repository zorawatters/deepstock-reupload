<<<<<<< HEAD
// //Loading data
// import * as d3 from 'd3'
//
// const loadData = d3.json("stockDataExample.json").then(function(data) {
//     console.log(data);
//     var line_data = {}
//     for (var i = 0; i < data.length; i++) {
//        line_data['timestamp'].push(data[i].date)
//        line_date['high'].push(data[i].High)
//        line_data.y.push(data[i].High)
//        console.log(data[i].Date);
//        console.log(data[i].Open);
//        console.log(data[i].High);
//        console.log(data[i].Low);
//        console.log(data[i].Close);
//        console.log(data[i].Volume);
//
//
//        //d3.select("body")
//        //     .selectAll("p" + i)
//         //    .data(data)
//          //   .enter()
//           //  .append("p")
//            // .text(data[i].Name + ", " + data[i].High)
//   }
=======
//Loading data
import * as d3 from 'd3'
/*
const loadData = d3.json("stockDataExample.json").then(function(data) {
    console.log(data);
    var line_data = {}
    for (var i = 0; i < data.length; i++) {
       line_data['timestamp'].push(data[i].date)
       line_date['high'].push(data[i].High)
       line_data.y.push(data[i].High)
       console.log(data[i].Date);
       console.log(data[i].Open);
       console.log(data[i].High);
       console.log(data[i].Low);
       console.log(data[i].Close);
       console.log(data[i].Volume);
   

       //d3.select("body")
       //     .selectAll("p" + i)
        //    .data(data)
         //   .enter()
          //  .append("p")
           // .text(data[i].Name + ", " + data[i].High)
  }
  const chartResultsData = data['chart']['result'][0];
  const quoteData = chartResultsData['indicators']['quote'][0];
  return chartResultsData['timestamp'].map((time, index) => ({
    date: new Date(time * 1000),
    high: quoteData['high'][index],
    low: quoteData['low'][index],
    open: quoteData['open'][index],
    close: quoteData['close'][index],
    volume: quoteData['volume'][index]
  }));
});
*/
/*async function get_chart(){
  const stock_json = await d3.json('stockDataExample.json')

  stock_json.forEach(data => {
    for(key in data){
      console.log(data[key])
    }
  })

  const chartResultsData = data['chart']['result'][0];
  const quoteData = chartResultsData['indicators']['quote'][0];
  return chartResultsData['timestamp'].map((time, index) => ({
    date: new Date(time * 1000),
    high: quoteData['high'][index],
    low: quoteData['low'][index],
    open: quoteData['open'][index],
    close: quoteData['close'][index],
    volume: quoteData['volume'][index]
  }));
}*/

//   "Date":"2020-03-06T00:00:00.000Z",
  // "Open":162.61,
  // "High":163.11,
  // "Low":156.0,
  // "Close":161.57,
  // "Volume":72790000,
  // "Dividends":0,
  // "Stock Splits":0

// .then(data => {
>>>>>>> 073ebfce4ba5af9fde00e860d062e6de3d860066
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
//
// /*async function get_chart(){
//   const stock_json = await d3.json('stockDataExample.json')
//
//   stock_json.forEach(data => {
//     for(key in data){
//       console.log(data[key])
//     }
//   })
//
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
// }*/
//
// //   "Date":"2020-03-06T00:00:00.000Z",
//   // "Open":162.61,
//   // "High":163.11,
//   // "Low":156.0,
//   // "Close":161.57,
//   // "Volume":72790000,
//   // "Dividends":0,
//   // "Stock Splits":0
//
// // .then(data => {
// //   const chartResultsData = data['chart']['result'][0];
// //   const quoteData = chartResultsData['indicators']['quote'][0];
// //   return chartResultsData['timestamp'].map((time, index) => ({
// //     date: new Date(time * 1000),
// //     high: quoteData['high'][index],
// //     low: quoteData['low'][index],
// //     open: quoteData['open'][index],
// //     close: quoteData['close'][index],
// //     volume: quoteData['volume'][index]
// //   }));
// // });
