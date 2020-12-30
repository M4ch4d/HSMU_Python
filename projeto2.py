"""1. até 20% acima do limite permitido na via, infração média. Valor: R$ 130,16;
2. de 21% até 50% acima do limite permitido na via, infração grave. Valor: R$ 195,23;
3. a partir de 51% acima do limite permitido na via, infração gravíssima. Valor: R$ 880,41.
Para ajudar os agentes de trânsito em sua fiscalização de rotina, crie um programa para preparar a infração por excesso de velocidade. Considere que o programa deve receber, pelo menos, o número da placa do veículo, a velocidade analisada e o limite de velocidade da via. Em seguida, retorne uma mensagem ao agente informando os dados do veículo (placa), a categoria da infração e o valor da multa aplicada.
"""
placa = input('Digite a placa do veículo: ')
velocidade = float(input('Digite a velocidade atingida: '))
limite = float(input('Digite a velocidade limite da via: '))

if velocidade > limite:
    multa = ((velocidade / limite) - 1) * 100
    if multa <= 20:
        print('INFRAÇÃO MÉDIA')
        print(placa)
        print('Multa aplicada de R$130,16')
    elif 21 <= multa <= 50:
        print('INFRAÇÃO GRAVE')
        print(placa)
        print('Multa aplicada de R$195,23')
    else:
        print('INFRAÇÃO GRAVÍSSIMA')
        print(placa)
        print('Multa aplicada de R$880,41')