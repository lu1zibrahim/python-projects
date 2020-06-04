def contar_caracteres(s):
    """ 
    Função que conta os caracteres de uma string
    ex:
    >>> contar_caracteres('luiz')
    i: 1
    l: 1
    u: 1
    z: 1
    >>> contar_caracteres('banana')
    a: 3
    b: 1
    n: 2

    """

    caracteres_ordenados = sorted(s)

    caracter_anterior = caracteres_ordenados[0]
    contagem = 1

    for caracter in caracteres_ordenados[1:]:
        if caracter == caracter_anterior:
            contagem += 1
        else:
            print(f'{caracter_anterior}:{contagem}')
            caracter_anterior = caracter
            contagem = 1
            
    print(f'{caracter_anterior}: {contagem}')


if __name__ == '__main__':
    contar_caracteres('luiz')
    print('\n')
    contar_caracteres('banana')