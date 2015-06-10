import gspread
import json

from email_lib import send_email
from spreadsheet_utils import *
from oauth2client.client import SignedJwtAssertionCredentials

with open('config.json') as json_data_file:
    data = json.load(json_data_file)['gspread']

json_key = json.load(open(str(data['private_key_file'])))
scope = ['https://spreadsheets.google.com/feeds']

credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'], scope)
gc = gspread.authorize(credentials)

worksheet = gc.open(str(data['sheet_name'])).sheet1

emails = clean(worksheet.col_values(1))
first_names = clean(worksheet.col_values(2))
last_names = clean(worksheet.col_values(3))
attending = clean(worksheet.col_values(4))

print emails

emails, first_names, last_names = filter_attending(emails, first_names, last_names, attending)

print emails
