from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from data_models.models import User, Task

db_engine = create_engine('sqlite:///base_tarefas.db')
Session = sessionmaker(bind=db_engine)




# CREATE

def insert_dados(dados):
    with Session() as session:
        session.add(dados)
        session.commit()

# READ

def read_dados(model_class, id):
    with Session() as session:
        dado = session.query(model_class).filter_by(id=id).first()
        return dado



# DELETE

def delete_dados(model_class, id):
    with Session() as session:
        dado = session.query(model_class).filter_by(id=id).first()
        if dado:
            session.delete(dado)
            session.commit()


# UPDATE

def update_dados(model_class, id, novos_dados):
    with Session() as session:
        dado = session.query(model_class).filter_by(id=id).first()
        if dado:
            for key, value in novos_dados.items():
                setattr(dado, key, value)
            session.commit()