# -*- coding: utf-8 -*-
from lib_commun import ouverture_fichier_csv, ecriture_fichier_csv

def gestionNotes():
    def ajoutNote(id_etudiant, annee, matiere, note):
        """
        Cette fonction a pour objectif
        IN :
        OUT :
        """
        nv_data = []
        id_data = []
        data = ouverture_fichier_csv("notes.csv")
        id_ = 1
        for j in range(1, len(data)):
            id_data.append(int(data[j][0]))
        for k in id_data:
            while id_ == k:
                id_ += 1
        '''for i in range(1, len(data)):
            if data[i][4] == email:
                print("Cet étudiant existe déjà")
                nv_data.clear()
                return'''
        nv_data.insert(0, id_)
        nv_data.insert(1, str(annee))
        nv_data.insert(2, id_etudiant)
        nv_data.insert(3, str(matiere))
        nv_data.insert(4, str(note))
        data.insert(id_ + 1, nv_data)
        ecriture_fichier_csv(data, "notes.csv")
        nv_data.clear()
        return


    def modificationNote(id_etudiant, annee, matiere, note):
        """
        Cette fonction a pour objectif
        IN :
        OUT :
        """
        data = ouverture_fichier_csv("notes.csv")
        for i in range(1, len(data)):
            if data[i][1] == annee:
                if data[i][2] == id_etudiant:
                    if data[i][3] == matiere:
                        data[i].pop(4)
                        data[i].insert(4, note)
        ecriture_fichier_csv(data, "notes.csv")
        return


    def affichageNote() :
            """
            Cette procédure a pour objectif d'afficher l'ensemble des informations notes des etudiants.
            Soit : ID, Matiere, Note
            IN : aucun paramètre en entrée
            OUT : aucun retour
            """
            ##################################################
            #ouverture et recuperation du contenu du fichier
            ##################################################
            nomfichier = "notes.csv"
            data = ouverture_fichier_csv(nomfichier)



            print("***********************************************************************************************************")
            print("*                                          Gestion Scolaire                                               *")
            print("***********************************************************************************************************")
            print("*   Année Scolaire      *   ID Etudiant           *        Matiere            *         Note              *")
            print("***********************************************************************************************************")

            for i in range(1,len(data)) :
                print("* {:<22}  * {:<20} * {:<30}  *  {:>3}  *" . format(data[i][1],data[i][2], data[i][3], data[i][4]))

            print("***********************************************************************************************************\n")
    while True:
            menu_choix = int(input("Rentrez votre choix ( valeur entre 1-5): \n 1- Ajout note \n 2- Modification note\n 3- Suppression note\n 4- Affichage notes\n 5- Sortie\n\n Reponse :\n"))

            if menu_choix == 1 :
                id_etudiant = input("Saisissez le ID d'etudiant\n->")
                annee = input("Saisissez l'année scolaire\n->")
                matiere = input("Saisissez le matiere\n->")
                note = input("Saisissez le note\n->")
                ajoutNote(id_etudiant,annee,matiere,note)

            if menu_choix == 2 :
                id_etudiant = input("Saisissez le ID d'etudiant\n->")
                annee = input("Saisissez l'année scolaire\n->")
                matiere = input("Saisissez le matiere\n->")
                note = input("Saisissez le note\n->")
                modificationNote(id_etudiant,annee,matiere,note)

            if menu_choix == 3 :
                id_etudiant = input("Saisissez le ID d'etudiant\n->")
                annee = input("Saisissez l'année scolaire\n->")
                matiere = input("Saisissez le matiere\n->")
                suppressionNote(id_etudiant,annee,matiere)

            if menu_choix == 4 :
                affichageNote()
            if menu_choix == 5 :
                break


        ##################################################
        #
    def suppressionNote(*donneesNote):
        """
        Cette fonction a pour objectif
        IN :
        OUT :
        """

        # Ne marche pas encore a continuer voir a refaire

        nomfichier = "notes.csv"
        data = ouverture_fichier_csv(nomfichier)
        supp_note = []
        for i in donneesNote:
            supp_note.append(i)
        print(supp_note)
        i = -1
        copie_data = data
        for note in copie_data:
            del note[0]
            if note == supp_note:
                del data[i]
                print("aaa")
            i += 1

        i = -1
        for note in data:
            note[0] = i
            i += 1
        data[0][0] = "ID"

        print(data)
        ecriture_fichier_csv(data, nomfichier)
        return
    ##################################################

