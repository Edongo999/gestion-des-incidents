from tkinter import *
import subprocess

def Signaler_Incident():
	subprocess.run(["python","Signaler_Incident.py"])

def afficher_tous_les_incidents():
	subprocess.run(["python","Historique_incident.py"])


 

 #titre general
root = Tk()
root.title("Gestion des incidents ")
root.geometry("600x600")

#Ajouter le titre
lbltitre = Label(root,bd = 20, relief = RIDGE, text = "GESTION DES INCIDENTS", font = ("Arial", 30), bg = "#9B59B6", fg="white")
lbltitre.place(x = 0, y = 0, width = 600, height = 500)

Button(root,text="Signaler Un Incident",font=("Cambria",18),command=Signaler_Incident, width=30, height=0).pack(pady=(100,20))
# Ajouter le bouton pour afficher tous les incidents
Button(root,text="Historique_incident",font=("Cambria",18),command=afficher_tous_les_incidents, width=30, height=0).pack(pady=(150,25))
btnAfficherTous = Button(root, text="Historique_incident", font=("Arial", 16), bg="darkblue", fg="yellow", command=afficher_tous_les_incidents)
btnAfficherTous.place(x=1130, y=300, width=300)



root.mainloop()