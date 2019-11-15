# MySQL vs MongoDB

This is a simple program written in Python that is meant for viewing easily, the performance of both Databases.
The language displayed in the program is Spanish, but the whole code is in English, keep that in mind.
<hr>

### MySLQ 

__Requirements__

You don't need [XAMPP](https://www.apachefriends.org/index.html), the database is online.

You need to install [PyMySQL](https://pypi.org/project/PyMySQL/) by [pip](https://pypi.org/project/pip/) 
with `pip install PyMySQL`.

__Features__
- [Create tables](#Create-tables)
- [Show all data](#Show-data)
- [Insert a lot of data](#Insert-data)
- [Delete the whole data](#Delete-data)
- [Exit](#Exit)

##### Create tables

It creates three tables:
- Alumno (Student)
- Materia (Subject)
- Calificaciones (Score)

Alumno (Student) table has this structure:

*value* | *type* | *key*
------------ | ------------- | -------------
id | INT NOT NULL AUTO_INCREMENT | PRIMARY KEY
nombre | varchar(255) NOT NULL | N/A

Materia (Subject) has this structure:

*value* | *type* | *key*
------------ | ------------- | -------------
clave | INT NOT NULL AUTO_INCREMENT | PRIMARY KEY
nombre | varchar(255) NOT NULL | N/A

Calificaciones (Score) has this structure:

_value_ | _type_ | _key_
------------ | ------------- | -------------
clave_Materia | int NOT NULL | FOREIGN KEY
id_Alumno | int NOT NULL | FOREIGN KEY
valor | float NOT NULL | N/A

##### Show data

It asks you for a number, and shows you that quantity of rows. Also tells you how many records has each table.

##### Insert data

As this program is just for checking performance, or for future comparison with MongoDB, the data will be automatically 
created, by [random](https://docs.python.org/2/library/random.html) function. This is it for the three tables. 
You just need to introduce the number of records you want to store.
[ACID](https://en.wikipedia.org/wiki/ACID) transactions are considered.

When storage in MySQL has begun, the program will create a .txt file, called 'timesMySQL.txt'. It saves the times when 
storing data begins, and when it ends.

##### Delete data

There are two ways data can be deleted:
1. Delete just the data
2. Delete data and tables

You cannot choose which record will be deleted, the whole data is deleted.

For obvious reasons, when the second option is chosen, you must re-create the tables, by using the feature
[Create tables](#Create-tables).

##### Exit

This option cancels the execution of the program.

<hr>

### MongoDB

__Requirements__

Install [MongoDB Comunity Edition](https://docs.mongodb.com/manual/installation/).

Install [MongoDB Compass](https://docs.mongodb.com/compass/master/install/).

For Python, install [PyMongo](https://pypi.org/project/pymongo/) by [pip](https://pypi.org/project/pip/) 
with `pip install pymongo`

__Features__

Apparently, it only inserts a lot of data.

With [MongoDB Compass](https://docs.mongodb.com/compass/master/install/) you can check the performance of the database and compare it with MySQL performance.
