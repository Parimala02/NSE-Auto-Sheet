import gspread
import json
import os
from oauth2client.service_account import ServiceAccountCredentials

scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

creds_dict = json.loads(os.environ["GCP_CREDENTIALS"])

creds = ServiceAccountCredentials.from_json_keyfile_dict(
    creds_dict,
    scope
)

client = gspread.authorize(creds)

spreadsheet_id = "1J4t2-naYt2UBtgCsPDw25qjwE14YdSo614doG5AM2LY"

worksheet = client.open_by_key(spreadsheet_id).worksheet("Top 250 Stocks")

print("Connected Successfully")
