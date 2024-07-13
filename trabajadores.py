import csv
from statistics import mean, geometric_mean
from random import randint

trabajadores=["Juan Pérez","María García","Carlos López","Ana Martínez", "Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]
trabajadores_sueldo=[]
def menu():
    print("--------------------------------------")
    print("1 Asignar sueldos aleatorios")
    print("2 Clasificar sueldos")
    print("3. Ver estadísticas.")
    print("4. Reporte de sueldos")
    print("5. Salir del programa")
    print("--------------------------------------")
def asignar_sueldos():
    for nombre in trabajadores:
        sueldo=randint(300,2500000)
        # print(f"{nombre} {sueldo} ")
        trabajadores_sueldo.append({"nombre":nombre,"sueldo":sueldo})
    print("sueldos asignados correctamente")

def clasificar_sueldo():
    total=0
    print(f"\nSaldos menores a $800.000 TOTAL:")
    for trabajador in trabajadores_sueldo:
        if trabajador["sueldo"] < 800000:
            print(f"{trabajador["nombre"]} {trabajador["sueldo"]}")
            total +=1
    print("\nsaldos entre 800.000 y 2.000.000")
    for trabajador in trabajadores_sueldo:
        if trabajador["sueldo"] in range(800000,2000000):
            print(f"{trabajador["nombre"]} {trabajador["sueldo"]}")
    print("\nsaldos superiores a 2.000.000")
    for trabajador in trabajadores_sueldo:
        if trabajador["sueldo"] > 2000000:
            print(f"{trabajador["nombre"]} {trabajador["sueldo"]}")
    for i in trabajadores_sueldo:
        total +=i["sueldo"]
    print(f"total sueldos: {total}")
            
sueldos=[]

def ver_estadisticas():
    for trabajador in trabajadores_sueldo:
        sueldos.append(trabajador["sueldo"])
    print(f"Sueldo mas alto: {max(sueldos)}")
    print(f"Sueldo mas bajo: {min(sueldos)}")
    print(f"Promedio de sueldos: {mean(sueldos)}")
    print(f"Media geometrica: {geometric_mean(sueldos)} ")
    
planilla=[]
def reporte_sueldos():
    print("Nonbre Empleado       Sueldo Bruto    Descuento Salud      Descuento AFP     Sueldo Bruto")
    for sueldo in trabajadores_sueldo:
        print(f"{sueldo["nombre"]}   {sueldo["sueldo"]}   {round(sueldo["sueldo"]*0.07)}  {round(sueldo["sueldo"]*0.12)}  {round(sueldo["sueldo"]*0.19)})")
        planilla.append([sueldo["nombre"],sueldo["sueldo"],round(sueldo["sueldo"]*0.07),round(sueldo["sueldo"]*0.12),round(sueldo["sueldo"]*0.19)])
    
def planilla_trabajadores():
    with open("reportes_sueldos.csv", "w", newline="", encoding="utf8") as archivo:
        writer=csv.writer(archivo)
        writer.writerow([planilla])
                
while True:
    menu()
    opc=input("ingrese opcion: ")
    if opc == "1":
        asignar_sueldos()
    elif opc == "2":
        clasificar_sueldo()
    elif opc == "3":
        ver_estadisticas()
    elif opc == "4":
        reporte_sueldos()
        planilla_trabajadores()
        print(planilla)
    elif opc == "5":
        print("saliendo del programa")
        break
    else:
        print("opcion incorrecta")