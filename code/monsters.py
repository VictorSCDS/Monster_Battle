import pygame
import time
import numpy as np
import sys
import os


class Pokemon:
    def __init__(self, name, types, moves, EVs, image_path):
        self.name = name
        self.types = types
        self.moves = moves
        self.attack = EVs['ATTACK']
        self.defense = EVs['DEFENSE']
        self.health = 20
        self.image_path = image_path

pokemons = [
    Pokemon("Charizard", "Fire", ["Flamethrower", "Wing Attack", "Fire Punch"], {'ATTACK':12, 'DEFENSE':8}, r"graphics\Monsters\Charizard.png"),
    Pokemon("Blastoise", "Water", ["Water Gun", "Surf", "Bubblebeam"], {'ATTACK':10, 'DEFENSE':10}, r"graphics\Monsters\Blastoise.png"),
    Pokemon("Venusaur", "Grass", ["Vine Whip", "Razor Leaf", "Razor Leaf"], {'ATTACK':8, 'DEFENSE':12}, r"graphics\Monsters\Venusaur.png"),
    Pokemon("Butterfree", "Bug", ["Gust", "Bug Bite", "Confusion"], {'ATTACK':7, 'DEFENSE':7}, r"graphics\Monsters\Butterfree.png"),
    Pokemon("Beedrill", "Bug", ["Rage", "Bug Bite", "Poison Sting"], {'ATTACK':9, 'DEFENSE':6}, r"graphics\Monsters\Beedrill.png"),
    Pokemon("Pidgeot", "Fly", ["Gust", "Wing Attack", "Flu"], {'ATTACK':9, 'DEFENSE':8}, r"graphics\Monsters\Pidgeot.png"),
    Pokemon("Raticate", "Normal", ["Bite", "Hiper Fang", "Super Fang"], {'ATTACK':9, 'DEFENSE':5}, r"graphics\Monsters\Raticate.png"),
    Pokemon("Pikachu", "Electric", ["Thunder", "Thunderbolt", "Thunder Shock"], {'ATTACK': 11, 'DEFENSE':5}, r"graphics\Monsters\Pikachu.png"),
    Pokemon("Persian", "Normal", ["Bite", "Extreme Speed", "Slash"], {'ATTACK':12, 'DEFENSE':7}, r"graphics\Monsters\Persian.png"),
]
