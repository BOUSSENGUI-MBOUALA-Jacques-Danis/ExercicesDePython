""" Écrire une fonction cube qui retourne le cube de son argument.
 Écrire une fonction volumeSphere qui calcule le volume dune sphère de 
rayon R fourni en argument et qui utilise la fonction cube.
Tester la fonction volumeSphere par un appel dans le programme principal.
Rappel : Le volume de lespace délimité par une sphère (on parle alors du volume de 
la boule) est égal à 4/3 multiplié par π et par son rayon R au cube.  TD2"""

def cube(nbr):
    nbr=float(input("entrez la valeur du rayon :"))
    cubes=(nbr*nbr*nbr)
    return cubes



def volumeSphere(r):
    r=cube("a")
    volume=((4*3.14)*r)/3
    print("le volume est de:",round(volume),"m3") 

volumeSphere("c")


