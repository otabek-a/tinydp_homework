from tinydb import TinyDB
import requests
doc=TinyDB('db.json')
db=TinyDB('tabel.json')
user={
    'name':'Otabek',
    'age':18,
    'surname':'otabek',
    'job':'student'
}
user2={
    'name':'sardor',
    'age':18,
    'surname':'muminjonov',
    'job':'student'
}
db.insert(user)
db.insert(user2)
url = 'https://randommer.io/api/Name?nameType=fullname&quantity=20'
headers={
    'X-Api-Key':'41c1434e36c349c3972448fca049b6e3'
}
response = requests.get(url,headers=headers)
r = response.json()
for i in r:
    doc.insert({'name':f'{i}'})

