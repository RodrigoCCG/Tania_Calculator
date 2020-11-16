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
        inter[i] = [float(i) for i in st.text_input("Ponto "+str(i),value=';'.join(inter[i])).split(';')]
    df = pd.DataFrame(data=inter,columns=['x','f(x)'])
    st.write("Pontos")
    st.write(df)
    if st.sidebar.button('Executar'):
        if met == 'Lagrange':
            res = Interpolacao.lagrange(x,df,dim)
            st.title("Resultados")
            st.write("Ls")
            st.write(res[0])
            st.write("Valor de P("+str(x)+")="+str(res[1]))
        elif met == 'Newton':
            res = Interpolacao.newton(x,df,dim)
            st.title("Resultados")
            st.write("Diferencas")
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
        sisl[i] = [float(i) for i in st.text_input("Linha "+str(i),value=';'.join(sisl[i])).split(';')]

    if met == 'Jacobi' or met == 'Gauss-Seidel':
        precisao = float(st.sidebar.text_input('Precisao',value=0))
        x0 = ['0' for i in range(dim)]
        x0 = [float(i) for i in st.text_input("X0",value=';'.join(x0)).split(';')]
        x0_df = pd.DataFrame(data=x0,columns=['x'])
        st.write(x0_df)
    
    st.write('Sistema')
    df = pd.DataFrame(data=sisl,columns=col)
    st.write(df)
    if st.sidebar.button('Executar'):
        if met == 'Gauss':
            res = SL_Direto.Gauss(df,dim)
            st.title("Resultados")
            st.write("Matriz fatorada")
            st.write(res[0])
            st.write("Valores de x")
            st.write(res[1])
            count=1
            for i in res[2]:
                st.header("Passo "+str(count))
                st.write("Matriz resultante")
                st.write(i[0])
                st.write("Matriz em fatoracao")
                st.write(i[1])
                count+=1


        elif met == 'LU':
            res = SL_Direto.LU(df,dim)
            st.write(LU)
            st.title("Resultados")
            st.write("L")
            st.write(res[0])
            st.write("U")
            st.write(res[1])
            st.write("Y")
            st.write(res[2])
            st.write("X")
            st.write(res[3])

        elif met == 'Jacobi':
            res = SL_Iterativo.Jacobi(df,dim,x0_df,precisao)
            st.title("Resultados")
            st.write("Matriz C")
            st.write(res[0])
            st.write("Matriz g")
            st.write(res[1])
            st.write("X")
            st.write(res[2])

        elif met == 'Gauss-Seidel':
            res = SL_Iterativo.Seidel(df,dim,x0_df,precisao)
            st.title("Resultados")
            st.write("Valores de x")
            st.write(res[0])