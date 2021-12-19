# -*- coding: utf-8 -*-
from lib_commun import ouverture_fichier_csv, ecriture_fichier_csv

def gestionEtudiants():
    def ajoutEtudiant(prenom, nom, genre, email, classe1):
        """
        Cette fonction a pour objectif
        IN : [prenom, nom, genre, email, groupe], nom_fichier
        OUT : retour nouvelle ligne + affectation ID
        """
        nv_data = []
        id_data = []
        data = ouverture_fichier_csv("etudiants.csv")
        id_etudiant = 1
        for j in range(1, len(data)):
            id_data.append(int(data[j][0]))
        for k in id_data:
            while id_etudiant == k:
                id_etudiant += 1
        for i in range(1, len(data)):
            if data[i][4] == email:
                print("Cet étudiant existe déjà")
                nv_data.clear()
                return
        nv_data.insert(0, id_etudiant)
        nv_data.insert(1, str(genre))
        nv_data.insert(2, str(nom))
        nv_data.insert(3, str(prenom))
        nv_data.insert(4, str(email))
        nv_data.insert(5, str(classe1))
        data.insert(id_etudiant, nv_data)
        ecriture_fichier_csv(data, "etudiants.csv")
        nv_data.clear()
        return

    def modificationEtudiant(id_,prenom, nom, genre, email, classe1) :
        """
        Cette fonction a pour objectif
        IN :
        OUT :
        """
        data = ouverture_fichier_csv("etudiants.csv")
        if genre == str():
            genre == data[int(id_)][1]
            print('Genre Non modifié')
        data[int(id_)].pop(1)
        data[int(id_)].insert(1,genre)
        if nom == str():
            nom == data[int(id_)][2]
            print('Nom non modifié')
        data[int(id_)].pop(2)
        data[int(id_)].insert(2,nom)
        if prenom  == str():
            prenom == data[int(id_)][3]
            print('Prénom Non modifié')
        data[int(id_)].pop(3)
        data[int(id_)].insert(3,prenom)
        if email == str():
            email == (data[int(id_)][4])
            print('Email non modifié')
        data[int(id_)].pop(4)
        data[int(id_)].insert(4,email)
        if classe1 == str():
            classe1 == data[int(id_)][5]
            print('Classe Non modifié')
        data[int(id_)].pop(5)
        data[int(id_)].insert(5,classe1)
        print("modificationEtudiant")
        ecriture_fichier_csv(data, "etudiants.csv")
        return

    def suppressionEtudiant(etudiant) :
        """
        Cette fonction a pour objectif
        IN :
        OUT :
        """
        id_data = []
        data = ouverture_fichier_csv("etudiants.csv")
        id_etudiant = 1
        for j in range(1, len(data)):
            id_data.append(int(data[j][0]))
        find = False
        for k in id_data:
            if etudiant == str(k):
                print("Cet étudiant est supprimé")
                data.pop(int(etudiant))
                find = True

                #Remet tous les IDs dans l'ordre
                i=0

                for etudiant in data:
                    etudiant[0] = i
                    i += 1
                data[0][0] = "ID"

                ecriture_fichier_csv(data, "etudiants.csv")

        if find == True:
            ecriture_fichier_csv(data, "etudiants.csv")
        else:
            print("Aucun étudiant n'a été trouvé")

        return
    def affichageEtudiant() :
            """
            Cette procédure a pour objectif d'afficher l'ensemble des informations administratives des etudiants.
            Soit : ID, prenom, nom, genre, email, groupe
            IN : aucun paramètre en entrée
            OUT : aucun retour
            """
            ##################################################
            #ouverture et recuperation du contenu du fichier
            ##################################################
            nomfichier = "etudiants.csv"
            data = ouverture_fichier_csv(nomfichier)



            print("***********************************************************************************************************")
            print("*                                          Gestion Scolaire                                               *")
            print("***********************************************************************************************************")
            print("*  ID   *   Genre      *     Prenom          *   Nom              * Email adresse          *   Groupe      ")
            print("***********************************************************************************************************")

            for i in range(1,len(data)) :
                print("* {:<8}  * {:<8}  * {:<15}  *  {:<15}  *  {:<25} * {:>5} *" . format(data[i][0], data[i][1], data[i][2], data[i][3], data[i][4], data[i][5]))

            print("***********************************************************************************************************\n")


    while True:
            menu_choix = int(input("Rentrez votre choix ( valeur entre 1-5): \n 1- Ajout etudiant \n 2- Modification etudiant\n 3- Suppression etudiant\n 4- Affichage etudiant\n 5- Sortie\n\n Reponse :\n"))

            if menu_choix == 1 :
                prenom = input("Saisissez le prenom d'etudiant\n->")
                nom = input("Saisissez le nom d'etudiant\n->")
                genre = input("Saisissez le genre d'etudiant\n->")
                email = input("Saisissez le email d'etudiant\n->")
                classe1 = input("Saisissez la classe d'étudiant\n->")
                ajoutEtudiant(prenom,nom,genre,email,classe1)

            if menu_choix == 2 :
                id_ = input("Saisissez ID d'etudiant\n->")
                prenom = input("Saisissez le prenom d'etudiant\n->")
                nom = input("Saisissez le nom d'etudiant\n->")
                genre = input("Saisissez le genre d'etudiant\n->")
                email = input("Saisissez le email d'etudiant\n->")
                classe1 = input("Saisissez la classe d'étudiant\n->")
                modificationEtudiant(id_,prenom,nom,genre,email,classe1)

            if menu_choix == 3 :
                id_ = input("Saisissez ID d'etudiant\n->")
                suppressionEtudiant(id_)
            if menu_choix == 4 :
                affichageEtudiant()

            if menu_choix == 5 :
                break