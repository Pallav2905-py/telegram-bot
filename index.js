const express = require('express')
const app = express()
const port = 3000

app.get('/', (req, res) => {
  res.send('Server is Running')
})

app.listen(port, () => {
  console.log(`Render Support for alive Deamon Support app listening on port ${port}`)
})