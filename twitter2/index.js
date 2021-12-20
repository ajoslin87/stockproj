var Twit = require('twit');
const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout 
});

rl.question("What would you like to search?", function(search){
    searchQuery = search;
    rl.close();
})

var dataLog=[];

var T = new Twit({
    consumer_key:         'XPMWorkzQS2VGyypoIgF8MG6V',
    consumer_secret:      'PO1bGlO2X1VwDAtiB2a3IEGCYw76mpkCimVsBj4IP4uJ91C0d4',
    access_token:         '256651975-AfyYLcBHq81IIs08fTcDJxjDkI6kQFpY9zbDBIDP',
    access_token_secret:  'fotBadtibQS4lok9iCTxboa7Cu1HAqTrNMquJRsnA8Ddj',
    timeout_ms:           60*1000,  // optional HTTP request timeout to apply to all requests.
    strictSSL:            true,     // optional - requires SSL certificates to be valid.
})


var getTwitter = function() {
    T.get('tweets/search/fullarchive/FADev', {
        query: searchQuery,
        fromDate: 202106302000,
        toDate: 202107011500,
        maxResults: 10

    }, function (err, data, response) {
        console.log(data)
        dataLog.push(data);
        //console.log(dataLog[0]);

    })
};

rl.on('close', function(){
getTwitter();
// process.exit(0);
});






