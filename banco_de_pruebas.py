from gestion_archivos import *

lugares = [
    {"ciudad": "Madrid", "pais": "España", "poblacion_millones": 6.78, "temperatura_media": 19.4, "codigo_postal": 28401, "es_capital": True},
    {"ciudad": "Buenos Aires", "pais": "Argentina", "poblacion_millones": 15.21, "temperatura_media": 22.1, "codigo_postal": 10234, "es_capital": True},
    {"ciudad": "Ciudad de México", "pais": "México", "poblacion_millones": 20.44, "temperatura_media": 18.7, "codigo_postal": 54023, "es_capital": True},
    {"ciudad": "Bogotá", "pais": "Colombia", "poblacion_millones": 8.13, "temperatura_media": 14.5, "codigo_postal": 110231, "es_capital": True},
    {"ciudad": "Lima", "pais": "Perú", "poblacion_millones": 9.83, "temperatura_media": 21.6, "codigo_postal": 15001, "es_capital": True},
    {"ciudad": "Santiago", "pais": "Chile", "poblacion_millones": 7.12, "temperatura_media": 17.8, "codigo_postal": 8320000, "es_capital": True},
    {"ciudad": "Quito", "pais": "Ecuador", "poblacion_millones": 2.78, "temperatura_media": 16.3, "codigo_postal": 170150, "es_capital": True},
    {"ciudad": "Caracas", "pais": "Venezuela", "poblacion_millones": 3.12, "temperatura_media": 25.4, "codigo_postal": 1010, "es_capital": True},
    {"ciudad": "Montevideo", "pais": "Uruguay", "poblacion_millones": 1.34, "temperatura_media": 18.2, "codigo_postal": 11200, "es_capital": True},
    {"ciudad": "San José", "pais": "Costa Rica", "poblacion_millones": 1.54, "temperatura_media": 23.1, "codigo_postal": 10101, "es_capital": True}
]

nombre_fichero= "lugares.csv"
de_lista_a_csv(lugares, nombre_fichero)

