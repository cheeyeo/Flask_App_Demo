### Flask project structure


https://realpython.com/flask-project/

https://realpython.com/flask-logging-messages/



Creating a generic(?) flask project structure


To run:
```
python -m flask --app board run --port 8000 --debug
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

https://www.docker.com/blog/how-to-use-the-postgres-docker-official-image/


TO install psycopg2 we need to install the following dep on ubuntu:
```
sudo apt install libpq-dev
```

Then:
```
pip install pyscopg2
```



### DATABASE

To connect to running postgresql container:
```
docker exec -it <container id> psql -U <username> <dbname>
```



https://medium.com/@yahiaqous/how-to-build-a-crud-api-using-python-flask-and-sqlalchemy-orm-with-postgresql-7869517f8930




### TODO:

Refactor to use Flask-sqlalchemy:

https://docs.sqlalchemy.org/en/20/orm/mapped_attributes.html#using-custom-datatypes-at-the-core-level

https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/


Add user login functionality:

( for in db authentication where user stored in db ):

https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login


https://flask-login.readthedocs.io/en/latest/


( using AWS COGNITO )
https://github.com/CloudySnake/flask-cognito-integration



On migrations:

`create_all()` doesn't recreate db tables if they already exists 


therefore need to add some kind of migration system:


https://flask-migrate.readthedocs.io/en/latest/




https://medium.com/@johnidouglasmarangon/using-migrations-in-python-sqlalchemy-with-alembic-docker-solution-bd79b219d6a



https://docs.sqlalchemy.org/en/20/tutorial/metadata.html#emitting-ddl-to-the-database