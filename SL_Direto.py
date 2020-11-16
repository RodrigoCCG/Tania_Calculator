import numpy as np 
import pandas as pd 

def Gauss(df,dim):
    """
    Realiza o calculo dos valores de x para um Sistema linear de dim variaveis e
    dim equacoes pelo metodo de eliminacao de Gauss
    Input
    df: DataFrame contendo o Sistema linear
    dim: quantidade de variaveis e equacoes
    Output:
    Tupla(df,df): Tupla com dois dataframes, o primeiro contendo o Sistema pos eliminacao e o 
    segundo contendo os valores de X. 
    Retorna uma mensagem de erro se nao foi possivel realizar a eliminacao
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

def LU(df, dim):
    """
    Realiza o calculo dos valores de x para um Sistema linear com dim variaveis e 
    dim equacoes pelo metodo de eliminacao de Fatoracao LU
    Input
    df: DataFrame contendo o Sistema linear
    dim: quantidade de variaveis e equacoes
    Output:
    Lista(df,df,df,df): Tupla com dois dataframes, o primeiro contendo a matriz L, o
    segundo contendo a matriz U, o terceiro os valores de y, e o quarto os valores de X. 
    Retorna uma mensagem de erro se nao foi possivel realizar a eliminacao
    """
    #Montar df da matriz L
    L_data=[]
    for i in range(dim):
        line=[]
        for j in range(dim):
            if j < i:
                line.append(-1)
            elif j > i:
                line.append(0)
            else:
                line.append(1)
        L_data.append(line)
    L = pd.DataFrame(data=L_data)

    #Montar df da matriz U
    U_data=[]
    for i in range(dim):
        line=[]
        for j in range(dim):
            if j < i:
                line.append(0)
            else:
                line.append(-1)
        U_data.append(line)
    U = pd.DataFrame(data=U_data)
    #Calcular L e U
    for i in range(dim):
        for j in range(dim):
            if i > j:
                val = df.iloc[i,j]
                for k in range(j):
                    val = (val-(L.iloc[i,k]*U.iloc[k,j]))
                L.iloc[i,j] = (val/U.iloc[j,j])
                print(L)
            else:
                val = df.iloc[i,j]
                for k in range(i):
                    val = (val-(L.iloc[i,k]*U.iloc[k,j]))
                U.iloc[i,j] = val
                print(U)
    #Calcular Y
    y_df = pd.DataFrame(data=range(dim),columns = ['y'])
    for i in range(dim):
        val = df.loc[i,'b']
        for j in range(i):
            val = val - (y_df.loc[j,'y']*L.iloc[i,j])
        y_df.iloc[i] = val
    x_df = pd.DataFrame(data=range(dim),columns = ['x'])
    #Calcular X
    for i in range(dim):
        k = dim-1-i
        val = y_df.iloc[k,0]
        for j in range(i):
            val = val -(U.iloc[k,dim-1-j]*x_df.iloc[dim-1-j,0])
        x_df.iloc[k,0] = val/U.iloc[k,k]
    return [L,U,y_df,x_df]