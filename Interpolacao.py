import numpy as np 
import pandas as pd 

def lagrange(x,df,count):
    """Realiza a interpolacao de um ponto x pelo metodo de Lagrange
    dado um conjunto de dados composto por count pontos, 
    no DataFrame df, separado em colunas x e f(x). Retorna uma tupla com um
    DataFlame contendo os valores de L, assim como o valor de x interporlado
    Input: 
    x:float -Valor a ser interpolado
    df:pandas.DataFrame -DataFrame constituido de count pontos nas colunas (x,f(x))
    count:int Quantidade de pontos no Dataframe
    Output:
    Tuple - Tupla contendo o Dataframe com os valores de L e o x Interpolado
    """
    res = pd.DataFrame(columns=['L'])
    for index in range(count):
        thisL = 1
        for i in range(count):
            if i != index:
                thisL = thisL*((x-float(df.loc[i,'x']))/
                    (float(df.loc[index,'x'])-float(df.loc[i,'x'])))
        res.at[index,'L']=thisL
    p = 0
    for index in range(count):
        p += float(df.loc[index,'f(x)'])*res.loc[index,'L']

    return (res,p)

def newton(x,df,count):
    """Realiza a interpolacao de um ponto x pelo metodo de Neuton
    dado um conjunto de dados composto por count pontos, 
    no DataFrame df, separado em colunas x e f(x). Retorna uma tupla com um
    DataFlame contendo os valores de F[n, n-1, ..., 1, 0], assim como o valor de x interporlado
    Input: 
    x:float -Valor a ser interpolado
    df:pandas.DataFrame -DataFrame constituido de count pontos nas colunas (x,f(x))
    count:int Quantidade de pontos no Dataframe
    Output:
    Tuple - Tupla contendo o Dataframe com os valores de F[n, n-1, ..., 1, 0] e o x Interpolado
    """
    res = pd.DataFrame(data=df.loc[range(count),'f(x)'])
    for valor in range(1,count):
        fs=[]
        for _ in range(count):
            fs.append('NaN')
        for i in range(valor, count):
            fs[i] = ((float(res.iloc[i,valor-1])-float(res.iloc[i-1,valor-1]))/
                    (float(df.loc[i,'x'])-float(df.loc[i-valor,'x'])))
        res.insert(loc=valor,column='f[i:(i-'+str(valor)+')]',value=fs)
    y = 0
    for i in range(count):
        mul=1
        for j in range(i):
            mul= mul*(x-float(df.loc[j,'x']))
        y+= float(res.iloc[i,i])*mul
    return (res,y)