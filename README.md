[![CircleCI](https://circleci.com/gh/serebrov/flask-vue-starter.svg?style=svg)](https://circleci.com/gh/serebrov/flask-vue-starter)

Starter example app: Flask (SQLAlchemy, PostgreSQL) + Vue.js (Typescript), docker setup for backend and frontend.

Backend setup (provides REST API for the frontend):

- [Flask 1.0.2](http://flask.pocoo.org/)
- [SQLAlchemy](https://www.sqlalchemy.org/) and [PostgreSQL 11.2](https://www.postgresql.org/)
- [Marshmallow](https://marshmallow.readthedocs.io/en/3.0/) for validation and serialization
- Testing with [pytest](https://docs.pytest.org/en/latest/)
- Linting with [mypy](http://mypy-lang.org/), [flake8](http://flake8.pycqa.org/en/latest/) and [black](https://github.com/ambv/black)
- Code formatting with [black](https://github.com/ambv/black)

Frontend setup:

- [Vue.js 2.6.6](https://vuejs.org/) with [vue-cli](https://cli.vuejs.org/)
- [Typescript 3.2.2](https://www.typescriptlang.org/)
- [axios](https://github.com/axios/axios) for HTTP requests
- [bootstrap-vue](https://bootstrap-vue.js.org/) for UI
- Testing with [jest](https://jestjs.io/)
- Linting with typescript, eslint and prettier
- Code formatting with prettier

Rebuild images / reinstall dependencies: `make build`.
Note: the dependencies are installed into the volume shared with the host system, so are available inside the source folders (so IDEs, for example, can use them for autocomplete, or people can use as a reference to quickly check how things are implemented inside the packages).

Backend dependencies are in `backend/venv` and frontend dependencies are in the `frontend/node_modules`.

Run docker compose setup: `make up`.

Create the initial DB (once the setup is running): ```make recreate-local-db```.

Run tests: `make test`.

Run linters: `make lint`.

Reformat sources: `make format-code`.
