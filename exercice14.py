"""Écrire une fonction en Python spécifiée comme suit : Paramètres un entier h, un entier 
m, un entier s. Valeur renvoyée le temps en secondes correspondant au cumul de h 
heures, m minutes et s secondes  TD2"""


def le_temps(h,m,s):
    h=int(input("enter la valeur de l'heure h :"))
    m=int(input("enter la valeur des minutes m :"))
    s=int(input("enter la valeur des seconde s :"))
    resultat = (h*3600) + (m*60) + s
    print(resultat,"s")

le_temps("x","y","z")


