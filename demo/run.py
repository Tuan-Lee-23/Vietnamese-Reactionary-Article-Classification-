import requests
key = 'bò đeo nơ'
r = requests.get('http://localhost:8000/query/' + key)
print(r.text)
