"""Écrire une fonction maximum permet dafficher le plus grand de trois nombres entrés 
au clavier     TD2"""



def max_de_deux(x,y):
    if x>y:
      return x
    return y

def maximum(b,y,z):
   return max_de_deux(b,max_de_deux(y,z))
   
print("le maximum est ",maximum(int(input("saisir le premier nombre :")),
              int(input("saisir le deuxième nombre :")),
              int(input("saisir le troisième nombre :"))))
