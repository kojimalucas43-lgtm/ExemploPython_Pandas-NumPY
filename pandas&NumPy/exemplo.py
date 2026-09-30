import pandas as pd
import numpy as np

dados = pd.read_excel("dados_exemplo.xlsx")
# display(dados) tudo
# dados.head() primeiros
# dados.tail() ultimos

# analise da estrtura da tabela -->
#print("\nQuantidade de linhas e colunas: ", dados.shape)
#print("\nNome das colunas: ", dados.columns)
#print("\nTipos de dados: ", dados.dtypes)
#print("\nInformações Gerais: ")
#dados.info()

# esse bang aí remove espaços e transforma os nomes em letras minusculas -->
#dados.columns = (
    #dados.columns
    ##.str.lower()
#)
#display(dados)

#Para limpar o nome dos alunos
#dados["aluno"] = (
#    dados["aluno"]
#    .astype("string")
#    .str.strip()
#    .str.title()
#)


# localizar dados ausentes
# print("Valores ausentes por coluna:")
# print(dados.isna().sum())


# Para visualizar as linhas com notas ausentes:
# linhas_incompletas = dados[
#     dados[["nota1", "nota2"]].isna().any(axis=1)
# ]
# display(linhas_incompletas)


# As notas ausentes serão substituídas pela média da respectiva coluna.
# media_nota1 = dados["nota1"].mean()
# media_nota2 = dados["nota2"].mean()


# dados["nota1"] = dados["nota1"].fillna(media_nota1)
# dados["nota2"] = dados["nota2"].fillna(media_nota2)
# Verificação:
# print(dados.isna().sum())


# As notas devem estar entre 0 e 10.
# notas_invalidas = dados[
#     ~dados["nota1"].between(0, 10) |
#     ~dados["nota2"].between(0, 10)
# ]


# display(notas_invalidas)
# Para limitar valores ao intervalo entre 0 e 10:
# dados["nota1"] = dados["nota1"].clip(0, 10)
# dados["nota2"] = dados["nota2"].clip(0, 10)


# calcular a média dos alunos
# dados["media"] = np.mean(
#     dados[["nota1", "nota2"]],
#     axis=1
# )


# dados["media"] = dados["media"].round(2)


# definir a situação
# dados["situacao"] = np.where(
#     dados["media"] >= 6,
#     "Aprovado",
#     "Reprovado"
# )
# Com três situações:
# condicoes = [
#     dados["media"] >= 6,
#     dados["media"] >= 4
# ]


# resultados = [
#     "Aprovado",
#     "Recuperação"
# ]
