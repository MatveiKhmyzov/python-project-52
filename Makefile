run:
	poetry run python manage.py runserver
PORT ?= 8000
start:
	poetry run python manage.py migrate && gunicorn task_manager.wsgi -w 5 -b 0.0.0.0:$(PORT)
superuser:
	poetry run python manage.py createsuperuser
migrations:
	poetry run python manage.py makemigrations
migrate:
	poetry run python manage.py migrate
shell:
	python manage.py shell_plus
test coverage:
	poetry run coverage run --source='.' manage.py test task_manager
lint:
	poetry run flake8 task_manager
