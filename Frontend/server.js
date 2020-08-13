const express = require('express');
var cors = require('cors')
const fetch   = require('node-fetch');
const bodyParser = require('body-parser')
const path = require('path');

const app = express();
app.use(cors())
console.log(__dirname)
app.use(express.static(path.join(__dirname, 'public')));
app.listen(process.env.PORT || 8080);