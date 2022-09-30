# work-assignment

## Google's Quick Start in setting up Credentials and Allowing APIs
https://developers.google.com/admin-sdk/directory/v1/quickstart/python

Ensure that you have the relevant scopes (Users and Groups) on the OAuth consent screen for the registered app credentials.

Once you have the credentials file from Google console, please keep the credentials file as `credentials.json` in the same folder as your script.

## Sample commands and scripts

#### Adding users to your Google Workspace
The script being used for this task is `create_users.py`. This script requires a CSV file in the format `firstName,lastName,jobPosition`.

_Note: A random password is generated and an email address is generated from the provided first and last names as `firstName.lastName@emea.i-leaflets.com`_

A sample file is provided with the repository for adding users: `users.csv`

###### Sample commands:
```
# Lists the help from the script
python3 create_users.py --help

# Creates the members specified in users.csv in the Google Workspace
# The script will ask you to enter "Proceed" in order for it to be executed
python3 create_users.py -f users.csv


### Example
syedfurqanahmed@Syeds-MBP work-assignment % python3 create_users.py --help
usage: create_users.py [-h] -f CSV
options:
  -h, --help         show this help message and exit
  -f CSV, --csv CSV  Input CSV file with format firstName,lastName,position
```


#### Creating a group in your Google Workspace

#### Listing group members in the Google Workspace

##  The way forward and potential improvements