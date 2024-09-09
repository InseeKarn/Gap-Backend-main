const express = require('express')
const router = express.Router()

router.get('/product',(req,res)=>{
  res.send('This is product endpoint')
})

module.exports = router