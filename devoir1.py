moyenne=float(input("entrez votre moyenne?:"))

while moyenne<0:
     print("moyenne non valide")
     break

if(moyenne==0):
    print("vous êtes null")
elif(moyenne>=1 and moyenne<=5):
    print("midiocre")
elif(moyenne>=6 and moyenne<=8) :       
      print("faible")
elif(moyenne==9):
      print("insuffisant")
elif(moyenne>=10 and moyenne<=11):
      print("passable") 
elif(moyenne>=12 and moyenne<=13):
      print("assez bien")
elif(moyenne>=14 and moyenne<=16):
  print("bien")
elif (moyenne>=17 and moyenne<19):
     print("très bien")  
elif(moyenne>=19 and moyenne<=20):
     print("excellent")      
else:
    print("erreur! moyenne incorrecte recommencez!")
                         
    