import random

j = 11
q = 12
k = 13
a = 14

carta = [2,3,4,5,6,7,8,9,10, j, q, k, a]

point_player = random.randint(6, 16)
point_enemigo = random.choice(carta) + random.choice(carta)
 

if point_enemigo > 21:
    point_enemigo = 20


mas_cartas = input("quieres mas cartas ? (s/n)")
print(point_player)
if mas_cartas == "s":
    mas_puntos = random.choice(carta)
    point_player += mas_puntos
    print(mas_puntos)
    print(point_player)

elif mas_cartas == "n" and point_player > point_enemigo and point_player <= 21:
    print("ganaste")

else:
    print("perdiste")

if point_player > 21:
   print("perdiste")

elif point_player > point_enemigo or point_player == 21:
    print("ganaste")    

elif point_player == point_enemigo:
    print("es un empate puntos jugador {} y  puntos enemigo {}".format(point_player, point_enemigo))




print("puntos enemigos {}".format(point_enemigo))


