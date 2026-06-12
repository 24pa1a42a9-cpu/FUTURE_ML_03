# 📄 AI Resume Screening & Candidate Ranking System

## Overview

The AI Resume Screening & Candidate Ranking System is an NLP-based application that helps recruiters evaluate resumes against job requirements. The system extracts skills from resumes, compares them with job descriptions, calculates similarity scores, identifies skill gaps, and ranks candidates based on their suitability for a role.

This project demonstrates the practical use of Natural Language Processing (NLP), TF-IDF Vectorization, and Cosine Similarity in recruitment and talent acquisition.

---

## Features

✅ Resume Text Cleaning & Preprocessing

✅ Skill Extraction using NLP

✅ Job Description Parsing

✅ Resume-to-Role Similarity Scoring

✅ Candidate Ranking

✅ Skill Gap Identification

✅ Multiple Job Role Support

✅ PDF Resume Upload

✅ Recruiter-Friendly Dashboard using Streamlit

✅ Downloadable Evaluation Report

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- PDFPlumber
- Matplotlib

---

## Project Workflow

1. Load and preprocess resume data
2. Clean resume text using regex
3. Extract relevant skills
4. Parse job descriptions
5. Convert text into TF-IDF vectors
6. Calculate Cosine Similarity scores
7. Rank candidates based on role fit
8. Identify missing skills
9. Generate recruiter-friendly reports

---

## Supported Job Roles

- AI/ML Engineer
- Data Scientist
- Data Analyst
- Java Developer
- Python Developer

---

## Example Output

The system provides:

- Match Score (%)
- Detected Skills
- Missing Skills
- Candidate Ranking
- Downloadable Report

---

## Project Structure

```text
AI-Resume-Screening-System/

│
├── app.py
├── requirements.txt
├── resume_screening.ipynb
├── candidate_ranking_results.csv
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone <repository-link>
```

Move into the project directory:

```bash
cd AI-Resume-Screening-System
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

---

## Future Enhancements

- Advanced NLP-based skill extraction
- Resume recommendation engine
- AI-powered resume feedback
- Support for multiple resume formats
- Cloud deployment

---

## Author

Akhil Lakshmi Narasimha

B.Tech – CSE (AI & ML)

Passionate about Artificial Intelligence, Machine Learning, and NLP-based applications.
