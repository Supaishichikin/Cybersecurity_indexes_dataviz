FROM python:3.9
WORKDIR /backend
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

COPY requirements.txt /backend/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /backend/requirements.txt

COPY alembic.ini /backend/alembic.ini
COPY migrations /backend/migrations

COPY app /backend/app

ENV PORT 5000
EXPOSE $PORT
COPY entrypoint.sh /backend/entrypoint.sh
CMD ["/bin/bash", "entrypoint.sh"]
