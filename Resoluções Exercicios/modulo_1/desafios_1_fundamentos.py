# EXERCICIOS DE CALCULO SIMPLES

# RECEBA TRES VALORES E APRESENTE A SOMA DOS QUADRADOS DOS VALORES RECEBIDOS:

valor1 = int(input('Digite um valor: ')) ** 2
valor2 = int(input('Digite outro valor: ')) ** 2
valor3 = int(input('Digite outro valor: ')) ** 2
soma = valor1 + valor2 + valor3
print(f'{soma} é a soma dos três valores digitados')



# RECEBA QUATRO NOTAS E CALCULE A MEDIA ARITIMETICA E APRESENTE O RESULTADO:

nota1 = int(input('Digite a primeira nota: '))
nota2 = int(input('Digite a segunda nota: '))
nota3 = int(input('Digite a terceira nota: '))
nota4 = int(input('Digite a quarta nota: '))
soma = nota1 + nota2 + nota3
media = soma / 4
print(f'A media das notas é de {media:.2f}' )



# RECEBA UM NUMERO INTEIRO E IMPRIMA SEU ANTECESSOR E SEU SUCESSOR:

num = int(input('Digite um numero inteiro: '))
antecessor = num -1
sucessor = num + 1
if num == 0:
  sucessor = (int(num)+1)
  print(f'sucessor: {sucessor}')
  antecessor = -1
  print(f'antecessor: {antecessor}')
else:
  print(f'sucessor: {sucessor}')
  print(f'antecessor: {antecessor}')



# RECEBA UM NUMERO INTEIRO E IMPRIMA A SOMA DO SUCESSOR DO SEU TRIPLO COM O ANTECESSOR DE SEU DOBRO:

num = int(input('Digite um numero inteiro: '))
sucessor_triplo = int(num * 3 + 1 )
antecessor_dobro = int(num * 2 - 1)
soma = sucessor_triplo + antecessor_dobro
print(soma)



# LEIA O TAMANHO DE UM LADO DE UM QUADRADO E IMPRIMA COMO RESULTADO A SUA AREA:

lado = float(input('Digite o tamanho de um dos lados do quadrado em cm: '))
area_total = lado ** 2
print(f' A area do quadrado pe igual a {area_total:.2f} cm²')



# RECEBA O VALOR DO RAIO DE UM CIRCULO E IMPRIMA A AREA DO CIRCULO CORRESPONDENTE:

raio = float(input('Digite o valor do raio do circúlo em cm: '))
pi = 3.14
area_circulo = pi * raio ** 2
print(f'{area_circulo:.2f} cm')



# RECEBA OS VALORES DOS CATETO DE UM TRIANGULO E IMPRIMA A HIPOTENUSA:
  # MODO SIMPLIFICADO:
import math

a = float(input('Digite o valor de um cateto a: '))
b = float(input('Digite o valor de um cateto b: '))
result = math.hypot(a,b)
print(f'Hipotenusa: {result:.2f}')

 # SEM IMPORT MATH:
a = float(input('Digite o valor de um cateto a: '))
b = float(input('Digite o valor de um cateto b: '))
result = a ** 2 + b ** 2
hipot = result ** (1/2)
print(f'hipotenusa: {hipot:.2f}')



# LEIA A ALTURA E O RAIO DE UM CILINDRO CIRCULAR E IMPRIMA O VOLUME DO CILINDRO:

altura_cilindro = float(input('Digite a altura do cilindro circular em cm: '))
raio = float(input('Digite o valor do raio do cilindro circular em cm: '))
pi = 3.14
volume_cilindro = pi * raio ** 2 * altura_cilindro
print(f'{volume_cilindro} cm²')



# FAÇA UM PROGRAMA QUE LEIA O VALOR DE UM PRODUTO E IMPRIMA O VALOR COM DESCONTO, EM VISTA QUE O DESCONTO SEJA DE 12%:

valor_produto = float(input("Qual o valor do produto? "))

valor_desc =  valor_produto * (12 / 100)

valor_com_desc = valor_produto - valor_desc

print(f'O valor do desconto é de {valor_desc:.2f} R$' )
print(f'O valor do produto com desconto é de {valor_com_desc:.2f} R$')




# LEIA O SALARIO DE UM FUNCIONARIO. CALCULE E IMPRIMA O VALOR DO NOVO SALARIO, SABENDO QUE O SEU AUEMTO FOI DE 25%:

salario_atual = float(input("Qual o valor do so seu salario? "))
aumento =  salario_atual * (25 / 100)
salario_novo = salario_atual + aumento
print(f'O valor do aumento é de {aumento:.2f} R$' )
print(f'O valor de seu novo salario é de {salario_novo:.2f} R$')



# A IMPORTANCIA DE 780MIL REAIS SERÁ DIVIDIDA ENTRE TRÊS GANHADORES DE UM CONCURSO. O PRIMEIRO GANHADOR RECEBERA 46%, O SEGUNDO GANHADOR RECEBERÁ 32% E O TERCEIRO GANHADOR RECEBERA O RESTANTE. CALCULE E IMPRIMA A QUANTIA GANHA POR CADA UM DOS GANHADORES:

primeiro_premio = 780_000 * (46 / 100)
segundo_premio = 780_000 * (32 / 100 )
terceiro_premio = 780_000 - primeiro_premio - segundo_premio
print(f'{primeiro_premio:.2f} R$')
print(f'{segundo_premio:.2f} R$')
print(f'{terceiro_premio:.2f} R$')



# UMA EMPRESA CONTRATA UM ENCANADOR A 30,00R$ POR DIA. FAÇA UM PROGRAMA QUE SOLICITE O NUMERO DE DIAS TRABALHADOS PELO ENCANADOR E IMPRIMA A QUANTIA LIQUIDA QUE DEVERÁ SER PAGA, SABENDO QUE SÃO DESCONTADOS 8% DE IMPOSTOS:

dias_trabalho = int(input('Quantos dias de trabalho?' ))
valor_total = dias_trabalho * 30
imposto = valor_total * (8 / 100)
valor_liquido = valor_total - imposto
print(f'Seu pagamento é de {valor_liquido:.2f}')



# FAÇA UM PROGRAMA QUE LEIA O VALOR DA HORA DE TRABALHO (EM REAIS) E NÚMERO DE HORAS TRABALHADAS NO MÊS. IMPRIMA O VALOR A SER PAGO AO FUNCIONARIO , ADICIONANDO 10% SOBRE O VALOR CALCULADO:

valor_hora = float(input('Qual o valor da sua hora de trabalho em reais? '))
horas_trabalhadas = float(input('Quantas horas trabalhadas no mes? '))
valor_total = valor_hora * horas_trabalhadas
adicional = valor_total * (10 / 100)
valor_liquido = valor_total + adicional
print(f'Seu pagamento é de {valor_liquido:.2f}R$')



# RECEBA O SALARIO-BASE DE UM FUNCIONÁRIO. CALCULE E IMPRIMA O SALARIO A RECEBER, SABENDO QUE ESSE FUNCIONARIO TEM UMA GRATIFICAÇÃO DE 5% SOBRE O SALARIO-BAS. ALEM DISSO, ELE PAGA 7% DE IMPOSTO SOBRE O SALARIO-BASE:

salario_base = float(input('Qual o valor de seu salário-base em reais? '))
gratificacao = salario_base * (5 / 100)
imposto = salario_base * (7 / 100)
valor_liquido = salario_base + gratificacao - imposto
print(f'Seu pagamento é de {valor_liquido:.2f}R$')



# ESCREVA UM PROGRAMA DE AJUDA PARA VENDEDORES. A PARTIR DO VAOR TOTAL LIDO, MOSTRE: O TOTAL A PAGAR COM DESCONTO DE 10%, O VALOR DE CADA PARCELA, NO PARCELAMENTO DE 3X SEM JUROS, A COMISSÃO DO VENDEDOR, NO CASO DA VENDA SER A VISTA (5% SOBRE O VALOR COM DESCONTO) E A COMISSÃO DO VENDEDOR, NO CASO DA VENDA SER PARCELADA (5% SOBRE O VALOR TOTAL):

preco = float(input('Qual o valor do produto? '))
desconto_avista = preco * (10 / 100)
preco_avista = preco - desconto_avista
parcela = preco / 3
comissao_avista = preco_avista * (5 / 100)
comissao_aprazo = preco * (5 / 100)
print(f'O valor a vista é de {preco_avista:.2f}R$')
print(f'A prazo, serão 3 parcelar no valor de {parcela:.2f}R$')
print(f'A comissão do vendedor na venda a vista, é de {comissao_avista:.2f}R$')
print(f'A comissão do vendedor na venda a prazo, é de {comissao_aprazo:.2f}R$')



# RECEBA A ALTURA DO DEGRAU DE UMA ESCADA E A ALTURA QUE O USUARIO ALCANÇAR SUBINDO A ESCADA. CALCULE E MOSTRE QUANTOS DEGRAUS O USUARIO DEVE SUBRIR PARA ALCANÇAR SEU OBJETIVO:

altura_degrau = float(input('Qual a altura do degrau em cm? '))
objetivo = float(input('Qual altura deseja alcançar em cm? '))
numero_degraus = objetivo / altura_degrau
print(f'Você devera subrir {numero_degraus:.2f}')