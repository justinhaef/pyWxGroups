import auth
import requests
import json
from pathlib import Path
import logging

logging.basicConfig(
    filename=Path('delete.log'),
    level=logging.INFO,
    format='%(name)s - %(levelname)s - %(message)s'
    )

def main():
    webex_oauth = auth.Auth()
    tokens = webex_oauth.kickoff()
    logging.debug(f"Access Token:{tokens['access_token']} Refresh Token:{tokens['refresh_token']}")
    access_token = tokens['access_token']
    url = 'https://webexapis.com/v1/groups'
    response = requests.get(url=url, headers={'Authorization': f'Bearer {access_token}'})
    if response.status_code != 401:
        logging.info(f'Gathered Groups')
        groups = json.loads(response.text)
        for group in groups['groups']:
            delete_url = f"{url}/{group['id']}"
            response = requests.delete(url=delete_url, headers={'Authorization': f'Bearer {access_token}'})
    print(f'Done: {response}')

if __name__ == "__main__":
    main()