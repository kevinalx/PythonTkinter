#Un alumno desea saber cual será su calificación final en la materia de Algoritmos. Dicha
#calificación se compone de los siguientes porcentajes:
#55% del promedio de sus tres calificaciones parciales.
#30% de la calificación del examen final.
#15% de la calificación de un trabajo final.
#Leer c1, c2, c3, ef, tf
#prom = (c1 + c2 + c3)/3
#ppar = prom * 0.55
#pef = ef * 0.30
#ptf = tf * 0.15
#cf = ppar + pef + ptf
#Imprimir cf
from tkinter import *


def calcular():
        prom = (calf1 + calf2 + calf3)/3
        ppar = prom * 0.55
        pef = examen * 0.30
        ptf = tf * 0.15
        cf = ppar + pef + ptf
        print(f"\nSu nota definitiva es de: {cf}")


top = Tk()
calf1 = float
calf2 = float
calf3 = float
examen = float
tf = int
top.geometry("400x400")
top.title("Sistema de calificaciones")
etiqueta1 = Label(top, text="Ingrese la calificacion 1  ").place(x=10, y=10)
C1 = Entry(top, textvariable=calf1).place(x=200, y=10)
etiqueta2 = Label(top, text="Ingrese la calificacion 2  " ).place(x=10, y=40)
C2 = Entry(top, textvariable=calf2).place(x=200, y=40)
etiqueta3 = Label(top, text="Ingrese su calificacion 3  ").place(x=10, y=70)
C3 = Entry(top, textvariable=calf3).place(x=200, y=70)
etiquetaExamen = Label(top, text="Ingrese su nota del examen final ").place(x=10, y=100)
examenFinal = Entry(top, textvariable=examen).place(x=200, y=100)
etiquetaFinal = Label(top, text="Ingrese nota de su trabajo final ").place(x=10, y=130)
trabajoFinal = Entry(top, textvariable=tf).place(x=200, y=130)
boton = Button(top, text="Calcular", command=calcular).place(x=10, y=160)


top.mainloop()