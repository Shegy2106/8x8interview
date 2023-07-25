from fastapi import FastAPI
from fastapi.responses import JSONResponse
from typing import Dict, Any
from fastapi.middleware.cors import CORSMiddleware

from .api.fetch_spreadsheet import fetch_spreadsheet

app = FastAPI()

origins = [
    "http://localhost:8080",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/post_spreadsheet/")
def post_spreadsheet(spreadsheet_data: Dict[Any, Any]):
    """
    Fetches the spreadsheet data from the Google Sheets API
    
    Parameters:
        - spreadsheet_id: SpreadsheetID which is part of the URL in Google Sheets
        - spreadsheet_range: Array of sheet pages
    Returns:
        - values: Values of sheet pages
    """
    return JSONResponse({
        "spreadsheet_data": fetch_spreadsheet(spreadsheet_data["spreadsheet_id"], spreadsheet_data["spreadsheet_range"])
    })
