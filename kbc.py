def optionselect():
 a=int(input("which option:"))
 return a 

opt=int(input("press 1 to start the game:"))
if opt==1:
 print("question 1: whats your pm name ? ")
 print("1- me ")
 print("2- you ")
 print("3-barrak obama" )
 print("4-narendra modi")
 option = optionselect()

 if option ==4:
     print("sahi jawab")
     print("you won prize money of =50000")
 
     print("next question")  
     print("question 2: whats your cm name ? ")
     print("1- me ")
     print(" 2- you ")
     print("3-yogiji" )
     print("4-narendra modi")
     
     option = optionselect()

     if option ==3:
      print("sahi jawab")
      print("you won prize money of =100000")
     else:
          print("galat jawab")
          print("you lost the game.")
      
 else:
      print("galat jawab")
      print("you lost the game.")
    
else:
  print("game not started")