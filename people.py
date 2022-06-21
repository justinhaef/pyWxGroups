import json
import requests
import logging
log = logging.getLogger(__name__)

class Get_People():

    def __init__(self, access_token: str, refresh_token: str):
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.base_url = 'https://webexapis.com/v1'

    def get_person_id(self, email):
        url = f'{self.base_url}/people'
        params = {
            "email": email,
        }
        response = requests.get(url=url, headers={'Authorization': f'Bearer {self.access_token}'}, params=params)
        if response.status_code != 401:
            json_response = json.loads(response.text)
            log.info(f"Person ID: {json_response['items'][0]['id']}")
            return json_response['items'][0]['id']
        else:
            log.warning('Access Token was Expired')