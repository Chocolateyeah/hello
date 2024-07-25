import streamlit as st

# 페이지 제목
st.title("주관식 문제")

# 문제 리스트 (공란으로 설정)
questions = [
    "문제 1: 일본국(日本国), 통칭 ()은 동아시아의 입헌군주국이다.",
    "문제 2: 동작이나 모양이 조금씩 다른 많은 그림이나 인형을 한 장면씩 촬영하여 영사하였을 때에 화상이 연속하여 움직이는 것처럼 보이게 하는 것.",
    "문제 3: 일본어에서 사용하는 두 가나 중 하나이다"
]

# 정답 설정
correct_answers = ["일본", "애니메이션", "히라가나"]

# CSS 스타일을 통해 가운데 정렬 적용
st.markdown("""
    <style>
        .center-text {
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# 각 문제에 대한 답변 입력 표시
answers = {}
for i, question in enumerate(questions):
    st.markdown(f"<div class='center-text'>{question}</div>", unsafe_allow_html=True)
    answers[i] = st.text_input(
        "답을 입력하세요:",
        key=f"q{i}"  # 각 문제에 대한 고유 키
    )

# 제출 버튼
if st.button("제출"):
    # 세션 상태에 답변과 정답 리스트 저장
    st.session_state.subjective_answers = answers
    st.session_state.correct_subjective_answers = correct_answers
    st.session_state.subjective_submitted = True

    # 결과 페이지로 이동
    st.experimental_rerun()
