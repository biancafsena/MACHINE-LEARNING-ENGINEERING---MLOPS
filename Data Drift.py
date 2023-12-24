# -*- coding: utf-8 -*-
"""Atividades em Aula - Encontro 4 - Tarefa 03 - Data Drift.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xaCyGc7EZ9L1p_h4fe63FgEojOFhCvgL
"""

# Parte 1: Importação de Bibliotecas e Obtenção de Dados

!git clone https://github.com/elthonf/azure-ml.git

import numpy as np
import pandas as pd
import math, random, json
from scipy.stats.stats import pearsonr
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots



#Parte 2: Data Drift e Funções Auxiliares

# Função describe e describe_cols

# Obtenção da referência (baseline)
mybase = pd.read_csv("./azure-ml/datasets/statistical/BaseDefault01.csv")
mybase_metadata = describe(mybase)
mybase_counts = describe_cols(mybase, mybase_metadata)

# Obtenção dos scorings atuais
myactual = pd.read_csv("./azure-ml/datasets/statistical/BaseMesAtual.csv")
myactual_metadata = describe(myactual)
myactual_counts = describe_cols(myactual, myactual_metadata)



# Funções relacionadas ao Data Drift

# Avaliação global
mystats = {}
for c in list(mybase_metadata.index):
    mystats[c] = {}
    mystats[c][f"dtypes"] = mybase_metadata.loc[c, "dtypes"]
    for m in ["nunique", "mean", "50%", "std"]:
        mystats[c][f"{m}.base"] = mybase_metadata.loc[c, m]
        mystats[c][f"{m}.actual"] = pd.NA if c not in list(myactual_metadata.index) else myactual_metadata.loc[c, m]
        mystats[c][f"{m}.var"] = (mystats[c][f"{m}.actual"] - mystats[c][f"{m}.base"] ) / (mystats[c][f"{m}.base"] or pd.NA)

mystats = pd.DataFrame(mystats)



# Parte 3: Análise de Data Drift Coluna a Coluna


# Análise de Data Drift para a coluna 'renda'
h0, h1, h2 = display_histogram('renda')
h2.show()
h1.show()
display_boxplot("renda").show()
p0, p1 = display_percentis('renda')
p1.show()

# Análise de Data Drift para a coluna 'idade'
h0, h1, h2 = display_histogram('idade')
h2.show()
h1.show()
display_boxplot("idade").show()
p0, p1 = display_percentis('idade')
p1.show()

# Análise de Data Drift para colunas categóricas
for c in ['etnia', 'sexo', 'casapropria', 'outrasrendas', 'estadocivil', 'escolaridade']:
    h0, h1 = display_histogramc(c, show=False)
    h1.show()

"""Resultados de Data Drift para algumas colunas específicas, como 'renda' e 'idade', bem como para colunas categóricas como 'etnia', 'sexo', 'casapropria', 'outrasrendas', 'estadocivil' e 'escolaridade'.



***Renda:***

Observamos mudanças significativas na distribuição da coluna 'renda', conforme mostrado nos histogramas, boxplot e análise de percentis. A variação pode indicar uma mudança no perfil econômico da população.



***Idade:***

Da mesma forma, a coluna 'idade' mostra variações na distribuição, sugerindo mudanças na faixa etária dos dados.



**Colunas Categóricas:**
As colunas categóricas também exibem variações nas distribuições. Isso pode indicar mudanças na composição demográfica ou em outros fatores relevantes.
Conclusão Geral:
Considerando que a tolerância para Data Drift é de 15% em comparação com a distribuição de referência, observamos variações superiores a esse limite em várias colunas. Essas mudanças são significativas e podem impactar a capacidade do modelo de generalizar para novos dados.



**Recomendação:**

Diante das mudanças observadas, é recomendável realizar um novo treinamento do modelo. As variações nas distribuições podem afetar a qualidade das previsões do modelo, e a atualização com dados mais recentes é necessária para manter a eficácia do modelo em ambientes em constante mudança.
"""