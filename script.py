import requests
import json
from generate_token import generate_token
from data import data

TOKEN = ""

def create_file(file_name, url):
    global TOKEN
    
    api_url = requests.get(url, headers={'Authorization': f"Bearer {TOKEN}"})
        
    if (api_url.status_code == 401):
        TOKEN = generate_token()
        response_api = requests.get(url, headers={'Authorization': f"Bearer {TOKEN}"}).json() 
        print("New Token")        
    
    if (api_url.status_code != 401 and api_url.status_code != 200):
        print(f"\033[91m ERREUR {api_url.status_code} DANS LE FICHIER : {file_name}")
        exit(1)
    
    response_api = requests.get(url, headers={'Authorization': f"Bearer {TOKEN}"}).json()
        
    return json.dump(response_api, open(f"./data/new/{file_name}.json", "w", encoding='utf8'), indent=3, ensure_ascii=False)


if __name__ == "__main__":
    for key in data.keys():
        create_file(key, data[key])