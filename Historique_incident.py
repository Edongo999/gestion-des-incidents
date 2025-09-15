# historique_incidfrom tkinter import ttk
from tkinter import *
from tkinter import messagebox
import mysql.connector
from datetime import datetime
from tkcalendar import DateEntry
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
import threading

import mysql.connector
from tkinter import Toplevel, ttk, messagebox

def afficher_historique(root):
    # Créer une nouvelle fenêtre pour l'historique des incidents
    historique_fenetre = Toplevel(root)
    historique_fenetre.title("Historique des Incidents")
    historique_fenetre.geometry("1300x400")

    # Créer un tableau pour afficher les incidents
    table = ttk.Treeview(historique_fenetre, columns=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10), height=5, show="headings")
    table.pack(fill=BOTH, expand=True)

    # Entêtes du tableau
    table.heading(1, text="CODE")
    table.heading(2, text="Titre")
    table.heading(3, text="Description")
    table.heading(4, text="Statut")
    
    table.heading(5, text="Priorité")
    table.heading(6, text="Catégorie")
    table.heading(7, text="Impact")
    table.heading(8, text="Service")
    table.heading(9, text="Utilisateur")
    table.heading(10, text="Date")

    # Définir les dimensions des colonnes
    for i in range(1, 11):
        table.column(i, width=150)

    # Créez la connexion à la base de données
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="gestion_incidents"
    )
    cuser = con.cursor()
    cuser.execute("SELECT * FROM incident")
    rows = cuser.fetchall()

    # Insérer les incidents dans le tableau
    for row in rows:
        table.insert('', END, values=row)
    
    con.close()
    messagebox.showinfo("Information", "Liste de tous les incidents signalés affichée avec succès")



# Titre général
root = Tk()
root.title("Gestion des incidents")
root.geometry("1500x600")  # Augmenter la largeur de la fenêtre
# Bouton pour afficher tous les incidents
btnAfficherHistorique = Button(root, text="Afficher Historique", font=("Arial", 16), bg="darkblue", fg="yellow", command=lambda: afficher_historique(table))
btnAfficherHistorique.place(x=1130, y=300, width=300)

root.mainloop()