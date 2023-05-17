# eScience calendar

Install javascript dependencies:

```npm install```

Install python dependencies; (inside a virtual environment)

```pip install -r requirements.txt```

Make sure to add your own `settings.py`. You can use `settings-example.py` as an example.

Run python:

```python server.py```

Run python (using gunicorn):

```gunicorn --bind 0.0.0.0:80 server:app```

## Run as a service in Linux
Edit `start-gunicorn.sh` and move to `/usr/local/bin/`
Move `calendar.service` to `/etc/systemd/system/calendar.service`
Start service and open firewall:
```bash
systemctl daemon-reload 
systemctl enable calendar.service
systemctl start calendar.service
firewall-cmd --add-port=80/tcp --permanent
```