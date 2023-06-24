"""Ecrire une fonction NbCMin(pass) qui retourne le nombre de caractères minuscules.
Ecrire une fonction NbCMaj(pass) qui retourne le nombre de caractères majuscules.
Ecrire une fonction NbCAlpha(pass) qui retourne le nombre de caractères non alphabétiques.
Ecrire une fonction LongMaj(pass) retourne la longueur de la plus longue séquence de lettres majuscules.
Ecrire une fonction LongMin(pass) retourne la longueur de la plus longue séquence de lettres minuscules.
Ecrire une fonction Score(pass) qui affiche le score dun mot de passe TD2"""


#fonction qui retourne le nombre de caractere minuscule

def NbCMin(password):

    count = 0
    for caractere in password:
        if caractere.islower():
            count += 1
    return count


#fonction qui retourne le nombre de caractere majuscule


def NbCMaj(password):
    count = 0
    for caractere in password:
        if caractere.isupper():
            count += 1
    return count


#fonction qui retourne le nombre de caractere non alphabetique
def  NbCAlpha(password):
    count = 0
    for caractere in password:
        if not caractere.isalpha():
            count += 1
    return count

#fonction qui retourne la longueur de la plus longue séquence de lettres majuscules

def LongMaj(password):
    max_longueur = 0
    longueur_actuelle = 0

    for caractere in password:
        if caractere.isupper():
            longueur_actuelle += 1
            if longueur_actuelle > max_longueur:
                max_longueur = longueur_actuelle
        else:
            longueur_actuelle = 0

    return max_longueur


#fonction qui retourne la longueur de la plus longue séquence de lettres minuscule

def LongMin(password):
    max_longueur = 0
    longueur_actuelle = 0

    for caractere in password:
        if caractere.islower():
            longueur_actuelle += 1
            if longueur_actuelle > max_longueur:
                max_longueur = longueur_actuelle
        else:
            longueur_actuelle = 0

    return max_longueur




#fonction Score(pass) qui affiche le score dun mot de passe

def Score(password):
    password=input("Enter un mot de pass :")
    nbr_total_C=len(password)   #pour avoir le nombre total de caractère
    nombreLettreMajuscule = NbCMaj(password)
    nombreLettreminuscule= NbCMin(password)
    nombreDecaractreNonAlph= NbCAlpha(password)
    sec_long_Min=LongMin(password)
    sec_long_Maj= LongMaj(password)
    penalite= sec_long_Min*2 + sec_long_Maj*3
    bonusSansPenalite= (nbr_total_C*4 )+ (nbr_total_C - nombreLettreMajuscule )*2 + ( nbr_total_C - nombreLettreminuscule)*3 +  nombreDecaractreNonAlph *5
    score=bonusSansPenalite - penalite +2
    if score <20 :
        print("mot de passe très faible car score ","=",score)
    elif(score>20 and score<40):
        print("mot de passe faible car score ","=",score)
    elif(score>40 and score<80):
        print("mot de passe est fort car score ","=",score)
    else:
        print("mot de passe très fort car score","=",score)


Score("chainess")