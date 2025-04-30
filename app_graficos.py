import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from docutils.nodes import title

st.title('Funções Gráficos')

tickers = ['PETR4.SA','VALE3.SA', 'EQTL3.SA', 'CSAN3.SA']

preco = yf.download(tickers, period='1y')['Close']

st.header('Função Nativas')

st.dataframe(preco.head(10))

st.subheader('Função st.line_chart()')

st.line_chart(preco, width=120, height=300)

st.subheader('Função st.area_chart()')

st.area_chart(preco, width=200, height=200)

st.subheader('Função st.bar_chart()')

st.bar_chart(preco, width=200, height=200)

dados = pd.DataFrame(np.random.randn(50, 3), columns=['a', 'b', 'c'])

st.dataframe(dados)

st.bar_chart(dados)

st.markdown('---')

st.header('Funções Específicas')

st.subheader('Função Matplotlib st.pyplot()')

fig = plt.figure()
ax = plt.axes()
ax.plot(preco.index, preco['VALE3.SA'])
plt.title('Preços Vale3')
st.pyplot(fig)

st.subheader('Função Plotly Express - st.plotly_express()')
fig = px.line(preco, title='Preço Ações')
st.plotly_chart(fig)

st.subheader('Função Plotly Graph Objects - st.plotly_chart()')
fig = go.Figure()
fig.add_trace(go.Scatter(x=preco.index, y=preco['VALE3.SA'], name='Vale3'))
fig.add_trace(go.Scatter(x=preco.index, y=preco['EQTL3.SA'], name='EQTL3.SA'))
fig.update_layout(title='<b>Preços das Ações</b>')

st.plotly_chart(fig)
