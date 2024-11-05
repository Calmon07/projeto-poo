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
    ataque1 = Column("ataque", String)
    ataque2 = Column("ataque", String)
    ataque3 = Column("ataque", String)
    ataque4 = Column("ataque", String)
    velocidade = Column("velocidade", Integer)
    tipo = Column("tipo", String)
    nome = Column("nome", String)
    regiao = Column("regiao", String)
    
    def __init__(self, id_pokemon, nome, hp, ataques, velocidade, tipo, regiao):
           self._id_pokemon = id_pokemon
           self.nome = nome
           self.hp = hp
           self.ataque = ataques #lista de ataques
           self.velocidade = velocidade
           self.tipo = tipo
           self.regiao = regiao

    def __repr__(self):
          return f'(Nome: {self.nome}) | Vida: {self.hp} | Ataque: {self.ataque} | Velocidade: {self.velocidade} | Tipo: {self.tipo} | Região: {self.regiao}\n'

class Ataque():
      def __init__(self, nome, tipo, dano):
            self.nome = nome
            self.tipo = tipo
            self.dano = dano

      def __repr__(self):
            return f'Tipo do ataque: {self.tipo} | Dano: {self.dano}'

      
#ataques primeira geração
#ataques de planta (bulbasaur) 
ChicotesDeVinha = Ataque('Chicotes de Vinha', 'Planta', 15) 
FolhasDeNavalha = Ataque('Folhas de Navalha', 'Planta', 20)

#ataques de fogo (charmander)
PresasDeFogo = Ataque('Presas de fogo', 'Fogo', 15)
LancaChamas = Ataque('Lança-Chamas', 'Fogo', 20)

#ataques de água (squirtle)
RajadaDeBolhas = Ataque('Rajada De Bolhas', 'Água', 15)
JatoDeAgua = Ataque('Jato de Água ', 'Água', 20)  

#ataques normal
Investida = Ataque('Investida', 'Normal', 10) 
Mordida = Ataque('Mordida', 'Normal', 15)

#ataques segunda geração
#ataques de planta (treecko)
BalaDeSemente = Ataque('Bala de Semente', 'Planta', 15) 
SementeSanguessuga = Ataque('Semente Sanguessuga', 'Planta', 20)

#ataques de fogo (torchic)
Brasa = Ataque('Brasa', 'Fogo', 15)
CargaDeChamas = Ataque('Carga de Chamas', 'Fogo', 20)

#ataques de água (mudkip)
PulsoDeAgua = Ataque('Pulso de Água ', 'Água', 15)
JatoDeAgua = Ataque('Jato de Água ', 'Água', 20)  

#ataques terceira geração
#ataques de planta (chikorita)
BalaDeSemente = Ataque('Bala de Semente', 'Planta', 15) 
SementeSanguessuga = Ataque('Semente Sanguessuga', 'Planta', 20)

#ataques de fogo (torchic)
Brasa = Ataque('Brasa', 'Fogo', 15)
CargaDeChamas = Ataque('Carga de Chamas', 'Fogo', 20)

#ataques de água (mudkip)
PulsoDeAgua = Ataque('Pulso de Água ', 'Água', 15)
JatoDeAgua = Ataque('Jato de Água ', 'Água', 20)  


Base.metadata.create_all(bind=engine)
