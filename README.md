# Cybersecurity indexes dataviz

## Requirements

- Docker
- Docker-compose

## Backend set up

Copy the `backend/example.env` file to `backend/.env` and set the variables:

- POSTGRES_HOST
- POSTGRES_USER
- POSTGRES_PASSWORD
- POSTGRES_PORT
- POSTGRES_DB
- DATABASE_URL

## Frontend set up

Copy the `frontend/example.env` file to `frontend/.env` and set the variables:

- REACT_APP_ROLLBAR_FRONTEND_TOKEN

## Run

```
$ docker-compose build
$ docker-compose up
```

## Access

Get `localhost:8080` for the front.

Get `localhost:5000` or `localhost:8080/api` for the back.

## Technology used
###  Backend
- FastApi

### Frontend
- React

### Database
- Postgresql
