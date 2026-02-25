import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load API key from .env
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(page_title="Studaiverse", page_icon="📚")

st.title("📚 Studaiverse")
st.subheader("AI-powered study roadmap from your syllabus")

uploaded_file = st.file_uploader("Upload your syllabus (PDF or TXT)")


def generate_roadmap(text):
    prompt = f"""
You are an expert study planner.

Based on the following syllabus, create:

1. A week-by-week study roadmap
2. Daily study tasks
3. Exam preparation strategy

Syllabus:
{text}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
    )

    return response.choices[0].message.content


if uploaded_file:
    syllabus_text = uploaded_file.read().decode("utf-8", errors="ignore")

    st.success("File uploaded successfully!")

    if st.button("Generate Study Roadmap"):
        with st.spinner("Creating your AI study plan..."):
            roadmap = generate_roadmap(syllabus_text)

        st.markdown("# Your Study Roadmap #")
        st.write(roadmap)


#____________________________Task manager __________________________________________
