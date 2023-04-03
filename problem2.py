angry = True
bored = True
hungry = False
tired = False

if angry and hungry and bored: 
  print("eat the Triceratops")
elif tired and hungry: 
  print("eat the Iguanadon")
elif hungry and bored:
  print("eat the Stegasaurus")
elif tired: 
  print("go to sleep")
elif angry and bored: 
  print("fight with the Velociraptor")
elif angry or bored: 
  print("roars")
else:
  print("gives a toothy smile")