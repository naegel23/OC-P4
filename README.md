# OC-P4
Chess software
Project 4 : Develop a software program in Python
Developing work, we had to build a chess tournament manager that can handle a database to save players data and running / finished tournaments.

Installation
You can use a package manager such as pip to install the following packages. This can also be done using the requirements.txt file which contains the packages and their version.

pip install tinydb 
pip install datetime

Use
You will see here how I import those packages and examples of how I used them in the engine.


# To handle (read & write) the database
from tinydb import TinyDB, Query
db = TinyDB('db.json')

# To get the actual date and format it
from datetime import datetime
datetime.strptime(birthdate, "%d/%m/%Y")
