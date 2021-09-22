from tkinter import *
import parser

calculadora = Tk()
calculadora.title("CALCULADORA")


pantalla = Entry(calculadora,bg = "aquamarine2", font = "Helvetic 40")
pantalla.grid(row=1, columnspan=6, sticky=W+E)

contadorParaLasPosiciones = 0

def obtenerNumerosDeLaPantalla(numero):
    global contadorParaLasPosiciones
    pantalla.insert(contadorParaLasPosiciones, numero)
    contadorParaLasPosiciones += 1

def obtenerOperadorDeLaPantalla(operador):
    global contadorParaLasPosiciones
    pantalla.insert(contadorParaLasPosiciones, operador)
    contadorParaLasPosiciones += 1

def calcular():
    display_state = pantalla.get()
    try:
        math_expression = parser.expr(display_state).compile()
        result = eval(math_expression)
        limpiarPantalla()
        pantalla.insert(0, result)
    except Exception:
        limpiarPantalla()
        pantalla.insert(0, 'Error')

def limpiarPantalla():
    pantalla.delete(0, END)




Button(calculadora, text="1", command=lambda: obtenerNumerosDeLaPantalla(1),bg = "aquamarine2", font = "Helvetic 25").grid(row=2, column=0, sticky=W+E)
Button(calculadora, text="2", command=lambda: obtenerNumerosDeLaPantalla(2),bg = "aquamarine2", font = "Helvetic 25").grid(row=2, column=1, sticky=W+E)
Button(calculadora, text="3", command=lambda: obtenerNumerosDeLaPantalla(3),bg = "aquamarine2", font = "Helvetic 25").grid(row=2, column=2, sticky=W+E)

Button(calculadora, text="4", command=lambda: obtenerNumerosDeLaPantalla(4),bg = "aquamarine2", font = "Helvetic 25").grid(row=3, column=0, sticky=W+E)
Button(calculadora, text="5", command=lambda: obtenerNumerosDeLaPantalla(5),bg = "aquamarine2", font = "Helvetic 25").grid(row=3, column=1, sticky=W+E)
Button(calculadora, text="6", command=lambda: obtenerNumerosDeLaPantalla(6),bg = "aquamarine2", font = "Helvetic 25").grid(row=3, column=2, sticky=W+E)

Button(calculadora, text="7", command=lambda: obtenerNumerosDeLaPantalla(7),bg = "aquamarine2", font = "Helvetic 25").grid(row=4, column=0, sticky=W+E)
Button(calculadora, text="8", command=lambda: obtenerNumerosDeLaPantalla(8),bg = "aquamarine2", font = "Helvetic 25").grid(row=4, column=1, sticky=W+E)
Button(calculadora, text="9", command=lambda: obtenerNumerosDeLaPantalla(9),bg = "aquamarine2", font = "Helvetic 25").grid(row=4, column=2, sticky=W+E)


Button(calculadora, text="C", command=lambda: limpiarPantalla(),bg = "aquamarine2", font = "Helvetic 25").grid(row=2, column=4, sticky=W+E, columnspan=2)
Button(calculadora, text="0", command=lambda: obtenerNumerosDeLaPantalla(0),bg = "aquamarine2", font = "Helvetic 25").grid(row=5, column=0, sticky=W+E)
Button(calculadora, text="=", command=lambda: calcular(),bg = "aquamarine2", font = "Helvetic 25").grid(row=5, column=1, sticky=W+E, columnspan=2)

Button(calculadora, text="+", command=lambda: obtenerOperadorDeLaPantalla("+"),bg = "aquamarine2", font = "Helvetic 25").grid(row=2, column=3, sticky=W+E)
Button(calculadora, text="-", command=lambda: obtenerOperadorDeLaPantalla("-"),bg = "aquamarine2", font = "Helvetic 25").grid(row=3, column=3, sticky=W+E)
Button(calculadora, text="*", command=lambda: obtenerOperadorDeLaPantalla("*"),bg = "aquamarine2", font = "Helvetic 25").grid(row=4, column=3, sticky=W+E)
Button(calculadora, text="/", command=lambda: obtenerOperadorDeLaPantalla("/"),bg = "aquamarine2", font = "Helvetic 25").grid(row=5, column=3, sticky=W+E)



calculadora.mainloop()