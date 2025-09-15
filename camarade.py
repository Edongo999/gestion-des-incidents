from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import mysql.connector
from datetime import datetime


def ajouter():
    try:
        titre = entrertitre.get()
        description = entrerdescription.get()
        etat = entreretat.get()
        priorite = entrerpriorité.get()
        categorie = entrercategorie.get()
        impact = entrerimpact.get()
        service = entrerservice.get()
        utilisateur = entrerutilisateur.get()
        signallement  = datetime.strptime(entrerdate_signallement.get(), '%d/%m/%Y').strftime('%Y-%m-%d')

        # Créez la connexion
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="gestion_incidents"
        )
        cuser = con.cursor()
        cuser.execute("INSERT INTO incident (numin,titre, description, etat, priorite, categorie, impact, service, utilisateur, date_signelement) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                      (titre, description, etat, priorite, categorie, impact, service, utilisateur, signallement ))
        con.commit()
        con.close()
        messagebox.showinfo("Incident ajouté")

        # Mettre à jour le tableau
        afficher()
    except ValueError:
        messagebox.showerror("Erreur", "Le format de la date doit être JJ/MM/AAAA")

def modifier():
    try:
        
        titre = entrertitre.get()
        description = entrerdescription.get()
        etat = entreretat.get()
        priorite = entrerpriorité.get()
        categorie = entrercategorie.get()
        impact = entrerimpact.get()
        service = entrerservice.get()
        utilisateur = entrerutilisateur.get()
        signallement  = datetime.strptime(entrerdate_signallement.get(), '%d/%m/%Y').strftime('%Y-%m-%d')

        # Créez la connexion
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="gestion_incidents"
        )
        cuser = con.cursor()
        cuser.execute("UPDATE incident SET titre=%s, description=%s, etat=%s, priorite=%s, categorie=%s, impact=%s, service=%s, utilisateur=%s, date_signallement=%s WHERE code=%s",
                      (titre, description, etat, priorite, categorie, impact, service, utilisateur, signallement))
        con.commit()
        con.close()
        messagebox.showinfo("Incident modifié")

        # Mettre à jour le tableau
        afficher()
    except ValueError:
        messagebox.showerror("Erreur", "Le format de la date doit être JJ/MM/AAAA")

def supprimer():
    codeSelectionner = table.item(table.selection())['values'][0]
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="gestion_incidents"
    )
    cuser = con.cursor()
    cuser.execute("DELETE FROM incident WHERE id ")
    con.commit()
    con.close()
    
    # SUPPRESSION DES EQUIPES DANS LA BASE DE DONNEES


    # Mettre à jour le tableau
    afficher()

def afficher():
    # Supprimer les anciennes données dans le tableau
    for i in table.get_children():
        table.delete(i)
    
    # Créez la connexion
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="gestion_incidents"
    )
    cuser = con.cursor()
    cuser.execute("SELECT * FROM incident")
    rows = cuser.fetchall()
    for row in rows:
        table.insert('', END, values=row)
    con.close()

# Titre général
root = Tk()
root.title("Gestion des incidents")
root.geometry("1500x600")  # Augmenter la largeur de la fenêtre

# Ajouter le titre
lbltitre = Label(root, bd=20, relief=RIDGE, text="INCIDENT", font=("Arial", 30), bg="darkblue", fg="white")
lbltitre.place(x=0, y=0, width=1500)

# Liste des incidents
lblListeincident = Label(root, text="LISTES DES INCIDENTS", font=("Arial", 16), bg="darkblue", fg="white")
lblListeincident.place(x=250, y=350, width=900)


# Texte titre incident
lbltitre = Label(root, text="Titre incident", font=("Arial", 16), bg="black", fg="white")
lbltitre.place(x=0, y=100, width=200)
entrertitre = Entry(root)
entrertitre.place(x=200, y=100, width=300, height=30)

# Texte description
lbldescription = Label(root, text="Description Incident", font=("Arial", 16), bg="black", fg="white")
lbldescription.place(x=600, y=100, width=200)
entrerdescription = Entry(root)
entrerdescription.place(x=800, y=100, width=300, height=30)

# Texte état
lbletat = Label(root, text="État", font=("Arial", 16), bg="black", fg="white")
lbletat.place(x=0, y=150, width=200)
entreretat = Entry(root)
entreretat.place(x=150, y=150, width=350, height=30)

# Texte priorité
lblpriorite = Label(root, text="Priorité Incident", font=("Arial", 16), bg="black", fg="white")
lblpriorite.place(x=600, y=150, width=200)
entrerpriorité = Entry(root)
entrerpriorité.place(x=800, y=150, width=300, height=30)

# Texte catégorie
lblcategorie = Label(root, text="Catégorie Incident", font=("Arial", 16), bg="black", fg="white")
lblcategorie.place(x=0, y=200, width=200)
entrercategorie = Entry(root)
entrercategorie.place(x=200, y=200, width=300, height=30)

# Texte impact
lblimpact = Label(root, text="Impact Incident", font=("Arial", 16), bg="black", fg="white")
lblimpact.place(x=600, y=200, width=200)
entrerimpact = Entry(root)
entrerimpact.place(x=800, y=200, width=300, height=30)

# Texte service affecté
lblservice = Label(root, text="Service Affecté", font=("Arial", 16), bg="black", fg="white")
lblservice.place(x=0, y=250, width=200)
entrerservice = Entry(root)
entrerservice.place(x=200, y=250, width=300, height=30)

# Texte utilisateur affecté
lblutilisateur = Label(root, text="Utilisateur Affecté", font=("Arial", 16), bg="black", fg="white")
lblutilisateur.place(x=600, y=250, width=200)
entrerutilisateur = Entry(root)
entrerutilisateur.place(x=800, y=250, width=300, height=30)

# Texte date de signalement de l'incident
lbldate_signallement = Label(root, text="Date de Signalement", font=("Arial", 16), bg="black", fg="white")
lbldate_signallement.place(x=0, y=300, width=200)
entrerdate_signallement = Entry(root)
entrerdate_signallement.place(x=200, y=300, width=300, height=30)


# Bouton Enregistrer
btnenregistrer = Button(root, text="Enregistrer", font=("Arial", 16), bg="darkblue", fg="yellow", command=ajouter)
btnenregistrer.place(x=1130, y=94, width=200)

# Bouton Modifier
btnmodifier = Button(root, text="Modifier", font=("Arial", 16), bg="darkblue", fg="yellow", command=modifier)
btnmodifier.place(x=1130, y=150, width=200)

# Bouton Supprimer
btnSupprimer = Button(root, text="Supprimer", font=("Arial", 16), bg="darkblue", fg="yellow", command=supprimer)
btnSupprimer.place(x=1130, y=200, width=200)

# afficher les informations de la table

# Tableau
table = ttk.Treeview(root, columns=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10), height=5, show="headings")
table.place(x=40, y=390, width=1320, height=300)  # Augmenter la largeur du tableau

# Entêtes du tableau
table.heading(1, text="CODE")
table.heading(2, text="Titre")
table.heading(3, text="Description")
table.heading(4, text="État")
table.heading(5, text="Priorité")
table.heading(6, text="Catégorie")
table.heading(7, text="Impact")
table.heading(8, text="Service")
table.heading(9, text="Utilisateur")
table.heading(10, text="Date")

# Définir les dimensions des colonnes
table.column(1, width=50)
table.column(2, width=100)
table.column(3, width=150)
table.column(4, width=150)
table.column(5, width=150)
table.column(6, width=150)
table.column(7, width=150)
table.column(8, width=150)
table.column(9, width=150)
table.column(10, width=100)

# Charger les données dans le tableau au démarrage
afficher()

root.mainloop()
