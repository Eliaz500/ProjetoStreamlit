import streamlit as st
import pandas as pd
import yfinance as yf


st.title('Funções Dados')

tickers = ['PETR4.SA','VALE3.SA', 'EQTL3.SA', 'CSAN3.SA']

preco = yf.download(tickers, period='1y')['Close']

st.header('Função st.dataframe()')
st.dataframe(preco, width=420, height=200)

st.header('Função st.table()')
st.table(preco.head(2))

st.subheader('Função st.dataframe e st.table com pandas style')
st.dataframe(preco.head(10).style.highlight_max(axis=1))

st.table(preco.head(10).style.highlight_max(axis=0))

st.metric('Temperatura', value='27ºC', delta='1%')

ultimo_petr4 = round(preco['PETR4.SA'].iloc[-1],2)
penultimo_petr4 = preco['PETR4.SA'].iloc[-2]
var_petr4 = round(((ultimo_petr4 / penultimo_petr4) - 1)* 100,2)

st.metric('Cotação PETR4.SA', value=ultimo_petr4, delta=f'{var_petr4}%')

st.subheader('Função st.json()')

json = {
    'Nome': 'Elias',
    'Sexo': 'Masculino',
    'End': [
        'Rua A',
        'Bairro B',
        'Cidade C',
        'Estado D',
    ],
}

st.json(json)

st.write(preco)
st.write(json)