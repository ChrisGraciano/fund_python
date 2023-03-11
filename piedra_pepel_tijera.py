#Creación del Juego: PIEDRA, PAPEL O TIJERA
import random

options = ("piedra", "papel", "tijera") #tupla

computer_wins = 0
user_wins = 0
rounds = 1

while True:
  print("*" * 10)
  print("Round", rounds)
  print("*" * 10)

  print("Victorias de Commputer => ", computer_wins)
  print("Victorias de User => ", user_wins)
  
  user_option = input("Piedra, Papel o Tijera => ")
  user_option = user_option.lower() #Vuelve la respuesta del usuario a minuscula
  
  if not user_option in options: #Valida que la respuesta del user este en la tupla
    print("La opción elegida no es valida")
    continue #Si el usuario pone un valor no valido, se salta lo que sigue y vuelve al inicio
    
  computer_option = random.choice(options) #Selección aleatoria de la tupla
  
  print("User Option =", user_option)
  print("Computer Option =", computer_option)
  
  if user_option == computer_option:
    print("¡Empate!")
  elif user_option == "piedra":
    if computer_option == "tijera":
      print("Piedra gana a Tijera")
      print("User ha ganado")
      user_wins += 1 #Esto suma una unidad al contador cuándo el usuario gana
    else:
      print("Papel gana a Piedra")
      print("Computer ha ganado")
      computer_wins += 1 #Esto suma una unidad al contador cuándo el computador gana
  elif user_option == "papel":
    if computer_option == "piedra":
      print("Papel gana a Piedra")
      print("User ha ganado")
      user_wins += 1 #Esto suma una unidad al contador cuándo el usuario gana
    else:
      print("Tijera gana a Papel")
      print("Computer ha ganado")
      computer_wins += 1 #Esto suma una unidad al contador cuándo el computador gana
  elif user_option == "tijera":
    if computer_option == "papel":
      print("Tijera gana a Papel")
      print("User ha ganado")
      user_wins += 1 #Esto suma una unidad al contador cuándo el usuario gana
    else:
      print("Piedra gana a Tijera")
      print("Computer ha Ganado")
      computer_wins += 1 #Esto suma una unidad al contador cuándo el computador gana

  if computer_wins == 3:
    print("***¡El Gran Ganador es COMPUTER!***")
    break

  if user_wins == 3:
    print("***¡El Gran Ganador es USER!***")
    break
    
  rounds += 1
