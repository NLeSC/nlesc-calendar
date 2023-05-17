#!/bin/bash
cd $CALENDAR_PATH
$CALENDAR_PATH/venv/bin/gunicorn --bind 0.0.0.0:80 server:app
