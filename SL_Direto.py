import numpy as np 
import pandas as pd 

def Gauss(df,dim):
    """
    Realiza o calculo dos valores de x para um Sistema linear dim variaveis e dim equacoes pelo metodo
    de eliminacao de Gauss
    Input
    df: DataFrame contendo o Sistema linear
    dim: quantidade de variaveis e equacoes
    Output:
    Tupla(df,df): Tupla com dois dataframes, o primeiro contendo o Sistema pos eliminacao e o 
    segundo contendo os valores de X. Retorna uma mensagem de erro se nao foi possivel realizar a
    eliminacao
    """
    #Cria o dataset de solucao do problema
    res = pd.DataFrame(data = df)
    x_df = pd.DataFrame(data=range(dim),columns = ['x'])
    g_res = pd.DataFrame(data = df)

    for i in range(dim):
        #seleciona o menor pivot
        res = res.sort_values(by=['x'+str(i)],ignore_index=True)
        inserted = False
        for j in range(dim):
            if res.iloc[j,i] != 0:
                #Realizar a eliminacao
                for k in range(j+1,dim):
                    res.iloc[k] = res.iloc[k].sub(res.iloc[j].mul(res.iloc[k,i]).div(res.iloc[j,i]))
                g_res.iloc[i] = res.iloc[j]
                res.at[j,0:dim]=0
                inserted = True
                break
        if not inserted:
            return ("ERRO","Nao foi possivel selecionar um pivo")
    res = g_res
    for i in range(dim):
        #Calcular os valores de X
        x_index = dim-1-i
        j = dim-1
        soma = res.loc[x_index,'b']
        while j != x_index:
            soma -= res.iloc[x_index,j]*x_df.iloc[j]
            j -= 1
        x_df.loc[x_index] = soma/res.iloc[x_index,j]


    return (res,x_df)