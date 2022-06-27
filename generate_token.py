import requests
from data import url
import os


def generate_token() :
    """Generate token from the API"""
    
    body= {"username" : os.getenv("USERNAME"), "password" : os.getenv("PASSWORD")}
    req = requests.post(f"{url}/token", json=body).json()
    
    return req["token"]