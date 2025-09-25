def mejor_ronda(evaluaciones):
    el_mejor = {}
    for i, rondas in enumerate(evaluaciones, start=1):
        puntos_equipo = dict(map(lambda equipo_info: (equipo_info[0], calcular_puntos(equipo_info[1])), rondas.items()))

        equipo_ganador = None
        puntos_maximos = -1
        for nombre_equipo, puntos in puntos_equipo.items():
            if puntos > puntos_maximos:
                puntos_maximos = puntos
                equipo_ganador = nombre_equipo

        el_mejor[f'Ronda {i}'] = (equipo_ganador, puntos_maximos)

    return el_mejor
