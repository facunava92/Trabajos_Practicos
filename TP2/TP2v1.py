#Programa para Generación de Estadísticas de COVID-19 (Coronavirus)

#En el contexto de la pandemia de COVID-19, se solicita desarrollar un programa que permita generar estadísticas
# sobre pacientes sospechosos, a los cuales se les ha realizado el test (o hisopado) de COVID-19 y a partir del mismo
# se genera información de utilidad para la toma de decisiones en nuestra Provincia.

#En primer lugar, el sistema debe solicitar la cuenta de usuario de la persona que generará el reporte. La cuenta
# debe ingresarse con formato nombre@dominio y el programa validará que cumpla con las siguientes reglas:

#Tener un sólo caracter @ en una posición intermedia de la cadena (ni la primera ni la última letra)
#No contener dos puntos seguidos (uno a continuación del otro)
#No empezar ni terminar con un punto
#Si la cuenta ingresada es inválida, se debe permitir el reingreso de la misma. Luego de tres intentos incorrectos,
# el programa debe detener la ejecución.

#Luego de confirmar que la cuenta es válida, solicitar al usuario que ingrese la cantidad de pacientes a procesar.
# Y a continuación, por cada paciente sospechoso, generar de manera aleatoria los siguientes datos:

#Edad
#Resultado del test (Positivo/Negativo)
#Región (Capital, Gran Córdoba, Norte y Sur)
#Si tuvo contacto con casos confirmados
#Si es personal de salud
#Si viajo al exterior
#El programa automáticamente determinará si se considera un caso autóctono. Se considera un caso autóctono si el
# resultado del test fue positivo y NO estuvo en contacto con casos confirmados, NO es personal de salud y NO viajó
# al exterior.

#Una vez cargados y procesados los datos de los n pacientes, mediante un menú de opciones, informar:

#Cantidad de casos confirmados (test positivo) y porcentaje sobre el total de casos.
#Edad promedio de los pacientes que pertenecen a grupo de riesgo (para pertenecer al grupo de riesgo el test debe ser
# negativo y tener más de 60 años).
#Cantidad y porcentaje que el personal de salud representa sobre el total de casos.
#Edad promedio entre los casos confirmados.
#Menor edad entre los casos autóctonos.
#Cantidad de casos confirmados por región y porcentaje que representa cada uno sobre el total de casos.
#Cantidad de casos confirmados con viaje al exterior.
#Cantidad de casos sospechosos en contacto con casos confirmados.
#Las regiones sin casos confirmados.
#Porcentaje de casos positivos autóctonos sobre el total de positivos.


print('Generación de Estadísticas sobre COVID-19')
print('*'*42)


# Cuenta de usuario formato nombre@dominio, validación



# Cantidad de pacientes a procesar

import random

pac_sospechosos = random.randint()


print('Edad: ')
print('Resultado del test (Positivo/Negativo): ')
print('Región (Capital, Gran Córdoba, Norte y Sur): ')
print('¿Tuvo contacto con casos confirmados?: ')
print('¿Es personal de salud?: ')
print('¿Viajó al exterior?: ')

print('Menú de opciones')
print('*'*20)

#Cantidad de casos confirmados (test positivo) y porcentaje sobre el total de casos.
#Edad promedio de los pacientes que pertenecen a grupo de riesgo (para pertenecer al grupo de riesgo el test debe ser
# negativo y tener más de 60 años).
#Cantidad y porcentaje que el personal de salud representa sobre el total de casos.
#Edad promedio entre los casos confirmados.
#Menor edad entre los casos autóctonos.
#Cantidad de casos confirmados por región y porcentaje que representa cada uno sobre el total de casos.
#Cantidad de casos confirmados con viaje al exterior.
#Cantidad de casos sospechosos en contacto con casos confirmados.
#Las regiones sin casos confirmados.
#Porcentaje de casos positivos autóctonos sobre el total de positivos.
