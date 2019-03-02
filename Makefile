DOCKER_COMPOSE = docker-compose
PG_URI = postgresql://testuser:testpw@postgresql:5432
TOOLS = @$(DOCKER_COMPOSE) run --rm backend

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
	$(DOCKER_COMPOSE) exec postgresql bash -c "echo 'drop database if exists forumtest' | psql $(PG_URI)"
	$(DOCKER_COMPOSE) exec postgresql bash -c "echo 'create database forumtest' | psql $(PG_URI)"
	$(DOCKER_COMPOSE) exec backend pytest


migrations-gen:
	$(DOCKER_COMPOSE) exec backend bash -c "echo $$DOCKER_PG_URI"
	$(DOCKER_COMPOSE) exec backend bash -c "./manage.py migrations revision --autogenerate"

migrations-upgrade:
	$(DOCKER_COMPOSE) exec backend bash -c "./manage.py migrations upgrade head"

migrations-downgrade:
	$(DOCKER_COMPOSE) exec backend bash -c "./manage.py migrations downgrade"

bash:
	# bash shell that is configured to use 'forum' database,
	# can be used to test scripts on a local db,
	# for example
	#     python -m scripts.data_update
	#     flask db_create_all
	$(TOOLS) bash

flask-shell:
	# bash shell that is configured to use 'forum' database,
	# can be used to test scripts on a local db,
	# for example
	#     python -m scripts.data_update
	$(TOOLS) flask shell
