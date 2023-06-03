import requests

with open('asf.jpg', 'rb') as f:
    image = f.read()
r = requests.post('http://127.0.0.1:8000/recognize/', files={'photo': image})

print(r.text)
