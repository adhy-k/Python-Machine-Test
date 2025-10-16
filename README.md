# Python Machine Test

This is a simple Django (4+) project using Django REST Framework. It demonstrates basic REST APIs, validation, models with relations, and a simple aggregation query using SQLite.(Just to Use a separate branch and create a Pull Request)

## Setup Instructions

- Create and activate a virtual environment (recommended).
- Install dependencies:

```bash
pip install -r requirements.txt
```

- Apply migrations (uses SQLite by default):

```bash
python manage.py makemigrations
python manage.py migrate
```

- Run the development server:

```bash
python manage.py runserver
```

The server runs at http://127.0.0.1:8000/


### 1) User Registration with Validation
- URL: `POST /register/`

- Rules:
  - username: unique, at least 5 characters
  - email: valid email format
  - password: at least 8 chars, must contain a number


### 2) Users API (No Auth)
- `GET /users/` → list all users
- `GET /users/{id}/` → get one user by id
- `DELETE /users/{id}/` → delete user by id


### 3) Expense Tracker (Relations & Queries)
- Models are defined:
  - `Category(name)`
  - `Expense(title, amount, category, date)`

Note: To test the summary, create `Category` and `Expense` rows via the Django admin or the Django shell:
```bash
python manage.py createsuperuser
python manage.py runserver
# go to http://127.0.0.1:8000/admin/


## Project Structure
- Django project: `testProject/`
- App: `project/`
- Entrypoint: `manage.py`

## Requirements
- See `requirements.txt` for versions.
- Database: SQLite (default) (no extra setup needed).
