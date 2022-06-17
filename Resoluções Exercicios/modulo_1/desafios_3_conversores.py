
# CONVERSOR DE GRAUS CELSIUS PARA FAHRENHEIT

temperatura_celsius = float(input('Digite a temperatura em graus Celsius '))
temperatura_fahrenheit = temperatura_celsius * (9.0 / 5.0) + 32.2
print(f' {temperatura_fahrenheit:.2f} Fahrenheit')


# CONVERSOR DE FAHRENHEIT PARA CELSIUS

temperatura_fahrenheit = float(input('Digite a temperatura em graus Fahrenheit' ))
temperatura_celsius = 5.0 * (temperatura_fahrenheit - 32.0) / 9.0
print(f' {temperatura_celsius:.2f} Celsius')


# CONVERSOR DE KENVIN PARA CELSIUS

temperatura_kelvin = float(input('Digite a temperatura em graus Kelvin' ))
temperatura_celsius = temperatura_kelvin - 273.15
print(f' {temperatura_celsius:.2f} Celsius')


# CONVERSOR DE CELSIUS PARA KELVIN

temperatura_celsius = float(input('Digite a temperatura em graus Celsius: '))
temperatura_kelvin = temperatura_celsius + 273.15
print(f' {temperatura_kelvin:.2f} Kelvin')


# CONVERSOR DE KM POR HR PARA METROS POR SEG

velocidade_km_hr = float(input('Qual sua velocidade em km/hr?' ))
velocidade_m_s = (velocidade_km_hr / 3.6)
print(f'Sua velocidade em metros por segundo é {velocidade_m_s:.2f} m/s')


# CONVERSOR DE METROS POR SEG PARA KM POR HR

velocidade_m_s = float(input('Qual sua velocidade em m/s?' ))
velocidade_km_hr = (velocidade_m_s * 3.6)
print(f'Sua velocidade em km por hora é {velocidade_km_hr:.2f} km/hr')


# CONVERSOR DE DISTANCIA EM MILHAS PARA KM

distancia_milhas = float(input('Qual sua distancia em milhas? '))
distancia_km = distancia_milhas * 1.61
print(f' Sua distancia é de {distancia_km:.2f} km')


# CONVERSOR DE DISTANCIA EM KM PARA MILHAS

distancia_km = float(input('Qual sua distancia em quilometros? '))
distancia_milhas = distancia_km / 1.61
print(f' Sua distancia é de {distancia_milhas:.2f} milhas')


# CONVERSOR GRAUS EM RADIANOS

valor_graus = float(input('Digite valor em graus: '))
pi = 3.14
valor_radianos = valor_graus * pi / 180
print(f'{valor_radianos:.1f} radianos')


# CONVERSOR RADIANOS EM GRAUS

valor_radiano = float(input('Digite valor em radiano: '))
pi = 3.14
valor_graus = valor_radiano * 180 / pi
print(f'{valor_graus:.1f}graus')


# CONVERSOR POLEGADAS PARA CM

polegadas = float(input('Digite o comprimeto em polegadas: '))
centimetros = polegadas * 2.54
print(f' o comprimento é {centimetros:.2f} centímetros')


# CONVERSOR CM PARA POLEGADAS

centimetros = float(input('Digite o comprimeto em centimetros: '))
polegadas = centimetros / 2.54
print(f' o comprimento é {polegadas:.2f} polegadas')


# CONVERSOR DE METROS CUBICOS PARA LITROS

metros_cubicos = float(input('Digite o volume em m³: '))
litros = metros_cubicos * 1000
print(f'{litros:.2f} litros')


# CONVERSOR DE METROS CUBICOS PARA LITROS

litros = float(input('Digite o volume em litros: '))
metros_cubicos = litros / 1000
print(f'{metros_cubicos:.2f} m³')


# CONVERSOR QUILOGRAMAS PARA LIBRAS

quilogramas = float(input('Digite o peso em quilogramas: '))
libras = quilogramas / 0.45
print(f'{libras:.2f} lb')


# CONVERSOR QUILOGRAMAS PARA LIBRAS

libras = float(input('Digite o peso em libras: '))
quilogramas = libras * 0.45
print(f'{quilogramas:.2f} kg')


# CONVERSOR DE JARDAS PARA METROS

jardas = float(input('Digite a distancia em jardas: '))
metros =  jardas * 0.91
print(f'{metros:.2f} metros')


# CONVERSOR DE METROS PARA JARDAS

metros = float(input('Digite a distancia em metros: '))
jardas =  metros / 0.91
print(f'{jardas:.2f} jardas')


# CONVERSOR DE METROS QUADRADOS EM ACRES

metros_quadrados = float(input('Digite a area em m²: '))
acre = metros_quadrados * 0.000247
print(f'{acre:.2f} acres')

# CONVERSOR DE ACRES EM METROS QUADRADOS

acres = float(input('Digite a area em m²: '))
metros_quadrados = acres * 4048.58
print(f'{metros_quadrados:.2f} m²')


# CONVERSOR METROS QUADRADOS EM HECTARES

metros_quadrados = float(input('Digite a area em m²: '))
hectares = metros_quadrados * 0.0001
print(f'{hectares:.2f} hectares')


# CONVERSOR HECTARES EM METROS QUADRADOS

hectares = float(input('Digite a area em hectares: '))
metros_quadrados = hectares * 1000
print(f'{metros_quadrados:.2f} m²')


# CONVERSOR DE REAL PARA DOLAR

real = float(input('Digite o valor em reais: '))
dolar = real * 5.65
print(f'{dolar:.2f} doláres')

