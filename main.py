from tinydb import TinyDB
import tinydb
db=TinyDB('table.json')
user={
    'first name':'otabek',
    'last name':'Abdurasulov',
    'age':18,
    'job':'student',
}
user2={
    'first name':'sardor',
    'last name':'muminjonov',
    'age':18,
    'job':'student',
}
db.insert(user)
db.insert(user2)