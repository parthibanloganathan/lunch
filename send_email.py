import yagmail
import datetime
import json
import random

with open('config.json') as config:
    data = json.load(config)

sender = str(data['sender'])
yag = yagmail.Connect(sender)

FIRST_NAMES = []
CAFES = []

people = ', '.join(FIRST_NAMES[:-1])
last_person = FIRST_NAMES[-1]
cafe = random.choice(CAFES)
signup_link = data['signup_link']

recipients = []

date = datetime.datetime.now()
subject = 'Intern Lunch Group - ' + str(date.month) + '/' + str(date.day)
message = str(data['message'])
contents = [message.format(people, last_person, cafe, signup_link)]

yag.send(recipients, subject, contents) 
