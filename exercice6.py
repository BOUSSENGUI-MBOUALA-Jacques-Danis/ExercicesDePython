"""nbr=int(input("veuillez entrer un nombre "))
res=nbr**0.5
print("la racine carré de",nbr,"est",round(res))   #round(nbr) permet de d'arrondire le nbr

on peut aussi utiliser la fonction pow(nbr,exposant) pour calculer la racine carré"""


nbr=float(input("veuillez entrer un nombre :"))
res=pow(nbr,0.5)
print(format(res,".1f"))   #POUR la racine cubique il suffit de mettre 1/3 en exposant dans pow()
