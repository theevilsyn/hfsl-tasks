import base64
import datetime
import pickle
import subprocess
from email.mime.text import MIMEText
from time import sleep

import pytz
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from requests import HTTPError

SCOPES = ["https://www.googleapis.com/auth/gmail.send"]

def get_service():
    flow = InstalledAppFlow.from_client_secrets_file(
        'credentials.json', SCOPES)
    creds = flow.run_console()
    with open('token.pickle', 'wb') as token:
        pickle.dump(creds, token)
    service = build('gmail', 'v1', credentials=creds)
    return service

def send_email(to, cc, subject, body, service):
    message = MIMEText(body)
    message['to'] = to
    message['cc'] = cc
    message['subject'] = subject
    create_message = {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}
    try:
        message = (service.users().messages().send(userId="me", body=create_message).execute())
        print(F'Sent message to {to} Message Id: {message["id"]}')
    except HTTPError as error:
        print(F'An error occurred: {error}')
        message = None

def main():
    # while true and send mail every 12 hours
    service = get_service()
    while True:
        # get time in EST time zone
        result = subprocess.run(["df", "-h"], stdout=subprocess.PIPE).stdout.decode()
        send_email(
                'fscadmin@stevens.edu',
                'jbommidi@stevens.edu',
                'Jaswanth Bommidi - Linux ML Task Update',
                f'df -h output at {datetime.datetime.now(pytz.timezone("US/Eastern"))} \n\n\n{result}',
                service,
        )
        print("sent email")
        sleep(12 * 60 * 60)

if __name__ == '__main__':
    main()