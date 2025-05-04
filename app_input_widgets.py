import streamlit as st
import pandas as pd
import yfinance as yf
from datetime import datetime

from app_graficos import tickers

st.title('Funções Input Widgets')

st.subheader('Função st.button()')
botao =st.button('Botão')
if botao:
    precos = yf.download('EQTL3.SA', period='1y')['Close']
    st.line_chart(precos)

st.markdown('---')

precos = yf.download('EQTL3.SA', period='1y')
precos['MM20'] = precos['Close'].rolling(20).mean()
st.dataframe(precos)

st.subheader('Função st.checkbox()')
check = st.checkbox('Média Móvel 20 Períodos')
if check:
    st.line_chart(precos['MM20'])
else:
    st.line_chart(precos['Volume'])


st.markdown('---')
st.subheader('Função st.radio()')
radio = st.radio('Selecione', ['A', 'B', 'C', 'D', 'E'])
st.write(radio)

papeis = st.radio('Papeis', ['PETR4', 'VALE3', 'EQTL3'])
if papeis == 'PETR4':
    ultimo = yf.download('PETR4.SA', period='1d')
if papeis == 'VALE3':
    ultimo= yf.download('VALE3.SA', period='1d')
if papeis == 'EQTL3':
    ultimo = yf.download('EQTL3.SA', period='1d')
    st.dataframe(ultimo)
    preco = ultimo['Volume']
    st.dataframe(preco)

st.write('Ultimo valor',radio,f'R${preco}')

st.markdown('---')
st.subheader('Função st.text_input() e st.number_input()')

nome = st.text_input('Digite seu Nome', value='Digite seu Nome', max_chars=10)
idade = st.number_input('Qual a sua Idade?', min_value=18, max_value=25, step=2)

st.write(nome, idade)

st.markdown('---')
st.subheader('Função st.selectbox() e st.multisect()')

tickers = ['ITUB4.SA', 'BBDC4.SA', 'BBAS3.SA', 'B3SA3.SA']

selecao = st.selectbox('Selecione o papel', tickers)
st.write(selecao)
preco = yf.download(selecao, period='1y')['Close']
st.dataframe(preco)
st.line_chart(preco)

multiselecao = st.multiselect('Selecione o papel', tickers)
preco = yf.download(selecao, period='1y')['Close']
st.dataframe(preco)
st.line_chart(preco)

st.markdown('---')
st.subheader('Função st.slider()')

idade = st.slider('Qual a sua Idade?', min_value=18, max_value=25, step=2)
st.write(idade)

data = st.slider('Qual a data?', datetime(2025,1,1), datetime(2027,1,1))
st.write(data)

salario = st.slider('Qual o seu salario?', min_value=0.0, max_value=800.00, step=200.00)
st.write(salario)

st.markdown('---')
st.subheader('Função st.select_slider()')

cores = ['azul', 'vermelho', 'preto', 'branco', 'verde', 'amarelo']

cor = st.select_slider('Cores', options=cores)
st.write(cor)

cor1, cor2 = st.select_slider('Cores', options=cores, value=('branco', 'verde'))
st.write(cor1, cor2)

st.markdown('---')
st.subheader('Função st.file_uploader()')
arquivo = st.file_uploader('Arquivo', type='csv')
if arquivo is not None:
    dados = pd.read_csv(arquivo)
    st.dataframe(dados.head())