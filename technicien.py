#importer les tkinter
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import sqlite3

def ajouter():
    nom=entrernom.get()
    prenom = entrerprenom.get()
    email = entreremail.get()
    telephone = entrertelephone.get()
    spécialité = entrercspécialité.get()
    

    #Creeon la connexion
    con = sqlite3.connect('hopital.db')
    cuser = con.cursor()
    cuser.execute("insert into technicien('code','nom','prenom','email','telephone','spécialité') values (?,?,?,?,?,?)",(nom,prenom,email,telephone,spécialité))
    con.commit()
    con.close()
    messagebox.showinfo("Technicien ajouter")

    #afficher
    con = sqlite3.connect('hopital.db')
    cuser = con.cursor()
    select = cuser.execute("select *from technicien order by code desc")
    select = list(select)
    table.insert('',END,values = select[0])
    con.close()

def modifier():
    matricule=entrernom.get()
    nom = entrerprenom.get()
    prenom = entreremail.get()
    age = entrertelephone.get()
    adresse = entrercspécialité.get()
    
    

     


def supprimer():
    codeSelectionner = table.item(table.selection())['values'][0]
    con = sqlite3.connect("hopital.db")
    cuser = con.cursor()
    delete  =cuser.execute("delete from patient where code = {}".format(codeSelectionner))
    con.commit()
    table.delete(table.selection())



#titre general
root = Tk()
root.title("Gestion des incidents ")
root.geometry("1300x600")


#Ajouter le titre
lbltitre = Label(root,bd = 20, relief = RIDGE, text = "TECHNICIEN", font = ("Arial", 30), bg = "darkblue", fg="white")
lbltitre.place(x = 0, y = 0, width = 1365)

#Liste des techniciens
lblListetechnicien = Label(root, text = "LISTES DES TECHNICIENS ", font = ("Arial", 16), bg = "darkblue", fg="white")
lblListetechnicien.place(x=600,y=100,width=750)



#text nom technicien
lblnom = Label(root, text = "nom technicien", font = ("Arial", 16), bg = "black", fg="white")
lblnom.place(x=0,y=100,width=200)
entrernom = Entry(root)
entrernom.place(x=200,y=100,width=300,height=30)

#text prenom technicien
lblprenom = Label(root, text = "prénom technicien", font = ("Arial", 16), bg = "black", fg="white")
lblprenom.place(x=0,y=150,width=200)
entrerprenom= Entry(root)
entrerprenom.place(x=200,y=150,width=300,height=30)

#text email
lblemail= Label(root, text = "Email", font = ("Arial", 16), bg = "black", fg="white")
lblemail.place(x=0,y=200,width=200)
entreremail = Entry(root)
entreremail.place(x=200,y=200,width=300,height=30)

#text téléphone
lbltelephone = Label(root, text = "Téléphone", font = ("Arial", 16), bg = "black", fg="white")
lbltelephone.place(x=0,y=250,width=200)
entrertelephone = Entry(root)
entrertelephone.place(x=200,y=250,width=300,height=30)

#text spécialité
lblspécialité = Label(root, text = "Spécialité", font = ("Arial", 16), bg = "black", fg="white")
lblspécialité.place(x=0,y=300,width=200)
entrercspécialité = Entry(root)
entrercspécialité.place(x=200,y=300,width=300,height=30)



#Enregistrer
btnenregistrer = Button(root, text = "Enregistrer", font = ("Arial", 16),bg = "darkblue", fg = "yellow", command = ajouter)
btnenregistrer.place(x=30, y= 450, width=200)

#modifier
btnmodofier = Button(root, text = "Modifier", font = ("Arial", 16),bg = "darkblue", fg = "yellow", command = modifier)
btnmodofier.place(x=270, y= 450, width=200)

#Supprimer
btnSupprimer = Button(root, text = "Supprimer", font = ("Arial", 16),bg = "darkblue", fg = "yellow", command = supprimer)
btnSupprimer.place(x=150, y= 500, width=200)



#Table
table = ttk.Treeview(root, columns = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10), height = 5, show = "headings")
table.place(x = 570,y = 150, width = 750, height = 500)

#Entete
table.heading(1 , text = "CODE")
table.heading(2 , text = "Nom")
table.heading(3 , text = "Prénom")
table.heading(4 , text = "Email")
table.heading(5 , text = "Téléphone")
table.heading(6 , text = "Spécialité")


#definir les dimentions des colonnes
table.column(1,width = 50)
table.column(2,width = 150)
table.column(3,width = 150)
table.column(4,width = 50)
table.column(5,width = 150)
table.column(6,width = 100)



# afficher les informations de la table



root.mainloop()