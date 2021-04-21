var config = require('config')
var express = require('express')
var data = require("/app/public/widgets.json")
var app = express()
app.set('port', (process.env.PORT || 5000))
app.use(express.static(__dirname + '/public'))

app.get('/name', function(request, response) {
  response.send(data + process.env.MYNAME)})

app.get('/api', function(request, response) {
    response.writeHead(200, {"Content-Type": "text/json"})
    response.end(JSON.stringify(data))
})
app.get('/', function(request, response) {
    if (config.util.getEnv("NODE_ENV") === "Testing") {    
      response.send('<b>You are working in the <em>TEST</em> environment.</b>')  }  
    else if (config.util.getEnv("NODE_ENV") === "HerokuTest") {   
      response.send('<b>You are working in the <em>TEST</em> environment that is in Heroku.</b>')  } 
    else if (config.util.getEnv("NODE_ENV") === "Production") {    response.send('<b>You are working in Production</b>')  } 
  
    else {    response.send('<b>Environment is unknown</b>')
    }})
 
  //response.send('Hello World! My name is = <em>' + process.env.MYNAME + '</em <br /> My Node Environemnt is :' + config.util.getEnv('NODE_ENV') + '</em></b>')})

app.listen(app.get('port'), function() {
  console.log("Node app is running at localhost:" + app.get('port'))
})
