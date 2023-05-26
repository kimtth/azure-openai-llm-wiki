const https = require('https');
const express = require("express");
const app = express();
var port = 8000;

app.use(express.static("public"));

app.listen(port, () => console.log('Your app is ready! Navigate to: http://localhost:' + port + '/.'));
