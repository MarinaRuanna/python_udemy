
# FAÇA UM PROGRAMA QUE LEIA DOIS NUMEROS E MOSTRE QUAL DELES É MAIOR:

a = int(input('Digite um numero: '))
b = int(input('Digite outro numero: '))
if a > b:
  print(a)
else:
  print(b)




# LEIA UM NUMERO FORNECIDO PELO USUARIO. SE ESSE NUMERO FOR POSITIVO, CALCULE A RAIZ QUADRADA DO NUMERO. SE O NUMERO FOR NEGATIVO, MOSTRE UMA MENSAGEM DIZENDO QUE O NUMERO É INVALIDO:

numero = int(input('Digite um numero positivo: '))
if numero <= 0:
  print('O numero digitado precisa ser positivo.')
else:
  raizquadr = numero ** (1/2)
  print(f'A raiz quadrada do numero digitado é {raizquadr:.2f}')



# LEIA UM NUMERO REAL. SE O NUMERO FOR POSITIVO, IMPRIMA A RAIZ QUADRADA. DO CONTRARIO, IIMPRIMA O NUMERO AO QUADRADO:

numero = int(input('Digite um numero positivo: '))
if numero <= 0:
  numaoquad = numero ** 2
  print(f'{numaoquad:.2f}')
else:
  raizquadr = numero ** (1/2)
  print(f'A raiz quadrada do numero digitado é {raizquadr:.2f}')



# FAÇA UM PROGRAMA QUE LEIA UM NUMERO E, CASO ELE SEJA POSITIVO, CALCULE E MOSTRE: O NUMRO DIGITADO AO QUADRADO E A RAIZ QUADRADA DO NUMERO DIGITADO:

numero = int(input('Digite um numero positivo: '))
if numero <= 0:
  print('O numero digitado precisa ser positivo.')
else:
  raizquadr = numero ** (1/2)
  numaoquad = numero ** 2
  print(f'O quadrado do numero digitado é {numaoquad:.1f} e raiz quadrada do numero digitado é {raizquadr:.2f}')



# FAÇA UM PROGRAMA QUE RECEBA UM NUMERO INTEIRO E VERIFIQUE SE ESSE NUMERO É PAR OU IMPAR:

numero = int(input('Digite um numero inteiro: '))

if numero%2:
  print(f'o numero {numero} é impar')
else:
  print(f'o numero {numero} é par')





# ESCREVA UM NUMERO QUE, DADOS DOIS NUMERO INTEIROS, MOSTRE NA TELA O MAIOR DELES ASSIM COMO A DIFERENÇA EXISTENTE ENTRE AMBOS:

a = int(input('Digite um numero: '))
b = int(input('Digite outro numero: '))
if a > b:
  diferenca = a - b
  print(f' O numero maior é o {a}, sendo a diferença entre os dois numeros igual a {diferenca}')
else:
  diferenca = b - a
  print(f' O numero maior é o {b}, sendo a diferença entre os dois numeros igual a {diferenca}')



# ESCREVA UM NUMERO QUE, DADOS DOIS NUMERO INTEIROS, MOSTRE NA TELA O MAIOR DELES. SE POR ACASO OS DOIS NUMEROS FOREM IGUAIS, IMPRIMA A MENSAGEM: 'NUMEROS IGUAIS':

a = int(input('Digite um numero: '))
b = int(input('Digite outro numero: '))
if a == b:
  print('Numeros iguais')
elif a > b:
  print(f' O numero maior é o {a}')
elif a < b:
  print(f' O numero maior é o {b}')



#  FAÇA UM PROGRAMA QUE LEIA DUAS NOTAS DE UM ALUNO, VERIFIQUE SE AS NOTAS SÃO VALIDAS E EXIBA NA TELA A MEDIA DESSAS NOTAS. UMA NOTA VALIDA DE SER, OBRIGATORIAMENTE, UM VALOR ENTRE 0.0 E 10.0, ONDE CASO A NOTA NÃO POSSUA UM VALOR VALIDO, ESTE FATO DEVE SER INFORMADO AO USUARIO E O PROGAMA ENCERRADO:

notaum = float(input('Digite a primeira nota: '))
notadois = float(input('Digite a segunda nota: '))
if notaum < 0 or notaum > 10:
  print('Valores invalidos')
elif notadois < 0 or notadois > 10:
  print('Valores invalidos')
else:
  media = (notaum + notadois) / 2
  print(f'A media das notas é {media}.')



# LEIA O SALARIO DE UM TRABALHADOS E O VALOR DA PRESTAÇÃO DE UM EMPRESTIMO. SE A PRESTAÇÃO FOR MAIOR QUE 20% DO SALARIO, IMPRIMA A MENSAGEM 'EMPRESTIMO NÃO CONCEDIDO', CASO CONTRARIO IMPRIMA: 'EMPRESTIMO CONSEDIDO':

salario = float(input('Digite o salario: '))
prestacao = float(input('Digite o valor da prestação: '))
porcentagem = (prestacao / salario) * 100
if porcentagem > 20:
  print('Emprestimno não concedido.')
elif porcentagem <= 20:
  print('Emprestimno concedido.')




# FAÇA UM PROGRAMA QUE RECEBA A ALTURA E O SEXO DE UMA PESSOA E CALCULE E MOSTRE SEU PESO IDEAL, UTILIZANDO AS SEGUINTES FORMULAS (ONDE h CORRESPONDE A ALTURA): MULHERES = (62.1 * h) - 44.7  E HOMENS = (72.7 * h) - 58:

h = float(input('Digite sua altura em metros: '))
s = input('Digite M para o sexo masculibo e F para feminino: ')

if s == 'M' or 'm':
  peso_ideal = (72.7 * h) - 58
  print(f'Seu peso ideal é {peso_ideal:.2f} kg')
elif s == 'F' or 'f':
  peso_ideal = (62.1 * h) - 44.7
  print(f'Seu peso ideal é {peso_ideal:.2f} kg')
else:
  print('Você não digitou um sexo valido')


# ESCREVA UM PROGRAMA QUE LEIA UM NUMERO INTEIRO MAIOR DO QUE ZERO E DEVOLVA, NA TELA, A SOMA DE TODOS OS SEUS ALGARISMOS. POR EXEMPLO AO NUMERO 251 CORRESPONDERÁ O VALOR 8 (2+5+1). SE O NUMERO LIDO NÃO FOR MAIOR QUE ZERO, O PROGRAMA TERMINARÁ COM A MENSAGEM: 'NUMERO INVALIDO':

n = int(input('Digite um numero inteiro maior que zero: '))

if n > 0:
  soma = 0
  while n > 0:
    digito = n % 10
    soma = soma + digito
    n = n // 10
  print(f'A soma dos digitos no numero digitado é {soma}.')

else:
  print('O numero precisa ser um inteiro positivo! ')




# LER UM NUMERO INTEIRO. SE O NUMERO LIDO FOR NEGATIVO, ESCREVA 'NUMERO INVALIDO'. SE O NUMERO FOR POSITIVO, CALCULE O LOGARITMO DESSE NUMERO:

n = int(input('Digite um numero inteiro: '))

if n < 0:
  print('Numero invalido.')

elif n> 0:
  import math
  logaritmo = math.log10(n)
  print(f'O logaritmo comum do numero digitado é {logaritmo}.')



# FAÇA UM ALGORITMO QUE CALCULE A MEDIA PONDERADA DAS NOTAS DE 3 PROVAS. A PRIMEIRA E A SEGUNDA TEM PESO 1 E A TERCEIRA TEM PESO 2. AO FINAL, MOSTRAR A MÉDIA DO ALUNO E INDICAR SE O ALUNO FOI APROVADO OU REPROVADO.A NOTA PARA APROVAÇÃO DEVE SER IGUAL OU SUPERIOR A 60 PONTOS:

num = float(input('Primeira nota: '))
ndois = float(input('Segunda nota: '))
ntres = float(input('Terceira nota: '))
mp = ((num * 1) + (ndois * 1) + (ntres * 2)) / (1 + 1 + 2)

if mp < 6:
  print('Reprovado.')

elif mp >= 6:
  print('Aprovado.')



# A NOTA FINAL DE UM ESTUDANTE É CALCULADA A PARTIR DE TRÊS NOTAS ATRIBUIDAS ENTRE O  INTERVALO DE 0 ATÉ 10, RESPECTIVAMENTE,A UM TRABALHO DE LABORATORIO, A UMA AVALIAÇÃO SEMESTRAL E UM EXAME FINAL. a MÉDIA DAS TRES NOTAS MENCIONADAS ANTERIORMENTE OBEDECE AOS PESOS: TRABALHO DE LABORATORIO * 2; AVALIAÇÃO SEMESTRAL * 3; EXAME FINAL 5. DE ACORDO COM O RESULTADO, MOSTRE NA TELA SE O ALUNO ESTA REPROVADO (MEDIA ENTRE 0,0 E 2,9), DE RECUPERAÇÃO (MEDIA DE 3,0 A 4,9) OU FOI APROVADO. FAÇA TODAS AS VERIFICAÇÕES NECESSARIAS:

trab = float(input('Digite a nota do trabalho de laboratorio: '))
aval = float(input('Digite a nota da avaliação semestral: '))
final = float(input('Digite a nota do exame final: '))
mp = ((trab *2) + (aval * 3) + (final * 5)) / ( 2 + 3 + 5)

if trab < 0:
  print('A nota do trabalho de laboratorio é invalida')
elif aval < 0:
  print('A nota da avaliação semestral é invalida')
elif final < 0:
  print('A nota da avaliação final é invalida')

elif trab > 10:
  print('A nota do trabalho de laboratorio é invalida')
elif aval > 10:
  print('A nota da avaliação semestral é invalida')
elif final > 10:
  print('A nota da avaliação final é invalida')

elif mp <= 2.9:
  print('Reprovado')
elif mp <= 4.9:
  print('Recuperação')
elif mp >= 5:
  print('Aprovado')


# USANDO SWITCH, ESCREVA UM PROGRAMA QUE LEIA UM INTEIRO ENTRE 1 E 7 E IMPRIMA O DIA DA SEMANA CORRESPODENTE A ESSE NUMERO. ISTO É, DOMINFO É 1, SEGUNDA 2, E ASSIM POR DIANTE:

def meu_switch(opcao):
    opcoes = {
        1: "Domingo",
        2: "Segunda",
        3: "Terça",
        4: "Quarta",
        5: "Quinta",
        6: "Sexta",
        7: "Sabado",
    }
    return opcoes.get(opcao, "Opção inválida.")

if __name__ == "__main__":
    opcao = int(input("Informe um número de 1 a 7: "))
    print (meu_switch(opcao))




# USANDO SWITCH, ESCREVA UM PROGRAMA QUE LEIA UM INTEIRO ENTRE 1 E 12 E IMPRIMA O MES CORRESPODENTE A ESSE NUMERO. ISTO É, JANEIRO É 1, FEVEREIRO É 2, E ASSIM POR DIANTE:

def meu_switch(opcao):
    opcoes = {
        1: "Janeiro",
        2: "Fevereiro",
        3: "Março",
        4: "Abril",
        5: "Maio",
        6: "Junho",
        7: "Julho",
        8: "Agosto",
        9: "Setembro",
        10: "Outubro",
        11: "Novembro",
        12: "Dezembro",
    }
    return opcoes.get(opcao, "Opção inválida.")

if __name__ == "__main__":
    opcao = int(input("Informe um número de 1 a 12: "))
    print (meu_switch(opcao))


# FAÇA UM PROGRAMA QUE CALÇCULE E MOSTRE A ÁREA DO TRAPEZIO. SABE-SE QUE: A = (basemaior + basemenor) * altura / 2 LEMBRE-SE A BASEMAIOR E A BASEMENOR DEVEM SER NUMEROS MAIORES QUE ZERO.

basemaior = float(input('Qual o comprimeto da base maior? '))
basemenor = float(input('Qual o comprimeto da base menor? '))

# FAÇA UM PROGRAMA QUE MOSTRE AO USUARIO UM MENU COM 4 OPÇOES DE OPERAÇÕES MATEMATICAS (AS BASICAS POR EXEMPLO). O USUARIO ESCOLHE UMA DAS OPÇÕES E O SEU PROGRAMA ENTÃO PEDE DOIS VALORES NUMERICOS E REALIZA A OPERAÇÃO, MOSTRANDO O RESULTADO E SAINDO:


# FAÇA UM PROGRAMA PARA VERIFICAR SE UM DETERMINADO NUMERO É DIVISIVEL POR 3 OU 5, MAS NÃO SIMULTANEAMENTE PELOS DOIS:


# DADOS TRES VALORES, A, B, C, VERIFICAR SE ELES PODEM SER VALORES DOS LADOS DE UM TRIANGULO, E SE FOREM, SE É UM TRINGULO ESCALENO, TRIANGULO EQUILÁTERO OU TRIANGULO ISOCELES, CONSIDERANDO OS SEGUINTES CONCEITOS:

'''
1. O COMPRIMENTO DE CADA LADO DE UM TRIANGULO É MENOR DO QUE A SOMA DOS OUTROS DOIS LADOS. 
2. CHAMA-SE EQUILATERO UM TRIANGULO COM OS TRES LADOS IGUAIS.
3. ISOCELES É O TRIANGULO QUE TEM O COMPRIMENTO DE 2 LADOS IGUAIS. 
4. ESCALENO É O TRIANGULO COM OS TRES LADOS DIFERENTES:
'''

# ESCREVA O MENU DE OPÇÕES ABAIXO. LEIA A OPÇÃO DO USUARIO E EXECUTE A OPERAÇÃO ESCOLHIDA. ESCREVA UMA MENSAGEM DE ERRO SE A OPÇÃO FOR INVALIDA:

'''
ESCOLHA UMA OPÇAO:
1. SOMA DE DOIS NUMEROS 
2. DIFERENÇA ENTRE DOIS NUMEROS (MAIOR PELO MENOR)
3. PRODUTO ENTRE 2 NUMEROS
4. DIVISÃO ENTRE DOIS NUMEROS (O DENOMINADOR NÃO PODE SER ZERO)
'''

# LEIA A IDADE E O TEMPO DE SERVIÇO DE UM TRABALHADOR E ESCREVA SE ELE PODE OU NÃO SE APOSENTAR. AS CONDIÇÕES PARA A APOSENTADORIA SÃO:
'''
1. TER PELO MENOS 65 ANOS
2. OU TER TRABALHADO POR PELO MENOS 30 ANOS
3. OU TER PELO MENOS 60 ANOS E TER TRABALHADO PELO MENOS 25 ANOS
'''

# DETERMINE SE DETERMINADO ANO É BISSEXTO. SENDO QUE UM ANO É BISSEXTO SE FOR DIVISIVEL POR 400 OU SE FOR DIVISIVEL POR 4 E NÃO FOR DIVISIVEL POR 100. POR EXEMPLO: 1988, 1992, 1996:


# UMA EMPRESA VENDE O MESMO PRODUTO PARA QUATRO DIFERENTES ESTADOS. CADA ESTADO POSSUI UMA TAXA DIFERENTE DE IMPOSTO SOBRE O PRODUTO (MG 7%, SP 12%, RJ 15%, MS 8%). FAÇA UM PROGRAMA EM QUE O USUARIO  ENTRE COM O VALOR E O ESTADO DE DESTINO DO PRODUTO E O PROGRAMA RETORNE O PREÇO FINAL DO PRODUTO ACRESCIDO DO IMPOSTO DO ESTADO EM QUE ELE FOI VENDIDO.  SE O ESTADO DIGITADO NÃO FOR VALIDO, MOSTRAR UMA MENSAGEM DE ERRO:


# CALCULE AS RAIZES DA EQUAÇÃO DE SEGUNDO GRAU: