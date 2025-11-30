from dotenv import load_dotenv
import os
import requests
from pprint import pprint

load_dotenv()

account_id = os.getenv('AccountId')
api_key = os.getenv('ApiKey')
location = os.getenv('Location')

headers = {
    'Ocp-Apim-Subscription-Key': api_key
}
token_url = f"https://api.videoindexer.ai/auth/{location}/Accounts/{account_id}/AccessToken"
token = requests.get(token_url, headers=headers).json()

videos_url = f"https://api.videoindexer.ai/{location}/Accounts/{account_id}/Videos"
params = {
    'accessToken': token
}
videos = requests.get(videos_url, params=params).json()
pprint(videos)