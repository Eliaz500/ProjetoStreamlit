import streamlit as st

st.title('Função Mídia')
st.header('Função st.image()')
st.image('thor.jpg', width=200, caption='Thor')

st.header('Função st.audio()')
st.audio('music.mp3', format='mp3')

st.header('Função st.video()')
st.video('video.mp4', format='mp4')
st.video('https://www.youtube.com/watch?v=si6Ox8IuZeU&list=RDsi6Ox8IuZeU&start_radio=1')


