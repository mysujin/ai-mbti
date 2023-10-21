import streamlit as st


from langchain.chat_models import ChatOpenAI


chat_model = ChatOpenAI()

st.title('MBTI 박사')

content = st.text_input('알고 싶은 MBTI 유형을 알려 주세요')

if st.button('MBTI 유형'):
    with st.spinner('처리 중  ...'):
        result = chat_model.predict(content + "의 MBTI 유형을 설명해줘")
        st.write(result)





