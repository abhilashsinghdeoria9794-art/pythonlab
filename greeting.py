import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
hr =int( time.strftime('%H'))
mn =int( time.strftime('%M'))
sc = int(time.strftime('%S'))
name=input("enter your name:")
if(12>hr>=00 and mn>=00 and sc>=00):
    print("good morning")
elif(18>hr>=12 and mn>=00 and sc>=00):
    print("good afternoon")
elif(20>hr>=18 and mn>=00 and sc>=00):
    print("good evening",name)
elif(hr>=20 and mn>=00 and sc>=00):
    print("good night")

#no need to worry about minutes and second just verify hours you will get your solution