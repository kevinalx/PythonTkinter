#Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas, el
#vendedor desea saber cuanto dinero obtendrá por concepto de comisiones por las tres
#ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo
#base y comisiones.

class Empleado:
    sb = 0

    def calcular(self,v1,v2,v3):
        com = (v1 + v2 + v3) * 0.10
        return  com

vendedor = Empleado()
vendedor.sb = int(input("Ingrese su  sueldo base: "))

v1 = int(input("Ingrese el valor de venta 1: "))
v2 = int(input("Ingrese el valor de venta 2: "))
v3 = int(input("Ingrese el valor de venta 3: "))

valor_com = vendedor.calcular(v1,v2,v3)
tot_vta = vendedor.sb * valor_com

print(f"\nSu comision es de: {valor_com}")
print(f"\nSu sueldo es de: {tot_vta}")


