import streamlit as st

# 로그인 상태 확인
if 'logged_in' not in st.session_state or not st.session_state.logged_in:
    st.error("로그인 후 접근할 수 있습니다.")
    st.stop()

# 페이지 제목
st.title("객관식 문제")

# 문제 리스트
questions = [
    "문제 1: 대한민국의 수도는 어디인가요?",
    "문제 2: Python에서 리스트를 만들 때 사용하는 기호는 무엇인가요?",
    "문제 3: 'Hello World'는 어떤 프로그래밍 언어에서 가장 기본적인 예제인가요?",
    "문제 4: 태양계에서 가장 큰 행성은 무엇인가요?"
]

# 선택지
options = [
    ["서울", "부산", "대구", "인천"],
    ["()", "{}", "[]", "<>"],
    ["Python", "Java", "C++", "JavaScript"],
    ["지구", "화성", "목성", "토성"]
]

# 정답 설정
correct_answers = ["서울", "[]", "Python", "목성"]

# CSS 스타일을 통해 가운데 정렬 적용
st.markdown("""
    <style>
        .center-text {
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# 각 문제에 대한 선택지 표시
answers = {}
for i, question in enumerate(questions):
    st.markdown(f"<div class='center-text'>{question}</div>", unsafe_allow_html=True)
    answers[i] = st.radio(
        "답을 선택하세요:",
        options[i],
        key=f"q{i}"  # 각 문제에 대한 고유 키
    )

# 제출 버튼
if st.button("제출"):
    # 세션 상태에 답변과 정답 리스트 저장
    st.session_state.answers = answers
    st.session_state.correct_answers = correct_answers
    st.session_state.submitted = True

    # 정답 확인 및 점수 계산
    st.session_state.score = 0
    st.session_state.correct_answers_count = 0

    for i, question in enumerate(correct_answers):
        user_answer = st.session_state.answers.get(i, "미선택")
        if user_answer == question:
            st.session_state.correct_answers_count += 1
        st.session_state.score = st.session_state.correct_answers_count

    # 결과 페이지로 이동
    st.experimental_rerun()
