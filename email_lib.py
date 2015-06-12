import yagmail
import datetime
import json
import random

def send_email(recipients):
    ''' Send an email to recipients '''
    with open('config.json') as config:
        data = json.load(config)['email']

    recipient_addresses, names = [address for (address, _, _, _) in recipients], [name for (_, name, _, _) in recipients]

    sender = str(data['sender'])
    yag = yagmail.Connect(sender)

    people = ', '.join(names[:-1])
    last_person = names[-1]
    cafes = data['cafes']
    cafe = random.choice(cafes)
    signup_link = data['signup_link']

    date = datetime.datetime.now()
    subject = str(data['subject']) + str(date.month) + '/' + str(date.day)
    message = str(data['message'])
    contents = [message.format(people, last_person, cafe, signup_link)]

    yag.send(recipient_addresses, subject, contents) 
