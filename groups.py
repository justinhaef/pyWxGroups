import json
import requests
import logging
log = logging.getLogger(__name__)

class Webex_Groups():

    def __init__(self, access_token: str, refresh_token: str):
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.base_url = 'https://webexapis.com/v1'

    def _create_group(self):
        url = f'{self.base_url}/groups'
        data = {
            "displayName": "Webex Network Recording",
            "description": "Test Users with Permissions to Network Record",
        }
        response = requests.post(url=url, headers={'Authorization': f'Bearer {self.access_token}'}, json=data)
        if response.status_code != 401:
            json_response = json.loads(response.text)
            log.info(f"Created Group ID: {json_response['id']}")
            return json_response['id']
        else:
            log.warning('Access Token was Expired')

    def _get_groups(self):
        url = f'{self.base_url}/groups'
        response = requests.get(url=url, headers={'Authorization': f'Bearer {self.access_token}'})
        if response.status_code != 401:
            log.info(f'Gathered Groups')
            groups = json.loads(response.text)
            for group in groups['groups']:
                print(f"Group Title: {group['displayName']}, Group ID: {group['id']}")
            return True
        else:
            log.warning('Access Token was Expired')
            return False

    def _add_users(self, group_id: str, user_id: str):
        url = f'{self.base_url}/groups/{group_id}'
        data = {
            "members": [
                {
                "id": user_id,
                "operation": "add"
                }
            ]
        }
        response = requests.patch(url=url, headers={'Authorization': f'Bearer {self.access_token}'}, json=data)
        if response.status_code != 401:
            json_response = json.loads(response.text)
            log.info(f"Added User {user_id} to Group ID: {json_response['id']}")
            return json_response['id']
        else:
            log.warning('Access Token was Expired')

    def creation(self):
        # Create Group
        created_id = self._create_group()
        return created_id

    def user_addition(self, group_id: str, user_id: str):
        # add users to group
        added_group_id = self._add_users(group_id=group_id, user_id=user_id)
        return added_group_id
