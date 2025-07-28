import customtkinter as ctk
import pygame
import numpy as np
from PIL import Image
from monsters import pokemons, Pokemon
from config import type_chart, AUDIO_PATH, IMAGES


class PokemonBattleApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        pygame.mixer.init()
        pygame.mixer.music.load(r"C:\Users\JESUS TE AMA\OneDrive\Documentos\GitHub\Monster_Battle\audio\battle.ogg")
        pygame.mixer.music.play(loops=-1) 
        self.title("Monster Battle")
        self.geometry("900x500")
        

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

        self.left_img_label = ctk.CTkLabel(self, text="")
        self.left_img_label.place(x=1, y=1)

        self.right_img_label = ctk.CTkLabel(self, text="")
        self.right_img_label.place(x=700, y=1)


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

        img1_path = r"C:\Users\JESUS TE AMA\OneDrive\Documentos\GitHub\Monster_Battle\graphics\Monsters\Blastoise.png"
        img2_path = r"C:\Users\JESUS TE AMA\OneDrive\Documentos\GitHub\Monster_Battle\graphics\Monsters\Charizard.png"

        img1 = Image.open(img1_path)
        img2 = Image.open(img2_path)

        self.tk_img1 = ctk.CTkImage(light_image=img1, size=(160, 160))
        self.tk_img2 = ctk.CTkImage(light_image=img2, size=(160, 160))

        self.left_img_label.configure(image=self.tk_img1, text="")
        self.right_img_label.configure(image=self.tk_img2, text="")


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
            self.after(1000, self.ask_restart_custom)
            return

        enemy_move = np.random.choice(self.pokemon2.moves)
        self.display_text(f"\n{self.pokemon2.name} usou {enemy_move}!\n")
        self.display_text(self.effectiveness_msg_2 + "\n")
        self.pokemon1.bars -= self.pokemon2.attack
        self.pokemon1.bars = max(0, self.pokemon1.bars)

        self.display_text(f"Vida de {self.pokemon1.name}: {'=' * self.pokemon1.bars}\n")
        if self.pokemon1.bars <= 0:
            self.display_text(f"\n{self.pokemon1.name} desmaiou!\nVocê perdeu!\n")
            self.after(100, self.ask_restart_custom)

    def display_text(self, text):
        self.output_box.configure(state="normal")
        self.output_box.insert("end", text)
        self.output_box.see("end")
        self.output_box.configure(state="disabled")

    def ask_restart_custom(self):
        popup = ctk.CTkToplevel(self)
        popup.title("Fim da Batalha")
        popup.geometry("300x150")
        popup.grab_set() 
        def nao():
            popup.destroy()
            pygame.mixer.music.stop()
            self.quit()


        label = ctk.CTkLabel(popup, text="Deseja jogar novamente?", font=("Arial", 16))
        label.pack(pady=20)

        button_frame = ctk.CTkFrame(popup)
        button_frame.pack(pady=10)

        def sim():
            popup.destroy()
            self.reset_battle()

        def nao():
            popup.destroy()
            self.quit()

        yes_btn = ctk.CTkButton(button_frame, text="Sim", command=sim, width=80)
        yes_btn.pack(side="left", padx=10)

        no_btn = ctk.CTkButton(button_frame, text="Não", command=nao, width=80)
        no_btn.pack(side="left", padx=10)


    def reset_battle(self):
        self.output_box.configure(state="normal")
        self.output_box.delete("1.0", "end")
        self.output_box.configure(state="disabled")
        for widget in self.attack_frame.winfo_children():
            widget.destroy()
        self.combo1.set(list(pokemons.keys())[0])
        self.combo2.set(list(pokemons.keys())[1])
