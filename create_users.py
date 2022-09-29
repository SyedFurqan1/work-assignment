# API Reference: https://developers.google.com/admin-sdk/directory/reference/rest/v1/users/insert
# Request Object of Users: https://developers.google.com/admin-sdk/directory/reference/rest/v1/users#User

import json
import csv
import os.path
import argparse
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build


# For Random Password Generation
# Ref: https://medium.com/analytics-vidhya/create-a-random-password-generator-using-python-2fea485e9da9
import random
import string
def get_random_password(length):
    # Define characters
    letters = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation
    all = letters + upper + num + symbols

    # Sample a specific length from the defined characters and create a password
    temp = random.sample(all,length)
    result_str = "".join(temp)
    return result_str
###############################

def google_quickstart():
    # If modifying these scopes, delete the file token.json.
    SCOPES = ['https://www.googleapis.com/auth/admin.directory.user']

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

def create_user(client, user):
    results = client.users().insert(body=user).execute()
    return results

def main(file):
    # Initialize Google API Client
    client = google_quickstart()

    # Create empty output CSV file
    with open('./output.csv', 'w+') as f:
        headers = "firstName,lastName,position,email,password\n"
        f.write(headers)

    # Reading the provided CSV file.
    with open(file, 'r') as file:
      csvreader = csv.reader(file)
      header = next(csvreader)

      for row in csvreader:
        # Extracting variable names to create a user json object
        user_first_name = row[0].title()
        user_last_name = row[1].title()
        user_email = row[0].split()[0].lower() + "." + row[1].split()[0].lower() + "@emea.i-leaflets.com"
        user_position = row[2].title()
        random_password = get_random_password(8)

        # Creating User object
        user = {
        "primaryEmail": user_email,
        "name": {
            "givenName": user_first_name, 
            "familyName": user_last_name,
            },
        "password": random_password,
        "organizations": [
                {   
                    "name": "i-leaflet",
                    "title": user_position
                }
            ]
        }

        # Creating User on Google Workspace
        results = create_user(client, user)
        print(results)

        # Open output file for writing, create if it does not exist
        with open('output.csv', 'a') as f:
            # create the csv writer
            # write a row to the csv file
            line = "%s,%s,%s,%s,%s\n"%(user_first_name,user_last_name,user_position,user_email,random_password)
            f.write(line)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--csv", help="Input CSV file with format firstName,lastName,position", required=True)
    args = parser.parse_args()
    print("Careful. \n The CSV Format should be firstName,lastName,position for the users. \n Proceeding will overwrite your output.csv file. \n")
    while input("Ensure you have a backup before proceeding.\n Do You Want To Continue? [Proceed/No]") == "Proceed":
        print("Alright, go ahead.")
        main(args.csv)
        break