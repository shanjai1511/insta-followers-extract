import gspread
from google.auth import exceptions
from google.auth.transport.requests import Request
from google.auth.service_account import Credentials


class GoogleSheetController:
    def __init__(self, credentials_path):
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        credentials = ServiceAccountCredentials.from_json_keyfile_name(credentials_path, scope)
        self.client = gspread.authorize(credentials)

    def get_sheet(self, sheet_url, sheet_index=0):
        spreadsheet = self.client.open_by_url(sheet_url)
        return spreadsheet.get_worksheet(sheet_index)

class DataComparer:
    def __init__(self, sheet_controller):
        self.sheet_controller = sheet_controller

    def compare_sheets(self, sheet1_url, sheet2_url):
        sheet1 = self.sheet_controller.get_sheet(sheet1_url)
        sheet2 = self.sheet_controller.get_sheet(sheet2_url)

        data_sheet1 = set(sheet1.col_values(1)[1:])  # Exclude header
        data_sheet2 = set(sheet2.col_values(1)[1:])  # Exclude header

        return data_sheet1 - data_sheet2

class ConsoleView:
    @staticmethod
    def print_missing_data(missing_data):
        if missing_data:
            print("Data present in sheet1 but not in sheet2:")
            for item in missing_data:
                print(item)
        else:
            print("No missing data found.")

def main():
    try:
        credentials_path = '/workspaces/insta-followers-extract/scraping-407215-2d3d1ad6fc20.json'  # Replace with your credentials path
        sheet1_url = 'https://docs.google.com/spreadsheets/d/1wLgOsqbkdAue6kV3AJZHOgp3kXOF0mvD1OYPLqpKR_M/edit#gid=0'
        sheet2_url = 'https://docs.google.com/spreadsheets/d/1wLgOsqbkdAue6kV3AJZHOgp3kXOF0mvD1OYPLqpKR_M/edit#gid=844854727'  # Replace with actual sheet2 GID

        sheet_controller = GoogleSheetController(credentials_path)
        data_comparer = DataComparer(sheet_controller)

        missing_data = data_comparer.compare_sheets(sheet1_url, sheet2_url)

        view = ConsoleView()
        view.print_missing_data(missing_data)

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()