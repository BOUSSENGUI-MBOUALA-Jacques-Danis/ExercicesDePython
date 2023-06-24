def  compteMots(phrase):
    phrase=input("veuillez écrire une phrase :")
    mots = phrase.split()  # Divise la phrase en une liste de mots en utilisant l'espace comme séparateur
    nombre_mots = len(mots)  # Compte le nombre de mots dans la liste
    print("le nombre de mot est de: ",nombre_mots)

compteMots("phrase")


"""TD2"""