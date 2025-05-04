import streamlit as st
import time
import pandas as pd
import yfinance
import yfinance as yf

st.title('Funções de Status Messages')

st.subheader('Função st.progress()')

st.progress(30)
st.progress(50)
st.progress(80)

st.progress(0.30)
st.progress(0.50)
st.progress(0.80)

barra_prog = st.progress(0)

# for progress in range(100):
#     barra_prog.progress(progress + 1)
#     time.sleep(0.1)


lista = ['EQTL3A', 'BBDC4.SA', 'VALE3.SA', 'B3SA3.SA']
coletar = st.button('Coletar')
volume = pd.Series()
if coletar:
    barra_progresso = st.progress(0)
    count = 0
    for ticker in lista:
        valor = yf.download(ticker, period='1d')
        volume[ticker] = valor
        count = count + (1/len(lista))
        barra_progresso.progress(count)
    st.bar_chart(volume)


st.markdown('---')
st.subheader('Função st.spinner()')

coletar_spinner = st.button('Coletar Spinner')
volume = pd.Series()
if coletar_spinner:
    with st.spinner(text='Tempo Spinner'):
        for ticker in lista:
            valor = yf.download(ticker, period='1d')
            volume[ticker] = valor
        st.success('Coleta finalizada!')
        st.bar_chart(volume)

with st.spinner('Coletando informações'):
    time.sleep(5)


st.markdown('---')
st.subheader('Função Mensagens')

st.success('Mensagens de sucesso!')
st.warning('Mensagem de Aviso!')
st.error('Mensagem de erro!')
st.info('Mensagem informação!')

botao_messagem = st.button('Teste Mensagem')
volume = pd.Series()
if botao_messagem:
    with st.spinner(text='Tempo Spinner'):
        try:
            for ticker in lista:
                valor = yf.download(ticker, period='1d')
                volume[ticker] = valor
            st.success('Coleta finalizada!')
            st.bar_chart(volume)
        except:
            st.error('Erro na leitura dos dados!')

