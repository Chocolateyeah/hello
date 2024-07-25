import streamlit as st

# 페이지 제목
st.title("로그인 페이지")

# 페이지 레이아웃 설정
# 로그인 박스
with st.container():
    st.markdown('<div class="login-container">', unsafe_allow_html=True)
    st.markdown('<div class="login-box">', unsafe_allow_html=True)
    
    # 동아대학교 로고 이미지 삽입
    st.image("https://ent.donga.ac.kr/upload/2024jungsi_8_pass/images/donga_logo.png")
    st.subheader("Sign In")

    # 학번 입력 필드
    email_or_phone = st.text_input("학번")

    # 로그인 버튼
    if st.button("Sign In", key="signin", use_container_width=True):
        if email_or_phone:
            st.session_state.logged_in = True
            st.session_state.email_or_phone = email_or_phone
            st.success("Login successful!")
            st.experimental_rerun()  # 페이지 새로고침하여 객관식 문제 페이지로 이동
        else:
            st.error("Please enter your student ID.")

    st.markdown('<div class="signup-text">New to Dong-A University? <a href="#">Sign up now</a></div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
