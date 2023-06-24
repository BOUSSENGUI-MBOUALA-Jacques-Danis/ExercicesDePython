moyenne=int(input("entrez votre moyenne?:"));

if(moyenne==0):
    print("vous êtes null")
elif(moyenne<=5):
    print("midiocre")
elif(moyenne>6 and moyenne<10) :       
      print("inssuffisant")
elif(moyenne>=10 and moyenne<=11):
      print("passable")
elif(moyenne>=12 and moyenne<14):
      print("assez bien") 
elif(moyenne>=14 and moyenne<16):
      print("bien")
elif(moyenne>=16 and moyenne<18):
  print("très bien")
elif (moyenne>=18 and moyenne<=20):
     print("excellent")    
else:
      print("erreur! moyenne incorrecte recommencez!")
                         
    