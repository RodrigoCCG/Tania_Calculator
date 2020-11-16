import numpy as np 
import pandas as pd 

def Jacobi(df,dim,x0,prec):
    """
    Realiza o calculo dos valores de x para um Sistema linear com dim variaveis e 
    dim equacoes pelo metodo Iterativo Gauss Jacobi
    Input
    df: DataFrame contendo o Sistema linear
    dim: quantidade de variaveis e equacoes
    x0: DataFrame contendo os valores iniciais de x0
    prec: float contendo o valor da precisao
    Output:
    Lista(df,df,df): Lista com tres dataframes, o primeiro contendo a matriz C, o
    segundo contendo a matriz g, e o terceiro os valores de X solucao. 
    Retorna uma mensagem de erro se nao foi possivel utilizar o metodo
    """
    for i in range(dim):
        if df.iloc[i,i] == 0:
            return ("ERRO","Matriz invalida para este metodo.","ERRO")
    xk = pd.DataFrame(data=x0,index=range(dim),columns=['x'])
    xk1 = pd.DataFrame(index=range(dim),columns=['x'])
    C= pd.DataFrame(columns=range(dim), index= range(dim))
    g = pd.DataFrame(index=range(dim),columns=['x'])
    alfa = 0
    for i in range(dim):
        for j in range(dim):
            if i == j:
                C.iloc[i,j] = 0
            else:
                C.iloc[i,j] = df.iloc[i,j]/df.iloc[i,i] 
                if C.iloc[i,j] > 0 and C.iloc[i,j] > alfa:
                    alfa = C.iloc[i,j]
                elif -C.iloc[i,j] >alfa:
                    alfa = -C.iloc[i,j]
                if alfa >= 1:
                    return ("ERRO","Nao Converge","Alfa = "+str(alfa))
    for i in range(dim):
        g.loc[i,'x'] = df.loc[i,'b']/df.iloc[i,i] 
    max_k = prec+1
    while max_k > prec:
        xk1 = g.sub(C.dot(xk))
        max_k = 0
        for i in range(dim):
            next_k = xk1.loc[i,'x'] - xk.loc[i,'x'] 
            if next_k < 0: next_k = -next_k
            if next_k > max_k: max_k = next_k
        xk = xk1
    return [C,g,xk]

def Seidel(df,dim,x0,prec):
    """
    Realiza o calculo dos valores de x para um Sistema linear com dim variaveis e 
    dim equacoes pelo metodo Iterativo Gauss Seidel
    Input
    df: DataFrame contendo o Sistema linear
    dim: quantidade de variaveis e equacoes
    x0: DataFrame contendo os valores iniciais de x0
    prec: float contendo o valor da precisao
    Output:
    Lista(df): Retorna os valores de xk resultante da aplicacao do metodo
    Retorna uma mensagem de erro se nao foi possivel utilizar o metodo
    """
    for i in range(dim):
        if df.iloc[i,i] == 0:
            return ("ERRO","Matriz invalida para este metodo.","ERRO")
    xk = pd.DataFrame(data=x0,index=range(dim),columns=['x'])
    xk1 = pd.DataFrame(index=range(dim),columns=['x'])
    print("Try")
    max_k = prec+1
    while max_k > prec:
        for i in range(dim):
            xk1.loc[i,'x'] = df.loc[i,'b']
            for j in range(dim):
                if i < j:
                    xk1.loc[i,'x'] = xk1.loc[i,'x'] - (df.iloc[i,j]*xk.loc[j,'x'])
                elif i > j:
                    xk1.loc[i,'x'] = xk1.loc[i,'x'] - (df.iloc[i,j]*xk1.loc[j,'x'])
            xk1.loc[i,'x'] = xk1.loc[i,'x']/df.iloc[i,i]
        max_k = 0
        for i in range(dim):
            next_k = xk1.loc[i,'x'] - xk.loc[i,'x'] 
            if next_k < 0: next_k = -next_k
            if next_k > max_k: max_k = next_k
        xk = xk1
    return [xk]