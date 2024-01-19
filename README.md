### Simple Flask project


A simple messageboard project built in Flask with a Postgresql backend.

It's running in dev mode locally via docker compose

Uses:

* Flask web framework
* SQLAlchemy and flask-sqlalchemy for ORM
* alembic for database migrations
* flask-login for user logins
* Docker and docker compose for application and postgresql db



### To run locally with docker-compose:

Copy `.env.example` to `.env` and fill in required env vars

To start both application and DB in terminal:
```
docker compose -f compose.yaml up
```

This will start up the postgresql DB first and after reaching a successful healthcheck, it will start the web application.

It creates a persistent docker volume for the database data.

The base database migration is ran automatically via `entrypoint.sh` script which is set as the enrtypoint for the dev image.


If changes are made to the database models, you need to generate a new migration using:
```
docker exec messageboard-web-1 alembic revision --autogenerate -m 'REASON FOR NEW MIGRATION'

docker exec messageboard-web-1 alembic upgrade head
```

If changes are made to the web app, it will reload the application code.



### Building production image

To build production docker image, from the root folder, run:
```
docker build -t web:latest -f board/Dockerfile --target prod .
```



### DATABASE MIGRATIONS

Handled by alembic

To generate baseline migrations for all the models' tables:

```
alembic revision --autogenerate -m 'Create baseline migrations
```

To run migration:
```
alembic upgrade head
```

Useful Alembic commands:

* Display the current revision for a database: `alembic current`

* View migrations history: `alembic history --verbose`

* Revert all migrations: `alembic downgrade base`

* Revert migrations one by one: `alembic downgrade -1`

* Apply all migrations: `alembic upgrade head`

* Apply migrations one by one: `alembic upgrade +1`

* Display all raw SQL: `alembic upgrade head --sql`

* Reset the database: `alembic downgrade base && alembic upgrade head`


More [Alembic commands]

[Alembic commands]: https://alembic.sqlalchemy.org/en/latest/api/commands.html


### DATABASE NOTES

* To install psycopg2 we need to install the following dep on ubuntu:
```
sudo apt install libpq-dev
```

Then:
```
pip install pyscopg2
```

To install without any system deps:
```
pip install pyscopg2-binary
```


* To connect to running postgresql container:
```
docker exec -it <container id> psql -U <username> <dbname>
```


### References

* [realpython post]
* [realpython post on flask]
* [Docker post on using postgres docker image]
* [Tutorial on using Flask and SQLAlchemy]
* [Validation with SQLAlchemy ORM models]
* [flask-sqlalchemy notes]
* [flask-login docs]
* [Using flask-login]
* [Using alembic with sqlalchemy]
* [sqlalchemy orm tutorial]
* [sqlalchemy custom datatypes]


[realpython post]: https://realpython.com/flask-project/

[realpython post on flask]: https://realpython.com/flask-logging-messages/

[Docker post on using postgres docker image]: https://www.docker.com/blog/how-to-use-the-postgres-docker-official-image/


[Tutorial on using Flask and SQLAlchemy]: https://medium.com/@yahiaqous/how-to-build-a-crud-api-using-python-flask-and-sqlalchemy-orm-with-postgresql-7869517f8930


[Validation with SQLAlchemy ORM models]: https://ed-a-nunes.medium.com/field-validation-for-backend-apis-with-python-flask-and-sqlalchemy-30e8cc0d260c


[flask-sqlalchemy notes]: https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/

[flask-login docs]: https://flask-login.readthedocs.io/en/latest/

[Using flask-login]: https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login

[Using alembic with sqlalchemy]: 
https://medium.com/@johnidouglasmarangon/using-migrations-in-python-sqlalchemy-with-alembic-docker-solution-bd79b219d6a

[sqlalchemy orm tutorial]: https://docs.sqlalchemy.org/en/20/tutorial

[sqlalchemy custom datatypes]: https://docs.sqlalchemy.org/en/20/orm/mapped_attributes.html#using-custom-datatypes-at-the-core-level


[On using depends_on condition]: https://www.warp.dev/terminus/docker-compose-depends-on

[Using docker-compose for local Flask dev]: https://dev.to/pacheco/dockerize-a-flask-app-and-debug-with-vscode-34i1


### TODO:

* Fix / update validation for models 

* Deploy to AWS ECS in cluster with ALB + RDS

* Try AWS Cognito for user authentication?

  https://github.com/CloudySnake/flask-cognito-integration
