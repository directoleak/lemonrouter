import requests

ipdata = requests.get('https://ifconfig.me')
ip = ipdata.text