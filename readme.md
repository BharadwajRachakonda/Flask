If you are reopening go to `.\env\Scripts\activate.ps1` and do you'r work.

`pip install virtualenv`

`virtualenv env`

`pip install flask`

--> Start server by

`python ./app.py`

`pip install flask-sqlalchemy`

`python`

```
from app import app, db
with app.app_context():
    db.create_all()
```

--> for deploying on Heroku

`pip install gunicorn`

--> Then install Heroku CLI

`pip freeze > requirements.txt`

--> create a Procfile
