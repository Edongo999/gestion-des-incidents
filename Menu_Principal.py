from tkinter import *
import subprocess

def Incident():
	subprocess.run(["python","Incident.py"])

def Technicien():
	subprocess.run(["python","Technicien.py"])

def Commentaire():
	subprocess.run(["Commentaire",".py"])

def Cathegorie():
	subprocess.run(["python","Categorie.py"])
 

 #titre general
root = Tk()
root.title("Gestion des incidents ")
root.geometry("600x600")

#Ajouter le titre
lbltitre = Label(root,bd = 20, relief = RIDGE, text = "GESTION DES INCIDENTS", font = ("Arial", 30), bg = "#9B59B6", fg="white")
lbltitre.place(x = 0, y = 0, width = 600, height = 500)

Button(root,text="Incident",font=("Cambria",18),command=Incident, width=30, height=0).pack(pady=(100,20))
Button(root,text="Technicien",font=("Cambria",18),command=Technicien, width=30, height=0).pack(pady=(0,20))
Button(root,text="Commntaire",font=("Cambria",18),command=Commentaire, width=30, height=0).pack(pady=(0,20))
Button(root,text="Categorie",font=("Cambria",18),command=Cathegorie, width=30, height=0).pack(pady=(0,20))


root.mainloop()