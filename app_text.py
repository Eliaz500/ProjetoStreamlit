import streamlit as st

st.title('Funções de Texto')

st.header('Este é um header')

st.subheader('Este subheader')

st.text('Este é um texto')

st.caption('Este é uma legenda')

#--------------------------------------------

st.markdown('**Negrito**')
st.markdown('*Itálico*')
st.markdown(':smile:')
st.markdown('<h1>HTML code</h1>', unsafe_allow_html=True)
st.markdown('---')

#-------------------------------------------------

st.code("st.markdown('**Negrito**')")

st.code(
    """
    st.markdown('**Negrito**')
st.markdown('*Itálico*')
st.markdown(':smile:')
st.markdown('<h1>HTML code</h1>', unsafe_allow_html=True)
st.markdown('---')
    """
)

#--------------------------------------------------

st.latex('a^2 + x + 3 = \sum ax^4')


#--------------------------------------------------
d = 555
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
st.write('Texto com st.write')
st.write(d)
st.write(lista)