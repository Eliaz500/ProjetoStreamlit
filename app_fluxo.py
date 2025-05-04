import streamlit as st

st.title('Controle de Fluxo')

st.subheader('Sem st.form()')

nome = st.text_input('Digite seu nome:')
idade = st.number_input('digite sua idade')
sexo = st.radio('Sexo', ['Masculino', 'Feminino'])
tipo = st.selectbox('PJ ou PF', ['Pessoa Júridica', 'Pessoa Física'])

st.write('Nome', nome)
st.write('Idade', idade)
st.write('Sexo', sexo)
st.write('Tipo', tipo)

st.markdown('---')
st.subheader('Com st.form()')

with st.form(key='form1'):
    nome = st.text_input('Digite seu nome:')
    idade = st.number_input('digite sua idade')
    sexo = st.radio('Sexo', ['Masculino', 'Feminino'])
    tipo = st.selectbox('PJ ou PF', ['Pessoa Juridica', 'Pessoa Física'])
    st.form_submit_button('Enviar')

st.write('Nome', nome)
st.write('Idade', idade)
st.write('Sexo', sexo)
st.write('Tipo', tipo)

st.markdown('---')
st.subheader('Com st.stop()')

nome = st.text_input('Digite seu nome:')
if nome == '':
    st.warning('Por favor, digite um nome completo')
    st.stop()
st.success('Obrigado por usar o programa!')

