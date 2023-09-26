
def classificar_idade(age):

    """Classifica uma pessoa com base em sua idade.
        param idade: Idade da pessoa em anos, apenas números inteiros.
        return: Uma string representando a classificação.
    """
    if age is None or not isinstance(age, int) or age < 0:
        return "Erro: Insira um número inteiro!"
    if age <= 13:
        return "Criança"
    elif age <= 17:
        return "Adolescente"
    else:
        return "Adulto"

# Testando a função
print(classificar_idade(5))   # Esperado: Criança
print(classificar_idade(13))   # Esperado: Criança
print(classificar_idade(15))  # Esperado: Adolescente
print(classificar_idade(17))  # Esperado: Adolescente
print(classificar_idade(18))  # Esperado: Adulto
print(classificar_idade(25))  # Esperado: Adulto
print(classificar_idade(25.5))  # "Erro: Insira um número inteiro!"
print(classificar_idade(-10))  # "Erro: Insira um número inteiro!"
print(classificar_idade("a"))  # "Erro: Insira um número inteiro!"
