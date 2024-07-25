import streamlit as st

# 페이지 제목
st.title("결과 페이지")

# CSS 스타일을 통해 가운데 정렬 적용
st.markdown("""
    <style>
        .center-text {
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# 학번 표시
if 'email_or_phone' in st.session_state:
    student_id = st.session_state.email_or_phone
    st.markdown(f"<div class='center-text'>{student_id}님 수고하셨습니다!</div>", unsafe_allow_html=True)

# 정답 확인하기 버튼
if st.button("정답 확인하기"):
    # 객관식 문제 결과 표시
    if 'submitted' in st.session_state and st.session_state.submitted:
        st.markdown("<div class='center-text'>객관식 정답:</div>", unsafe_allow_html=True)
        
        # 세션 상태에서 정답 리스트와 사용자 답변 가져오기
        correct_answers = st.session_state.correct_answers
        answers = st.session_state.answers

        # 총 개수와 맞춘 개수
        total_questions = len(answers)
        correct_count = sum(1 for i in range(total_questions) if answers.get(i, "") == correct_answers[i])

        # 총점 및 맞춘 개수 표시
        st.markdown(f"<div class='center-text'>{correct_count}/{total_questions}</div>", unsafe_allow_html=True)

        # 제출 상태 초기화
        st.session_state.submitted = False

    # 주관식 문제 결과 표시
    if 'subjective_submitted' in st.session_state and st.session_state.subjective_submitted:
        st.markdown("<div class='center-text'>주관식 정답:</div>", unsafe_allow_html=True)

        # 세션 상태에서 정답 리스트와 사용자 답변 가져오기
        correct_answers = st.session_state.correct_subjective_answers
        answers = st.session_state.subjective_answers

        # 총 개수와 맞춘 개수
        total_questions = len(answers)
        correct_count = sum(1 for i in range(total_questions) if answers.get(i, "").strip() == correct_answers[i])

        # 총점 및 맞춘 개수 표시
        st.markdown(f"<div class='center-text'>{correct_count}/{total_questions}</div>", unsafe_allow_html=True)

        # 제출 상태 초기화
        st.session_state.subjective_submitted = False

    # 제출 상태가 없거나 페이지가 새로 로드된 경우
    if 'submitted' not in st.session_state and 'subjective_submitted' not in st.session_state:
        st.write("문제를 제출한 후 결과를 확인하세요.")
else:
    st.write("정답을 확인하려면 버튼을 클릭하세요.")
