import gspread
import google
from google.oauth2.service_account import Credentials


def get_gsheets_connection(sheet_name, worksheet="Sheet1"):
    scopes = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive",
    ]

    credentials, _ = google.auth.default(scopes=scopes)
    gc = gspread.Client(credentials)
    sh = gc.open(sheet_name)
    return sh.worksheet(worksheet)


# def get_gsheets_connection(sheet_name, worksheet="Sheet1", cred_file='svc.json'):
#     scopes = [
#         "https://www.googleapis.com/auth/spreadsheets",
#         "https://www.googleapis.com/auth/drive",
#     ]

#     # Load credentials from the specified file
#     credentials = Credentials.from_service_account_file(cred_file, scopes=scopes)

#     gc = gspread.authorize(credentials)
#     sh = gc.open(sheet_name)
#     return sh.worksheet(worksheet)


# takes a worksheet connection returned by get_gsheets_connection
def read_gsheet(conn):
    return conn.get_all_records()


def write_gsheet(conn, row):
    conn.insert_row(row, 2, value_input_option='USER_ENTERED')

def read_from_url(url):
    scopes = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive",
    ]

    credentials, _ = google.auth.default(scopes=scopes)
    gc = gspread.Client(credentials)
    sh = gc.open_by_url(url)
    return sh.worksheet('Sheet1').get_all_records()

# def read_from_url(url, cred_file='svc.json'):
#     scopes = [
#         "https://www.googleapis.com/auth/spreadsheets",
#         "https://www.googleapis.com/auth/drive",
#     ]

#     credentials = Credentials.from_service_account_file(cred_file, scopes=scopes)
#     gc = gspread.Client(credentials)
#     sh = gc.open_by_url(url)
#     return sh.worksheet('Sheet1').get_all_records()
