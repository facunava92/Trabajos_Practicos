#Banderas
sospechoso = False
autoctono = False
fiebre  = False
grupo_de_riesgo = False
personal = False

sintomas = 0
antecedentes = 0

#Entrada de Datos
print('\n## Programa para determinar casos sospechosos de COVID-19 ##\n')
edad = int(input('\tIngrese su edad: '))
if (edad>60):
    grupo_de_riesgo = True
temperatura = int(input('\tIngrese su temperatura corporal: '))
if(temperatura>37):
    fiebre = True
neumonia = int(input('\t¿Tiene neumonía? 1-Si | 0-No: '))

if neumonia:
    #Determinamos si es autoctono, quedaba a nuestro criterio agregarlo o no.
    contacto = int(input('\t¿Estuvo en contacto con casos confirmados? 1-Si | 0-No: '))
    viaje = int(input('\t¿Realizó viajes fuera del país? 1-Si | 0-No: '))
    zonas = int(input('\t¿Estuvo en zonas de transmisión local? 1-Si | 0-No: '))
elif fiebre:
        tos = int(input('\t¿Tiene tos? 1-Si | 0-No: '))
        odinofagia = int(input('\t¿Tiene dificultad para tragar? (odinofagia) 1-Si | 0-No: '))
        respirar = int(input('\t¿Tiene dificultad para respirar? 1-Si | 0-No: '))
        sintomas = tos + odinofagia + respirar

        if sintomas:
            personal = int(input('\t¿Es usted un personal de salud? 1-Si | 0-No: '))
            if(not personal):
                print('\t En los últimos 14 días ...')
                contacto = int(input('\t¿Estuvo en contacto con casos confirmados? 1-Si | 0-No: '))
                viaje = int(input('\t¿Realizó viajes fuera del país? 1-Si |0-No: '))
                zonas = int(input('\t¿Estuvo en zonas de transmisión local? 1-Si | 0-No: '))
                antecedentes = contacto + viaje + zonas

# Validacion de casos
if( neumonia or (fiebre and sintomas and (personal or antecedentes))):
    sospechoso = True

if not personal:
    if((sintomas>=2 or neumonia) and (not contacto and not viaje and zonas)):
        autoctono = True

#Salida
print("\n\t ------------------------- RESULTADOS -------------------------")
if(sospechoso):
    print('\n\t--> Caso Sospechoso <--')
    if(not neumonia):
        print('\t\tPresenta los siguientes síntomas:')
        if fiebre:
            print('\t\t #Fiebre.')
        if respirar:
            print('\t\t #Dificultad para respirar.')
        if(odinofagia):
            print('\t\t #Dolor de garganta para tragar (odinofagia).')
        if(tos):
            print('\t\t #Tos seca.')
        if (personal):
            print('\n\t\t **Paciente forma parte de personal de la salud.')
    else:
        print('\t\tDiagnostico clínico y radiológico compatible con neumonía')

    if(autoctono):
        print('\n\t\tCASO AUTÓCTONO!!')
    elif not personal:
         print('\n\t\tCASO NO AUTÓCTONO!!')
else:
    print('\n\t--> Caso NO sospechoso <--')
    if (grupo_de_riesgo):
        print('\t\t **Paciente comprendido dentro del grupo de riesgo.')

print("\n\t --------------------------------------------------------------")
