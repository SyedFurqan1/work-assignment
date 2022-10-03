# API Reference: https://developers.google.com/admin-sdk/directory/reference/rest/v1/groups/insert
# Request Object of Group: https://developers.google.com/admin-sdk/directory/reference/rest/v1/groups#Group

import os.path
import argparse
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

def google_quickstart():
    # If modifying these scopes, delete the file token.json.
    SCOPES = ['https://www.googleapis.com/auth/admin.directory.group']

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

# The following function is just to list the groups. Not being used in this script.
def list_group(client):
    results = client.groups().list(customer='my_customer', maxResults=10).execute()
    return results

def create_group(client, group):
    results = client.groups().insert(body=group).execute()
    return results

def main(group_name, group_email):
    # Initialize Google API Client
    client = google_quickstart()

    group =   {
        "id": "testgroupid",
        "email": group_email,
        "name": group_name,
        "description": "Test group created for Work Assignment.",
        "adminCreated": True
    }

    # Creating Group on Google Workspace
    results = create_group(client, group)
    print(results)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-g", "--group", help="Group Name", required=True)
    parser.add_argument("-e", "--email", help="Group Email", required=True)
    args = parser.parse_args()
    
    print("Note: Please use the domain in your email to be @emea.i-leaflets.com!")
    while input("Proceeding will create the group with the name provided as the input.\n Do You Want To Continue? [Proceed/No]") == "Proceed":
        print("Alright, go ahead.")
        main(args.group, args.email)
        break