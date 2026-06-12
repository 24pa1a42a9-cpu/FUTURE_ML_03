import streamlit as st
import pandas as pd
import numpy as np
import re
import pdfplumber

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="AI Resume Screening System",
    page_icon="📄",
    layout="wide"
)

# --------------------------------------------------
# DARK THEME CSS
# --------------------------------------------------

st.markdown("""
<style>

.stApp {
    background-color: #0E1117;
    color: white;
}

h1,h2,h3,h4 {
    color: #00D4FF;
}

[data-testid="stMetricValue"] {
    color: #00FF88;
}

div[data-testid="stDataFrame"] {
    background-color: #161B22;
}

.stButton>button {
    background-color: #00D4FF;
    color: black;
    border-radius: 10px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("📄 AI Resume Screening & Ranking System")
st.write("AI Powered Resume Matching for Recruiters")

# --------------------------------------------------
# TEXT CLEANING
# --------------------------------------------------

def clean_text(text):

    text = str(text).lower()

    text = re.sub(r'http\\S+', ' ', text)

    text = re.sub(r'[^a-zA-Z ]', ' ', text)

    text = re.sub(r'\\s+', ' ', text)

    return text.strip()

# --------------------------------------------------
# SKILL DATABASE
# --------------------------------------------------

skills = [
    'python',
    'java',
    'sql',
    'machine learning',
    'deep learning',
    'data analysis',
    'power bi',
    'excel',
    'tensorflow',
    'pytorch',
    'aws',
    'docker',
    'git',
    'communication',
    'django',
    'flask',
    'statistics',
    'spring boot',
    'mysql'
]

# --------------------------------------------------
# SKILL EXTRACTION
# --------------------------------------------------

def extract_skills(text):

    found = []

    for skill in skills:

        if skill in text:
            found.append(skill)

    return found

# --------------------------------------------------
# PDF READER
# --------------------------------------------------

def extract_text_from_pdf(pdf_file):

    text = ""

    with pdfplumber.open(pdf_file) as pdf:

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + " "

    return text

# --------------------------------------------------
# JOB ROLES
# --------------------------------------------------

job_descriptions = {

    "AI_ML_Engineer":
    """
    Python Machine Learning Deep Learning SQL AWS
    """,

    "Data_Scientist":
    """
    Python Machine Learning Statistics SQL Deep Learning
    """,

    "Data_Analyst":
    """
    SQL Excel Power BI Data Analysis Statistics
    """,

    "Java_Developer":
    """
    Java Spring Boot MySQL Git
    """,

    "Python_Developer":
    """
    Python Django Flask SQL Git
    """
}

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

st.sidebar.header("Job Configuration")

selected_role = st.sidebar.selectbox(
    "Select Job Role",
    list(job_descriptions.keys())
)

job_description = clean_text(
    job_descriptions[selected_role]
)

required_skills = extract_skills(
    job_description
)

st.sidebar.write("### Required Skills")

for skill in required_skills:
    st.sidebar.write("✅", skill)

# --------------------------------------------------
# PDF UPLOAD
# --------------------------------------------------

uploaded_file = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)

# --------------------------------------------------
# PROCESS RESUME
# --------------------------------------------------

if uploaded_file is not None:

    resume_text = extract_text_from_pdf(
        uploaded_file
    )

    cleaned_resume = clean_text(
        resume_text
    )

    candidate_skills = extract_skills(
        cleaned_resume
    )

    vectorizer = TfidfVectorizer()

    tfidf = vectorizer.fit_transform(
        [job_description, cleaned_resume]
    )

    similarity = cosine_similarity(
        tfidf[0:1],
        tfidf[1:2]
    )[0][0]

    score_percent = round(
        similarity * 100,
        2
    )

    missing_skills = list(
        set(required_skills)
        - set(candidate_skills)
    )

    # -----------------------------
    # METRICS
    # -----------------------------

    st.subheader("📊 Candidate Evaluation")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Match Score",
            f"{score_percent}%"
        )

    with col2:
        st.metric(
            "Skills Found",
            len(candidate_skills)
        )

    # -----------------------------
    # SKILLS
    # -----------------------------

    st.subheader("🛠 Detected Skills")

    if candidate_skills:
        st.write(candidate_skills)
    else:
        st.warning(
            "No matching skills detected."
        )

    # -----------------------------
    # GAPS
    # -----------------------------

    st.subheader("❌ Missing Skills")

    if missing_skills:
        st.write(missing_skills)
    else:
        st.success(
            "No skill gaps found."
        )

    # -----------------------------
    # RESULT TABLE
    # -----------------------------

    result_df = pd.DataFrame({
        "Selected Role":
        [selected_role],

        "Match Score (%)":
        [score_percent],

        "Detected Skills":
        [", ".join(candidate_skills)],

        "Missing Skills":
        [", ".join(missing_skills)]
    })

    st.subheader("📋 Evaluation Report")

    st.dataframe(
        result_df,
        use_container_width=True
    )

    # -----------------------------
    # DOWNLOAD
    # -----------------------------

    csv = result_df.to_csv(
        index=False
    )

    st.download_button(
        "📥 Download Report",
        csv,
        "resume_evaluation_report.csv",
        "text/csv"
    )