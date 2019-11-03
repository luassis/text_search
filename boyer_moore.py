"""
Algoritmo de Busca - Boyer Moore

Objetivo: Comparar os caracteres de dois textos e verificar se existe String Matching

Entrada:
Texto: Texto para realizar a busca
Padrão: String de busca
"""


# Entrada de dados
print('Informe o padrão: ')
s_padrao = input()

print('Informe o texto: ')
s_texto = input()


# Função que calcula a tabela de saltos para cada caractere presente no texto padrão
def calcula_tabela_saltos(padrao):

    tam = len(padrao)
    i = 1

    # Dicionário que deve conter os valores dos saltos de cada caractere
    tabela_saltos = {'outros': tam}

    for indice, char in enumerate(padrao):
        if indice < len(padrao) - 1:
            tabela_saltos[char] = tam - i
        else:
            if char not in tabela_saltos:
                tabela_saltos[char] = tam
        i += 1
    print(f'Tabela de saltos: {tabela_saltos}')
    print('')
    return tabela_saltos


def consulta_valor_dicionario(caractere, tabela_saltos):
    if caractere in tabela_saltos:
        return tabela_saltos.get(caractere)
    else:
        return tabela_saltos.get("outros")


def busca_bm_primeira_ocorrencia(padrao, texto, tabela_saltos):

    tam = len(padrao)
    posicao = tam - 1

    while posicao < len(texto):
        print(f'posicao do texto: {posicao}')
        if padrao[tam-1] != texto[posicao]:
            salto = consulta_valor_dicionario(texto[posicao], tabela_saltos)
            print(f'caractere: {texto[posicao]}, salto: {salto}')
            posicao += salto
        else:
            inicio = posicao-tam+1
            fim = posicao+1
            sub_texto = texto[inicio:fim]
            if sub_texto == padrao:
                return inicio
            else:
                salto = consulta_valor_dicionario(texto[posicao], tabela_saltos)
                print(f'caractere: {texto[posicao]}, salto: {salto}')
                posicao += salto
        print('')
    return -1


def busca_bm_todas_ocorrencias(padrao, texto, tabela_saltos):

    tam = len(padrao)
    posicao = tam - 1
    retorno = []

    while posicao < len(texto):
        print(f'posicao do texto: {posicao}')
        if padrao[tam-1] != texto[posicao]:
            salto = consulta_valor_dicionario(texto[posicao], tabela_saltos)
            print(f'caractere: {texto[posicao]}, salto: {salto}')
            posicao += salto
        else:
            inicio = posicao-tam+1
            fim = posicao+1
            sub_texto = texto[inicio:fim]
            if sub_texto == padrao:
                retorno.append(inicio)
                posicao += 1
            else:
                salto = consulta_valor_dicionario(texto[posicao], tabela_saltos)
                print(f'caractere: {texto[posicao]}, salto: {salto}')
                posicao += salto
        print('')
    return retorno


tabela = calcula_tabela_saltos(s_padrao)

ocorrencia = busca_bm_primeira_ocorrencia(s_padrao, s_texto, tabela)
if ocorrencia == -1:
    print('Não existe ocorrência do padrão do texto')
else:
    print(f'O padrão foi encontrado no texto na posição: {ocorrencia}')


ocorrencias = busca_bm_todas_ocorrencias(s_padrao, s_texto, tabela)
if len(ocorrencias) == 0:
    print('Não existem ocorrências do padrão do texto')
else:
    print(f'O padrão foi encontrado no texto nas posições: {ocorrencias}')

