const express = require('express');
const app = express();
const PORT = 5000;

// Route
app.get('/', (req, res) => {
  res.send('AI Powered Investment Platform on port',PORT);
});

// Start server
app.listen(PORT, () => {
  console.log(`Server is running at http://localhost:${PORT}`);
});
