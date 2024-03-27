import requests
from database_gpt import *

def create_new_token():
    """Создание нового токена"""
    metadata_url = "http://169.254.169.254/computeMetadata/v1/instance/service-accounts/default/token"
    headers = {"Metadata-Flavor": "Google"}
    response = requests.get(metadata_url, headers=headers)
    print(response.json())
    print(response.json()["access_token"])
    new_iam_token(f"{response.json()["access_token"]}")
    timez_new((response.json())["expires_in"])
