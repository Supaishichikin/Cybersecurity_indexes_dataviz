#!/bin/bash
echo $PATH
/usr/local/bin/alembic upgrade head
/usr/local/bin/uvicorn app.main:app --host 0.0.0.0 --port $PORT --reload