from crud.crud import insert_dados, read_dados, update_dados, delete_dados
from data_models.models import User, Task
from datetime import datetime


user1 = User(name="lucas", email="lucas@gmail.com", created=datetime.now())
task1 = Task(created=datetime.now(), updated=datetime.now(), task="teste",priority="urgente", status="teste", userid=1)

user2 = User(name="Pedro", email="pedro@gmail.com", created=datetime.now())
task2 = Task(created=datetime.now(), updated=datetime.now(), task="teste",priority="urgente", status="teste", userid=1)

user3 = User(name="Joao", email="joao@gmail.com", created=datetime.now())
task3 = Task(created=datetime.now(), updated=datetime.now(), task="teste",priority="urgente", status="teste", userid=1)

user4 = User(name="Mateus", email="mateus@gmail.com", created=datetime.now())
task4 = Task(created=datetime.now(), updated=datetime.now(), task="teste",priority="urgente", status="teste", userid=1)


insert_dados(user1)
insert_dados(task1)

insert_dados(user2)
insert_dados(task2)

insert_dados(user3)
insert_dados(task3)

insert_dados(user4)
insert_dados(task4)

read_dados(user1)
read_dados(task1)

delete_dados(user2)
delete_dados(task2)

update_dados(user3)
update_dados(task3)
