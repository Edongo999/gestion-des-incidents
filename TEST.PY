from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import mysql.connector
from datetime import datetime
from tkcalendar import DateEntry
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
import threading

from Historique_incident import afficher_historique  # Importer la fonction

def ajouter():
    try:
        titre = entrertitre.get()
        description = entrerdescription.get()
        etat = combostatut.get()
        priorite = entrerpriorité.get()
        categorie = entrercategorie.get()
        impact = entrerimpact.get()
        service = entrerservice.get()
        utilisateur = entrerutilisateur.get()
        signallement = entrerdate_signallement.get_date().strftime('%Y-%m-%d')  # Conversion de la date
        
        # Créez la connexion
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="gestion_incidents"
        )
        cuser = con.cursor()
        cuser.execute("INSERT INTO incident (titre, description, etat, priorite, categorie, impact, service, utilisateur, date_signalement) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", 
                      (titre, description, etat, priorite, categorie, impact, service, utilisateur, signallement))
        con.commit()
        con.close()
        messagebox.showinfo("Information", "Incident ajouté avec succès")
        afficher()  # Mettre à jour le tableau
    except ValueError:
        messagebox.showerror("Erreur", "Le format de la date doit être JJ/MM/AAAA")

def modifier():
    try:
        codeSelectionner = table.item(table.selection())['values'][0]
        titre = entrertitre.get()
        description = entrerdescription.get()
        etat = combostatut.get()
        priorite = entrerpriorité.get()
        categorie = entrercategorie.get()
        impact = entrerimpact.get()
        service = entrerservice.get()
        utilisateur = entrerutilisateur.get()
        signallement = entrerdate_signallement.get_date().strftime('%Y-%m-%d')  # Conversion de la date
        
        # Créez la connexion
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="gestion_incidents"
        )
        cuser = con.cursor()
        cuser.execute("UPDATE incident SET titre=%s, description=%s, etat=%s, priorite=%s, categorie=%s, impact=%s, service=%s, utilisateur=%s, date_signallement=%s WHERE id=%s", 
                      (titre, description, etat, priorite, categorie, impact, service, utilisateur, signallement, codeSelectionner))
        con.commit()
        con.close()
        messagebox.showinfo("Information", "Incident modifié avec succès")
        afficher()  # Mettre à jour le tableau
    except ValueError:
        messagebox.showerror("Erreur", "Le format de la date doit être JJ/MM/AAAA")
    except IndexError:
        messagebox.showerror("Erreur", "Aucun incident sélectionné pour modification")

def supprimer():
    try:
        codeSelectionner = table.item(table.selection())['values'][0]
        
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="gestion_incidents"
        )
        cuser = con.cursor()
        cuser.execute("DELETE FROM incident WHERE id = %s", (codeSelectionner,))
        con.commit()
        con.close()
        
        messagebox.showinfo("Information", "Incident supprimé avec succès")
        afficher()  # Mettre à jour le tableau
    except IndexError:
        messagebox.showerror("Erreur", "Aucun incident sélectionné pour suppression")

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

def imprimer():
    # Demander confirmation d'impression
    reponse = messagebox.askyesno("Confirmation", "Voulez-vous imprimer le tableau ?")
    if reponse:
        apercu_impression()

def apercu_impression():
    # Afficher l'aperçu du tableau avant impression
    apercu = Toplevel(root)
    apercu.title("Aperçu avant impression")
    apercu.geometry("1300x400")

    # Créer un tableau pour l'aperçu
    table_apercu = ttk.Treeview(apercu, columns=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10), height=5, show="headings")
    table_apercu.pack(fill=BOTH, expand=True)

    # Entêtes du tableau
    table_apercu.heading(1, text="CODE")
    table_apercu.heading(2, text="Titre")
    table_apercu.heading(3, text="Description")
    table_apercu.heading(4, text="Statut")
    table_apercu.heading(5, text="Priorité")
    table_apercu.heading(6, text="Catégorie")
    table_apercu.heading(7, text="Impact")
    table_apercu.heading(8, text="Service")
    table_apercu.heading(9, text="Utilisateur")
    table_apercu.heading(10, text="Date")

    # Définir les dimensions des colonnes
    for i in range(1, 11):
      table_apercu.column(i, width=150)

    # Charger les données dans le tableau de l'aperçu
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
        table_apercu.insert('', END, values=row)
    
    con.close()

    # Bouton pour lancer l'impression
    btn_imprimer = Button(apercu, text="Imprimer", command=lambda: lancer_impression(apercu), font=("Arial", 14), bg="darkblue", fg="yellow")
    btn_imprimer.pack(pady=20)

def lancer_impression(apercu):
    # Créer une fenêtre de chargement avec une animation de rond tournant
    chargement = Toplevel(root)
    chargement.title("Impression en cours")
    chargement.geometry("300x100")
    canvas_loading = Canvas(chargement, width=100, height=100)
    canvas_loading.pack(pady=20)

    # Fonction pour animer un rond tournant
    def animer_loading(canvas, angle):
        canvas.delete("all")
        canvas.create_arc(10, 10, 90, 90, start=angle, extent=150, outline="blue", width=5)
        angle += 10
        if angle >= 360:
            angle = 0
        canvas.after(50, animer_loading, canvas, angle)
    animer_loading(canvas_loading, 0)

        # Créer une fonction pour lancer l'impression dans un thread séparé
    def impression():
        pdf_filename = "liste_incidents.pdf"
        c = canvas.Canvas(pdf_filename, pagesize=letter)
        width, height = letter

        c.setFont("Helvetica-Bold", 18)
        c.drawCentredString(width / 2.0, height - 40, "Liste des Incidents")

        col_width = [40, 100, 150, 100, 100, 150, 100, 150, 150, 150]
        headers = ["CODE", "Titre", "Description", "Statut", "Priorité", "Catégorie", "Impact", "Service", "Utilisateur", "Date"]

        c.setFont("Helvetica-Bold", 10)
        x_offset = 30
        y_offset = height - 60

        for i, header in enumerate(headers):
            c.drawString(x_offset + sum(col_width[:i]), y_offset, header)
            c.rect(x_offset + sum(col_width[:i]), y_offset - 10, col_width[i], 20)

        # Fonction pour dessiner du texte avec retour à la ligne
        def draw_wrapped_text(c, text, x, y, width):
            if not text: return 0
            max_width = width - 5  # Reduce width to account for padding
            words = text.split()
            lines = []
            if words:
                current_line = words[0]
            else:
                current_line = ""

            for word in words[1:]:
                if c.stringWidth(current_line + " " + word) < max_width:
                    current_line += " " + word
                else:
                    lines.append(current_line)
                    current_line = word

            lines.append(current_line)
            text_height = len(lines) * 12  # Approximate height for each line of text

            for i, line in enumerate(lines):
                c.drawString(x + 2, y - (i * 12) - 2, line)
            return text_height

        # Ajouter les lignes de données avec bordures et retour automatique de texte
        y_offset -= 20

        for row in table.get_children():
            values = table.item(row)['values']
            max_cell_height = 0

            for i, value in enumerate(values):
                cell_height = draw_wrapped_text(c, str(value), x_offset + sum(col_width[:i]), y_offset, col_width[i])
                if cell_height > max_cell_height:
                    max_cell_height = cell_height

            for i, value in enumerate(values):
                c.rect(x_offset + sum(col_width[:i]), y_offset - max_cell_height, col_width[i], max_cell_height)  # Ajuster la bordure
            y_offset -= max_cell_height

        # Sauvegarder le fichier PDF
        c.save()

        # Fermer la fenêtre de chargement après impression
        chargement.destroy()
        messagebox.showinfo("Information", f"Liste des incidents imprimée avec succès dans {pdf_filename}")

    thread_impression = threading.Thread(target=impression)
    thread_impression.start()

def obtenir_role_utilisateur():
    utilisateur = entrerutilisateur.get()
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="gestion_incidents"
    )
    cuser = con.cursor()
    cuser.execute("SELECT role FROM utilisateur WHERE Nom=%s", (utilisateur,))
    role = cuser.fetchone()
    con.close()
    return role[0] if role else 'standard'

def mettre_a_jour_statut(nouveau_statut):
    try:
        codeSelectionner = table.item(table.selection())['values'][0]
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="gestion_incidents"
        )
        cuser = con.cursor()
        cuser.execute("UPDATE incident SET etat=%s WHERE id=%s", (nouveau_statut, codeSelectionner))
        con.commit()
        con.close()
        messagebox.showinfo("Information", f"Le statut de l'incident a été mis à jour en '{nouveau_statut}'")
        afficher()  # Mettre à jour la liste des incidents affichée
    except IndexError:
        messagebox.showerror("Erreur", "Aucun incident sélectionné pour mise à jour du statut")

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
entrertitre = Entry(root, font=("Arial", 16))
entrertitre.place(x=200, y=100, width=300, height=30)

# Texte description
lbldescription = Label(root, text="Description Incident", font=("Arial", 16), bg="black", fg="white")
lbldescription.place(x=600, y=100, width=200)
entrerdescription = Entry(root, font=("Arial", 16))
entrerdescription.place(x=800, y=100, width=300, height=30)

# Liste déroulante pour statut
lblstatut = Label(root, text="Statut", font=("Arial", 16), bg="black", fg="white")
lblstatut.place(x=0, y=150, width=200)
combostatut = ttk.Combobox(root, values=["En attente", "En cours", "Résolu"], font=("Arial", 16))
combostatut.place(x=200, y=150, width=300, height=30)
combostatut.current(0)  # Définir la valeur par défaut à "En attente"

# Texte priorité
lblpriorite = Label(root, text="Priorité Incident", font=("Arial", 16), bg="black", fg="white")
lblpriorite.place(x=600, y=150, width=200)
entrerpriorité = Entry(root, font=("Arial", 16))
entrerpriorité.place(x=800, y=150, width=300, height=30)

# Texte catégorie
lblcategorie = Label(root, text="Catégorie Incident", font=("Arial", 16), bg="black", fg="white")
lblcategorie.place(x=0, y=200, width=200)
entrercategorie = Entry(root, font=("Arial", 16))
entrercategorie.place(x=200, y=200, width=300, height=30)

# Texte impact
lblimpact = Label(root, text="Impact Incident", font=("Arial", 16), bg="black", fg="white")
lblimpact.place(x=600, y=200, width=200)
entrerimpact = Entry(root, font=("Arial", 16))
entrerimpact.place(x=800, y=200, width=300, height=30)

# Texte service affecté
lblservice = Label(root, text="Service Affecté", font=("Arial", 16), bg="black", fg="white")
lblservice.place(x=0, y=250, width=200)
entrerservice = Entry(root, font=("Arial", 16))
entrerservice.place(x=200, y=250, width=300, height=30)

# Texte utilisateur affecté
lblutilisateur = Label(root, text="Utilisateur Affecté", font=("Arial", 16), bg="black", fg="white")
lblutilisateur.place(x=600, y=250, width=200)
entrerutilisateur = Entry(root, font=("Arial", 16))
entrerutilisateur.place(x=800, y=250, width=300, height=30)

# Texte date de signalement de l'incident
lbldate_signallement = Label(root, text="Date de Signalement", font=("Arial", 16), bg="black", fg="white")
lbldate_signallement.place(x=0, y=300, width=200)
entrerdate_signallement = DateEntry(root, date_pattern='dd/mm/yyyy', background='gray15', foreground='white', borderwidth='2', state='readonly', font=("Arial", 14))
entrerdate_signallement.place(x=200, y=300, width=300, height=30)

# Bouton Enregistrer
btnenregistrer = Button(root, text="Enregistrer", font=("Arial", 16), bg="darkblue", fg="yellow", command=ajouter)
btnenregistrer.place(x=1130, y=94, width=200)

# Bouton Modifier
btnmodifier = Button(root, text="Modifier", font=("Arial", 16), bg="darkblue", fg="yellow", command=modifier)
btnmodifier.place(x=1130, y=150, width=200)

# Bouton Modifier
btnmodifier = Button(root, text="Modifier", font=("Arial", 16), bg="darkblue", fg="yellow", command=modifier)
btnmodifier.place(x=1130, y=150, width=200)

# Bouton Supprimer
btnSupprimer = Button(root, text="Supprimer", font=("Arial", 16), bg="darkblue", fg="yellow", command=supprimer)
btnSupprimer.place(x=1130, y=200, width=200)

# Bouton Imprimer
btnImprimer = Button(root, text="Imprimer", font=("Arial", 16), bg="darkblue", fg="yellow", command=imprimer)
btnImprimer.place(x=1130, y=250, width=200)

# Bouton pour afficher tous les incidents
btnAfficherHistorique = Button(root, text="Afficher Historique", font=("Arial", 16), bg="darkblue", fg="yellow", command=lambda: afficher_historique(table))
btnAfficherHistorique.place(x=1130, y=300, width=300)

# Initialiser le statut des champs en fonction du rôle de l'utilisateur
role_utilisateur = obtenir_role_utilisateur()
if role_utilisateur != 'technicien':
    combostatut.state(['disabled'])
else:
    btn_statut_en_cours = Button(root, text="En cours", command=lambda: mettre_a_jour_statut("En cours"))
    btn_statut_en_cours.place(x=0, y=350, width=200)
    btn_statut_resolu = Button(root, text="Résolu", command=lambda: mettre_a_jour_statut("Résolu"))
    btn_statut_resolu.place(x=200, y=350, width=200)

# Créer le tableau pour afficher les incidents
table = ttk.Treeview(root, columns=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10), height=5, show="headings")
table.place(x=40, y=390, width=1320, height=300)  # Augmenter la largeur du tableau

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

for i in range(1, 11):
    table.column(i, width=150)

afficher()
root.mainloop()
