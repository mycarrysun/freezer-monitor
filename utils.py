import os
import requests
from dotenv import load_dotenv, set_key

API_TOKEN = 'API_TOKEN'

def make_api_request(path, method='POST', json={}):
    load_dotenv(override=True)
    endpoint = f"{os.getenv('FREEZERBOT_API_HOST', 'https://freezerbot.nextwebtoday.com')}/api/{path}"
    headers = {
        'Authorization': f"Bearer {os.getenv(API_TOKEN)}",
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    return requests.request(method, endpoint, headers=headers, json=json)


def configure_api_token():
    load_dotenv(override=True)
    has_api_token = os.getenv(API_TOKEN) is not None
    if has_api_token:
        confirm = input('You already have an API token set. Do you want to replace it? (y/n): ')
        if confirm == 'y':
            prompt_for_api_token()
    else:
        prompt_for_api_token()


def prompt_for_api_token():
    api_token = input('Please enter your API token created for this sensor in the FreezerBot app: ')
    set_api_token(api_token)


def set_api_token(token):
    set_key('.env', API_TOKEN, token)
