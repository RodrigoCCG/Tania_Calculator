import numpy as np 
import pandas as pd 

def Jacobi(df,dim,x0,prec):
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
        print("________________________________")
        print(C.dot(xk))
        xk1 = g.sub(C.dot(xk))
        print(xk1)
        max_k = 0
        for i in range(dim):
            next_k = xk1.loc[i,'x'] - xk.loc[i,'x'] 
            if next_k < 0: next_k = -next_k
            if next_k > max_k: max_k = next_k
        xk = xk1
    return (C,g,xk)