from fastapi import FastAPI
from fastapi.responses import JSONResponse
from typing import Dict, Any
from fastapi.middleware.cors import CORSMiddleware

from .api.fetch_spreadsheet import fetch_spreadsheet

app = FastAPI()

# Set the allowed origins to include your frontend domain
origins = [
    "http://localhost:5173",
    # Add more origins if needed
]

# Add the CORS middleware to allow requests from the specified origins
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
        - spreadsheet_id: 
        - spreadsheet_range: 
    Returns:
        - values: 
    """
    return JSONResponse({
        "spreadsheet_data": fetch_spreadsheet(spreadsheet_data["spreadsheet_id"], spreadsheet_data["spreadsheet_range"])
    })
