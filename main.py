"""
coding: utf-8 

Ce programme est un automate qui vérifie si une phrase est correcte ou non.

Author: Evan

Date: 24/09/2024

Monsieur MOREL m'a dit : "de ne pas séparer les fonctions de l'automate et de les mettre dans le même fichier car c'est comme ça qu'on fait."
"""

import re

dico = {}  # Création du dictionnaire à partir d'un fichier texte.
with open("dico.txt", "r", encoding="utf-8") as file:
    for line in file:
        key, value = line.strip().split(" ")
        dico[key.strip()] = int(value.strip())


a = "le joli chat, mange martin."


table_de_transition = [
    [1, 8, 8, 8, 4, 8],
    [8, 1, 2, 8, 8, 8],
    [8, 2, 8, 3, 8, 8],
    [5, 8, 8, 8, 7, 9],
    [8, 8, 8, 3, 8, 8],
    [8, 5, 6, 8, 8, 8],
    [8, 6, 8, 8, 8, 9],
    [8, 8, 8, 8, 8, 9],
]


def automate(phrase):
    """Ce programme est un automate qui vérifie si une phrase est correcte ou non.

    Args:
        phrase (str): La phrase à vérifier.

    Returns:
        Boolean: True si la phrase est correcte, False sinon.
    """
    
    etat = 0

    phrase = re.findall(r"\w+|[^\w\s]", phrase)  # On sépare les mots de la phrase en utilisant les espaces et les ponctuations.

    for mot in phrase:
        if dico[mot] == 6:
            pass
        else:
            etat = table_de_transition[etat][dico[mot]]
            if etat == 8:
                return False
    return etat == 9


print(automate(a))
