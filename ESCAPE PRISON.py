import random



titulo = "PRISON ESCAPE"
print("\n" + titulo + "\n" + "-" * len(titulo))

print("YO Y MI AMIGO LOGRAMOS ESCAPAR DE LA CERDA")
print("LOGRAMOS LLEGAR AL PATIO DE LA PRISION, OH NO UN GUARDIA DECTETO NUESTRA PRECENCIA CORRE AMIGO CORRE")
print("\n")
print("OH NO ACABAN DE ATRAPAR A MI AMIGO  \n "
      "SOLO ES CUESTION DE TIEMPO PARA QUE ME ATRAPEN DEBO SALIR DE LA PRISION ")
print("\n")
print("HAY UNA PUERTA QUE CONDUCE A LA ZONA DE DESCARGA PUEDO INTENTAR SALIR POR HAY \n"
      " Y HAY OTRA PUERTA EN EL PISO AL PARECER CONDUCE A LAS ALCANTARILLAS PUEDO BUSCAR UNA SALIDA POR HAY ")
print("\n")
eleccion = input("ESCOGE UNA OPCION\n"
                 "A - PARA VOLVER ENTRAR A PRISION Y TRATAR DE ESCAPAR POR ZONA DE DESCARGA \n   "
                 "B - PARA ELEGIR BUSCAR UNA SALIDA EN LAS ALCANTARILLA   ")
print("\n")
if eleccion == "A":
    print("EH ENTRADO A LA ZONA DE DESCARGA ")
    print("OH NO ME ACABA DE VER LOS GUARDIAS")
    print("\n")
    segunda_eleccion = input("TIENES DOS OPCIONES ELIGE CON GRAN DETERMINACION\n"
                             "A - SI ELIGES A PODRAS ENTREGARTE Y VIVIRAS  \n"
                             "B - SI ELIGES B TRATARAS DE ESCAPAR DE LOS GUARDIAS ESTO INTENTARAN MATARTE \n"
                             " SI LO LOGRAN SE ACABA LA HISTORIA Y TODO SERA POR NADA  ")
    print("\n")

    if segunda_eleccion == "A":
        print("SALVASTE TU VIDA PERO ESTARAS ENCERRADO POR SIEMPRE ")
    elif segunda_eleccion == 'B':
        print("EN HORA BUENA LOGRASTE ESCAPAR ILESO DIRIGETE A LA PUERTA.  ")
        print("OH NO LA PUERTA TIENE CLAVE DEBO COLOCAR UN NUMERO 1 DE 2 SI FALLO SONARA LA ALARMA"
              "Y VOY A MORIR")
        contrasena = random.randint(1, 2)
        tercera_eleccion = int(input("elige un numero del 1 a 2  "))
        if tercera_eleccion == contrasena:
            print("FELICIDADES LOGRASTE SALIR")
        else:
            print("TE DESCUBRIERON ESTAS MUERTO. EL NUMERO ERA {}".format(contrasena))

if eleccion == "B":
    print("ENTRASTE A LA ALCANTARILLA, OH QUE MAL OLOR HAY AQUI. PERO NO ME PUEDO RENDIR")
    print("EH ENCONTRADO UN TUVO DE METAL ME PODRIA AYUDAR PERO PESA MUCHO ME RESTRASARIA ")
    opcion = input("[A] PARA ESCOGER EL METAL/B] PARA NO COGERLO   ")

    tubo_de_metal = False

    if opcion == "A":
        tubo_de_metal = True
        print("AS COGIDO EL TUVO DE METAL ")
    elif opcion == "B":
        print("NO COGISTE EL TUBO DE METAL")

    print("EH ENCONTRADO UNA PUERTA MUY EXTRAÑA TIENE UN TECLADO EN LA ME DIJE QUE ELIJA UN NUMERO PARA ABRISE  ")
    puerta_extrana = input("DESEAS ABRIR LA PUERTA? ([S] SI/[N] NO)  ")
    contrasena_extrana = random.randint(1, 100)
    if puerta_extrana == "S":
        abriendo_puerta = int(input('introduce la contrasena '))
        if abriendo_puerta == contrasena_extrana:
            print("OH NO ERA UNA TRAMPA ESTAS MUERTO")
            exit()
        if puerta_extrana != contrasena_extrana:
            print("INCORRECTA LA CLAVE ERA {} SE A BLOQUEADO LA PUERTA YA NO SE PUEDE ABRIR".format(contrasena_extrana))
            print("MEJOR SEGURI MI CAMINO")
            barrotes = input("QUE BIEN EH ENCONTRADO UNOS BARROTES MI MEJOR OPCION ES TRATAR DE ROMPERLO \n"
                             " [S] PARA ROMPERLO\n"
                             " [N] PARA NO)")
            if barrotes == "S" and tubo_de_metal == True:
                print("FELICIDADES PASASTE EL JUEGO. JUEGO TERMINADO")
            elif barrotes == "S" and tubo_de_metal == False:
                print("NO PUEDES ABRIR LA PUERTA NO TIENES EL TUVO DE METAL TE ENCONTRAN LOS GUARDIAS ESTAS MUERTO")
            elif barrotes == "N" and tubo_de_metal == True:
                print("TE ENCONTRAN LOS GUARDIAS ESTAS MUERTO")
            elif barrotes == "N":
                print("TE ENCONTRAN LOS GUARDIAS ESTAS MUERTO")

    if puerta_extrana == "N":
        print("MEJOR SEGUIRE MI CAMINO")
        barrotes = input("QUE BIEN EH ENCONTRADO UNOS BARROTES MI MEJOR OPCION ES TRATAR DE ROMPERLO \n"
              " [S] PARA ROMPERLO\n"
              " [N] PARA NO)")
        if barrotes == "S" and tubo_de_metal == True:
            print("FELICIDADES PASASTE EL JUEGO. JUEGO TERMINADO")
        elif barrotes == "S" and tubo_de_metal == False:
            print("NO PUEDES ABRIR LA PUERTA NO TIENES EL TUVO DE METAL TE ENCONTRAN LOS GUARDIAS ESTAS MUERTO")
        elif barrotes == "N" and tubo_de_metal == True:
            print("TE ENCONTRAN LOS GUARDIAS ESTAS MUERTO")
        elif barrotes == "N":
            print("TE ENCONTRAN LOS GUARDIAS ESTAS MUERTO")


else:
    print("elegiste mal")
    exit()