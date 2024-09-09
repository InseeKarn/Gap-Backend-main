const express = require('express')

const productRouter = require('./Routes/product')
const app = express();

// // Route 1
// app.get('')


// Route 2
app.use('/api', productRouter)

app.listen(5000,()=> console.log('server is Online!'))