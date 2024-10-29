from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base 

engine = create_engine('sqlite:///biblioteca.db')
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Pokemon(Base):
    __tablename__ = "pokemons"  

    id_pokemon = Column("id", Integer, primary_key=True, autoincrement=True)
    hp = Column("hp", Integer)
    ataque = Column("ataque", Integer)
    velocidade = Column("velocidade", Integer)
    tipo = Column("tipo", String)
    nome = Column("nome", String)
    regiao = Column("regiao", String)
    


    def __init__(self, id_pokemon, nome, hp, ataque, velocidade, tipo, regiao):
           self._id_pokemon = id_pokemon
           self.nome = nome
           self.hp = hp
           self.ataque = ataque
           self.velocidade = velocidade
           self.tipo = tipo
           self.regiao = regiao

    def __repr__(self):
          return f'(Nome: {self.nome}) | Vida: {self.hp} | Ataque: {self.ataque} | Velocidade: {self.velocidade} | Tipo: {self.tipo} | Região: {self.regiao}\n'
    
    #def atacar(self, )
          
Base.metadata.create_all(bind=engine)
