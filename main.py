import turtle
from turtle import forward, right, onkeypress, listen, bye, done

wn = turtle.Screen()
wn.bgcolor("blue")  # Agregando color a la pantalla
wn.title("LABERINTO")  # Poniendo titulo
wn.setup(700, 700)  # Creando tamaño a la ventana


class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)

        self.shape("square")  # Poniendo la forma
        self.color("white")  # Poniendo color al laberinto
        self.color("")  # Poniendo color al laberinto
        self.penup()
        self.speed(0)


bloques = Pen()


def iniciar_lab(nivel):
    for fila in range(len(nivel)):
        for columna in range(len(nivel[fila])):

            caracter = nivel[fila][columna]
            ejeX = -288 + (columna * 23)
            ejeY = 288 - (fila * 23)

            if caracter == 3:
                bloques.color("yellow")
                bloques.goto(ejeX, ejeY)
                bloques.stamp()
            elif caracter == 0 or caracter == "0":
                bloques.color("white")
                bloques.goto(ejeX, ejeY)
                bloques.stamp()
            elif caracter == -1 or caracter == "x":
                bloques.color("green")
                bloques.goto(ejeX, ejeY)
                bloques.stamp()
            elif caracter == "B":
                bloques.color("red")
                bloques.goto(ejeX, ejeY)
                bloques.stamp()
            elif caracter == 1:
                bloques.color("black")
                bloques.goto(ejeX, ejeY)
                bloques.stamp()


laberinto = [[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1],
             [1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1],
             [1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1],
             [1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1],
             [1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1],
             [1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1],
             [1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1],
             [1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
             [1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1],
             [1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
             [1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
             [1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1],
             [1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1],
             [1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1],
             [1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1],
             [1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1],
             [1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1],
             [1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
             [1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1],
             [1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
             [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 3],
             [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

iniciar_lab(laberinto)
pen = Pen()


def imp(laberinto):
    for x in laberinto:
        for y in x:
            print(" ", y, " ", end=" ")
        print()


imp(laberinto)


def recorrido(i, j):
    if laberinto[i][j] == 3:
        return [(i, j)]

    if laberinto[i][j] == 1:
        return []

    laberinto[i][j] = -1

    if i > 0 and laberinto[i - 1][j] in [0, 3]:  # arriba
        camino = recorrido(i - 1, j)
        if camino: return [(i, j)] + camino

    if j < len(laberinto[i]) - 1 and laberinto[i][j + 1] in [0, 3]:  # para la derecha
        camino = recorrido(i, j + 1)
        if camino: return [(i, j)] + camino

    if i < len(laberinto) - 1 and laberinto[i + 1][j] in [0, 3]:  # para abajo
        camino = recorrido(i + 1, j)
        if camino: return [(i, j)] + camino

    if j > 0 and laberinto[i][j - 1] in [0, 3]:  # para la izquierda
        camino = recorrido(i, j - 1)
        if camino: return [(i, j)] + camino

    laberinto[i][j] = "B"
    return []


def agregarLab(laberinto, laberintoResuelto):
    for x in laberinto:
        for y in x:
            if y == -1:
                y = "x"
                laberintoResuelto = laberinto
                return laberintoResuelto


for x in recorrido(21,8):
    print(f" {x} ")


def implab(laberinto):
    for x in laberinto:
        for y in x:
            if y == -1:
                y = "x"
                print(" ", y, " ", end=" ")

            else:
                print(" ", y, " ", end=" ")

        print()


implab(laberinto)

iniciar_lab(laberinto)
pen1 = Pen()
turtle.onkeypress(bye, 'q')
turtle.listen()
done()

print("carlos")
