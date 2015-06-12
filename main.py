import gspread
import json

from email_lib import send_email
from spreadsheet_utils import *
from oauth2client.client import SignedJwtAssertionCredentials
from random import shuffle

with open('config.json') as json_data_file:
    data = json.load(json_data_file)['gspread']

json_key = json.load(open(str(data['private_key_file'])))
scope = ['https://spreadsheets.google.com/feeds']

credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'], scope)
gc = gspread.authorize(credentials)

worksheet = gc.open(str(data['sheet_name'])).sheet1

emails = clean(worksheet.col_values(2))
first_names = clean(worksheet.col_values(3))
last_names = clean(worksheet.col_values(4))
attending = clean(worksheet.col_values(5))
availability = clean(worksheet.col_values(6))

attendees = filter_attending_and_compress(emails, first_names, last_names, attending, availability)

# Randomly permute list
shuffle(attendees)

group_size = int(data['group_size'])

itr = [iter(attendees)]*group_size

attendees = zip(*itr)

for group in attendees:
    send_email(group)
