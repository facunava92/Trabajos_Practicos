# /usr/bin/python
import random


def validacion(intentos):
    for i in range(intentos):
        email = input('Ingrese su e-mail: ')
        N = len(email)
        cont_arroba = 0
        access = True

        if email[0] == '@' or email[N - 1] == '@' or email[0] == '.' or email[N - 1] == '.':
            access = False

        if access:
            for n in range(N - 1):
                if email[n] == '@':
                    cont_arroba += 1
                    if (cont_arroba > 1):
                        access = False
                        break

                if email[n] == '.':
                    if email[n + 1] == '.':
                        access = False

            if (cont_arroba < 1):
                access = False

        if (access):
            return True
        else:
            if (i < intentos - 1):
                print('E-mail erroneo, vuelva a intentarlo.\n')
            else:
                print('E-mail erroneo, se han agotado los intentos.\n')



def autoctono(test, contacto, personal, viajo):
    if test == 'positivo' and contacto == 'No' and personal == 'No' and viajo == 'No':
        return True
    else:
        return False


intentos = 3
edad_max = 122

casos = 0
menor_edad = 0
total_edad = 0
cont_edadriesgo = 0
cont_personal = 0
cont_viaje = 0
cont_autoc = 0
cont_norte = 0
cont_sur = 0
cont_capital = 0
cont_gcba = 0
cont_contacto = 0
cont_riesgo = 0

print('\t #Trabajo practico II: \n')
access = validacion(intentos)
if access:
    print('Acceso al sistema')
    pacientes = int(input('Ingrese la cantidad de pacientes:  '))

    while pacientes <= 0:
        pacientes = int(input('Error, ingrese un número de pacientes mayor a 0:  '))

    for i in range(pacientes):
        # Generacion de datios aleatorios:
        test = random.choice(['positivo', 'negativo'])
        edad = random.randint(0, edad_max)
        region = random.choice(['Capital', 'Gran Cordoba', 'Norte', 'Sur'])
        contacto = random.choice(['Si', 'No'])
        personal = random.choice(['Si', 'No'])
        viajo = random.choice(['Si', 'No'])

        # Clasificacion de datos
        if test == 'positivo':
            casos += 1
            total_edad += edad
            if personal == 'Si':
                cont_personal += 1
            if viajo == 'Si':
                cont_viaje += 1
            if region == 'Norte':
                cont_norte += 1
            if region == 'Capital':
                cont_capital += 1
            if region == 'Sur':
                cont_sur += 1
            if region == 'Gran Cordoba':
                cont_gcba += 1

        if autoctono(test, contacto, personal, viajo):
            cont_autoc += 1
            # Caso autoctono
            if edad < menor_edad:
                menor_edad = edad

        if test == 'negativo' and edad > 60:
            cont_edadriesgo += edad
            cont_riesgo += 1

        if contacto == 'Si':
            cont_contacto += 1

    #Procesamiento de datos
    porc_positivos = round((casos/pacientes), 2) * 100

    if not(cont_autoc):
        menor_edad = False

    if cont_riesgo >= 1:
        prom_edadriesgo = round((cont_edadriesgo/cont_riesgo), 2)
    else:
        prom_edadriesgo = False

    if casos >= 1:
        prom_edadcasos = round((total_edad/casos), 2)
        porc_personal = round((cont_personal/casos), 2) * 100
        porc_norte = round((cont_norte/casos), 2) * 100
        porc_sur = round((cont_sur/casos), 2) * 100
        porc_gcba = round((cont_gcba/casos), 2) * 100
        porc_capital = round((cont_capital/casos), 2) * 100
        porc_autoctono = round((cont_autoc/casos), 2) * 100
    else:
        prom_edadcasos = False
        porc_personal = False
        porc_norte = False
        porc_sur = False
        porc_gcba = False
        porc_capital = False
        porc_autoctono = False

    op = -1
    while (op != 0):
        print('Elija una de las opciones: ')
        print('\t 1.  Cantidad de casos confirmados (test positivo) y porcentaje sobre el total de casos.')
        print('\t 2.  Edad promedio de los pacientes que pertenecen a un grupo de riesgo.')
        print('\t 3.  Cantidad y porcentaje que el personal de salud representa sobre el total de casos.')
        print('\t 4.  Edad promedio entre los casos confirmados.')
        print('\t 5.  Menor edad entre los casos autóctonos.')
        print('\t 6.  Cantidad de casos confirmados por región y porcentaje que representa cada uno sobre el \
        total de casos.')
        print('\t 7.  Cantidad de casos confirmados con viaje al exterior.')
        print('\t 8.  Cantidad de casos sospechosos en contacto con casos confirmados.')
        print('\t 9.  Las regiones sin cacos confirmados.')
        print('\t 10. Porcentaje de casos positivos autóctonos sobre el total de positivos.')
        print('\t 0.  Salir')

        op = int(input('Ingrese el número de la opción elegida: '))

        if op == 1:
            if casos:
                print('Se han confirmado', casos, 'casos, representan un', porc_positivos, '% sobre el total.')
            else:
                print('No se han registrado casos positivos.')
        elif op == 2:
            if prom_edadriesgo:
                print('La edad promedio de los pacientes que pertenecen al grupo de riesgo es de', prom_edadriesgo, 'años.')
            else:
                print('No existen casos dentro del grupo de riesgo.')
        elif op == 3:
            if cont_personal:
                print('Se han encontrado', cont_personal, 'personas que forman parte del personal de salud y \
                representan un', porc_personal, '% con respecto al total de casos.')
            else:
                print('No se registran casos que correspondan a personal de la salud.')
        elif op == 4:
            if prom_edadcasos:
                print('La edad promedio de los casos confirmados fue de', prom_edadcasos,'años.')
            else:
                print('No se han detectado casos positivos.')
        elif op == 5:
            if menor_edad:
                print('La menor edad entre los casos autóctonos es de', menor_edad, 'años')
            else:
                print('No se han registrado casos autóctonos.')
        elif op == 6:
            print('Casos por region[porcentaje con respecto al total] ')
            if cont_capital:
                print('Capital:', cont_capital, '[', porc_capital, '%]')
            if cont_gcba:
                print('Gran Córdoba:', cont_gcba, '[', porc_gcba, '%]')
            if cont_norte:
                print('Norte:', cont_norte, '[', porc_norte, '%]')
            if cont_sur:
                print('Sur:', cont_sur, '[', porc_sur, '%]')
        elif op == 7:
            if cont_viaje:
                print('La cantidad de casos positivos con viajes al exterior es de:', cont_viaje)
            else:
                print('No se han registrado casos con viaje al exterior.')
        elif op == 8:
            if cont_contacto:
                print('La cantida de casos sospechoso en contacto con casos confimados es de:', cont_contacto)
            else:
                print('No se han registrado casos que hayan tenido contacto con casos confirmados.')
        elif op == 9:
            if (cont_sur and cont_gcba and cont_capital and cont_norte):
                print('Se han registrado casos positivos en todas las regiones.')
            else:
                print('Las regiones donde no se han registrado casos son:')
                if not(cont_sur):
                    print('\t *Sur')
                if not(cont_norte):
                    print('\t *Norte')
                if not(cont_capital):
                    print('\t *Capital')
                if not(cont_gcba):
                    print('\t *Gran Córdoba')
        elif op == 10:
            if cont_autoc:
                print('El porcentaje de casos autóctonos con respecto al total de positivos es de:', porc_autoctono)
            else:
                print('No se han registrado casos autóctonos.')
        elif op == 0:
            print('ADIOS!')

else:
    print('Acceso DENEGADO')
