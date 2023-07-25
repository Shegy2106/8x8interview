import React, { useState, useMemo, useEffect } from "react";
import axios from "axios";
import Table from "./Table";

const SpreadsheetTable = () => {
  const [data, setData] = useState([]);
 
  
  const generateColumns = (data) => {
    if (data.length === 0) {
      return []; 
    }

    return Object.keys(data[0]).map((key) => ({
      Header: key,
      accessor: key,
    }));
  };

  const generatedColumns = useMemo(() => generateColumns(data), [data]);
  
  // Define columns for the table
  // const columns = useMemo(
  //   () => [
  //     {
  //       // first group - TV Show
  //       Header: "Personal Call Handling",
  //       // First group columns
  //       columns: [
  //         {
  //           Header: "Number",
  //           accessor: "Number",
  //         },
  //         {
  //           Header: "Message",
  //           accessor: "Message",
  //         },
  //         {
  //           Header: "Handling",
  //           accessor: "Handling",
  //         },
  //         {
  //           Header: "Language",
  //           accessor: "Language",
  //         },
  //       ],
  //     },
      // {
      //   // Second group - Details
      //   Header: "Details",
      //   // Second group columns
      //   columns: [
      //     {
      //       Header: "Language",
      //       accessor: "show.language",
      //     },
      //     {
      //       Header: "Genre(s)",
      //       accessor: "show.genres",
      //     },
      //     {
      //       Header: "Runtime",
      //       accessor: "show.runtime",
      //     },
      //     {
      //       Header: "Status",
      //       accessor: "show.status",
      //     },
      //   ],
      // },
  //   ],
  //   []
  // );


  useEffect(() => {
    (async () => {
      try {
        const spreadsheet_id = "1m3vhA2A2ACOfcKJnfjGPybyIlQwYPxIyMf0F0gJjgHQ"
        const spreadsheet_range = "Personal Call Handling";
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
    <div>
      <h1>Spreadsheet Data</h1>
      {data.length === 0 ? (
        <p>Loading data...</p>
      ) : (
        <Table data={data} columns={generatedColumns} />
      )}
    </div>
  );
};

export default SpreadsheetTable;
