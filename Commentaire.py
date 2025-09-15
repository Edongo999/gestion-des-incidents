#importer les tkinter
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import sqlite3

def ajouter():
    matricule=entrertitre.get()
    contenu = entrerdescription.get()
    date_commentaire= entreretat.get()
    

    #Creeon la connexion
    con = sqlite3.connect('hopital.db')
    cuser = con.cursor()
    cuser.execute("insert into patient('code','contenu','date_commentaire') values (?,?,?)",(matricule,contenu,date_commentaire))
    con.commit()
    con.close()
    messagebox.showinfo("Patient ajouter")

    #afficher
    con = sqlite3.connect('hopital.db')
    cuser = con.cursor()
    select = cuser.execute("select *from patient order by code desc")
    select = list(select)
    table.insert('',END,values = select[0])
    con.close()

def modifier():
    matricule=entrertitre.get()
    nom = entrerdescription.get()
    prenom = entreretat.get()
    age = entrerpriorité.get()
    adresse = entrercategorie.get()
    telephone = entrerimpact.get()
    remarque = entrerservice_affecté.get()
    remarque = entrerutilisateur_affecté.get()
    remarque = entrerdate_creation.get()

     


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
lbltitre = Label(root,bd = 20, relief = RIDGE, text = "Commentaire", font = ("Arial", 30), bg = "darkblue", fg="white")
lbltitre.place(x = 0, y = 0, width = 1365)

#Liste des commentaires
lblListecommentaire = Label(root, text = "LISTES DES COMMENTAIRES ", font = ("Arial", 16), bg = "darkblue", fg="white")
lblListecommentaire.place(x=600,y=100,width=750)



#text titre incident
lbltitre = Label(root, text = "titre incident", font = ("Arial", 16), bg = "black", fg="white")
lbltitre.place(x=0,y=100,width=200)
entrertitre = Entry(root)
entrertitre.place(x=200,y=100,width=300,height=30)

#text description
lbldescription = Label(root, text = "Description Incident", font = ("Arial", 16), bg = "black", fg="white")
lbldescription.place(x=0,y=150,width=200)
entrerdescription= Entry(root)
entrerdescription.place(x=200,y=150,width=300,height=30)

#text etat
lbletat= Label(root, text = "Etat", font = ("Arial", 16), bg = "black", fg="white")
lbletat.place(x=0,y=200,width=200)
entreretat = Entry(root)
entreretat.place(x=200,y=200,width=300,height=30)



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
table.heading(2 , text = "Contenu")
table.heading(3 , text = "Date_Commentaire")


#definir les dimentions des colonnes
table.column(1,width = 50)
table.column(2,width = 150)
table.column(3,width = 150)






root.mainloop()