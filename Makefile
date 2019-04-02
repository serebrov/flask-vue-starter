DOCKER_COMPOSE = docker-compose
PG_URI = postgresql://testuser:testpw@postgresql:5432

BACKEND = @$(DOCKER_COMPOSE) run --rm backend
FRONTEND = @$(DOCKER_COMPOSE) run --rm frontend

up:
	$(DOCKER_COMPOSE) up --build # --force-recreate

recreate-local-db:
	$(DOCKER_COMPOSE) stop backend
	$(DOCKER_COMPOSE) exec postgresql bash -c "echo 'drop database forum' | psql $(PG_URI) && echo 'create database forum' | psql $(PG_URI)"
	$(DOCKER_COMPOSE) start backend
	$(DOCKER_COMPOSE) exec backend flask db_create_all

psql:
	$(DOCKER_COMPOSE) exec postgresql psql $(PG_URI)/forum

test:
	$(MAKE) backend-test
	$(MAKE) frontend-test

backend-test:
	$(DOCKER_COMPOSE) exec backend pytest

backend-bash:
	# bash shell that is configured to use 'forum' database,
	# can be used to test scripts on a local db,
	# for example
	#     python -m scripts.data_update
	#     flask db_create_all
	#     flask shell
	$(BACKEND) bash

frontend-bash:
	$(FRONTEND) bash

frontend-test:
	$(FRONTEND) yarn test:unit
	# $(FRONTEND) yarn test:e2e --headless

# Run linters.
lint:
	$(BACKEND) bash -c "mypy . && flake8 ."
	$(BACKEND) bash -c "black --check --diff ."
	$(FRONTEND) bash -c "yarn prettier-check"
	$(FRONTEND) bash -c "yarn lint"

# Format code.
format-code:
	$(BACKEND) bash -c "black ."
	$(FRONTEND) bash -c "yarn format"
