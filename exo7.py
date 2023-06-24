import math
a=float(input("entrez la valeure de a :"))
b=float(input("entrez la valeure de b :"))
c=float(input("entrez la valeure de c :"))
deltat= b**2-4*a*c
if (deltat==0):
    x0=(-b)/(2*a)
    print("une solution réelle ","x0","=",format(x0,".1f"))
elif (deltat>0):
    x1=(-b-math.sqrt(deltat)) /(2*a)
    x2=(-b+math.sqrt(deltat)) /(2*a)
    print("deux solutions réelles ","x1","=",format(x1,".1f") ,"et","x2,","=",format(x2,".1f")) 
elif (deltat<0):
    
    print("aucune solution réelle possible")
else:
    print("merci de réessayer")    

    #programme qui trouve le solutions d'un polynome du second degré

