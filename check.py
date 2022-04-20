from app import db, Login
from random import randint

logins = Login.query.all()

for x in logins:
    print (f'{x}')