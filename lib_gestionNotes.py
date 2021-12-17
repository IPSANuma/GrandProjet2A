# -*- coding: utf-8 -*-
from lib_commun import ouverture_fichier_csv, ecriture_fichier_csv


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


def suppressionNote(id_etudiant, annee, matiere):
    """
    Cette fonction a pour objectif
    IN :
    OUT :
    """
    p = 0
    id_data = []
    data = ouverture_fichier_csv("notes.csv")
    id_ = 1
    for j in range(1, len(data)):
        id_data.append(int(data[j][0]))
    for k in id_data:
        while id_ == k:
            id_ += 1
        if data[id_][1] == annee:
            p = p + 1
            if data[id_][3] == matiere:
                p = p + 1
        if p == int(2):
            data.pop(int(id_))
    ecriture_fichier_csv(data, "notes.csv")
    data.clear()
    return
