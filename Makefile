DOCKER_COMPOSE = docker-compose
PG_URI = postgresql://testuser:testpw@postgresql:5432
TOOLS = @$(DOCKER_COMPOSE) run --rm app

up:
	$(DOCKER_COMPOSE) up --build # --force-recreate

recreate-local-db:
	$(DOCKER_COMPOSE) exec postgresql bash -c "echo 'drop database forum' | psql $(PG_URI) && echo 'create database forum' | psql $(PG_URI)"

psql:
	$(DOCKER_COMPOSE) exec postgresql psql $(PG_URI)/forum

migrations-gen:
	$(DOCKER_COMPOSE) exec app bash -c "echo $$DOCKER_PG_URI"
	$(DOCKER_COMPOSE) exec app bash -c "./manage.py migrations revision --autogenerate"

migrations-upgrade:
	$(DOCKER_COMPOSE) exec app bash -c "./manage.py migrations upgrade head"

migrations-downgrade:
	$(DOCKER_COMPOSE) exec app bash -c "./manage.py migrations downgrade"

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
