import requests

with open('rec.png', 'rb') as f:
    image = f.read()
r = requests.post('http://127.0.0.1:8000/answer/', files={'photo': image})

print(r.text)
