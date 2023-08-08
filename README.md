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

## Run

```
$ docker-compose build
$ docker-compose up
```

## Access

Get `localhost:8080` for the front.

Get `localhost:5000` or `localhost:8080/api/` for the back.

## Technology used
###  Backend
- Flask

### Frontend
- React

### Database
- Postgresql
