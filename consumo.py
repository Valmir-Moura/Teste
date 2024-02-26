#CONSUMO DE ENERGIA

def consumo(): #Funão Consumo.
    data = input('Informe o Ano: ')
    data = input('Data Atual: ')
    consumo1 = input('Leitura Atual Kwh.: ')
    data = input('Data Anterior: ')
    consumo2 = input('Leitura Anterior Kwh.: ')
    Total = int(consumo1) - int(consumo2)
    print(str('Total' + ' ' + str(Total) + ' ' + 'Kwh.'))

consumo()