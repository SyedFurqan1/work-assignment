# work-assignment

## Google's Quick Start in setting up Credentials and Allowing APIs
https://developers.google.com/admin-sdk/directory/v1/quickstart/python

Ensure that you have the relevant scopes (Users and Groups) on the OAuth consent screen for the registered app credentials.

Once you have the credentials file from Google console, please keep the credentials file as `credentials.json` in the same folder as your script.

## Sample commands and scripts

#### Adding users to your Google Workspace
The script being used for this task is `create_users.py`. This script requires a CSV file in the format `firstName,lastName,jobPosition`.

_Note: A random password is generated and an email address is generated from the provided first and last names as `firstName.lastName@emea.i-leaflets.com`_

A sample CSV file is provided with the repository for adding users: `users.csv`

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

The script being used for this task is `create_group.py`. This script requires two arguments, group name and group email address.

###### Sample commands:
```
# Lists the help from the script
python3 create_group.py --help

# Creates the group with the passed group name and group email address.
python3 create_group.py -g "Test Group" -e "testgroup@emea.i-leaflets.com"

## Example 1
syedfurqanahmed@Syeds-MBP work-assignment % python3 create_group.py --help
usage: create_group.py [-h] -g GROUP -e EMAIL

options:
  -h, --help            show this help message and exit
  -g GROUP, --group GROUP
                        Group Name
  -e EMAIL, --email EMAIL
                        Group Email

## Example 2
syedfurqanahmed@Syeds-MBP work-assignment % python3 create_group.py -g "Test Group" -e "testgroup@emea.i-leaflets.com"
Note: Please use the domain in your email to be @emea.i-leaflets.com!
Proceeding will create the group with the name provided as the input.
 Do You Want To Continue? [Proceed/No]

```

#### Adding members to a specific group in your Google Workspace
The script being used for this task is `add_members.py`. This script requires a target group email and a CSV file in the format `email,role,type`.

_Note: For ROLE and TYPE, please this [Google reference link](https://developers.google.com/admin-sdk/directory/reference/rest/v1/members#Member)._

A sample CSV file is provided with the repository for adding members to a target group: `members.csv`.

###### Sample commands:
```
# Lists the help from the script
python3 add_members.py --help

# Add members in members.csv to the target group email address.
python3 add_members.py -e "testgroup" -m members.csv

## Example 1
syedfurqanahmed@Syeds-MBP work-assignment % python3 add_members.py --help
usage: add_members.py [-h] -e EMAIL -m MEMBERS

options:
  -h, --help            show this help message and exit
  -e EMAIL, --email EMAIL
                        Group Email
  -m MEMBERS, --members MEMBERS
                        Member Emails CSV

## Example 2
syedfurqanahmed@Syeds-MBP work-assignment % python3 add_members.py -e "testgroup@emea.i-leaflets.com" -m members.csv
Careful. 
 The CSV Format should be email,role,type for the members. 

Proceeding will add the group members in the file provided as the input.
 Do You Want To Continue? [Proceed/No]
```


#### Listing group members in the Google Workspace [Optional]
The script being used for this task is `list_members.py`. The script requires a group email to list the members in the group.

###### Sample commands:
```
# Lists the help from the script
python3 list_members.py --help

# List members in the specified group
python3 list_members.py -e "testgroup@emea.i-leaflets.com"

## Example 
syedfurqanahmed@Syeds-MBP work-assignment % python3 list_members.py --help
usage: list_members.py [-h] -e EMAIL

options:
  -h, --help            show this help message and exit
  -e EMAIL, --email EMAIL
                        Group Email
```

##  The way forward and potential improvements

A potential way to improve the scripts is to add try and except statements to catch any exceptions the Google Directory API can throw.