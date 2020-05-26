from graphics import *

def main():
    win = GraphWin("Minha Janela", 800, 500)
    win.setBackground(color_rgb(154, 241, 255))

    # # ---------- Círculo ----------
    # circlePosition = Point(250, 250)

    # cir = Circle(circlePosition, 30)
    # cir.setFill(color_rgb(100,255,50))
    # cir.setOutline(color_rgb(255, 255, 255))
    # cir.draw(win)

    # # ---------- Ponto ----------
    # pt = Point(400, 250)
    # pt.setOutline(color_rgb(255,255,0))
    # pt.draw(win)

    # # ---------- Linha ----------
    # pt1 = Point(400, 250)
    # pt2 = Point(300, 400)

    # line = Line(pt1, pt2)
    # line.setOutline(color_rgb(0, 255, 255))
    # line.setWidth(5)
    # line.draw(win)

    # # ---------- Retângulo ----------
    # pt3 = Point(100, 300)
    # pt4 = Point(200, 200)

    # rect = Rectangle(pt3, pt4)
    # rect.setOutline(color_rgb(0, 255, 255))
    # rect.setFill(color_rgb(255,0,255))
    # rect.setWidth(5)
    # rect.draw(win)

    # # ---------- Polígono ----------
    # points = [
    #     Point(400, 100),
    #     Point(10, 100),
    #     Point(550, 300)
    # ]

    # pol = Polygon(points)
    # pol.setFill(color_rgb(255,0,255))
    # pol.setOutline(color_rgb(0,255,255))
    # pol.setWidth(10)
    # pol.draw(win)

    # # ---------- Texto ----------
    # txt = Text(Point(400, 250), "Olá, Mundo!!")
    # txt.setTextColor('blue')
    # txt.setSize(30)
    # txt.setFace('helvetica')
    # txt.draw(win)

    # # ---------- Imagem ----------
    # img = Image(Point(400, 250), "img/apple.gif")
    # img.draw(win)

    # # ---------- Caixa de Texto ----------
    # qtdCaracteres = 50

    # inputBox = Entry(Point(400, 220), qtdCaracteres)
    # inputBox.draw(win)

    # texto = inputBox.getText()

    # txt = Text(Point(400, 280), texto)
    # txt.setTextColor('black')
    # txt.setSize(20)
    # txt.setFace('helvetica')
    # txt.draw(win)

    # while True:
    #     txt.setText(inputBox.getText())

    win.getMouse()
    win.close()

main()