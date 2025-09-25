def calcular_puntos(info):
    puntos = info['innovacion'] * 3 + info['presentacion']
    if info['errores']:
        puntos -= 1
    return puntos