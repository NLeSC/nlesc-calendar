# eScience calendar

Install javascript dependencies:

```npm install```

Install python dependencies;

```pip install -r requirements.txt```

Make sure to add your own `settings.py`. You can use `settings-example.py` as an example.

Run python:

```python server.py```

Run python (using gunicorn):

```gunicorn --bind 0.0.0.0:80 server:app```
