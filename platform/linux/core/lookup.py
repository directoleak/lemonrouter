import requests

ipdata = requests.get('https://api.ipify.org')
ip = ipdata.text