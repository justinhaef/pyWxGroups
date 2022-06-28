import json
import requests
import logging
log = logging.getLogger(__name__)

class Get_People():

    def __init__(self, access_token: str):
        self.access_token = access_token
        self.base_url = 'https://webexapis.com/v1'

    def get_person_id(self, email):
        url = f'{self.base_url}/people'
        # print(f'Email: {email}')
        params = {
            "email": email,
        }
        response = requests.get(url=url, headers={'Authorization': f'Bearer {self.access_token}'}, params=params)
        if response.status_code != 401:
            json_response = json.loads(response.text)
            # print(json.dumps(json_response, indent=4))
            log.info(f"Person ID: {json_response['items'][0]['id']}")
            return json_response['items'][0]['id']
        else:
            log.warning('Access Token was Expired')

class Create_People():
    """ Class to create a large group of users to populate Control Hub for testing.
    """
    def __init__(self, access_token: str) -> None:
        self.access_token = access_token
        self.base_url = 'https://webexapis.com/v1'

    def person(self, firstname: str, lastname: str, email: str) -> bool:
        url = f'{self.base_url}/people'
        data = {
            "emails": [
                email
            ],
            "firstName": firstname,
            "lastName": lastname
        }
        response = requests.post(url=url, headers={'Authorization': f'Bearer {self.access_token}'}, json=data)
        json_response = json.loads(response.text)
        if response.status_code != 200:
            log.error(f"Email: {email} Failed: {response.status_code}:{json_response}")
            return False
        else:
            log.debug(f"Email: {email} Created: {response.status_code}:{json_response}")
            return True

