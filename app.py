# === import required libraries ===
import streamlit as st
from docx import Document
import PyPDF2
from io import StringIO
import os

# === Configure Streamlit page ===
st.set_page_config(page_title="📝 Text Summarizer", layout="centered")

# === Loading CSS Styles ===
css_path = os.path.join(os.path.dirname(__file__), "style.css")
with open(css_path) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# === Title and subtitle ===
st.markdown("<h1>📝 Text Summarizer</h1>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Transform Long Texts into Concise Summaries with File Upload or Manual Input</div>", unsafe_allow_html=True)

# === Input method selection ===
input_method = st.radio("📥 Select how you want to enter text:", ["Upload File", "Type Manually"])
text = ""

# === File upload handling ===
if input_method == "Upload File":
    uploaded_file = st.file_uploader("Upload a PDF, DOCX, or TXT file", type=["pdf", "docx", "txt"])
    if uploaded_file:
        if uploaded_file.type == "application/pdf":
            reader = PyPDF2.PdfReader(uploaded_file)
            for page in reader.pages:
                text += page.extract_text()
        elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            doc = Document(uploaded_file)
            text = "\n".join([para.text for para in doc.paragraphs])
        elif uploaded_file.type == "text/plain":
            stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
            text = stringio.read()
else:
    text = st.text_area("Enter your text here:", height=250)

if text:
    st.info(f"Original Word Count: {len(text.split())}")

# === Summary style selection ===
summary_type = st.radio("Choose summarization style:", ["Basic Summary", "Deep Thinking"])

# === Summary functions ===
def basic_summary(text):
    sentences = text.split(". ")
    highlight_count = max(1, len(sentences) // 3)
    return ". ".join(sentences[:highlight_count]).strip()

def deep_thinking_summary(text):
    sentences = text.split(". ")
    sorted_sentences = sorted(sentences, key=len, reverse=True)
    pick_count = max(3, len(sentences) // 4)
    return ". ".join(sorted_sentences[:pick_count]).strip()

# === Buttons ===
col1, col2 = st.columns(2)

with col1:
    if st.button("Summarize"):
        if text:
            result = basic_summary(text) if summary_type == "Basic Summary" else deep_thinking_summary(text)
            st.success("✅ Summary Generated")
            st.markdown("### Summary:")
            st.markdown(f"<div class='summary-box'>{result}</div>", unsafe_allow_html=True)
            st.info(f"Summary Word Count: {len(result.split())}")
        else:
            st.warning("Please provide some text.")

with col2:
    if st.button("Clear"):
        st.rerun()

st.markdown("<hr style='margin-top: 30px;'>", unsafe_allow_html=True)
