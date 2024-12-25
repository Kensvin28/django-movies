# Django Movies Project

A Django-based web application for managing and displaying movie information.

## Features

- Browse a collection of movies
- View detailed movie information
- Admin interface for managing movie data
- Search functionality
- Responsive design

## Requirements

- Python 3.x
- Django
- Other dependencies listed in requirements.txt

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Kensvin28/django-movies.git
cd django-movies
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create a superuser (optional):
```bash
python manage.py createsuperuser
```

6. Start the development server:
```bash
python manage.py runserver
```

The application will be available at `http://localhost:8000`

## Project Structure

- `movies/` - Main application directory containing models, views, and templates
- `moviesite/` - Project configuration directory
- `manage.py` - Django's command-line utility for administrative tasks
- `db.sqlite3` - SQLite database file