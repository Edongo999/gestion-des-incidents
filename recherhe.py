import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def envoyer_email_incident(admin_email, titre, description, utilisateur, date_signallement):
    # Configuration SMTP
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = "landryamengne@gmail.com"  # Remplacez par votre adresse email
    sender_password = "sasouker"  # Remplacez par votre mot de passe ou mot de passe d'application

    # Création du message email
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = admin_email
    message['Subject'] = "Nouveau Signalement d'Incident"
    
    # Contenu du message
    body = f"""
    Bonjour Administrateur,

    Un nouvel incident a été signalé par l'utilisateur : {utilisateur}

    **Titre** : {titre}
    **Description** : {description}
    **Date de Signalement** : {date_signallement}

    Merci de prendre en charge cet incident.

    Cordialement,
    Votre application de gestion des incidents.
    """
    message.attach(MIMEText(body, 'plain'))

    try:
        # Connexion au serveur SMTP
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Active la sécurité TLS
        server.login(sender_email, sender_password)  # Authentification
        # Envoi du message
        server.send_message(message)
        print("Email envoyé avec succès à l'administrateur.")
        server.quit()
    except Exception as e:
        print(f"Erreur lors de l'envoi de l'email : {e}")

def ajouter():
    try:
        # Récupération des données depuis les champs
        titre = entrertitre.get()
        description = entrerdescription.get()
        etat = combostatut.get()
        priorite = entrerpriorité.get()
        categorie = entrercategorie.get()
        impact = entrerimpact.get()
        service = entrerservice.get()
        utilisateur = entrerutilisateur.get()
        signallement = entrerdate_signallement.get_date().strftime('%Y-%m-%d')
        
        # Connexion à la base de données
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="gestion_incidents"
        )
        cuser = con.cursor()
        cuser.execute("INSERT INTO incident (titre, description, etat, priorite, categorie, impact, service, utilisateur, date_signallement) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                      (titre, description, etat, priorite, categorie, impact, service, utilisateur, signallement))
        con.commit()
        con.close()
        
        # Envoi d'un email à l'administrateur
        admin_email = "landryamengne@gmail.com"  # Remplacez par l'email de l'administrateur
        envoyer_email_incident(admin_email, titre, description, utilisateur, signallement)
        
        # Message de confirmation
        messagebox.showinfo("Information", "Incident ajouté avec succès et email envoyé.")
        afficher()  # Mettre à jour le tableau
    except ValueError:
        messagebox.showerror("Erreur", "Le format de la date doit être JJ/MM/AAAA")
    except Exception as e:
        messagebox.showerror("Erreur", f"Une erreur est survenue : {e}")
