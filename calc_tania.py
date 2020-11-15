import streamlit as st
import numpy as np 
import pandas as pd 

import Interpolacao 
import SL_Iterativo
import SL_Direto

st.title('Interpolacao e Sistemas Lineares')

tipo = st.sidebar.selectbox('Tipo',['Sistema Linear','Interpolacao'])
if tipo == 'Interpolacao':
    dim = st.sidebar.number_input('Numero de pontos',value=3)
    met = st.sidebar.selectbox('Metodo',['Lagrange','Newton'])
    x = float(st.sidebar.text_input('Valor de X',value=0))

    st.write('Interpolacao')
    st.write("Insira os valores das linhas no formato x;y")
    st.write("Exemplo: se f(5)=3 digite 5;3")
    inter = []
    for _ in range(dim):
        inter.append(['0','0'])

    for i in range(dim):
        inter[i] = st.text_input("Ponto "+str(i),value=';'.join(inter[i])).split(';')
    df = pd.DataFrame(data=inter,columns=['x','f(x)'])
    st.write("Pontos")
    st.write(df)
    if st.sidebar.button('Executar'):
        if met == 'Lagrange':
            res = Interpolacao.lagrange(x,df,dim)
            st.title("Resultados")
            st.write(res[0])
            st.write("Valor de P("+str(x)+")="+str(res[1]))
        elif met == 'Newton':
            res = Interpolacao.newton(x,df,dim)
            st.write(res[0])
            st.write("Valor de P("+str(x)+")="+str(res[1]))
            

elif tipo == 'Sistema Linear':
    dim = st.sidebar.number_input('Dimensoes da Matriz',value=3)
    met = st.sidebar.selectbox('Metodo',['Gauss','LU','Jacobi','Gauss-Seidel'])

    st.write('Sistema Linear')
    st.write("Insira os valores das linhas, cada numero separado por ;")
    sisl = []
    a = []
    col = []
    for _ in range(dim+1):
        a.append('0')
    for i in range(dim):
        col.append('x'+str(i))
        sisl.append(a)
    col.append('b')

    for i in range(dim):
        sisl[i] = st.text_input("Linha "+str(i),value=';'.join(sisl[i])).split(';')
    map(float(),sisl)

    st.write('Sistema')
    df = pd.DataFrame(data=sisl,columns=col)

    st.write(df)