var express = require('express')
var app = express()

app.use(express.static('public'));
app.use('/css', express.static(__dirname + '/public/css'));
var server = app.listen(8080, function(){
    var port = server.address().port;
    console.log("Server started at http://localhost:%s", port);
});