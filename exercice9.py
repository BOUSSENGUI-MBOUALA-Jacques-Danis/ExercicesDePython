nom=input("quel est votre nom?")
prenom=input("quel est votre prenom?")
taille=int(input("quelle est votre taille?"))
poids=int(input("quelle est votre masse?"))
if(poids<18.4):
    print("la personne nommée",nom , prenom,"est une personne maigre")
elif(poids>=18.5 and poids<=24.9):
    print("la personne nommée",nom , prenom,"est une personne dont la corpulance est normale")
elif(poids>=25 and poids<=29.9):
    print("la personne nommée",nom , prenom,"est une personne en surpoids")
elif(poids>=30 and poids<=34.9): 
    print("la personne nommée",nom , prenom,"est une personne en obésité modérée")
elif(poids>=35 and poids<=39.9):
    print("la personne nommée",nom , prenom,"est une personne en obésité sévere")  
else:
    print("la personne nommée",nom , prenom,"est une personne en obésité morbide")    

