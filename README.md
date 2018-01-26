[MIT License](LICENSE.txt)

# Pretty ToDo List

A simple To Do list.

### Running the project
- `pipenv install --dev`
- `npm install`
- `npm run start`
- `pipenv shell`
- `python manage.py runserver`

### Testing
`make test`

Will run django tests using `--keepdb` and `--parallel`. You may pass a path to the desired test module in the make command. E.g.:

`make test someapp.tests.test_views`

### Adding new pypi libs
Just run `pipenv install LIB_NAME_ON_PYPI` and then `pipenv lock` to lock the version in Pipfile.lock file

## Linting
- Manually with `prospector` and `npm run lint` on project root.
- During development with an editor compatible with prospector and ESLint.

## Pre-commit hooks
- Run `pre-commit install` to enable the hook into your git repo. The hook will run automatically for each commit.
- Run `git commit -m "Your message" -n` to skip the hook if you need.

### How to test Heroku deployment
Push your changes to a branch and visit `https://dashboard.heroku.com/new?template=https://github.com/fill-org-or-user/fill-project-repo-name/tree/fill-branch` (replace all `fill-*`).

### Deploy to Heroku
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

P.S. if you want to deploy in a different way please check the `app.json` file for what needs to be configured.

### Demo
[Click here to see a demo](https://prettytodolists.herokuapp.com/)

[MIT License](LICENSE.txt)
