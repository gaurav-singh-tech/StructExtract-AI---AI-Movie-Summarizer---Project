import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_mistralai import ChatMistralAI

load_dotenv()

# Initialize model
model = ChatMistralAI(model="mistral-small-2506")

prompt = ChatPromptTemplate.from_messages([
    ("system",
"""You are an expert information extraction assistant.

Extract useful movie information from the paragraph.

Rules:
1. Do not invent information.
2. If information is missing write "Not specified".
3. Keep answers short and clear.

Return the output exactly in this format:

Movie Name:
Director:
Genre:
Main Cast:
Story Premise:
Setting/Location:
Key Themes:
Central Conflict:

Quick Summary:
"""),

("human", "Extract information from the paragraph:\n{paragraph}")
])


# ---------------- UI ---------------- #

st.set_page_config(page_title="Movie Information Extractor", layout="centered")

st.title("🎬 Movie Information Extractor")
st.caption("Extract key movie details from a paragraph using AI")

paragraph = st.text_area(
    "Enter a paragraph about a movie",
    height=200,
    placeholder="Paste a movie description here..."
)


col1, col2 = st.columns([1,1])

with col1:
    extract = st.button("Extract Information")

with col2:
    example = st.button("Load Example")


# Example paragraph
if example:
    paragraph = """Interstellar is a science fiction film directed by Christopher Nolan. 
    The film stars Matthew McConaughey, Anne Hathaway, Jessica Chastain, and Michael Caine. 
    The story follows a group of astronauts who travel through a wormhole near Saturn 
    in search of a new home for humanity as Earth is becoming uninhabitable."""

    st.text_area("Example Paragraph", paragraph, height=200)


# Run extraction
if extract:

    if paragraph.strip() == "":
        st.warning("Please enter a paragraph first.")
    
    else:
        with st.spinner("Extracting information..."):
            final_prompt = prompt.invoke({"paragraph": paragraph})
            response = model.invoke(final_prompt)

        st.divider()

        st.subheader("📊 Extracted Information")

        st.markdown(response.content)