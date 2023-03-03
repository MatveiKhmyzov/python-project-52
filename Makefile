run:
	poetry run python manage.py runserver
PORT ?= 8000
start:
	poetry run python manage.py migrate && gunicorn task_manager.wsgi -w 5 -b 0.0.0.0:$(PORT)