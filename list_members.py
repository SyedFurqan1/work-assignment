# API Reference: https://developers.google.com/admin-sdk/directory/reference/rest/v1/members
# Request Object of Members: https://developers.google.com/admin-sdk/directory/reference/rest/v1/members#Member

import os.path
import argparse
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

def google_quickstart():
    # If modifying these scopes, delete the file token.json.
    SCOPES = ['https://www.googleapis.com/auth/admin.directory.member']

    # Reference sample authentication code from Google: https://developers.google.com/admin-sdk/directory/v1/quickstart/python 
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    
    service = build('admin', 'directory_v1', credentials=creds)

    return service

def list_members(client, group_key):
    results = client.members().list(groupKey=group_key, includeDerivedMembership=True).execute()
    return results

def main(group_key):
    # Initialize Google API Client
    client = google_quickstart()

    # Adding members to the group
    results = list_members(client, group_key)
    print(results)



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--email", help="Group Email", required=True)
    args = parser.parse_args()

    while input("Proceeding will list the members in the group provided as the input.\n Do You Want To Continue? [Proceed/No]") == "Proceed":
        print("Alright, go ahead.")
        main(args.email)
        break