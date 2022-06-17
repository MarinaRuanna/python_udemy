
# FAÇA UM PROGRAMA QUE CONVERTA UMA LETRA MAIUSCULA EM LETRA MINUSCULA. USE A TABELA ASCII OARA RESOLVER O PROBREMA:

nome = input('Digite um nome: ')
print(nome.lower())



# FAÇA UM PROGRAMA QUE LEIA UM NUMERO INTEIRO POSITIVO DE TRES DIGITOS (DE 100 A 999). GERE OUTRO NUMERO FORMADO PELOS DIGITOS INVERTIDOS DO NUMERO LIDO:

num = input('Digite um numero de 3 digitos:' )
while not len(str(num)) == 3:
  num = input('Digite um numero de 3 digitos:')
else:
  print(str(num[::-1]))


# LEIA UM NUMERO QUATRO DIGITOS (DE 1000 A 9999). IMPRIMA UM DIGITO POR LINHA:

nums = int(input('Digite um numero de 4 digitos:' ))
while not len(str(nums)) == 4:
  nums = input('Digite um numero de 4 digitos:')
else:
  for num in nums:
    print(num)



# LEIA UM VALOR INTEIRO EM SEGUNDOS, E IMPRIMA EM HORAS, MINUTOS E SEGUNDOS:

entrada = int(input('Os segundos que deseja converter: '))
dias = entrada // 86400
seg_rest = entrada % 86400
horas = seg_rest // 36000
seg_rest = seg_rest % 36000
minutos = seg_rest // 60
seg_rest = seg_rest % 60
segundos = seg_rest

if horas >= 24:
  dias = horas // 24
  horas = horas % 24

print('{}:{}:{}:{}'.format(dias,horas,minutos,segundos))



# FAÇA UM PROGRAMA QUE LEIA O HORARIO (HORA, MINUTO E SEGUNDO) DE INICIO E A DURAÇÃO, EM SEGUNDOS, DE UMA EXPERIENCIA BIOLOGICA. O PROGRAMA DEVE RESULTAR COM O NOVO HORARIO (HORA, MINUTO E SEGUNDO) DO TERMINO DA MESMA:

print('Preencha os campos com o horario de inicio: ')
h = int(input('horas: '))
m = int(input('minutos: '))
s = int(input('segundos: '))
d = int(input(' Digite a duração da experiencia em segundos: '))

s_final = (s + d) % 60
m_final = ( m + (d + s) // 60) % 60
h_final = ( h + (m + (d + s) // 60) // 60) % 24

print(' A experiencia encerrará a {}:{}:{}'.format(h_final,m_final,s_final))



# IMPLEMENTE UM PROGRAMA QUE CALCULE O ANO DE NASCIMENTO DE UMA PESSOA A PARTIR DE SUA IDADE E DO ANO ATUAL:

idade = int(input('Digite sua idade: '))
ano_nasc = 2021 - idade
print(f' O ano do seu nascimento é {ano_nasc}.')




# ESCREVA UM PROGRAMA QUE LEIA AS COORDENADAS x E y DE PONTOS NO R² E CALCULE SUA DISTANCIA DE ORIGEM (0,0):

x = int(input('Digite a coordernada x: '))
y = int(input('Digite a coordernada y: '))
distancia = (x ** 2 + y ** 2) ** (1/2)

print(f' A distancia entre a origem e o ponto de coordenadas ({x},{y})é: {distancia:.2f}')




#  TRÊS AMIGOS JOGARAM NA LOTERIA. CASO ELES GANHEM, O PREMIO DEVE SER REPARTIDO PROPORCIONALMENTE AO VALOR QUE CADA UM DEU PARA A REALIZAÇÃO DA APOSTA. FAÇA UM PROGRAMA QUE LEIA QUANTO CADA APOSTADOR INVESTIU, O VALOR DO PREMIO, E IMPRIMA QUANTO CADA UM GANHARIA DO PREMIO COM BASE NO VALOR INVESTIDO:


valorum = int(input('Quanto o primeiro apostador pagou? '))
valordois = int(input('Quanto o segundo apostador pagou? '))
valortres = int(input('Quanto o terceiro apostador pagou? '))
valordopremio = int(input('Digite o valor do premio: '))

valordaaposta = valorum + valordois + valortres
porc_um = (valorum / valordaaposta) * 100
porc_dois = (valordois / valordaaposta) * 100
porc_tres = (valortres / valordaaposta) * 100

premioum = valordopremio * (porc_um / 100)
premiodois = valordopremio * (porc_dois / 100)
premiotres = valordopremio * (porc_tres / 100)

print('O primeiro apostador receberá {:.2f}R$, o segundo apostador receberá {:.2f}R$ e o terceiro apostador receberá {:.2f}'.format(premioum,premiodois,premiotres))



# FAÇA UM PROGRAMA PARA LER AS DIMENSÕES DE UM TERRENO (COMPRIMENTO C E LARGURA L), BEM COMO O PREÇO DO METRO DE TELA P. IMPRIMA O CUSTO PARA CERCAR ESTE MESMO TERRENO COM TELA.

c = int(input('Qual o comprimento do terreno? '))
l = int(input('Qual a largura do terreno? '))
p = int(input('Qual o preço do metro da tela? '))
custocomp = c * p
custolarg = l * p
valor_total = (custocomp * 2) + (custolarg * 2)

print('O valor total para cercar o terreno com tela é de {:.2f}R$'.format(valor_total))

