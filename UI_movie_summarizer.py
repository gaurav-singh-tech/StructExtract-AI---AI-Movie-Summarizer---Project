import streamlit as st
import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_mistralai import ChatMistralAI

# -------------------------------
# 🔐 API KEY
# -------------------------------
api_key = os.getenv("MISTRAL_API_KEY")

if not api_key:
    st.error("Add MISTRAL_API_KEY in Streamlit Secrets")
    st.stop()

# -------------------------------
# 🤖 MODEL
# -------------------------------
model = ChatMistralAI(
    model="mistral-small-2506",
    api_key=api_key
)

# -------------------------------
# 🎨 UI CONFIG
# -------------------------------
st.set_page_config(page_title="StructExtract-AI", layout="wide")

st.title("🎬 StructExtract-AI")
st.caption("Convert unstructured text into structured insights | Architected by Gaurav Singh")

st.divider()

# -------------------------------
# 📝 INPUT SECTION
# -------------------------------
st.subheader("📄 Input Paragraph")

paragraph = st.text_area(
    "Paste movie description",
    height=200,
    placeholder="Enter movie description..."
)

# -------------------------------
# ⚙️ PROMPT
# -------------------------------
prompt = ChatPromptTemplate.from_messages([
    ("system",
"""You are an expert information extraction assistant.

Extract movie information:

- Movie Name
- Director
- Genre
- Main Cast
- Story Premise
- Setting
- Themes
- Conflict

Rules:
- Do NOT hallucinate
- If missing → write 'Not specified'
- Keep output clean and structured

Finally add 2-3 line summary
"""),
    ("human", "{paragraph}")
])

# -------------------------------
# 🚀 BUTTON
# -------------------------------
if st.button("Extract Information"):

    if not paragraph.strip():
        st.warning("Please enter a paragraph")
    else:
        with st.spinner("Extracting..."):
            final_prompt = prompt.invoke({"paragraph": paragraph})
            response = model.invoke(final_prompt)

        st.divider()
        st.subheader("📊 Extracted Output")

        st.markdown(response.content)

# -------------------------------
# 🧠 SIDEBAR
# -------------------------------
st.sidebar.title("⚙️ About Project")

st.sidebar.write("""
**StructExtract-AI**

AI-powered system to convert
unstructured text into
structured information.

Use cases:
- Movies
- Resumes
- Financial docs
""")
