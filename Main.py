import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Set up credentials
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_name('path/to/your/credentials.json', scope)
client = gspread.authorize(credentials)

# Open the Google Sheet by URL
sheet_url = 'https://docs.google.com/spreadsheets/d/1wLgOsqbkdAue6kV3AJZHOgp3kXOF0mvD1OYPLqpKR_M/edit#gid=0'
spreadsheet = client.open_by_url(sheet_url)

# Select the desired worksheets
sheet1 = spreadsheet.get_worksheet(0)  # Assuming the first sheet
sheet2 = spreadsheet.get_worksheet(1)  # Assuming the second sheet

# Get data in the first column of both sheets
data_sheet1 = sheet1.col_values(1)
data_sheet2 = sheet2.col_values(1)

# Compare data and print if not present in sheet2
for item in data_sheet1:
    if item not in data_sheet2:
        print(f"Data in sheet1 not present in sheet2: {item}")
