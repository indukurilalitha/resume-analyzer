
import streamlit as st
from PyPDF2 import PdfReader
import re

# App title
st.title("📄 AI-Powered Resume Analyzer (Simulated AI)")

def analyze_resume_with_ai(resume_text, job_description):
    # Clean simulated AI analysis result
    return f"""
    📊 AI Analysis Result:

    1️⃣ Top 5 Matching Skills:
    - Java
    - SQL
    - UI/UX Design
    - Problem-solving
    - Prompt Engineering

    2️⃣ 5 Important Missing Skills:
    - Web Application Development
    - AI Project Experience
    - Cloud Deployment
    - REST API Integration
    - Team Collaboration Tools (like Git)

    3️⃣ Fit Percentage:
    78%

    4️⃣ Suggestions:
    Enhance exposure to AI project work and web app frameworks. Add experience with cloud platforms and team collaboration tools.
    """

# File uploader for PDF resumes
uploaded_file = st.file_uploader("Upload your Resume (PDF)", type="pdf")

# Text area for Job Description
job_description = st.text_area("Paste Job Description here")

# Analyze button
if st.button("Analyze Resume"):
    if uploaded_file is not None:
        # Read PDF text
        pdf_reader = PdfReader(uploaded_file)
        resume_text = ""
        for page in pdf_reader.pages:
            resume_text += page.extract_text()

        # Extract 'Skills' section using regex
        skills_match = re.search(r'Skills(.*?)(Strengths|Projects|Certifications|Achievements|Internships|Education|Languages|Hobbies|$)',
                                 resume_text, re.DOTALL | re.IGNORECASE)

        if skills_match:
            skills_text = skills_match.group(1).replace('\n', ' ').strip()
        else:
            skills_text = resume_text[:600].replace('\n', ' ')

        if job_description.strip() == "":
            st.warning("⚠️ Please paste a Job Description.")
        else:
            with st.spinner("Analyzing..."):
                ai_result = analyze_resume_with_ai(skills_text, job_description)
                st.subheader("📊 AI Analysis Result:")
                st.write(ai_result)
    else:
        st.warning("⚠️ Please upload a PDF resume.")
