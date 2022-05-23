import json

colores = {
    "": "sin color",
    "red":  "rojo",
    "yellow": "amarillo",
    "brown": "café",
    "blue": "azul",
    "skyblue": "celeste",
    "green": "verde",
    "purple": "morado"
}

# Abrir el archivo JSON.
f = open('metro_stations.json', encoding='utf-8')

# Transformar a diccionario.
lineas = json.load(f)

# escribir la información.
for linea in lineas:
    color = colores[lineas[linea]["color"]]
    print(f'--[ Línea {linea} ]-[ color {color} ]--')
    for estacion in lineas[linea]["estaciones"]:
        print(estacion)
    print('--[ Combinaciones ]--')
    for combinacion in lineas[linea]["combinaciones"]:
        print(combinacion)
    print()
  
# Cerrar el archivo.
f.close()
