# survey-example

Example staff survey for technical test - not a real project.

In advance of the technical test, clone this repo.

Push your copy of the repository to a suitable service so that we can see the results (eg GitLab or GitHub). That is, don't push changes to this repo, as multiple people will be completing the technical test.

Before taking the technical test, ensure that you can get the Django app up and running (instructions below). Also make sure that you are able to make changes to the codebase and create pull requests in your repo. Make sure that this repo is public so assessors can see your code.

The technical test will consist of a few code-based tasks (making changes to this repo). There will also be a couple of related questions for discussion. These discussions will give you a chance to demonstrate your wider technical skills, and show how you can turn user requirements into technical requirements.

## Summary

The Cabinet Office are running a staff survey to understand staff wellbeing. Cabinet Office employees will be asked to complete this survey.

- Personal staff details (for example name, email) will not be submitted with their survey responses (session ID will be stored to distinguish participants)
- The survey collects info on team and location, in addition to answers to wellbeing questions
- Separately to survey responses, staff can enter feedback and their email if they wish to discuss issues more

This is a Django app with a SQLite database.

## How to run with Docker

### Running the app

- Run the app locally `docker-compose up --build --force-recreate web`
- Go to `http://localhost:8000` in a browser to try the app

### Other useful commands

- Run tests `docker-compose up --build --force-recreate tests`
- To run other management commands `docker-compose run web python manage.py <MANAGEMENT_COMMAND>`

## How to run without Docker

### Setup

- Install packages with `pip install -r requirements.lock` (ideally into a virtual environment)
- Run migrations `python manage.py migrate` (only need to do this once, or if you make changes to models)

### Running the app

- Run the app locally `python manage.py runserver`
- Go to `http://localhost:8000` in the browser to try the app

### Other useful commands

- To run tests `python manage.py test`
- To run the Django shell `python manage.py shell`
- To collect static files `python manage.py collectstatic`

This has been tested using Python 3.8.
