import streamlit as st

st.set_page_config(page_title="면접 연습 RAG", page_icon="microphone")

def generate_question(topic):
    return f"{topic}에 대해 본인의 생각과 근거를 바탕으로 설명해보세요."

def evaluate_answer(question, answer):
    return """
장점:
- 질문의 핵심에 맞게 답변하려는 흐름이 있습니다.

보완점:
- 구체적인 사례나 근거를 더 넣으면 좋습니다.
- 답변의 시작, 근거, 마무리 구조를 더 명확히 하면 좋습니다.

개선 방향:
- 먼저 자신의 입장을 말하고, 그 이유를 2가지 정도 제시한 뒤, 마지막에 정리해보세요.
"""

st.title("면접 연습")

topic = st.text_input(
    "연습할 주제를 입력하세요",
    placeholder="예: AI와 교육의 미래"
)

if st.button("질문 생성"):
    if topic:
        st.session_state.question = generate_question(topic)
    else:
        st.warning("주제를 먼저 입력해주세요.")

if "question" in st.session_state:
    st.subheader("면접 질문")
    st.write(st.session_state.question)

    answer = st.text_area("내 답변", height=180)

    if st.button("답변 평가"):
        if answer.strip():
            feedback = evaluate_answer(st.session_state.question, answer)
            st.subheader("피드백")
            st.write(feedback)
        else:
            st.warning("답변을 입력해주세요.")
