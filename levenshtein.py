# -*- coding: utf-8 -*-

"""
Algoritmo de similaridade - Levenshtein
"""

import numpy as np

print('Informe o primeiro texto: ')
string1 = input()
print('Informe o segundo texto: ')
string2 = input()


def levenshtein_caractere(s1, s2):
    m = len(s1) + 1
    n = len(s2) + 1

    matriz = np.zeros((m, n))

    for i in range(0, m):
        matriz[i][0] = i

    for i in range(0, n):
        matriz[0][i] = i

    for i in range(1, m):
        for j in range(1, n):
            if s1[i - 1] == s2[j - 1]:
                matriz[i, j] = min(
                    matriz[i - 1, j] + 1,
                    matriz[i - 1, j - 1],
                    matriz[i, j - 1] + 1
                )
            else:
                matriz[i, j] = min(
                    matriz[i - 1, j] + 1,
                    matriz[i - 1, j - 1] + 1,
                    matriz[i, j - 1] + 1
                )
    print(matriz)
    distancia = (matriz[m - 1, n - 1])
    print('Distância de Levenshtein: ', distancia)
    return distancia


def levenshtein_palavra(s1, s2):
    l1 = s1.split(' ')
    l2 = s2.split(' ')
    # print(l1)
    # print(l2)
    m = len(l1) + 1
    n = len(l2) + 1

    matriz = np.zeros((m, n))

    for i in range(0, m):
        matriz[i][0] = i

    for i in range(0, n):
        matriz[0][i] = i

    for i in range(1, m):
        for j in range(1, n):
            if l1[i - 1] == l2[j - 1]:
                matriz[i, j] = min(
                    matriz[i - 1, j] + 1,
                    matriz[i - 1, j - 1],
                    matriz[i, j - 1] + 1
                )
            else:
                matriz[i, j] = min(
                    matriz[i - 1, j] + 1,
                    matriz[i - 1, j - 1] + 1,
                    matriz[i, j - 1] + 1
                )
    # print(matriz)
    distancia = (matriz[m - 1, n - 1])
    # print('Tamanho texto1: ', m - 1)
    # print('Tamanho texto2: ', n - 1)
    # print('Distância de Levenshtein: ', distancia)
    return distancia, m-1, n-1


def remover_acentos(texto):
    texto = texto.replace('á', 'a')
    texto = texto.replace('à', 'a')
    texto = texto.replace('ã', 'a')
    texto = texto.replace('é', 'e')
    texto = texto.replace('ê', 'e')
    texto = texto.replace('í', 'i')
    texto = texto.replace('ó', 'o')
    texto = texto.replace('ô', 'o')
    texto = texto.replace('õ', 'o')
    texto = texto.replace('ú', 'u')
    return texto


def remover_caracteres_especiais(texto):
    texto = texto.replace('-', '')
    texto = texto.replace('ª', '')
    texto = texto.replace('º', '')
    texto = texto.replace('#', '')
    texto = texto.replace('"', '')
    texto = texto.replace("'", '')
    texto = texto.replace('<', '')
    texto = texto.replace('>', '')
    texto = texto.replace('(', '')
    texto = texto.replace(')', '')
    texto = texto.replace('‘', '')
    texto = texto.replace('’', '')
    texto = texto.replace('“', '')
    texto = texto.replace('”', '')
    texto = texto.replace('/', '')
    return texto


def remover_sinais_pontuacao(texto):
    texto = texto.replace(',', '')
    texto = texto.replace(';', '')
    texto = texto.replace(':', '')
    texto = texto.replace('?', '.')
    texto = texto.replace('!', '.')
    return texto


def remover_palavras_simples(texto):
    texto = texto.replace(' a ', ' ')
    texto = texto.replace(' e ', ' ')
    texto = texto.replace(' o ', ' ')
    texto = texto.replace(' ao ', ' ')
    texto = texto.replace(' da ', ' ')
    texto = texto.replace(' de ', ' ')
    texto = texto.replace(' do ', ' ')
    texto = texto.replace(' das ', ' ')
    texto = texto.replace(' dos ', ' ')
    texto = texto.replace(' em ', ' ')
    texto = texto.replace(' na ', ' ')
    texto = texto.replace(' no ', ' ')
    texto = texto.replace(' nas ', ' ')
    texto = texto.replace(' nos ', ' ')
    texto = texto.replace(' um ', ' ')
    texto = texto.replace(' uns ', ' ')
    texto = texto.replace(' uma ', ' ')
    texto = texto.replace(' umas ', ' ')
    return texto


def limpar_texto(texto):
    texto = texto.lower()
    texto = remover_acentos(texto)
    texto = remover_caracteres_especiais(texto)
    texto = remover_sinais_pontuacao(texto)
    texto = remover_palavras_simples(texto)
    return texto


def compara_textos(texto1, texto2):
    texto1 = limpar_texto(texto1)
    texto2 = limpar_texto(texto2)

    print('Tamanho do texto1: ', len(texto1))
    print('Tamanho do texto2: ', len(texto2))
    print('')

    lista1 = texto1.split('. ')
    lista2 = texto2.split('. ')

    print('Quantidade de frases do texto1: ', len(lista1))
    print('Quantidade de frases do texto2: ', len(lista2))
    print('')

    lista_similaridade = []

    for i in range(0, len(lista1)):
        d_max = 1000
        posicao_j = 0
        qt_palavras1 = 0
        qt_palavras2 = 0
        print(lista1[i])
        for j in range(0, len(lista2)):
            # print(lista2[j])
            distancia, m, n = levenshtein_palavra(lista1[i], lista2[j])
            if distancia < d_max:
                d_max = distancia
                posicao_j = j
                qt_palavras1 = m
                qt_palavras2 = n
        percent_distancia = (d_max / qt_palavras1) * 100
        percent_similaridade = 100 - percent_distancia
        lista_similaridade.append([qt_palavras1, percent_similaridade])
        print('Frase com maior similaridade:')
        print(lista2[posicao_j])
        print(f'Quantidade de palavras da frase {i + 1}: {qt_palavras1}')
        print(f'Quantidade de palavras da frase {posicao_j + 1}: {qt_palavras2}')
        print('Distância Mínima: ', d_max)
        print('Percentual de similaridade: ', percent_similaridade)
        print('')

    peso = 0
    soma = 0
    for i in range(0, len(lista_similaridade)):
        peso = peso + lista_similaridade[i][0]
        soma = soma + (lista_similaridade[i][0] * lista_similaridade[i][1])
    media_ponderada = soma / peso
    print('')
    print('Lista de similaridades: ', lista_similaridade)
    print('Similaridade total entre os textos: ', media_ponderada)


compara_textos(string1, string2)



