var Stocks = require('stocks.js');
var stocks = new Stocks('RZXB30M95TMXXOAZ');


async function query(ticker){

  var options = {
    symbol: ticker,
    interval: '1min',
    amount: 2
  };
  
var result = await stocks.timeSeries(options);

console.log(result);

}

module.exports.query = query; 

