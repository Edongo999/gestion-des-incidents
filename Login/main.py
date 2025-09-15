import subprocess
import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

login = ctk.CTk()
login.geometry("700x550")

def connexion():
    print("Bienvenue")

def Menu_Principal():
    subprocess.run(["python", "Menu_Principal.py"])

frame = ctk.CTkFrame(master=login)
frame.pack(pady=40, padx=80, fill="both", expand=True)

label = ctk.CTkLabel(master=frame, text="Se connecter")
label.pack(pady=12, padx=10)

champ1 = ctk.CTkEntry(master=frame, placeholder_text="Identifiant")
champ1.pack(pady=20)

champ2 = ctk.CTkEntry(master=frame, placeholder_text="Mot de passe", show="*")
champ2.pack(pady=12)

# Ajout du champ de sélection pour le type d'utilisateur
label_user_type = ctk.CTkLabel(master=frame, text="Type d'utilisateur")
label_user_type.pack(pady=12, padx=10)

user_type = ctk.StringVar(value="Sélectionner")
user_type_menu = ctk.CTkOptionMenu(master=frame, variable=user_type, values=["Admin", "Standard", "Technicien"])
user_type_menu.pack(pady=12, padx=10)

button = ctk.CTkButton(master=frame, text="Connexion", command=Menu_Principal)
button.pack(pady=12, padx=10)

checkbox = ctk.CTkCheckBox(master=frame, text="Se souvenir de moi")
checkbox.pack(pady=12, padx=10)

login.mainloop()
