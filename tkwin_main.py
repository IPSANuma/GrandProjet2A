import tkinter as tk
from tkwin_etud import run_win_etud
from tkwin_notes import run_win_notes


#Configuration de l'app
app = tk.Tk()
app.title("Accueil")
app.geometry("600x300")

#Configuration de la Frame affichant le titre et les copyright
frame = tk.Frame(app, bg="white")
titre = tk.Label(frame, text="Accueil", font=("Helvica", 44),anchor="center",relief="ridge")
copyright = tk.Label(frame, text="Samy Kerouani, Youenn Geenen-Dornic, Numa Cornec", font=("Helvica", 8),anchor="e")
copyright.place(relx=0,rely=0.95,relwidth=1, relheight=0.05)
frame.place(relwidth=1, relheight=1)
titre.place(relwidth=1, relheight= 0.2)


#Bouton ouvrant la fenètre Gestion étudiant
btn_etud = tk.Button(frame, text="Gestion etudiants", font=("Helvica", 12), bg="light grey",relief="raised",
                     command=lambda:(run_win_etud(app)))
#Bouton ouvrant la fenètre Gestion notes
btn_note = tk.Button(frame, text="Gestion notes", font=("Helvica", 12), bg="light grey",relief="raised",
                     command=lambda:(run_win_notes(app)))
#Bouton quitter
btn_quit = tk.Button(frame, text="Quitter", font=("Helvica", 12), bg="light grey",relief="raised",
                     command=lambda:quit())


#Bouton placement des boutons
btn_etud.place(relx=0.15, rely=0.4, relwidth=0.25, relheight=0.12)
btn_note.place(relx=0.55, rely=0.4, relwidth=0.25, relheight=0.12)
btn_quit.place(relx=0.35, rely=0.65, relwidth=0.25, relheight=0.12)

#app.resizable(False,False)
app.mainloop()