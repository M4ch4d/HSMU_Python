"""O Imposto Sobre Serviços (ISS) é uma tributação que deve ser paga por empresas e profissionais liberais, que trabalham por conta própria, ao município no qual estão registrados. O percentual a ser pago varia de 2% a 5% e é definido por cada município. Além do imposto municipal, existem os estaduais, como o ICMS, que é o Imposto sobre a Circulação de Mercadorias e Serviços. Cada estado do Brasil pratica um percentual diferente sobre o produto ou serviço.

A empresa fictícia ZANPAX, localizada em Recife - PE, desenvolverá um sistema de controle de estoque para uma restaurante. O valor total do projeto foi orçado em R$ 56.300 e, antes de fechar o negócio com o cliente, a empresa precisa saber o quanto irá pagar de tributos.

Crie um programa que exiba todos os impostos a serem pagos pela empresa, considerando que o ISS cobrado em Recife é de 4% e o ICMS cobrado pelo estado de Pernambuco é de 18%.

"""

valor = 56.300
iss = (valor * 4)/100
icms = ((18 * valor)/100)
print('O valor a ser pago em ICMS pelo projeto do restaurente será de:', icms)
print('O valor a ser pago em tributos ISS pelo projeto do restaurente será de:', iss)
