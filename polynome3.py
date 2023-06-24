import math
a=float(input("entrez la valeure de a associée au degré trois du polynôme :"))
b=float(input("entrez la valeure de b associée au degré deux du polynôme :"))
c=float(input("entrez la valeure de c associée au degré un du polynôme :"))
d=float(input("entrez la valeure de d associée au degré zéro du polynôme :"))

reponse = int(print("le polynôme à t'il une racine evidente? 0 pour non 1 pour oui :"))

racineEvidente=float(input("Entrez la solution evidente :"))
coef2 = reponse*a + b
coef3 = reponse*reponse + reponse*b + c
deltat= coef2**2-4*a*coef3
if (deltat==0):
    x2=(-coef2)/(2*a)
    print("deux solutions réelle ","x2","=",format(x2,".1f"),"x1 = ", reponse)
elif (deltat>0):
    x3=(-coef2-math.sqrt(deltat)) /(2*a)
    x2=(-coef2+math.sqrt(deltat)) /(2*a)
    print("trois solutions réelles ","x3","=",format(x3,".1f") ,"et","x2,","=",format(x2,".1f"),"x1 = ", reponse) 
else :
    (deltat<0)
    print("une solution réelle possible x1 = ",reponse)
  


