
class Pokemon:
    def __init__(self, name, types, moves, EVs):
        self.name = name
        self.types = types
        self.moves = moves
        self.base_attack = EVs['ATTACK']
        self.base_defense = EVs['DEFENSE']
        self.attack = self.base_attack
        self.defense = self.base_defense
        self.bars = 50

    def reset_stats(self):
        self.attack = self.base_attack
        self.defense = self.base_defense
        self.bars = 50

pokemons = {
    "Charizard": Pokemon("Charizard", "Fire", ["Flamethrower", "Wing Attack", "Fire Punch"], {'ATTACK':12, 'DEFENSE':8}),
    "Blastoise": Pokemon("Blastoise", "Water", ["Water Gun", "Surf", "Bubblebeam"], {'ATTACK':10, 'DEFENSE':10}, ),
    "Venusaur": Pokemon("Venusaur", "Grass", ["Vine Whip", "Razor Leaf", "Razor Leaf"], {'ATTACK':8, 'DEFENSE':12}, ),
    "Butterfree": Pokemon("Butterfree", "Bug", ["Gust", "Bug Bite", "Confusion"], {'ATTACK':7, 'DEFENSE':7},),
    "Beedrill": Pokemon("Beedrill", "Bug", ["Rage", "Bug Bite", "Poison Sting"], {'ATTACK':9, 'DEFENSE':6}, ),
    "Pidgeot": Pokemon("Pidgeot", "Fly", ["Gust", "Wing Attack", "Flu"], {'ATTACK':9, 'DEFENSE':8}, ),
    "Raticate": Pokemon("Raticate", "Normal", ["Bite", "Hiper Fang", "Super Fang"], {'ATTACK':9, 'DEFENSE':5}, ),
    "Pikachu": Pokemon("Pikachu", "Electric", ["Thunder", "Thunderbolt", "Thunder Shock"], {'ATTACK': 11, 'DEFENSE':5}, ),
    "Persian": Pokemon("Persian", "Normal", ["Bite", "Extreme Speed", "Slash"], {'ATTACK':12, 'DEFENSE':7}, ),
}

