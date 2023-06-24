nbr1=int(input("veuillez entrer un nombre :"))
nbr2=int(input("veuillez entrer un autre nombre :"))
nbr3=int(input("veuillez entrer un dernier nombre :"))
nombre=[nbr1,nbr2,nbr3]
max_valeure = max(nombre)
min_valeure = min(nombre)
print('la valeure maximale est:', max_valeure, " qui a l'indice:", nombre.index(max_valeure))
print('et la valeure manimale est:', min_valeure, " qui a l'indice:", nombre.index(min_valeure))

#AUTRE METHODE
"""""
nbr1=int(input("veuillez entrer un nombre "))
nbr2=int(input("veuillez entrer un autre nombre "))
nbr3=int(input("veuillez entrer un dernier nombre "))
nombre=[nbr1,nbr2,nbr3]

max_value = 0
min_valeure=0

for num in nombre:
    if ( num > max_value):
        max_value = num
print('valeure maximale:', max_value) """

