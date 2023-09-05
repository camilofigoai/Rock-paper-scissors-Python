import random

options=('piedra','papel','tijera')

computer_wins=0
user_wins=0
rounds=1

print('*'*10)
print('Te doy la bienvenida a piedra, papel y tijera')
print('*'*10)


while True:
  print('*'*10)
  print('ROUND', rounds)
  print('*'*10)
  print('Ganados por el usuario: ', user_wins)
  print('Ganados por el computador: ', computer_wins)
  
  user_option=input("Escribe tu opción: piedra, papel o tijera: ")
  user_option=user_option.lower()

  rounds+=1
  
  if not user_option in options:
    print('Esa no es una opción válida, por favor escribe tu opción')
    continue

  computer_option=random.choice(options)
  
  print('La opción del usuario es: ', user_option)
  print('La opción del computador es: ', computer_option)
  
  if user_option==computer_option:
    print("Empate!")
  elif user_option=="piedra":
    if computer_option=="tijera":
      print("piedra gana a tijera")
      print("Gana el usuario")
      user_wins+=1
    else:
      print("papel gana a piedra")
      print("Gana el computador")
      computer_wins+=1
  elif user_option=="papel":
    if computer_option=="piedra":
      print("papel gana a piedra")
      print("Gana el usuario")
      user_wins+=1
    else:
      print("tijera gana a papel")
      print("Gana el computador")
      computer_wins+=1
  elif user_option=="tijera":
    if computer_option=="papel":
      print("tijera gana a papel")
      print("Gana el usuario")
      user_wins+=1
    else:
      print("piedra gana a tijera")
      print("Gana el computador")
      computer_wins+=1

  if computer_wins==2:
    print('*'*10)
    print('El computador alcanzó dos victorias, el juego terminó')
    print('*'*10)
    break

  if user_wins==2:
    print('*'*10)
    print('El usuario alcanzó dos victorias, el juego terminó')
    print('*'*10)
    break

  