# pulse-survey-example

Example pulse survey for technical test - not a real project.

In advance of the technical test, clone this repo. Push your copy of the repository to a suitable service so that we can see the results (eg GitLab or GitHub). That is, don't push changes to this repo, as multiple people will be completing the technical test.

Before taking the technical test, ensure that you can get the Django app up and running (instructions below). Also make sure that you are able to make changes to the codebase and create pull requests in your repo. Make sure that this repo is public so assessors can see your code.

## Summary

The Cabinet Office are running a pulse survey to understand staff wellbeing. Cabinet Office employees will be asked to complete this survey.

- Staff details will not be submitted with their survey responses (session ID will be stored to distinguish participants)
- Collect info on team and location, in addition to answers to wellbeing questions
- Separately to survey responses, staff can enter feedback and their email if they wish to discuss issues more

This is a Django app with a SQLite database.

## How to run with Docker

- Run the app locally `docker-compose up --build`
- Go to `http://localhost:8000` in a browser to try the app

## How to run without Docker

- Install packages with `pip install -r requirements.lock` (ideally into a virtual environment)
- Run migrations `python manage.py migrate` (only need to do this once, or if you make changes to models)
- Run the app locally `python manage.py runserver`
- Go to `http://localhost:8000` in the browser to try the app

This has been tested using Python 3.8.
