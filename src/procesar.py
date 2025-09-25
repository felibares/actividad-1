from calcular_punt import calcular_puntos 
from imprimir_tabla import mostrar_tabla
def procesar_evaluaciones(evaluaciones):
    acumulado = {}

    for i, ronda in enumerate(evaluaciones, start=1):
        print(f"\nRonda {i}")

        puntos_equipo = dict(map(lambda equipo_info: (equipo_info[0], calcular_puntos(equipo_info[1])), ronda.items()))

        equipo_ganador = None
        puntos_max = -1
        for nombre_equipo, puntos in puntos_equipo.items():
            if puntos > puntos_max:
                puntos_max = puntos
                equipo_ganador = nombre_equipo

        print(f"{'Equipo':<10} {'Innovación':<10} {'Presentación':<13} {'Errores':<8} {'Puntos':<6} {'Ganador':<8}")
        ordenados_ronda = sorted(puntos_equipo.items(), key=lambda item: item[1], reverse=True)
        for nombre_equipo, puntos in ordenados_ronda:
            datos_equipo = ronda[nombre_equipo]
            errores = int(datos_equipo['errores'])
            ganador = '1' if nombre_equipo == equipo_ganador else ''
            print(f"{nombre_equipo:<10} {datos_equipo['innovacion']:<10} {datos_equipo['presentacion']:<13} {errores:<8} {puntos:<6} {ganador:<8}")

        print(f"Mejor equipo: {equipo_ganador} con {puntos_max} puntos")

        for nombre_equipo, datos_equipo in ronda.items():
            if nombre_equipo not in acumulado:
                acumulado[nombre_equipo] = {
                    'innovacion': 0,
                    'presentacion': 0,
                    'errores': 0,
                    'mejores': 0,
                    'total': 0
                }

            acumulado[nombre_equipo]['innovacion'] += datos_equipo['innovacion']
            acumulado[nombre_equipo]['presentacion'] += datos_equipo['presentacion']
            acumulado[nombre_equipo]['errores'] += int(datos_equipo['errores'])
            acumulado[nombre_equipo]['total'] += puntos_equipo[nombre_equipo]

        acumulado[equipo_ganador]['mejores'] += 1

    print("\nTabla final acumulada:")
    mostrar_tabla(acumulado)

    return acumulado 

