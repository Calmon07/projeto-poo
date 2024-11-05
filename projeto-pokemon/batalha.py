import os
from listaPokemon import *
from pokemon_db import *

def limpar_tela():
    os.system('cls')

def batalhar():
    print('BATALHA POKEMON')


    while hp_deTalPokemon > 0:
        ataque = int(input('Qual ataque você irá usar?\n 1.Ataque 1  | 2.Ataque 2\n 3.Ataque 3 | 4.Ataque 4'))

        if ataque == 1: 
            #ataque1 - self.hp
            pass
        elif ataque == 2:  
            #ataque2 - self.hp
            pass
        elif ataque == 3:
            #ataque3 - self.hp
            pass
        else:
            #ataque4 - self.hp
            pass


def escolher_pokemon():
    print()

def mochila():
    pass

def fugir():
    limpar_tela()
    print('Você fugiu! ')


def decisao():
    print('Você foi desafiado pelo Treinador Gleison!\n')

    pergunta = int(input('O que você deseja fazer?\n 1. Batalhar | 2.Pokemon\n 3.Mochila | 4.Fugir '))

    limpar_tela()

    if pergunta == 1:
        batalhar()
    elif pergunta == 2:
        escolher_pokemon()
    elif pergunta == 3:
        mochila()
    else:
        fugir()




def main():
    decisao()


if __name__ == '__main__':
    main()