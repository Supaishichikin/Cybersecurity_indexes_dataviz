#!/bin/bash

/usr/local/bin/alembic upgrade head
/usr/local/bin/gunicorn -b 0.0.0.0:$PORT app.main:app --reload
