### Flask project structure


https://realpython.com/flask-project/

Creating a generic(?) flask project structure


To run:
```
python -m flask --app board run --port 8000 --debug
```


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

https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/


Add user login functionality:

( for in db authentication where user stored in db ):

https://flask-login.readthedocs.io/en/latest/


( using AWS COGNITO )
https://github.com/CloudySnake/flask-cognito-integration



On migrations

https://medium.com/@johnidouglasmarangon/using-migrations-in-python-sqlalchemy-with-alembic-docker-solution-bd79b219d6a



https://docs.sqlalchemy.org/en/20/tutorial/metadata.html#emitting-ddl-to-the-database