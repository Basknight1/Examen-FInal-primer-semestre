import funciones as fn
#0. Inicializar sueldos para poder asignarles un sueldo aleatorio.
#1.Asignar sueldos aleatorios -> generar 10 sueldos aleatorios.
#2. Clasificar sueldos ->  clasificar segun (menor a 800, entre 800,25.. y mayor a 25...)
#3. Ver estadisticas -> mostrar sueldos(max,min,prom,total)
#4. Reporte de sueldos -> formato csv
#5. Salir -> despedida con nombre y rut.
trabajadores = ["Juan Pérez”,”María García”,”Carlos López”,”Ana Martínez”,”Pedro Rodríguez”,”Laura Hernández”,”Miguel Sánchez”,”Isabel Gómez”,”Francisco Díaz”,”Elena Fernández"]

sueldo_trabajadores = {}

while True:
    try:
        print("ANALISIS DE DATOS DE TRABAJADORES")
        print("\n¿QUÉ NECESITA HACER?\n0. INICIALIZAR SUELDOS\n1. ASIGNAR SUELDOS ALEATORIOS\n2. CLASIFICAR SUELDOS\n3. VER ESTADISTICAS\n4. REPORTE DE SUELDOS.\n5. SALIR DEL PROGRAMA.")

        opc = int(input("Ingrese una opción: "))
        
        if opc == 0:
            sueldo_trabajadores = {trabajador:0 for trabajador in trabajadores}
            print("Sueldos Inicializados correctamente")
        elif opc == 1:
            if not sueldo_trabajadores:
                print("Primero debe inicializar.")
            else:
                trabajadores = fn.asignar_sueldos(trabajadores)
        
        elif opc == 2:
            if sueldo_trabajadores:
                fn.clasificar_sueldos(sueldo_trabajadores)
            else:
                print("Primero debe asignar los sueldos.")

        elif opc == 3:
            if sueldo_trabajadores:
                max_sueldo,min_sueldo,promedio_sueldo = fn.ver_estadisticas(sueldo_trabajadores)
                if max_sueldo is not None:
                    print("Sueldo máximo: ",max_sueldo)
                    print("Sueldo mínimo: ",min_sueldo)
                    print("Promedio sueldo: ",promedio_sueldo)
            else:
                print("Primero debe asignar los sueldos.")

        elif opc ==4 :
            if sueldo_trabajadores:
                fn.reporte_sueldos(sueldo_trabajadores)
            else:
                print("Primero debe asignar los sueldos.")

        elif opc == 5:
            print("Saliendo del Programa...\nDesarrollado por Bastian Matus\nRUT 20.830.555-7")
            break

        else:
            print("Opción no válida, por favor ingrese una opción entre 1 y 5.")            
    except ValueError:
        print("Ingrese solo números.")
