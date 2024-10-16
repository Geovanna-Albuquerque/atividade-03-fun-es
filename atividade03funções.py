# Crie duas funções:
# - calcular_area_base, que recebe o raio de um círculo e retorna sua área.
# - calcular_volume_cilindro, que utiliza a função calcular_area_base para calcular o volume de um cilindro dado o raio e a altura.

import math

def calcular_area_base(raio):
    """Calcula a área da base de um círculo dado seu raio."""
    area = math.pi * (raio ** 2)
    return area

def calcular_volume_cilindro(raio, altura):
    """Calcula o volume de um cilindro dado o raio da base e a altura."""
    area_base = calcular_area_base(raio)
    volume = area_base * altura
    return volume