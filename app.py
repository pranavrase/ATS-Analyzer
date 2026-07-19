import streamlit as st
from file_reader import read_pdf, read_docx
from analyzer import analyze_resume

# Page Configuration
st.set_page_config( page_title="ATS Analyzer", page_icon="📄", layout="wide")

# Title
st.title("📄 ATS Resume Analyzer")
st.write("Upload your resume and get AI-powered analysis.")
st.divider()

# File Upload
uploaded_file = st.file_uploader("Upload Resume", type=["pdf", "docx"])

resume_text = ""

if uploaded_file is not None:
    if uploaded_file.name.endswith(".pdf"):
        resume_text = read_pdf(uploaded_file)
    elif uploaded_file.name.endswith(".docx"):
        resume_text = read_docx(uploaded_file)

    st.success("Resume uploaded successfully!")
    
    if st.button("Analyze Resume", use_container_width=True):
        with st.spinner("Analyzing Resume..."):
            result = analyze_resume(resume_text)

        st.success("Analysis Completed!")
        st.divider()
        st.header("📊 Resume Analysis")
        st.markdown(result)

        st.download_button(
        label="📥 Download Report",
        data=result,
        file_name="resume_analysis.txt",
        mime="text/plain"
        )