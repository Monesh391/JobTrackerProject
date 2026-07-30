# Job Tracker API

A backend REST API built using Django REST Framework to manage job applications efficiently. The application supports secure JWT authentication and allows users to create, view, update, and delete job records.

## Features

- JWT Authentication
- Create Job
- View Jobs
- Update Job
- Delete Job
- RESTful API
- SQLite (Render Deployment)
- PostgreSQL (Development)

## Tech Stack

- Python
- Django
- Django REST Framework
- Simple JWT
- PostgreSQL
- SQLite
- Git
- Render

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /api/token/ | Login |
| POST | /api/token/refresh/ | Refresh Token |
| GET | /api/jobs/ | Get Jobs |
| POST | /api/jobs/ | Create Job |
| PUT | /api/jobs/<id>/ | Update Job |
| DELETE | /api/jobs/<id>/ | Delete Job |

## Installation

```bash
git clone <repository-url>
cd JobTrackerProject

python -m venv venv

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver
```

## Deployment

Deployed on Render.

## Future Improvements

- Swagger Documentation
- Pagination
- Search & Filtering
- Docker Support
- Unit Testing

## Author

Monesh
