import streamlit as st
from study_assistant_full import run_study_assistant

st.set_page_config(page_title="📚 Study Assistant AI", layout="centered")

st.title("🎓 Study Assistant AI Agent")
st.markdown("This assistant can explain topics, answer questions, and generate quizzes!")

with st.form("input_form"):
    topic = st.text_input("Enter a study topic:", value="Photosynthesis")
    question = st.text_input("Enter a question:", value="Why is chlorophyll important?")
    submitted = st.form_submit_button("Run Study Assistant")

if submitted:
    with st.spinner("Running the AI agents..."):
        result = run_study_assistant(topic, question)

    st.subheader("🧠 Output:")
    st.markdown(result)
