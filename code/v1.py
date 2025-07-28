import customtkinter as ctk
import time
import numpy as np
import threading

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class Pokemon:
    def __init__(self, name, types, moves, EVs):
        self.name = name
        self.types = types
        self.moves = moves
        self.base_attack = EVs['ATTACK']
        self.base_defense = EVs['DEFENSE']
        self.attack = self.base_attack
        self.defense = self.base_defense
        self.bars = 20

    def reset_stats(self):
        self.attack = self.base_attack
        self.defense = self.base_defense
        self.bars = 20

pokemons = {
    "Charizard": Pokemon('Charizard', 'Fire', ['Flamethrower', 'Fly', 'Blast Burn', 'Fire Punch'], {'ATTACK': 12, 'DEFENSE': 8}),
    "Blastoise": Pokemon('Blastoise', 'Water', ['Water Gun', 'Bubblebeam', 'Hydro Pump', 'Surf'], {'ATTACK': 10, 'DEFENSE': 10}),
    "Venusaur": Pokemon('Venusaur', 'Grass', ['Vine Whip', 'Razor Leaf', 'Earthquake', 'Frenzy Plant'], {'ATTACK': 8, 'DEFENSE': 12}),
}

type_chart = ['Fire', 'Water', 'Grass']

class PokemonBattleApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Pokémon Battle")
        self.geometry("700x520")

        self.pokemon1 = None
        self.pokemon2 = None

        self.label1 = ctk.CTkLabel(self, text="Escolha o seu Pokémon:")
        self.label1.pack(pady=5)
        self.combo1 = ctk.CTkOptionMenu(self, values=list(pokemons.keys()))
        self.combo1.pack()

        self.label2 = ctk.CTkLabel(self, text="Escolha o Pokémon adversário:")
        self.label2.pack(pady=5)
        self.combo2 = ctk.CTkOptionMenu(self, values=list(pokemons.keys()))
        self.combo2.pack()

        self.start_button = ctk.CTkButton(self, text="Começar Batalha", command=self.start_battle)
        self.start_button.pack(pady=10)

        self.output_box = ctk.CTkTextbox(self, width=650, height=200)
        self.output_box.pack(pady=10)
        self.output_box.configure(state="disabled")

        self.attack_frame = ctk.CTkFrame(self)
        self.attack_frame.pack(pady=10)

    def start_battle(self):
        name1 = self.combo1.get()
        name2 = self.combo2.get()

        if name1 == name2:
            self.display_text("Escolha dois Pokémon diferentes.\n")
            return

        self.pokemon1 = pokemons[name1]
        self.pokemon2 = pokemons[name2]

        self.pokemon1.reset_stats()
        self.pokemon2.reset_stats()

        self.calculate_type_advantage()

        self.display_text(f"{self.pokemon1.name} ({self.pokemon1.types}) vs {self.pokemon2.name} ({self.pokemon2.types})\n")
        self.display_text("Batalha começou!\n")
        self.show_moves()

    def calculate_type_advantage(self):
        t1 = self.pokemon1.types
        t2 = self.pokemon2.types

        i1 = type_chart.index(t1)
        i2 = type_chart.index(t2)

        if t1 == t2:
            self.effectiveness_msg_1 = "Não é muito efetivo..."
            self.effectiveness_msg_2 = "Não é muito efetivo..."
        elif i2 == (i1 + 1) % 3:
            self.pokemon2.attack *= 2
            self.pokemon2.defense *= 2
            self.pokemon1.attack = max(1, self.pokemon1.attack // 2)
            self.pokemon1.defense = max(1, self.pokemon1.defense // 2)
            self.effectiveness_msg_1 = "Não é muito efetivo..."
            self.effectiveness_msg_2 = "É super efetivo!"
        elif i2 == (i1 + 2) % 3:
            self.pokemon1.attack *= 2
            self.pokemon1.defense *= 2
            self.pokemon2.attack = max(1, self.pokemon2.attack // 2)
            self.pokemon2.defense = max(1, self.pokemon2.defense // 2)
            self.effectiveness_msg_1 = "É super efetivo!"
            self.effectiveness_msg_2 = "Não é muito efetivo..."
        else:
            self.effectiveness_msg_1 = ""
            self.effectiveness_msg_2 = ""

    def show_moves(self):
        for widget in self.attack_frame.winfo_children():
            widget.destroy()

        for move in self.pokemon1.moves:
            btn = ctk.CTkButton(self.attack_frame, text=move, command=lambda m=move: self.attack(m))
            btn.pack(side="left", padx=5)

    def attack(self, move):
        self.display_text(f"\n{self.pokemon1.name} usou {move}!\n")
        self.display_text(self.effectiveness_msg_1 + "\n")
        self.pokemon2.bars -= self.pokemon1.attack
        self.pokemon2.bars = max(0, self.pokemon2.bars)

        self.display_text(f"Vida de {self.pokemon2.name}: {'=' * self.pokemon2.bars}\n")
        if self.pokemon2.bars <= 0:
            self.display_text(f"\n{self.pokemon2.name} desmaiou!\nVocê venceu!\n")
            return

        enemy_move = np.random.choice(self.pokemon2.moves)
        self.display_text(f"\n{self.pokemon2.name} usou {enemy_move}!\n")
        self.display_text(self.effectiveness_msg_2 + "\n")
        self.pokemon1.bars -= self.pokemon2.attack
        self.pokemon1.bars = max(0, self.pokemon1.bars)

        self.display_text(f"Vida de {self.pokemon1.name}: {'=' * self.pokemon1.bars}\n")
        if self.pokemon1.bars <= 0:
            self.display_text(f"\n{self.pokemon1.name} desmaiou!\nVocê perdeu!\n")

    def display_text(self, text):
        self.output_box.configure(state="normal")
        self.output_box.insert("end", text)
        self.output_box.see("end")
        self.output_box.configure(state="disabled")

if __name__ == "__main__":
    app = PokemonBattleApp()
    app.mainloop()
