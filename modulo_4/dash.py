import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

import streamlit as st

st.title('Dashboard de EDA')

# Personalização da SideBar
st.sidebar.title('Menu')

arquivo = st.sidebar.file_uploader(
    label = 'Selecione o arquivo (csv ou Excel)',
    type = ['csv', 'xlsx']
)

if arquivo is not None:
    try:
        df = pd.read_csv(arquivo)
    except:
        df = pd.read_excel(arquivo)
        
    cb_dataframe = st.sidebar.checkbox('Mostrar DataFrame')
    numeric_columns = df.select_dtypes(['float64', 'float32', 'int64', 'int32']).columns
    
    if cb_dataframe:
        # Dataframe
        st.write('## Dataframe')
        df_ajustado = df.astype(str)
        st.dataframe(df_ajustado)
        st.write(f'Dimensões do DataFrame: {df.shape[0]} linhas e {df.shape[1]} colunas')
        
    cb_corr = st.sidebar.checkbox('Mostrar Heatmap de correlação')
    
    if cb_corr:
        # Heatmap de correlação
        st.write('## Heatmap de correlação')
        fig = plt.figure()
        sns.heatmap(df.corr())
        st.pyplot(fig)
    biblioteca = st.sidebar.selectbox('Selecione a biblioteca desejada', options = ['Seaborn', 'Matplotlib', 'Plotly'])    
    tipo_grafico = st.sidebar.selectbox('Selecione o tipo de gráfico desejado', options = ['Lineplot', 'Scatterplot', 'Barplot', 'Histogram', 'Boxplot'])    
    try:
        if biblioteca == 'Matplotlib':
        
            if tipo_grafico == 'Scatterplot':
                xaxis = st.sidebar.selectbox('Selecione a variável do eixo X', options = numeric_columns)
                yaxis = st.sidebar.selectbox('Selecione a variável do eixo Y', options = numeric_columns)
                
                # Plotagem de gráfico com Matplotlib
                st.write('## Gráfico com Matplotlib Scatterplot')

                fig = plt.figure()
                plt.scatter(data = df, x = xaxis, y = yaxis)
                plt.title(f'Gráfico de dispersão {xaxis} x {yaxis}')
                plt.xlabel(xaxis)
                plt.ylabel(yaxis)
                st.pyplot(fig)
                
            elif tipo_grafico == 'Lineplot':
                xaxis = st.sidebar.selectbox('Selecione a variável do eixo X', options = numeric_columns)
                yaxis = st.sidebar.selectbox('Selecione a variável do eixo Y', options = numeric_columns)
                
                # Plotagem de gráfico com Matplotlib
                st.write('## Gráfico com Matplotlib Lineplot')

                fig = plt.figure()
                plt.plot(df[xaxis], df[yaxis])
                plt.title(f'Gráfico de Linha {xaxis} x {yaxis}')
                plt.xlabel(xaxis)
                plt.ylabel(yaxis)
                st.pyplot(fig)
            
            elif tipo_grafico == 'Barplot':
                xaxis = st.sidebar.selectbox('Selecione a variável do eixo X', options = df.columns)
                yaxis = st.sidebar.selectbox('Selecione a variável do eixo Y', options = numeric_columns)
                
                st.write('## Gráfico com Matplotlib Barplot')

                fig = plt.figure()
                plt.bar(df[xaxis], df[yaxis])
                plt.title(f'Gráfico de Barras {xaxis} x {yaxis}')
                plt.xlabel(xaxis)
                plt.ylabel(yaxis)
                st.pyplot(fig)
                
        elif biblioteca == 'Seaborn':
            if tipo_grafico == 'Scatterplot':
                xaxis = st.sidebar.selectbox('Selecione a variável do eixo X', options = numeric_columns)
                yaxis = st.sidebar.selectbox('Selecione a variável do eixo Y', options = numeric_columns)
                
                # Plotagem de gráfico com Matplotlib
                st.write('## Gráfico com Seaborn Scatterplot')

                fig = plt.figure()
                sns.scatterplot(data = df, x = xaxis, y = yaxis)
                plt.title(f'Gráfico de dispersão {xaxis} x {yaxis}')
                plt.xlabel(xaxis)
                plt.ylabel(yaxis)
                st.pyplot(fig)
                
            elif tipo_grafico == 'Lineplot':
                xaxis = st.sidebar.selectbox('Selecione a variável do eixo X', options = numeric_columns)
                yaxis = st.sidebar.selectbox('Selecione a variável do eixo Y', options = numeric_columns)
                
                # Plotagem de gráfico com Matplotlib
                st.write('## Gráfico com Seaborn Lineplot')

                fig = plt.figure()
                sns.lineplot(df[xaxis], df[yaxis])
                plt.title(f'Gráfico de Linha {xaxis} x {yaxis}')
                plt.xlabel(xaxis)
                plt.ylabel(yaxis)
                st.pyplot(fig)
            
            elif tipo_grafico == 'Barplot':
                xaxis = st.sidebar.selectbox('Selecione a variável do eixo X', options = df.columns)
                yaxis = st.sidebar.selectbox('Selecione a variável do eixo Y', options = numeric_columns)
                
                st.write('## Gráfico com Seaborn Barplot')

                fig = plt.figure()
                sns.barplot(df[xaxis], df[yaxis])
                plt.title(f'Gráfico de Barras {xaxis} x {yaxis}')
                plt.xlabel(xaxis)
                plt.ylabel(yaxis)
                st.pyplot(fig)
                
        elif biblioteca == 'Plotly':
           if tipo_grafico == 'Scatterplot':
                xaxis = st.sidebar.selectbox('Selecione a variável do eixo X', options = numeric_columns)
                yaxis = st.sidebar.selectbox('Selecione a variável do eixo Y', options = numeric_columns)
                
                fig = px.scatter(x = df[xaxis], y = df[yaxis])
                st.plotly_chart(fig)
    except:
       st.write('Deu erro')


