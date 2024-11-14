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

`pip install gunicorn` - **enables multithreaded applications.**

<br>

> - **Then install Heroku CLI from [here](https://devcenter.heroku.com/articles/heroku-cli)**

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

###

# Flask

## Packages

- Install flask as `pip install flask`

- Install flask-sqlalchemy as `pip install -U Flask-SQLAlchemy`

## Content

- Hello World

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run(debug=True, port=8000)
```

> The flask run command can do more than just start the development server. By enabling debug mode, the server will automatically reload if code changes, and will show an interactive debugger in the browser if an error occurs during a request.

- HTTP Methods

```python
@app.route('/', methods=['GET', 'POST'])

## You can also use as following

@app.get('/login')
def login_get():
    return show_the_login_form()

@app.post('/login')
def login_post():
    return do_the_login()
```

> The endpoint only works for specified methods.

- Variable Rules

```python
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'
```

> You can add variable sections to a URL by marking sections with <variable_name>. Your function then receives the <variable_name> as a keyword argument. Optionally, you can use a converter to specify the type of the argument like <converter:variable_name>.

- URL Building

```python
from flask import url_for

@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))
```

```Output
/
/login
/login?next=/
/user/John%20Doe
```

> To build a URL to a specific function, use the url_for() function. It accepts the name of the function as its first argument and any number of keyword arguments, each corresponding to a variable part of the URL rule. Unknown variable parts are appended to the URL as query parameters.

- Static Files

```python
url_for('static', filename='style.css')
```

> Dynamic web applications also need static files. That’s usually where the CSS and JavaScript files are coming from. Ideally your web server is configured to serve them for you, but during development Flask can do that as well. Just create a folder called static in your package or next to your module and it will be available at /static on the application.
> To generate URLs for static files, use the special 'static' endpoint name

- Rendering Templates

```python
from flask import render_template

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', person=name)
```

> To render a template you can use the render_template() method. All you have to do is provide the name of the template and the variables you want to pass to the template engine as keyword arguments.

> Flask will look for templates in the templates folder. So if your application is a module, this folder is next to that module, if it’s a package it’s actually inside your package

- Jinja

```html
<!DOCTYPE html>
<title>Hello from Flask</title>
{% if person %}
<h1>Hello {{ person }}!</h1>
{% else %}
<h1>Hello, World!</h1>
{% endif %}
```

> Inside templates you also have access to the config, request, session and g [1] objects as well as the url_for() and get_flashed_messages() functions.

- The Request Object

```python
@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)
```

> The current request method is available by using the method attribute. To access form data (data transmitted in a POST or PUT request) you can use the form attribute.

- Url Parameters

```python
searchword = request.args.get('key', '')
```

> To access parameters submitted in the URL (?key=value) you can use the args attribute

- File Uploads

```python
from flask import request

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/uploaded_file.txt')
    ...
```

**_You can handle uploaded files with Flask easily. Just make sure not to forget to set the `enctype="multipart/form-data"` attribute on your HTML form, otherwise the browser will not transmit your files at all._**

```python
from werkzeug.utils import secure_filename

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['the_file']
        file.save(f"/var/www/uploads/{secure_filename(file.filename)}")
    ...
```

> If you want to know how the file was named on the client before it was uploaded to your application, you can access the filename attribute. However please keep in mind that this value can be forged so never ever trust that value. If you want to use the filename of the client to store the file on the server, pass it through the secure_filename() function

- Cookies

Reading cookies:

```python
from flask import request

@app.route('/')
def index():
    username = request.cookies.get('username')
    # use cookies.get(key) instead of cookies[key] to not get a
    # KeyError if the cookie is missing.
```

Storing cookies:

```python
from flask import make_response

@app.route('/')
def index():
    resp = make_response(render_template(...))
    resp.set_cookie('username', 'the username')
    return resp
```

**_Note that cookies are set on response objects. Since you normally just return strings from the view functions Flask will convert them into response objects for you. If you explicitly want to do that you can use the `make_response()` function and then modify it._**

- Redirects and Errors

```python
from flask import abort, redirect, url_for

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    abort(401)
    this_is_never_executed()
```

```python
from flask import render_template

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404
```

> By default a black and white error page is shown for each error code. If you want to customize the error page, you can use the errorhandler() decorator

**_`Note the 404 after the render_template() call`. This tells Flask that the status code of that page should be 404 which means not found. By default 200 is assumed which translates to: all went well._**

- APIs with JSON

```python
@app.route("/me")
def me_api():
    user = get_current_user()
    return {
        "username": user.username,
        "theme": user.theme,
        "image": url_for("user_image", filename=user.image),
    }

@app.route("/users")
def users_api():
    users = get_all_users()
    return [user.to_json() for user in users]
```

> A common response format when writing an API is JSON. It’s easy to get started writing such an API with Flask. If you return a dict or list from a view, it will be converted to a JSON response.

- Sessions

```python
from flask import session

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    if 'username' in session:
        return f'Logged in as {session["username"]}'
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))
```

> In addition to the request object there is also a second object called session which allows you to store information specific to a user from one request to the next. This is implemented on top of cookies for you and signs the cookies cryptographically. What this means is that the user could look at the contents of your cookie but not modify it, unless they know the secret key used for signing.

> In order to use sessions you have to set a secret key.

- Hooking in WSGI Middleware

```python
from werkzeug.middleware.proxy_fix import ProxyFix
app.wsgi_app = ProxyFix(app.wsgi_app)
```

> To add WSGI middleware to your Flask application, wrap the application’s wsgi_app attribute. For example, to apply Werkzeug’s ProxyFix middleware for running behind Nginx

###

</br>

# Profiles

<div align="left">
  <a href="mailto:rbharadwaj022@gmail.com" target="_blank">
    <img src="https://img.shields.io/static/v1?message=Gmail&logo=gmail&label=&color=D14836&logoColor=white&labelColor=&style=for-the-badge" height="35" alt="gmail logo"  />
  </a>
  <a href="https://www.linkedin.com/in/bharadwaj-rachakonda-b36658258/" target="_blank">
    <img src="https://img.shields.io/static/v1?message=LinkedIn&logo=linkedin&label=&color=0077B5&logoColor=white&labelColor=&style=for-the-badge" height="35" alt="linkedin logo"  />
  </a>
  <a href="https://www.hackerrank.com/profile/rbharadwaj022" target="_blank">
    <img src="https://img.shields.io/static/v1?message=HackerRank&logo=hackerrank&label=&color=2EC866&logoColor=white&labelColor=&style=for-the-badge" height="35" alt="hackerrank logo"  />
  </a>
  <a href="https://bharadwajrachakonda.github.io/Portfolio/" target="_blank">
    <img src="https://img.shields.io/static/v1?message=Portfolio&logo=codepen&label=&color=000000&logoColor=white&labelColor=&style=for-the-badge" height="35" alt="codepen logo"  />
  </a>
  <a href="https://leetcode.com/u/BharadwajRachakonda/" target="_blank">
    <img src="https://img.shields.io/static/v1?message=LeetCode&logo=leetcode&label=&color=FFA116&logoColor=white&labelColor=&style=for-the-badge" height="35" alt="leetcode logo"  />
</a>
</div>

###
