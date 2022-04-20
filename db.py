from sqlalchemy import false
from app import db, Login
db.create_all()  # sukurs mūsų lentelę DB

# Iš karto inicijuosime testams keletą įrašų:
best = Login('Best', True, "Nothing")
login = Login('Login', False, None)
ever = Login('Ever', False, None)

# Pridėsime šiuos veikėjus į mūsų DB
db.session.add_all([best, login, ever])
# .commit išsaugo pakeitimus
db.session.commit()

# 1
# 2
# 4
# 3