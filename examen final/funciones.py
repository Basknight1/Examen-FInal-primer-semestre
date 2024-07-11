import csv
import random

def asignar_sueldos(trabajadores):# 1
    sueldo_trabajadores = {}
    for trabajador in trabajadores:
        sueldo = random.randint(300000,25000000)
        sueldo_trabajadores[trabajador] = sueldo
    #DESCUENTOS
    descuento_salud = sueldo* 0.07
    descuento_afp = sueldo * 0.12
    sueldo_liquido = descuento_afp - descuento_salud
    print("Sueldos aleatorios asignados correctamente.")

def clasificar_sueldos(sueldo_trabajadores):#2
    menor_800 = {}
    entre_800_2000000 = {}
    mayor_2000000 = {}
    for trabajador, sueldo in sueldo_trabajadores.items():
        if sueldo < 800000:
            menor_800[trabajador] = sueldo
        elif sueldo <=2000000:
            entre_800_2000000[trabajador] = sueldo
        else:
            mayor_2000000[trabajador] = sueldo
    print("Sueldos menores a $800.000 TOTAL: ",len(menor_800))
    for trabajador,sueldo in menor_800.items():
        print(trabajador,sueldo)

    print("Sueldos entre a $800.000 y $2.000.000 TOTAL: ",len(entre_800_2000000))
    for trabajador,sueldo in entre_800_2000000.items():
        print(trabajador,sueldo)

    print("Sueldos mayores a $2.000.000 TOTAL: ",len(mayor_2000000))
    for trabajador,sueldo in mayor_2000000.items():
        print(trabajador,sueldo)

def ver_estadisticas(sueldo_trabajadores):#3
    sueldos = list(sueldo_trabajadores.values())
    if not sueldos:
        print("no se han asignado sueldos.")
        return None,None,None
    else:
        max_sueldo = max(sueldos)
        min_sueldo = min(sueldos)
        promedio_sueldo = sum(sueldos) / len(sueldos)
        return max_sueldo,min_sueldo,promedio_sueldo

def reporte_sueldos(sueldo_trabajadores):#4
    # descuento_salud = sueldo* 0.07
    # descuento_afp = sueldo * 0.12
    # sueldo_liquido = descuento_afp - descuento_salud
    with open('reporte_sueldos','w',newline='') as archivo:
        escritor = csv.writer(archivo,delimiter=':')
        for trabajador,sueldo_base,descuento_salud,descuento_afp,sueldo_liquido in sueldo_trabajadores.items():
            escritor.writerow(['Nombre de empleado',trabajador])
            escritor.writerow(['Sueldo Base',sueldo_base])
            escritor.writerow(['Descuento de salud',descuento_salud])
            escritor.writerow(['Descuento de afp',descuento_afp])
            escritor.writerow(['Sueldo liquido',sueldo_liquido])
    print("Reporte Generado exitosamente.")