


def ronda_f():
    global ronda
    ronda+= 1 
    print("-._.--._.--._.--._.--._.--._.--._.-")
    print("   +++  Comienza la ronda "+ str(ronda)+"  +++")
    for _ in range(2):
        turno_f()
        if(ganado):
            break
       
        
    

def turno_f():
    global jugador, turno
    print("------------------------------------")
    print("  ¡Empieza el turno "+ str(turno) +"!  |  ¡Jugador "+ str(jugador) +" es tu turno!")
    input_cdn()
    if(ganado):
        jugador = jugador
    else:
        if(jugador>1):
            jugador = 1
        else:
            jugador += 1
    turno += 1
    

def pnt_tablero():
    global valores
    tablero = [
        ["  ", "___", "   ", "___", "   ", "___", "   "],
        ["| ", " "+str(valores[0]) +" ", " | ", " "+str(valores[1]) +" ", " | ", " "+str(valores[2]) +" ", " | "],
        ["  ", "___", "   ", "___", "   ", "___", "   "],
        ["| ", " "+str(valores[3]) +" ", " | ", " "+str(valores[4]) +" ", " | ", " "+str(valores[5]) +" ", " | "],
        ["  ", "___", "   ", "___", "   ", "___", "   "],
        ["| ", " "+str(valores[6]) +" ", " | ", " "+str(valores[7]) +" ", " | ", " "+str(valores[8]) +" ", " | "],
        ["  ", "___", "   ", "___", "   ", "___", "   "],
    ]
    
    for row in tablero:
        
        for i in range(7):
            
            print(row[i], end="")
            
        print("")
        
def input_cdn():
    global valores
    cas = input("Inserte casilla:");
    res= [int(s) for s in cas.split() if s.isdigit()]
    res = res[0] - 1
    
    if(res>9): 
        print("""Las casillas correctas son:
                1 | 2 | 3
                --|---|--
                4 | 5 | 6
                --|---|--
                7 | 8 | 9
        """)
        print("Vulelva a intentar profavor")
        input_cdn()
        
    casilla = valores[res]
    if(casilla!=" "):
        print("Esa casilla no está diponible")
        print("Vulelva a intentar profavor")
        input_cdn()
    else:
        if(jugador==1):
            valores[res] = "X"
        else:
            valores[res] = "O"
            
        validar()
    pnt_tablero()


def validar():
    global ganado
    elemento =""
    
    if(jugador==1):
        elemento = "X"
    else: 
        elemento = "O"
    # Verificar las reglas
    reglas = [
        valores[0] == valores[1] == valores[2] == elemento,
        valores[3] == valores[4] == valores[5] == elemento,
        valores[6] == valores[7] == valores[8] == elemento,
        valores[0] == valores[4] == valores[8] == elemento,
        valores[0] == valores[3] == valores[6] == elemento,
        valores[1] == valores[4] == valores[8] == elemento,
        valores[2] == valores[4] == valores[6] == elemento,
        valores[2] == valores[5] == valores[8] == elemento
    ]
    if any(reglas):
        print("Ha ganado Jugador "+str(jugador)+"!")
        ganado = True
        
    else:
        print("Ninguna de las reglas se cumple.")

        
    

if __name__ == "__main__":
    print("""
    _____ _     _             
    / ____| |   (_)            
    | |    | |__  _ _ __   __ _ 
    | |    | '_ \| | '_ \ / _` |
    | |____| | | | | | | | (_| |
    \_____|_| |_|_|_| |_|\__, |
                        __/ |
                        |___/ 
    Bienvenido al Juego del Gato!
    El tablero se verá así:
    1 | 2 | 3
    --|---|--
    4 | 5 | 6
    --|---|--
    7 | 8 | 9

    Para jugar, simplemente ingresa el número de la casilla en la que quieres colocar tu ficha.
    El jugador 1 es 'X' y el jugador 2 es 'O'.
    ¡Que empiece la diversión!
    """)
    valores = [" "," "," "," "," "," "," "," "," "]
    ganado = False
    jugador = 1 #Jugador 1 o 2
    ronda = 0 # La ronda acaba cuando el jugador 2 termina su turno
    turno = 1 # Un turno es la participación de un jugador (input)
    c_disponibles = 9
    
    while c_disponibles != 0 :
        
        if(ganado):
            break
        ronda_f()
        c_disponibles -=1
        
    if(ganado):
        print("¡Jugador "+str(jugador)+" has ganado!")
        print("¡Felicidades!")
    else:
        print("Se ha llenado el tablero y no ha habido un ganador :(")
        print("Fin del Juego.")
    

##print(tablero)