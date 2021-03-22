//Used some links for help, here are my references
//https://www.geeksforgeeks.org/node-js-os-uptime-method/ : 
//https://


.com/questions/28705009/how-do-i-get-the-server-uptime-in-node-js/28706630

var http = require("http");h
var fs = require("fs");
var os = require("os");kk 

var ip = require('ip');
const { cpuUsage } = require("process");
const { time } = require("console");


http.createServer(function(req, res){

    if (req.url === "/") {
        fs.readFile("./public/index.html", "UTF-8", function(err, body){
        res.writeHead(200, {"Content-Type": "text/html"});
        res.end(body);
    });
}
    else if(req.url.match("/sysinfo")) {
        myHostName=os.hostname();
        myfreemem=os.freemem();
        
        var ut_sec = os.uptime(); 
var ut_min = ut_sec/60; 
var ut_hour = ut_min/60; 
   
ut_sec = Math.floor(ut_sec); 
ut_min = Math.floor(ut_min); 
ut_hour = Math.floor(ut_hour); 
  
ut_hour = ut_hour%60; 
ut_min = ut_min%60; 
ut_sec = ut_sec%60; 
  
        
        html=`    
        <!DOCTYPE html>
        <html>
          <head>
            <title>Node JS Response</title>
          </head>
          <body>
            <p>Hostname: ${myHostName}</p>
            <p>IP: ${ip.address()}</p>
            <p>Server Uptime: ${ut_hour} Hours ${ut_min} mins ${ut_sec} seconds </p>
            <p>Total Memory: ${os.totalmem /1024/ 1024 }MB  </p>
            <p>Free Memory: ${myfreemem / 1024 /1024 }MB </p>
            <p>Number of CPUs: ${os.cpus().length} </p>            
          </body>
        </html>` 
        res.writeHead(200, {"Content-Type": "text/html"});
        res.end(html);
    }
    else {
        res.writeHead(404, {"Content-Type": "text/plain"});
        res.end(`404 File Not Found at ${req.url}`);
    }
}).listen(3000);

console.log("Server listening on port 3000");
