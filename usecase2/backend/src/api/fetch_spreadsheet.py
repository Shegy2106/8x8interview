from __future__ import print_function

from ..utils.generate_credentials import generate_credentials
from ..utils.convert_to_dictionary import convert_to_dictionary

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1m3vhA2A2ACOfcKJnfjGPybyIlQwYPxIyMf0F0gJjgHQ'
SAMPLE_RANGE_NAME = 'Personal Call Handling'

def fetch_spreadsheet(spreadsheet_id, spreadsheet_range):
    creds = generate_credentials(SCOPES)

    try:
        service = build('sheets', 'v4', credentials=creds)
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=spreadsheet_id,
                                    range=spreadsheet_range).execute()
        values = result.get('values', [])

        if not values:
            print('No data found.')
            return

        for row in values:
            print(row)
    except HttpError as err:
        print(err)

    values_dictionary = convert_to_dictionary(values)
    
    return values_dictionary