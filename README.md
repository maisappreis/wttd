# Eventex

It's a small event system.

## 🛠️ Installation

In the project directory `/wttd`:

1 - Create your `.env`

2 - Create a virtual environment:
```
python -m venv .wttd
```

3 - Activate the Virtual Environment:

- on Mac (bash/zsh)
```
source .wttd/bin/activate
```

- on Windows (PowerShell)
```
.wttd\Scripts\Activate.ps1
```

4 - Install the dependencies:
```
pip install -r requirements-dev.txt
```

5 - Run the tests
```
python manage.py test
```

## 🌱 On Development

In the project directory `/wttd`:

1 - Activate the Virtual Environment:

- on Mac (bash/zsh)
```
source .wttd/bin/activate
```

- on Windows (PowerShell)
```
.wttd\Scripts\Activate.ps1
```

2 - Run in the development mode:
```
python manage.py runserver
```


## 💻 On Production

1. Create an instance on Heroku
2. Send settings to Heroku
3. Set a secure SECRET_KEY for the instance
4. Set DEGUB=False
5. Configure email service
6. Send the code to Heroku


```console
heroku create myinstance
heroku config:push
heroku config:set SECRET_KEY=`XXX`
heroku config:set DEGUB=False

# configure email
git push heroku master --force
```