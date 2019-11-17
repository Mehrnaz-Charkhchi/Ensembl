import os

from peewee import MySQLDatabase

mysql_db_connection = MySQLDatabase(
    os.getenv('REMOTE_MYSQL_DB'),
    user=os.getenv('REMOTE_MYSQL_USERNAME'),
    password=os.getenv('REMOTE_MYSQL_PASSWORD'),
    host=os.getenv('REMOTE_MYSQL_URL'),
    port=int(os.getenv('REMOTE_MYSQL_PORT')),
)
