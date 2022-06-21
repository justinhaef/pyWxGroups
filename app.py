import auth
import groups
import people
from pathlib import Path
import logging

logging.basicConfig(
    filename=Path('app.log'),
    level=logging.INFO,
    format='%(name)s - %(levelname)s - %(message)s'
    )

users = [
    "Ben@jhaefner.wbx.ai",
    "Suzy@jhaefner.wbx.ai"
]

def group(access_token: str, refresh_token: str):
    wbx_groups = groups.Webex_Groups(access_token=access_token, refresh_token=refresh_token)
    created_group = wbx_groups.creation()
    people_ids = get_user_id(access_token=access_token, refresh_token=refresh_token)
    for user in people_ids:
        result = wbx_groups.user_addition(group_id=created_group, user_id=user)
    return result

def get_user_id(access_token: str, refresh_token: str):
    wbx_people = people.Get_People(access_token=access_token, refresh_token=refresh_token)
    people_ids = []
    for email in users:
        id = wbx_people.get_person_id(email=email)
        people_ids.append(id)
    return people_ids

def main():
    webex_oauth = auth.Auth()
    tokens = webex_oauth.kickoff()
    logging.debug(f"Access Token:{tokens['access_token']} Refresh Token:{tokens['refresh_token']}")
    response = group(access_token=tokens['access_token'], refresh_token=tokens['refresh_token'])
    print(f'Done: {response}')

if __name__ == "__main__":
    main()