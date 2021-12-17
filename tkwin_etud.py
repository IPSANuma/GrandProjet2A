import tkinter as tk
from tkinter import ttk
from lib_commun import ouverture_fichier_csv,ecriture_fichier_csv
from lib_gestionEtudiants import ajoutEtudiant,modificationEtudiant,suppressionEtudiant
from tkinter import messagebox

def valider(master,prenom,nom,genre,email,groupe):
    """
    Fonction qui récupère les chaines de charactères rentrées dans les champs (Entry)
     et qui les réinjecte dans la fonction ajoutEtudiant de la lib_gestionEtudiants
        Elle réactualise le tableau à la fin

          En somme elle permet d'ajouter un étudiant
    """
    prenom = prenom.get()
    nom = nom.get()
    email = email.get()
    groupe = groupe.get()


    if prenom == "":
        messagebox.showerror("Erreur de prenom", "Aucun prénom n'est renseigné.")
        pass

    elif nom == "":
        messagebox.showerror("Erreur de prenom", "Aucun nom n'est renseigné.")
        pass

    elif email == "":
        messagebox.showerror("Erreur de email", "Aucun email n'est renseigné.")
        pass

    elif groupe == "":
        messagebox.showerror("Erreur de groupe", "Aucun groupe n'est renseigné.")
        pass

    else:
        ajoutEtudiant(prenom,nom,genre,email,groupe)
        print(prenom,nom,genre,email,groupe)
        tableau(master)

def modifier(master,id,prenom,nom,genre,email,groupe):
    """
    Fonction qui récupère les chaines de charactères rentrées dans les champs (Entry)
     et qui les réinjecte dans la fonction modificationEtudiant de la lib_gestionEtudiants
     Elle réactualise le tableau à la fin

     En somme elle permet de modifier un étudiant
    """
    id = int(id.get())
    nom = str(nom.get()).upper()
    prenom = prenom.get()
    email = email.get()
    groupe = groupe.get()
    modificationEtudiant(id,prenom,nom,genre,email,groupe)
    tableau(master)

def supprimer(master,id):
    """    Fonction qui récupère les chaines de charactères rentrées dans les champs (Entry)
     et qui les réinjecte dans la fonction ajoutEtudiant de la lib_gestionEtudiants
        Elle réactualise le tableau à la fin

          En somme elle permet de supprimer un étudiant"""
    suppressionEtudiant(id.get())
    tableau(master)
#Tableau étudiant

def tableau(master):

    """Génère l'affichage du fichier étudiants.csv. On utilise Treeview pour afficher les données sous forme de tableau."""
    tab = ttk.Treeview(master)
    tab.place(relx= 0.35,rely=0.05,relheight=0.85,relwidth= 0.55)
    data_tab = ouverture_fichier_csv("etudiants.csv")
    tab['column'] = data_tab[0]
    width_column = [1,1,45,45,120,20] #Largeur des colonnes

    for i in range(len(data_tab[0])):
        tab.column(str(data_tab[0][i]), minwidth=0 ,width = width_column[i])
        tab.heading(str(data_tab[0][i]),text=str(data_tab[0][i]))

    tab['show'] = 'headings'

    for i in range(len(data_tab)-1):
        tab.insert('',tk.END, values =data_tab[i+1])

    vsb = ttk.Scrollbar(master, orient="vertical", command=tab.yview)

    vsb.place(relx=0.9,rely=0.05,relwidth=0.1,relheight=0.85)

    tab.configure(yscrollcommand=vsb.set)


def run_win_etud(master):

    """Génère une fenètre fille (après avoir cliqué sur Gestion étudiant) et affiche la fenètre de Gestion étudiant"""

    # Lier la fenêtre à la fenêtre mère
    nw = tk.Toplevel(master)
    nw.geometry("1200x640")
    #Titre de la fenêtre
    nw.title("Gestion étudiants")

    tableau(nw)

    # Frame pour ajouter l'étudiant
    ajt_etud= tk.Frame(nw,bg="white" , highlightbackground="grey", highlightthickness=1)
    ajt_etud.place(relx=0.025,rely=0.05,relheight=0.9,relwidth=0.3)

    # Text prenom
    label_prenom = tk.Label(ajt_etud, text="Prénom",font=("Helvica",15),bg="white",relief="flat")
    label_prenom.place(relx=0.05, rely=0.1, relwidth=0.3, relheight=0.1)

    # Entry value prenom
    entry_prenom = tk.Entry(ajt_etud , highlightbackground="grey", highlightthickness=1)
    entry_prenom.place(relx=0.55, rely=0.1, relwidth=0.3, relheight=0.1)

    # Text nom
    label_nom = tk.Label(ajt_etud, text="Nom",font=("Helvica",15),bg="white",relief="flat")
    label_nom.place(relx=0.05, rely=0.25, relwidth=0.3, relheight=0.1)

    # Entry value nom
    entry_nom = tk.Entry(ajt_etud , highlightbackground="grey", highlightthickness=1)
    entry_nom.place(relx=0.55, rely=0.25, relwidth=0.3, relheight=0.1)

    # Text genre
    label_genre = tk.Label(ajt_etud, text="Genre",font=("Helvica",15),bg="white",relief="flat")
    label_genre.place(relx=0.05, rely=0.4, relwidth=0.3, relheight=0.1)

    # Radio button value genre
    varGr = tk.IntVar()

    def selection_genre():
        """Fonction qui récupère les informations des radiobuttons et renvoie le genre sélectionné"""
        choice = varGr.get()

        if choice == 0:
            output = "M"

        elif choice == 1:
            output = "F"

        return output

#Radiobutton permettant de choisir le sexe
    radio_but_genre_homme = tk.Radiobutton(ajt_etud, variable=varGr, text='Homme', value=0,anchor="w",command=lambda :selection_genre(), bg="white")
    radio_but_genre_femme = tk.Radiobutton(ajt_etud, variable=varGr, text='Femme', value=1,anchor="w",command=lambda :selection_genre(), bg="white")
    radio_but_genre_homme.place(relx=0.55, rely=0.4, relwidth=0.3, relheight=0.1)
    radio_but_genre_femme.place(relx=0.55, rely=0.4+0.6*10**-1, relwidth=0.3, relheight=0.1)


    # Text email
    label_email = tk.Label(ajt_etud, text="Email", font=("Helvica", 15),bg="white",relief="flat")
    label_email.place(relx=0.05, rely=0.55, relwidth=0.3, relheight=0.1)

    # Entry value email
    entry_email = tk.Entry(ajt_etud , highlightbackground="grey", highlightthickness=1)
    entry_email.place(relx=0.55, rely=0.55, relwidth=0.3, relheight=0.1)

    # Text groupe
    label_groupe = tk.Label(ajt_etud, text="Groupe", font=("Helvica", 15),bg="white",relief="flat")
    label_groupe.place(relx=0.05, rely=0.7, relwidth=0.3, relheight=0.1)

    # Entry value groupe
    entry_groupe = tk.Entry(ajt_etud , highlightbackground="grey", highlightthickness=1)
    entry_groupe.place(relx=0.55, rely=0.7, relwidth=0.3, relheight=0.1)

    # Bouton ajouter
    btn_ajouter = tk.Button(ajt_etud,text="Ajouter" ,command=lambda: valider(nw,entry_prenom,entry_nom,selection_genre(),entry_email,entry_groupe))
    btn_ajouter.place(relx=0.1, rely=0.85, relwidth=0.35, relheight=0.05)

    # Bouton modifier
    btn_modifier = tk.Button(ajt_etud,text="Modifier", command=lambda: modifier(nw,entry_id,entry_prenom,entry_nom,selection_genre(),entry_email,entry_groupe))
    btn_modifier.place(relx=0.55, rely=0.85, relwidth=0.35, relheight=0.05)

    # Entry value id
    entry_id = tk.Entry(ajt_etud , highlightbackground="grey", highlightthickness=1)
    entry_id.place(relx=0.15, rely=0.925, relwidth=0.1, relheight=0.05)

    # Bouton supprimer
    btn_modifier = tk.Button(ajt_etud,text="Supprimer", command=lambda: supprimer(nw,entry_id))
    btn_modifier.place(relx=0.325, rely=0.925, relwidth=0.35, relheight=0.05)

    # Frame pour ajouter l'étudiant
    tab_etud= tk.Frame(nw,bg="white",relief="sunken")
    tab_etud.place(relx=3.05,rely=0.05,relheight=0.9,relwidth=0.6)

    # Bouton retour
    btn_return = tk.Button(nw,text="retour",command=lambda: nw.destroy())
    btn_return.place(relx=0.6,rely=0.925,relheight=0.05,relwidth=0.1)

