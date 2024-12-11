import os
import openai
import streamlit as st

# OpenAI API 키 설정
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

openai.api_key = os.environ.get("OPENAI_API_KEY")

st.title('🎨 제품 홍보 포스터 생성기')
keyword = st.text_input("키워드를 입력하세요.")

if st.button('포스터 생성하기 🖼️'):
    with st.spinner('포스터를 생성 중입니다...'):
        try:
            # DALL·E를 사용하여 이미지 생성
            response = openai.Image.create(
                model="dall-e-3",
                prompt=f"{keyword}를 주제로 한 제품 홍보 포스터. 창의적이고 시각적으로 매력적인 디자인.",
                n=1,  # 생성할 이미지 개수
                size="1024x1024"  # 이미지 해상도
            )

            # 생성된 이미지 URL 가져오기
            image_url = response['data'][0]['url']

            # Streamlit에 이미지 표시
            st.image(image_url, caption=f"{keyword} 홍보 포스터", use_column_width=True)

        except Exception as e:
            st.error(f"이미지 생성 중 오류가 발생했습니다: {str(e)}")
