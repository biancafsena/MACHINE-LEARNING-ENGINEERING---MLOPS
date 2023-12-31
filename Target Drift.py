# -*- coding: utf-8 -*-
"""Target Drift.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qKOa371G6DKmgVMnWgDiIpAj3bZwtDL0
"""

import pandas as pd
import numpy as np

def detectar_desvio(df):
    """
    Detecta desvios significativos entre as colunas 'spent' e 'expected' em um DataFrame.
    Retorna um DataFrame contendo as entradas com desvios significativos.

    Parameters:
    - df (pd.DataFrame): DataFrame contendo as colunas 'spent' e 'expected'.

    Returns:
    - pd.DataFrame: DataFrame contendo as entradas com desvios significativos.
    """
    df['deviation'] = np.abs(df['spent'] - df['expected'])
    threshold = 0.1 * df['expected']
    significant_deviation = df[df['deviation'] > threshold]
    return significant_deviation

def main():
    data_url = 'https://storage.googleapis.com/ds-publico/IA/MonitoringDrifts.csv'
    df = pd.read_csv(data_url, delimiter=",")

    significant_deviation = detectar_desvio(df)

    if not significant_deviation.empty:
        print("Desvio significativo detectado. Possível calibração necessária.")
        cols_to_display = ['month', 'class_choosen', 'class_predicted', 'spent', 'expected', 'deviation']
        print(significant_deviation[cols_to_display])
    else:
        print("Nenhum desvio significativo detectado.")

if __name__ == "__main__":
    main()