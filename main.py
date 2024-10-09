from crud.crud import insert_dados, ler_dados, delete_user, update_user, update_task
from data_models.models import User, Task
from datetime import datetime
from fastapi import FastAPI
import uvicorn


app = FastAPI()

user1 = User(name="lucas", email="lucas@gmail.com", created=datetime.now())
task1 = Task(created=datetime.now(), updated=datetime.now(), task="teste",priority="urgente", status="teste", userid=1)

@app.get('/primeiroendpoint')
def meuprimeiroendpoint():
    return 'Meu primeiro endpoint'

@app.get('/leituradetabela')
def ler_tabela(entidade:int):
    if entidade == 1:
        tabela = User
    if entidade == 2:
        tabela = Task
    return ler_dados(tabela)

@app.post('/insert_user')
def inserir_user(nome_in:str, email_in:str):
    usuario = User(name=nome_in, email=email_in, created=datetime.now())
    insert_dados(usuario)
    return ler_dados(User)

@app.post('/insert_task')
def inserir_task(task_in:str, priority_in:str, status_in:str, uid_in:int):
    tarefa = Task(created=datetime.now(), updated=datetime.now(), task=task_in,priority=priority_in, status=status_in, userid=uid_in)
    insert_dados(tarefa)
    return ler_dados(Task)

@app.delete('/del_user')
def delete_user_id(id:int):
    delete_user(id, User)
    return delete_user(id, User)

@app.put('/update_user')
def atualizar_usuario(id: int, nome: str = None, email: str = None):
    updated_data = {}
    if nome:
        updated_data['name'] = nome
    if email:
        updated_data['email'] = email

    if updated_data:
        result = update_user(id, updated_data, User)
        return result
    else:
        return 'Nenhum dado para atualizar'
    
@app.put('/update_task')
def atualizar_tarefa(id: int, task: str = None, priority: str = None, status: str = None):
    updated_data = {}
    if task:
        updated_data['task'] = task
    if priority:
        updated_data['priority'] = priority
    if status:
        updated_data['status'] = status

    if updated_data:
        result = update_task(id, updated_data, Task)
        return result
    else:
        return 'Nenhum dado para atualizar'


uvicorn.run(app,port=8888)
