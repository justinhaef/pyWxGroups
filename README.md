# Webex Groups API Demo Application

## Purpose

This demo application was created to show how a company could leverage the Groups API to manage users via Templates.  

## How to use

You'll need to enter the application at app.py.  `python app.py` would be how you'd kick it off.  It will then go through the OAuth exchange.  Your integration will need to have both `identity:groups_rw` and `spark-admin:people_read` scopes.  You'll need to put in your `APP_CLIENTID=` and `APP_SECRETID=` in the `.env-template` file.  Also, rename `.env-template` to just `.env`.  

The application will then create a group, search out the user IDs of the user's email addresses you have listed in `app.py` and finally add those users to the newly created group. 

## To Do

1. Remove the need to pass around the tokens in the code.
1. Add the argparse so we can delete the testing groups via commandline.
1. Also leverage argparse so we can add users to an existing group.