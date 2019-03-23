Example CRUD app: Flask (SQLAlchemy, PostgreSQL) + Vue.js (Typescript), docker setup for backend and frontend.

Backend setup:

- [Flask 1.0.2](http://flask.pocoo.org/) 1.0.2
- [SQLAlchemy](https://www.sqlalchemy.org/) and [PostgreSQL 11.2](https://www.postgresql.org/)
- [Marshmallow](https://marshmallow.readthedocs.io/en/3.0/) for validation and serialization
- Testing with [pytest](https://docs.pytest.org/en/latest/)

Frontend setup:

- [Vue.js 2.6.6](https://vuejs.org/) with [vue-cli](https://cli.vuejs.org/)
- [Typescript 3.2.2](https://www.typescriptlang.org/)
- [axios](https://github.com/axios/axios) for HTTP requests
- [bootstrap-vue](https://bootstrap-vue.js.org/) for UI
- Testing with [jest](https://jestjs.io/)

Run docker compose setup: `make up`.

Create the initial DB (once the setup is running): ```make recreate-local-db```.

Run tests `make test`.
