from os import access
import auth
import requests
import json
import people
from pathlib import Path
import logging

logging.basicConfig(
    filename=Path('add_users.log'),
    level=logging.INFO,
    format='%(name)s - %(levelname)s - %(message)s'
    )

def main():
    webex_oauth = auth.Auth()
    tokens = webex_oauth.kickoff()
    logging.debug(f"Access Token:{tokens['access_token']} Refresh Token:{tokens['refresh_token']}")
    access_token = tokens['access_token']
    add_people = people.Create_People(access_token=access_token)
    response = add_people.person(firstname="Jeff", lastname="Haefner", email="jeff@jhaefner.wbx.ai")
    print(f'Done: {response}')

if __name__ == "__main__":
    main()
