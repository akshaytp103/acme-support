# Zenpy accepts an API token
creds = {
    'email' : 'akshaytp103@gmail.com',
    'token' : 'YhpbglCFeDdWAHNiIWHINK8heUwNASv8rz5QiSZU',
    'subdomain': 'brototype7977'
}


# Or a password
creds = {
    'email' : 'akshaytp103@gmail.com',
    'password' : 'Itisgoodpass1*',
    'subdomain': 'brototype7977'
}

# Import the Zenpy Class
from zenpy import Zenpy
import requests

# Default
zenpy_client = Zenpy(**creds)

# Alternatively you can provide your own requests.Session object
zenpy_client = Zenpy(**creds, session=requests.Session())

# If you are providing your own HTTPAdapter object, Zenpy provides defaults via the
# Zenpy.http_adapter_kwargs() method. You can choose to use these defaults like so:
# session = requests.Session()
# session.mount('https://brototype7977.zendesk.com/', MyAdapter(**Zenpy.http_adapter_kwargs()))
# zenpy_client = Zenpy(**creds, session=requests.Session())