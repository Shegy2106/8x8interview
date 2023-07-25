import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import SpreadsheetTable from './SpreadsheetTable.jsx'
import './index.css'

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <SpreadsheetTable />
  </React.StrictMode>,
)
