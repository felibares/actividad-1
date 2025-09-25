def mostrar_tabla(acumulado):
    ordenados = sorted(acumulado.items(), key=lambda equipo_datos: equipo_datos[1]['total'], reverse=True)

    print(f"{'Equipo':<10} {'Innovación':<10} {'Presentación':<13} {'Errores':<8} {'Mejores':<9} {'Total':<6}")
    for nombre_equipo, datos in ordenados:
        print(f"{nombre_equipo:<10} {datos['innovacion']:<10} {datos['presentacion']:<13} {datos['errores']:<8} {datos['mejores']:<9} {datos['total']:<6}")