const express = require('express')
require('dotenv').config()

const app = express()


app.get('/', (req, res) => {
    res.send('hi')
})

app.listen(process.env.PORT, ()=> {
    console.log('listening on: ' + process.env.PORT);
})