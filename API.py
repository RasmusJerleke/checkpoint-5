import requests

def get_phone(name):
    print(requests.get(f'http://localhost:5000/api?action=phone&name={name}').text)

def get_name(phone):
    print(requests.get(f'http://localhost:5000/api?action=name&phone={phone}').text)