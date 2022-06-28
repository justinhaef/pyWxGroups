import auth
import groups
import people
from pathlib import Path
import csv
import argparse
import logging

logging.basicConfig(
    filename=Path('app.log'),
    level=logging.INFO,
    format='%(name)s - %(levelname)s - %(message)s'
    )


def group(access_token: str, groupName: str, filename: str):
    wbx_groups = groups.Webex_Groups(access_token=access_token)
    created_group = wbx_groups.creation(group=groupName)
    people_ids = get_user_id(access_token=access_token, filename=filename)
    for user in people_ids:
        result = wbx_groups.user_addition(group_id=created_group, user_id=user)
    return result

def get_user_id(access_token: str, filename: str):
    wbx_people = people.Get_People(access_token=access_token)
    people_ids = []
    with open(Path(filename), 'r', encoding='utf-8-sig') as usersfile:
        users = csv.reader(usersfile)
        for row in users:
            id = wbx_people.get_person_id(email=row)
            people_ids.append(id)
    return people_ids

def main(groupName: str, filename: str):
    webex_oauth = auth.Auth()
    tokens = webex_oauth.kickoff()
    logging.debug(f"Access Token:{tokens['access_token']} Refresh Token:{tokens['refresh_token']}")
    response = group(access_token=tokens['access_token'], groupName=groupName, filename=filename)
    print(f'Done: {response}')

if __name__ == "__main__":
    argument_parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter,
        description="""
            Webex Groups CLI.
            """,
    )

    argument_parser.add_argument(
        "-f",
        "--file",
        help="File Name in Files Folder",
        dest="filename",
        required=False,
    )
    
    argument_parser.add_argument(
        "-g",
        "--group",
        help="New Group Name",
        dest="group",
        required=False,
    )

    args = argument_parser.parse_args()

    if Path('./files', args.filename).is_file():
        # send the file path to the main function
        result = main(groupName=args.group, filename=Path('./files', args.filename).resolve())