
import tkinter as tk
from tkinter import ttk
from lib_commun import ouverture_fichier_csv,ecriture_fichier_csv
from lib_gestionNotes import ajoutNote,modificationNote,suppressionNote

def ajout(master,id_etudiant, annee, matiere, note):
    id_ = id_etudiant.get()
    annee_ = annee.get()
    mat_ = matiere.get()
    note_ = note.get()
    ajoutNote(id_, annee_, mat_, note_)

    tableau(master)

def modifier(master,id_etudiant, annee, matiere, note):
    id_ = id_etudiant.get()
    annee_ = annee.get()
    mat_ = matiere.get()
    note_ = note.get()

    modificationNote(id_, annee_, mat_, note_)

    tableau(master)


def supprimer(master,id_etudiant,annee,matiere):
    id_ = id_etudiant.get()
    annee_ = annee.get()
    mat_ = matiere.get()


    suppressionNote(id_, annee_, mat_)
    tableau(master)

def tableau(master):
    tab = ttk.Treeview(master)
    tab.place(relx= 0.375,rely=0.1,relheight=0.8,relwidth= 0.525)
    data_tab = ouverture_fichier_csv("notes.csv")
    tab['column'] = data_tab[0]

    for i in data_tab[0]:
        tab.column(str(i), width = 20)
        tab.heading(str(i),text=str(i))
    tab['show'] = 'headings'

    for i in range(len(data_tab)-1):
        tab.insert('',tk.END, values =data_tab[i+1])

    #Scrollbar

    vsb = ttk.Scrollbar(master, orient="vertical", command=tab.yview)

    vsb.place(relx=0.9,rely=0.1,relwidth=0.1,relheight=0.8)

    tab.configure(yscrollcommand=vsb.set)

def run_win_notes(master):
    nw = tk.Toplevel(master)
    nw.title("Gestion notes")

    nw.geometry("640x400")

    #Affiche le tableau des notes
    tableau(nw)

    # Frame pour modifier/ajouter/supprimer des notes
    note_frame = tk.Frame(nw,bg="white" , highlightbackground="grey", highlightthickness=1)
    note_frame.place(relx=0.05,rely=0.20,relheight=0.6,relwidth=0.3)

    # Text annee
    label_annee = tk.Label(note_frame, text="Année",font=("Helvica",15),bg="white",relief="flat")
    label_annee.place(relx=0.1, rely=0.1, relwidth=0.3, relheight=0.1)

    # Entry value annee
    entry_annee = tk.Entry(note_frame , highlightbackground="grey", highlightthickness=1)
    entry_annee.place(relx=0.55, rely=0.1, relwidth=0.3, relheight=0.1)

    # Text matiere
    label_matiere = tk.Label(note_frame, text="Matière",font=("Helvica",15),bg="white",relief="flat")
    label_matiere.place(relx=0, rely=0.25, relwidth=0.5, relheight=0.1)

    # Entry value matiere
    entry_matiere = tk.Entry(note_frame , highlightbackground="grey", highlightthickness=1)
    entry_matiere.place(relx=0.55, rely=0.25, relwidth=0.3, relheight=0.1)

    # Text note
    label_note = tk.Label(note_frame, text="Note", font=("Helvica", 15),bg="white",relief="flat")
    label_note.place(relx=0.1, rely=0.40, relwidth=0.3, relheight=0.1)

    # Entry value note
    entry_note = tk.Entry(note_frame , highlightbackground="grey", highlightthickness=1)
    entry_note.place(relx=0.55, rely=0.40, relwidth=0.3, relheight=0.1)


    # Text id etudiant
    label_id_etudiant = tk.Label(note_frame, text="ID", font=("Helvica", 15),bg="white",relief="flat")
    label_id_etudiant.place(relx=0.1, rely=0.55, relwidth=0.3, relheight=0.1)

    # Entry value id etudiant
    entry_id_etudiant = tk.Entry(note_frame , highlightbackground="grey", highlightthickness=1)
    entry_id_etudiant.place(relx=0.55, rely=0.55, relwidth=0.3, relheight=0.1)

    # Bouton ajouter
    btn_ajouter = tk.Button(note_frame,text="Ajouter", command=lambda:ajout(nw,entry_id_etudiant,entry_annee,entry_matiere,entry_note))
    btn_ajouter.place(relx=0.1, rely=0.70, relwidth=0.35, relheight=0.1)

    # Bouton modifier
    btn_modifier = tk.Button(note_frame,text="Modifier", command=lambda:modifier(nw,entry_id_etudiant,entry_annee,entry_matiere,entry_note))
    btn_modifier.place(relx=0.55, rely=0.70, relwidth=0.35, relheight=0.1)

    # Bouton supprimer
    btn_modifier = tk.Button(note_frame,text="Supprimer",command=lambda:supprimer(nw,entry_id_etudiant,entry_annee,entry_matiere))
    btn_modifier.place(relx=0.325, rely=0.85, relwidth=0.35, relheight=0.1)

    # Frame pour ajouter l'étudiant
    tab_etud= tk.Frame(nw,bg="white" , highlightbackground="grey", highlightthickness=1)
    tab_etud.place(relx=3.05,rely=0.05,relheight=0.9,relwidth=0.6)

    btn_return = tk.Button(nw,text="retour",command=lambda:nw.destroy())
    btn_return.place(relx=0.775,rely=0.925,relheight=0.05,relwidth=0.1)

