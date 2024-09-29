# All CLI off Flask

**If you are reopening go to** `.\env\Scripts\activate.ps1` **and do you'r work.**

`pip install virtualenv`

`virtualenv env`

`pip install flask`

<br>

> - **Start server by**

<br>

`python ./app.py`

`pip install flask-sqlalchemy`

`python`

```
from app import app, db
with app.app_context():
    db.create_all()
```

<br>

> - **for deploying on Heroku**

<br>

`pip install gunicorn`

<br>

> - **Then install Heroku CLI**

<br>

`pip freeze > requirements.txt`

<br>

> - **create a Procfile**

<br>

**enter** `web: gunicorn app:app` **in it**

<br>

> - **enter following command's on you'r CLI without env**

<br>

`heroku login` - **open you'r browser and login to Heroku**

<br>

`git init` - **initialize a git repository**

<br>

`git add .` - **add all your documents**

<br>

`git commit -m "Initial commit"` - **commit the changes**

<br>

`heroku create {project_name}` - **create you'r website [Herpku is not free now you need to pay first].**

<br>

`git remote -v` - **to check the fetch and push url's**

<br>

`git push heroku master` - **Complete the deploymnet.**

<br>

`heroku logs --tail` - **check you'r application error'.**

<br>
