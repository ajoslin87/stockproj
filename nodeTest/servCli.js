const mqtt = require('mqtt')

// const io = reqire('socket.io')

var query = require ('./stockMachine');

const options={
    port:1883
}
var client = mqtt.connect({ host: "broker.hivemq.com", options});

client.subscribe('aj/switch/ticker/#')

client.on('connect', function(){
    console.log('connected')
})

client.on('message', function(topic, message){
    var ticker = message.toString();
    console.log(message.toString());
    query.query(ticker)
})

