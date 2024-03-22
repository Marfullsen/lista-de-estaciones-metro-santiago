<p align="center">
    <img src="./docs/img/train.png" alt="Train Icon" width="300">
</p>

<div align="center">

# Listado de las estaciones del metro

[![Python3](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)

</div>

<p align="center">
  Listado de las estaciones de la red del metro de Santiago de Chile
</p>

## ¿Qué es este listado?
El listado presentado es un indexado de todos los nombres de las estaciones de todos los tramos (líneas) del metro para ser usado con fines informáticos (crear aplicaciones, obtener los nombres, etc).

## ¿Es posible visualizar el contenido del archivo en formato JSON?
Si, los datos pueden ser visualizados ejecutando el archivo **show_stations.py**.

<p align="center">
  <a href="./show_stations.py" rel="noopener">
  <img src="./docs/img/python-output-subway-line-4A.png" alt="show_stations.py"></a>
</p>

## ¿Cuándo se actualizó?
Actualizado en marzo del año 2024.
Contiene las nuevas estaciones de la línea 2 (línea amarilla) y línea 3 (línea marrón/café).

## ¿Qué contiene el archivo JSON?
El archivo **metro_stations.json** contiene el listado con todos los nombres de las estaciones del metro de Santiago de Chile indexados en formato JSON.

## ¿Qué patrón sigue el listado?
El listado viene organizado por líneas (tramos), siendo la **clave** su número respectivo, y el **valor** es **un objeto** con el color de la línea en formato _string_, un arreglo con las estaciones y un arreglo con las combinaciones disponibles.

### Patrón
```js
{
  "0": {
      "color": "",
      "estaciones": [

      ],
      "combinaciones": [

      ]
    }
}
```

### Ejemplo ficticio
```js
{
  "12": {
      "color": "blue",
      "estaciones": [
        "Marfullsen", "Sorrego", "Morat", "Maikowski", "Karlshafen"
      ],
      "combinaciones": [
        "Sorrego", "Morat"
      ]
    },
    ...
}
```

## Mapa de la red del metro de Santiago de Chile

<p align="center">
  <a href="https://www.dtpm.cl/index.php/sistema-transporte-publico-santiago/metro" rel="noopener">
  <img src="./docs/img/mapa_metro_santiago.png" alt="Map of stations"></a>
</p>

## Referencias

- [Underground icons created by smalllikeart - Flaticon](https://www.flaticon.com/free-icons/underground "underground icons")
- [Metro icons created by Freepik - Flaticon](https://www.flaticon.com/free-icons/metro "metro icons")
- Code image by [Carbon](https://carbon.now.sh/)
- Photo by Thom Milkovic on Unsplash
