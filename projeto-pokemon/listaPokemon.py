from pokemon_db import *

#Time do oponente
listaPokemonsOponente = []

#Times possíveis para o jogador
listaPokemonJogador1 = []
listaPokemonJogador2 = []
listaPokemonJogador3 = []

#def __init__(self, id_pokemon, nome, hp, ataque1, ataque2, ataque3, ataque4, velocidade, tipo, regiao):

#Pokemons Oponente
pokemonOponente1 = Pokemon(1, 'Bulbasaur', 80, 'Scratch', 5, 20, 'Planta', 'Kanto')
pokemonOponente2 = Pokemon(2, 'Charmander', 70, 'Scratch', 5, 17, 'Fogo', 'Kanto')
pokemonOponente3 = Pokemon(3, 'Squirtle', 80, 'Scratch', 5, 15, 'Água', 'Kanto')

#Pokemons primeiro trio jogador
pokemonJogador1 = Pokemon(1, 'Treecko', 60, 'Scratch', 5, 20, 'Planta', 'Kanto')
pokemonJogador2
pokemonJogador3

listaPokemonsOponente.append(pokemon1)
listaPokemonsOponente.append(pokemon2)
listaPokemonsOponente.append(pokemon3)

print(listaPokemonsOponente)

session.add(pokemon3)
session.commit()