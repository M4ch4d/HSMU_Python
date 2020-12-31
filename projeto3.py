"""
Um condomínio realiza uma eleição para síndico anualmente. Para otimizar o processo de votação e apuração, há a necessidade de criar um sistema de votação digital. Para isso, você deve fazer um programa em que seja possível registrar os votos e, em seguida, apresentar o resultado final.
A eleição pode ter entre uma e três chapas, sendo elas Azul, Vermelho e Amarelo, cada uma com apenas um candidato. O condomínio possui 35 apartamentos e apenas um morador de cada residência pode votar. O resultado deve exibir quantos votos teve cada candidato, a quantidade de votos nulos e brancos e a porcentagem deles sobre o total de votos.
"""
print("Sistema eleitoral: Condomínio Águas Barrosas")

Amarelo = ''
Vermelho = ''
Azul = ''
moradias = {}
num = 0
votosA = votosB = votosC = votosNulos = votosBranco = 0

while num < 35:
    moradias[num+1] = 'voto'
    num += 1


chapas = int(input('Quantas Chapas disputarão a Eleição? 2 ou 3?'))
while 1 < chapas > 3:
    print()
    print('Favor digitar apenas os números 2 ou 3')
    chapas = int(input('Quantas Chapas disputarão a Eleição? (2 a 3 chapas permitidas'))
print()
print('Cadastre o Candidato')
if chapas == 3:
    Amarelo = input('Qual o Represantante da Chapa Amarela?: ')
    print()
    Vermelho = input('Qual o Represantante da Chapa Vermelha?: ')
    print()
    Azul = input('Qual o Represantante da Chapa Azul?: ')

elif chapas == 2:
    Azul = input('Qual o Represantante da Chapa Amarela?: ')
    print()
    Vermelho = input('Qual o Represantante da Chapa Vermelha?: ')

print()
print('-=' * 20)
print(f'{"VOTAÇÃO":^35}')
print('-=' * 20)
print()
continuar = ' '
while continuar != 'N':
    ap = int(input('Qual seu apartamento?: '))
    if chapas == 3:
        if moradias[ap] != 'voto':
            print('Esse apartamento já atingiu o número máximo de votos! \n Voto não computado!')
            print()
        else:
            print()
            moradias[ap] = input(f'Em quem você quer votar? (Digite a letra correspondente ao candidato): \n '
                                     f'A - {Amarelo} \n B - {Vermelho} \n C - {Azul} \n '
                                     f'X - Voto em Branco \n').upper().strip()
            print('Voto Computado!')
            print()
    elif chapas == 2:
        if moradias[ap] != 'voto':
            print('Esse apartamento já atingiu o número máximo de votos! \n Voto não computado!')
            print()
        else:
            print()
            moradias[ap] = input(f'Em quem você quer votar?(Digite a letra correspondente ao candidato):'
                                     f' \n A - {Amarelo} \n B - {Vermelho}  \n X - Voto em Branco \n').upper().strip()
            print('Voto Computado!')
            print()
    continuar = input('Há mais pessoas para votar? [S/N]: ').strip().upper()
for d in moradias:
    if moradias[d] == 'A':
        votosA += 1
    elif moradias[d] == 'B':
        votosB += 1
    elif moradias[d] == 'C':
        if chapas == 2:
            votosNulos += 1
        else:
            votosC += 1
    elif moradias[d] == 'X':
        votosBranco += 1
    else:
        votosNulos += 1
pVotosBranco = (votosBranco * 100)/35
pVotosNulo = (votosNulos * 100)/35
print('-'*30)
print(f'{"Resultado da Eleição":^35}')
print('-'*30)
print()
if chapas == 2:
    print(f'O candidato da Chapa Amarela "{Azul}" obteve {votosC} voto(s)')
    print(f'O candidato da Chapa Vermelha "{Vermelho}" obteve {votosB} voto(s)')
else:
    print(f'O candidato da Chapa Amarela "{Azul}" obteve {votosC} voto(s)')
    print(f'O candidato da Chapa Vermelha "{Vermelho}" obteve {votosB} voto(s)')
    print(f'O candidato da Chapa Azul "{Amarelo}" obteve {votosA} voto(s)')
print(f'Total de votos em Branco: {votosBranco}, totalizando {pVotosBranco:.1f}% dos votos')
print(f'Total de votos Nulos: {votosNulos}, totalizando {pVotosNulo:.1f}% dos votos')
print('Fim da sessão')
print("O condomínio agradece seu voto! Justiça eleitoral")

