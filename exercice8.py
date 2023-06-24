forme=input("triangle,carré,rectangle; quelle est la forme de votre terrin parmi les trois?")
if forme =="triangle":
    h=int(input("quelle est sa hauteure?"))
    b=int(input("quelle est sa base?"))
    prix=int(input("quelle est le prix du metre carré?"))
    superficie = (b*h)/2
    prix= prix*superficie
    print("le prix de vente est de:",str(prix),"FCFA","avec une superficie de:",superficie,"m2")
elif forme == "carré":
    c=int(input("quelle est la longuere du côté?"))
    prix=int(input("quelle est le prix du metre carré?"))
    c=c*c
    prix=c*prix
    print("le prix de vente est de:",str(prix),"FCFA","avec une superficie de:",c,"m2")
elif forme == "rectangle":
     long =int(input("quelle est sa longuere?"))
     larg =int(input("quelle est sa largeure?"))
     prix=int(input("quelle est le prix du metre carré?"))
     aire=long*larg
     prix=prix*aire
     print("le prix de vente est de:",str(prix),"FCFA","avec une superficie de:",aire,"m2")
else :
    print("erreur! rspectez la syntaxe et les trois forme géometrique")



