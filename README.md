### Hexlet tests and linter status
[![Actions Status](https://github.com/MatveiKhmyzov/python-project-52/workflows/hexlet-check/badge.svg)](https://github.com/MatveiKhmyzov/python-project-52/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/ef621430ca780e48ccf3/maintainability)](https://codeclimate.com/github/MatveiKhmyzov/python-project-52/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/ef621430ca780e48ccf3/test_coverage)](https://codeclimate.com/github/MatveiKhmyzov/python-project-52/test_coverage)
### Link to domain
[Task Manager](https://python-project-52-production-f24f.up.railway.app)
### About project
Task Manager is a task management system. It allows you to set tasks, assign performers and change their statuses.
### Auxiliary tools and rules for working with the service
Versions of Python and Django are 3.10 and 4.1.7 respectively. It also needs in PostgreSQL as database and for work with database is psycopg2-binary with 2.9.5-version.
To use the application, you need to clone the repository to your computer and then install all necessary dependencies:
```console
make install
```
For correct work of application, it is necessary to create .env file in root directory of project with variables:
DATABASE_URL (database connection string), SECRET_KEY (session secret key) and ROLLBAR_TOKEN (if it will be required).
To create the necessary tables in the database, start the migration process:
```console
make migrate
```
Start the Gunicorn Web-server by running:
```console
make start
```
To run local server:
```console
make run
```
For users: registration and authorization are required to gain access to the main functionality.
Further, there are some possibilities for managing labels, statuses, as well as your tasks and information about the user.
All restrictions, as well as successful actions, are accompanied by informational messages.
