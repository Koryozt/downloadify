import requests
import helpers
import base64
from exceptions import InvalidCredentialsException, TokenAlreadyInUseException

class Authorization():
    def __init__(self, client_id:str, client_secret:str) -> None:
        self.URL = 'https://accounts.spotify.com/api/token'
        self.CLIENT_ID = client_id,
        self.CLIENT_SECRET = client_secret

    def _create_options(self) -> dict[str, any]:
        credentials = f'{self.CLIENT_ID}:{self.CLIENT_SECRET}'
        
        encoded_credentials = base64.b64encode(
            credentials.encode('utf-8')).decode('utf-8')

        headers = {
            'Authorization': 'Basic ' + encoded_credentials
        }	

        payload = {
            'grant_type': 'client_credentials'
        }

        auth_options = {
            'url': self.URL,
            'headers': headers,
            'form': payload,
            'json': True
        }

        return auth_options
    
    def get_auth_token_information(self) -> dict[str, any]:
        if not self.CLIENT_ID or not self.CLIENT_SECRET:
            raise InvalidCredentialsException
        
        auth_options = self._create_options()

        try:	
            response = requests.post(
                url= auth_options['url'],
                headers=auth_options['headers'],
                data=auth_options['form'])

            if not response:
                raise TypeError

            information = {
                'value': response['access_token'],
                'type': response['token_type'],
                'exp': response['expires_in']
            }

            return information
                
        except requests.exceptions.HTTPError as e:
            print(e)

class Request():
    def __init__(self) -> None:
        self.BASE_URL = "https://api.spotify.com"
        self.token = None

    def set_token(self, token:str) -> None:
        if not token:
            raise TypeError

        if token is self.token:
            raise TokenAlreadyInUseException
        
        self.token = token



