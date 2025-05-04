import time

import streamlit as st

st.title('Funções de Layout')

st.sidebar.image('logo_ufape.png')
st.sidebar.title('Sidebar')

operacao = st.sidebar.radio('Escolha a Operação', ['Adição', 'Subtração', 'Multiplicação', 'Divisão'])

a = st.number_input('Numero A')
b = st.number_input('Numero B')

if operacao == 'Adição':
    st.write('Resultado: ', a+b)
if operacao == 'Subtração':
    st.write('Resultado: ', a-b)
if operacao == 'Multiplicação':
    st.write('Resultado: ', a*b)
if operacao == 'Divisão' and b != 0:
    st.write('Resultado: ', a/b)
else:
    st.write('Valor inválido')

with st.expander('Ajuda'):
    st.write('Insira dois valores para serem somados')

with st.expander('Quadrado'):
    c = st.number_input('Numero C')
    st.write('Número elevedado ao quadrado', c*c)

st.markdown('---')

st.subheader('Função st.container()')

st.header('Concatenar Nomes')

primeiro_nome = st.text_input('Primeiro Nome')

container_a = st.container()

ultimo_nome = st.text_input('Último Nome')
opcao_nome = st.checkbox('Incluir o nome do meio')
if opcao_nome:
    nome_meio = container_a.text_input('Nome do meio')
else:
    nome_meio = ''
st.write('Nome Completo: ', primeiro_nome, nome_meio, ultimo_nome)

st.markdown('---')

st.subheader('Função st.empty()')

st.header('Contador')

contador = st.empty()

with contador:
    for segundos in range(10):
        st.write(segundos, 'Segundos passados')
        time.sleep(1)

st.markdown('---')

st.subheader('Função st.columns()')

col1, col2, col3 = st.columns([1, 1, 2])

with col1:
    primeiro = st.number_input('Numero 1')
    check1 = st.checkbox('Check1')
with col2:
    segundo = st.number_input('Numero 2')
with col3:
    terceiro = st.number_input('Numero 3')
    check3 = st.checkbox('Check3')