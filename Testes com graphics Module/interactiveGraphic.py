from graphics import *

def main():
    # ==================== Criando Janela ====================
    win = GraphWin("Interatividade com graphics.py", 500, 500)
    win.setBackground(color_rgb(255,255,255))

    # ==================== Criando Círculo ====================
    circlePosition = Point(250, 250)

    cir = Circle(circlePosition, 50)
    cir.setFill(color_rgb(100, 255, 50))
    cir.setOutline(color_rgb(255, 255, 255))
    cir.draw(win)

    # ==================== Movendo Círculo com teclado ====================
    txt = Text(Point(250, 10), "Mova o círculo com as setas do teclado")
    txt.setTextColor('black')
    txt.setSize(10)
    txt.setFace('helvetica')
    txt.draw(win)

    txt2 = Text(Point(250, 20), "")
    txt2.setTextColor('black')
    txt2.setSize(10)
    txt2.setFace('helvetica')
    txt2.draw(win)

    moveStep = 20

    while True:
        keyPressed = win.getKey()
        txt2.setText("Tecla Pressionada: %s" % str(keyPressed))

        if keyPressed == "Up":
            cir.move(0,-moveStep)
        elif keyPressed == "Down":
            cir.move(0,moveStep)
        elif keyPressed == "Left":
            cir.move(-moveStep,0)
        elif keyPressed == "Right":
            cir.move(moveStep,0)

        keyPressed = 0

    win.getMouse()
    win.close()

main()