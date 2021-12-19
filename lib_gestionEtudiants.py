# -*- coding: utf-8 -*-
from lib_commun import ouverture_fichier_csv, ecriture_fichier_csv


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


def modificationEtudiant(id_, prenom, nom, genre, email, classe1):
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
    data[int(id_)].insert(1, genre)
    if nom == str():
        nom == data[int(id_)][2]
        print('Nom non modifié')
    data[int(id_)].pop(2)
    data[int(id_)].insert(2, nom)
    if prenom == str():
        prenom == data[int(id_)][3]
        print('Prénom Non modifié')
    data[int(id_)].pop(3)
    data[int(id_)].insert(3, prenom)
    if email == str():
        email == (data[int(id_)][4])
        print('Email non modifié')
    data[int(id_)].pop(4)
    data[int(id_)].insert(4, email)
    if classe1 == str():
        classe1 == data[int(id_)][5]
        print('Classe Non modifié')
    data[int(id_)].pop(5)
    data[int(id_)].insert(5, classe1)
    print("modificationEtudiant")
    ecriture_fichier_csv(data, "etudiants.csv")
    return


def SupressionNoteEtudiant(etudiant):
    data = ouverture_fichier_csv("notes.csv")
    list_note_suppr = list()
    i = 0
    for note in data:
        if note[2] == etudiant:
            print(note)
            list_note_suppr.append(note)

            del data[i]
        i += 1
    # Remet tous les IDs et ID_ETUDIANTs de note dans l'ordres

    k = 0
    for l in range(2, len(data)):
        k += 1
        data[l - 1][2] = k
        data[l-1][0] = l - 2
        if int(data[l][2]) <  int(data[l-1][2]):
            k = 1
    data_mat = ouverture_fichier_csv("matieres.csv")
    data_stud = ouverture_fichier_csv("etudiants.csv")


    stud_id_lenght = len(data_stud)-1



    for mat in data_mat:
        indexmat = 1

        for i in range(1,len(data)):

            if data[i][3] == mat:
                data[i][3] = mat
            indexmat += 1

        for i in range(indexmat,stud_id_lenght):
            data[i][2] = i+1

    data[0][0] = "ID"
    data[0][2] = "ID_ETUDIANT"

    ecriture_fichier_csv(data, "notes.csv")
    #print(list_note_suppr)
    return list_note_suppr

def suppressionEtudiant(etudiant):
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

    message = SupressionNoteEtudiant(etudiant[0])

    for k in id_data:
        if etudiant == str(k):
            data.pop(int(etudiant))
            find = True

            # Remet tous les IDs dans l'ordre
            i = 0

            for etudiant in data:
                etudiant[0] = i
                i += 1
            data[0][0] = "ID"

            ecriture_fichier_csv(data, "etudiants.csv")
            print("Cet étudiant est supprimé")
            return message

    if find == True:
        ecriture_fichier_csv(data, "etudiants.csv")
    else:
        print("Aucun étudiant n'a été trouvé")

