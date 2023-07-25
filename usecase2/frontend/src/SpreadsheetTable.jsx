import React, { useState, useMemo, useEffect } from "react";
import axios from "axios";
import Table from "./Table";
import './assets/spreadsheet.css'

const SpreadsheetTable = () => {
  const [data, setData] = useState([]);
  const [currentPage, setCurrentPage] = useState(0);
  const spreadsheet_id = "1m3vhA2A2ACOfcKJnfjGPybyIlQwYPxIyMf0F0gJjgHQ"
  const spreadsheet_range = ["Personal Call Handling", "DNIS"];
 
  const generateColumns = (data) => {
    if (data.length === 0) {
      return []; 
    }

    return Object.keys(currentSheetData[0]).map((key) => ({
      Header: key,
      accessor: key,
    }));
  };

  const handleClickSheet = (index) => {
    setCurrentPage(index)
  }

  const currentSheetName = spreadsheet_range[currentPage];

  const currentSheetData = data[currentSheetName];

  const generatedColumns = useMemo(() => generateColumns(data), [data, currentPage]);

  useEffect(() => {
    (async () => {
      try {
        const response = await axios.post("http://localhost:8000/post_spreadsheet", {
          spreadsheet_id,
          spreadsheet_range,
        });
        
        setData(response.data.spreadsheet_data);
      } catch (error) {
        console.error("Error fetching data:", error);
        setData([]);
      }
    })();
  }, []);

  return (
    <>
      <h1>Spreadsheet Data</h1>
      <div className="dataTable">
        {data.length === 0 ? (
          <p>Loading data...</p>
        ) : (
          <React.Fragment>
            <div className="sheetsButtons">
              {spreadsheet_range.map((sheet, index) => (
                  <button
                    key={index}
                    onClick={() => handleClickSheet(index)}
                    disabled={index === currentPage}
                  >
                    {sheet}
                  </button>
                ))}
            </div>
            <Table data={currentSheetData} columns={generatedColumns} />
            <div className="sheetsButtons">
              {spreadsheet_range.map((sheet, index) => (
                  <button
                    key={index}
                    onClick={() => handleClickSheet(index)}
                    disabled={index === currentPage}
                  >
                    {sheet}
                  </button>
                ))}
            </div>
          </React.Fragment>
        )}
      </div>
    </>
  );
};

export default SpreadsheetTable;
