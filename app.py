import streamlit as st
import PyPDF2
import re

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="AI Resume Screening System",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Screening & ATS Analyzer")

# =========================
# LOAD MODEL
# =========================

@st.cache_resource
def load_model():
    return SentenceTransformer("all-MiniLM-L6-v2")

model = load_model()

# =========================
# JOB DESCRIPTION INPUT
# =========================

job_description = st.text_area(
    "Paste Job Description",
    height=200
)

# =========================
# RESUME UPLOAD
# =========================

uploaded_file = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)

# =========================
# SKILLS DATABASE
# =========================

skills = [
    "python",
    "java",
    "c++",
    "machine learning",
    "deep learning",
    "tensorflow",
    "pytorch",
    "sql",
    "excel",
    "power bi",
    "tableau",
    "aws",
    "docker",
    "git",
    "html",
    "css",
    "javascript",
    "react",
    "data analysis"
]

# =========================
# PDF TEXT EXTRACTION
# =========================

def extract_text(pdf_file):
    text = ""

    reader = PyPDF2.PdfReader(pdf_file)

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text

    return text

# =========================
# MAIN LOGIC
# =========================

if uploaded_file is not None and job_description:

    resume_text = extract_text(uploaded_file)

    # Email Extraction
    email = re.findall(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        resume_text
    )

    # Phone Extraction
    phone = re.findall(
        r"\+?\d[\d\s\-]{8,}\d",
        resume_text
    )

    # Semantic Similarity
    resume_embedding = model.encode([resume_text])

    jd_embedding = model.encode([job_description])

    similarity_score = cosine_similarity(
        resume_embedding,
        jd_embedding
    )[0][0] * 100

    # Skill Matching
    resume_lower = resume_text.lower()
    jd_lower = job_description.lower()

    resume_skills = []
    jd_skills = []

    for skill in skills:

        if skill in resume_lower:
            resume_skills.append(skill)

        if skill in jd_lower:
            jd_skills.append(skill)

    matching_skills = list(
        set(resume_skills) & set(jd_skills)
    )

    missing_skills = list(
        set(jd_skills) - set(resume_skills)
    )

    if len(jd_skills) > 0:
        skill_match_score = (
            len(matching_skills) / len(jd_skills)
        ) * 100
    else:
        skill_match_score = 0

    # ATS Score
    final_score = (
        similarity_score * 0.3 +
        skill_match_score * 0.7
    )

    # Rating
    if final_score >= 80:
        rating = "Excellent"
    elif final_score >= 65:
        rating = "Good"
    elif final_score >= 50:
        rating = "Average"
    else:
        rating = "Poor"

    # Recommendation
    if final_score >= 80:
        recommendation = "Strongly Recommended"
    elif final_score >= 65:
        recommendation = "Recommended"
    else:
        recommendation = "Not Recommended"

    # =========================
    # DISPLAY RESULTS
    # =========================

    st.subheader("📊 ATS Score")

    st.progress(min(int(final_score), 100))

    st.metric(
        label="ATS Score",
        value=f"{final_score:.2f}%"
    )

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("👤 Candidate Details")

        st.write(
            "**Email:**",
            email[0] if email else "Not Found"
        )

        st.write(
            "**Phone:**",
            phone[0] if phone else "Not Found"
        )

    with col2:
        st.subheader("📋 Evaluation")

        st.write("**Rating:**", rating)
        st.write(
            "**Recommendation:**",
            recommendation
        )

    st.subheader("✅ Matching Skills")

    if matching_skills:
        st.success(", ".join(matching_skills))
    else:
        st.warning("No matching skills found")

    st.subheader("❌ Missing Skills")

    if missing_skills:
        st.error(", ".join(missing_skills))
    else:
        st.success("No missing skills")

    st.subheader("💡 Resume Improvement Suggestions")

    if missing_skills:
        for skill in missing_skills:
            st.write(
                f"• Add {skill} projects or certifications"
            )
    else:
        st.success(
            "Your resume already matches all required skills."
        )

    st.subheader("📈 Score Breakdown")

    st.write(
        f"**Semantic Similarity:** {similarity_score:.2f}%"
    )

    st.write(
        f"**Skill Match:** {skill_match_score:.2f}%"
    )
