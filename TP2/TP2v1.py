import random


def validacion(intentos):
    for i in range(intentos):
        email = input('* Ingrese su e-mail: ')
        cont_arroba = 0
        access = True

        if email[0] == '@' or email[-1] == '@' or email[0] == '.' or email[-1] == '.':
            access = False

        if ".." in email:
            access = False
        
        if access:
            for caracter in email: 
                if caracter == '@':
                    cont_arroba += 1
                    if (cont_arroba > 1):
                        access = False
                        break
            
            if (cont_arroba < 1):
                access = False

        if (access):
            return True
        else:
            if (i < intentos - 1):
                print('E-mail erroneo, vuelva a intentarlo.\n')
            else:
                print('E-mail erroneo, se han agotado los intentos.\n')


intentos = 3
edad_max = 122

casos = 0
menor_edad = edad_max
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

print('\t\t\t\t ### Trabajo Práctico 02: Generación de Estadísticas sobre COVID-19 ###\n')
access = validacion(intentos)
if access:
    print('\t\t\t\t Acceso al sistema!!!\n')
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
            
            # Caso autoctono
            if (contacto == 'No' and personal == 'No' and viajo == 'No'):
                cont_autoc += 1
                if edad < menor_edad:
                    menor_edad = edad

        if test == 'negativo' and edad > 60:
            cont_edadriesgo += edad
            cont_riesgo += 1

        if contacto == 'Si':
            cont_contacto += 1

    #Procesamiento de datos
    porc_positivos = round((casos/pacientes), 2) * 100
    porc_personal = round((cont_personal/pacientes*100), 2)

    if cont_riesgo >= 1:
        prom_edadriesgo = round((cont_edadriesgo/cont_riesgo), 2)
    else:
        prom_edadriesgo = 0

    if not(cont_autoc):
        menor_edad = False

    if casos >= 1:
        prom_edadcasos = round((total_edad/casos), 2)
        porc_autoctono = round((cont_autoc/casos*100), 2)
        porc_norte = round((cont_norte/casos*100), 2)
        porc_sur = round((cont_sur/casos*100), 2)
        porc_gcba = round((cont_gcba/casos*100), 2)
        porc_capital = round((cont_capital/casos*100), 2)
    else:
        prom_edadcasos = 0
        porc_autoctono = 0
        porc_norte = 0
        porc_sur = 0
        porc_gcba = 0
        porc_capital = 0

    op = -1
    while (op != 0):
        print('==============================================================================================================')
        print('Elija una de las opciones: ')
        print('\t 1.  Cantidad de casos confirmados (test positivo) y porcentaje sobre el total de casos.')
        print('\t 2.  Edad promedio de los pacientes que pertenecen a un grupo de riesgo.')
        print('\t 3.  Cantidad y porcentaje que el personal de salud representa sobre el total de casos.')
        print('\t 4.  Edad promedio entre los casos confirmados.')
        print('\t 5.  Menor edad entre los casos autóctonos.')
        print('\t 6.  Cantidad de casos confirmados por región y porcentaje que representa cada uno sobre el total de casos.')
        print('\t 7.  Cantidad de casos confirmados con viaje al exterior.')
        print('\t 8.  Cantidad de casos sospechosos en contacto con casos confirmados.')
        print('\t 9.  Las regiones sin casos confirmados.')
        print('\t 10. Porcentaje de casos positivos autóctonos sobre el total de positivos.')
        print('\t 0.  Salir')
        print('============================================================================================================== \n')

        op = int(input('Ingrese el número de la opción elegida: '))

        if op == 1:
            if casos:
                print('\t\t ----------------------------------------------------------------------- ')
                print('\t\t || Se han confirmado', casos, 'casos, representan un', porc_positivos, '% sobre el total. ||')
                print('\t\t ----------------------------------------------------------------------- ')
            else:
                print('\t\t -------------------------------------------')
                print('\t\t || No se han registrado casos positivos. ||')
                print('\t\t -------------------------------------------')
        elif op == 2:
            if prom_edadriesgo:
                print('\t\t --------------------------------------------------------------------------------------------')
                print('\t\t || La edad promedio de los pacientes que pertenecen al grupo de riesgo es de', prom_edadriesgo, 'años. ||')
                print('\t\t --------------------------------------------------------------------------------------------')
            else:
                print('\t\t --------------------------------------------------')
                print('\t\t || No existen casos dentro del grupo de riesgo. ||')
                print('\t\t --------------------------------------------------')
        elif op == 3:
            if cont_personal:
                print('\t\t -----------------------------------------------------------------------------------------------------------------------------------')
                print('\t\t || Se han encontrado', cont_personal, 'personas que forman parte del personal de salud y representan un',porc_personal, '% con respecto al total de casos. ||')
                print('\t\t -----------------------------------------------------------------------------------------------------------------------------------')
            else:
                print('\t\t --------------------------------------------------------------------')
                print('\t\t || No se registran casos que correspondan a personal de la salud. ||')
                print('\t\t --------------------------------------------------------------------')
        elif op == 4:
            if prom_edadcasos:
                print('\t\t  -----------------------------------------------------------------')
                print('\t\t || La edad promedio de los casos confirmados fue de', prom_edadcasos, 'años. ||')
                print('\t\t  -----------------------------------------------------------------')
            else:
                print('\t\t ------------------------------------------')
                print('\t\t || No se han detectado casos positivos. ||')
                print('\t\t ------------------------------------------')
        elif op == 5:
            if menor_edad:
                print('\t\t --------------------------------------------------------------')
                print('\t\t || La menor edad entre los casos autóctonos es de', menor_edad, 'años. ||')
                print('\t\t --------------------------------------------------------------')
            else:
                print('\t\t --------------------------------------------')
                print('\t\t || No se han registrado casos autóctonos. ||')
                print('\t\t --------------------------------------------')
        elif op == 6:
            print('\t\t -------------------------------------------------------')
            print('\t\t || Casos por region [porcentaje con respecto al total] ')
            print('\t\t ||     * Capital:', cont_capital, '[', porc_capital, '%]')
            print('\t\t ||     * Gran Córdoba:', cont_gcba, '[', porc_gcba, '%]')
            print('\t\t ||     * Norte:', cont_norte, '[', porc_norte, '%]')
            print('\t\t ||     * Sur:', cont_sur, '[', porc_sur, '%]')
            print('\t\t -------------------------------------------------------')
        elif op == 7:
            if cont_viaje:
                print('\t\t ----------------------------------------------------------------------')
                print('\t\t || La cantidad de casos positivos con viajes al exterior es de:', cont_viaje, '. ||')
                print('\t\t ----------------------------------------------------------------------')
            else:
                print('\t\t -------------------------------------------------------')
                print('\t\t || No se han registrado casos con viaje al exterior. ||')
                print('\t\t -------------------------------------------------------')
        elif op == 8:
            if cont_contacto:
                print('\t\t ----------------------------------------------------------------------------------')
                print('\t\t || La cantidad de casos sospechoso en contacto con casos confimados es de:', cont_contacto, '. ||')
                print('\t\t ----------------------------------------------------------------------------------')
            else:
                print('\t\t ---------------------------------------------------------------------------------')
                print('\t\t || No se han registrado casos que hayan tenido contacto con casos confirmados. ||')
                print('\t\t ---------------------------------------------------------------------------------')
        elif op == 9:
            if (cont_sur and cont_gcba and cont_capital and cont_norte):
                print('\t\t --------------------------------------------------------------')
                print('\t\t || Se han registrado casos positivos en todas las regiones. ||')
                print('\t\t --------------------------------------------------------------')
            else:
                print('\t\t --------------------------------------------------------')
                print('\t\t || Las regiones donde no se han registrado casos son: ||')
                if not(cont_sur):
                    print('\t\t ||    *Sur                                            ||')
                if not(cont_norte):
                    print('\t\t ||    *Norte                                          ||')
                if not(cont_capital):
                    print('\t\t ||    *Capital                                        ||')
                if not(cont_gcba):
                    print('\t\t ||    *Gran Córdoba                                   ||')
                print('\t\t --------------------------------------------------------')
        elif op == 10:
            if cont_autoc:
                print('\t\t -------------------------------------------------------------------------------------------')
                print('\t\t || El porcentaje de casos autóctonos con respecto al total de positivos es de:', porc_autoctono, '%. ||')
                print('\t\t -------------------------------------------------------------------------------------------')
            else:
                print('\t\t --------------------------------------------')
                print('\t\t || No se han registrado casos autóctonos. ||')
                print('\t\t --------------------------------------------')
        elif op == 0:
            print('ADIOS!')

else:
    print('Acceso DENEGADO')
