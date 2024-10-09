from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from data_models.models import User, Task

db_engine = create_engine('sqlite:///base_tarefas.db')
Session = sessionmaker(bind=db_engine)




# CREATE

def insert_dados(dados):
    with Session() as session:
        session.add(dados)
        session.commit()

#READ

def ler_dados(tabela):
    with Session() as session:
        registros = session.query(tabela).all()
        return registros
    

#DELETE

def delete_user(id_in, model):
    with Session() as session:
        registros_deletado = session.query(model).filter_by(id=id_in).first()
        session.delete(registros_deletado)
        session.commit()
    return 'Registro deletado com sucesso'



# UPDATE User
def update_user(id_in, updated_data, model):
    with Session() as session:
        registro = session.query(model).filter_by(id=id_in).first()
        if registro:
            for key, value in updated_data.items():
                setattr(registro, key, value)
            session.commit()
            return f'Usuário com ID {id_in} atualizado com sucesso'
        else:
            return f'Usuário com ID {id_in} não encontrado'


# UPDATE Task
def update_task(id_in, updated_data, model):
    with Session() as session:
        registro = session.query(model).filter_by(id=id_in).first()
        if registro:
            for key, value in updated_data.items():
                setattr(registro, key, value)
            registro.updated = datetime.now()
            session.commit()
            return f'Tarefa com ID {id_in} atualizada com sucesso'
        else:
            return f'Tarefa com ID {id_in} não encontrada'

