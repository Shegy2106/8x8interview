from __future__ import print_function

from ..utils.generate_credentials import generate_credentials
from ..utils.convert_to_dictionary import convert_to_dictionary

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

def fetch_spreadsheet(spreadsheet_id, spreadsheet_range):
    creds = generate_credentials(SCOPES)

    values_dictionary = {}

    for i in range(len(spreadsheet_range)):
        try:
            service = build('sheets', 'v4', credentials=creds)
            sheet = service.spreadsheets()
            result = sheet.values().get(spreadsheetId=spreadsheet_id,
                                        range=spreadsheet_range[i]).execute()
            values = result.get('values', [])

            if not values:
                print('No data found.')
                return

            for row in values:
                print(row)
            
            
            values_dictionary[spreadsheet_range[i]] = convert_to_dictionary(values)

        except HttpError as err:
            print(err)
        
    
    return values_dictionary