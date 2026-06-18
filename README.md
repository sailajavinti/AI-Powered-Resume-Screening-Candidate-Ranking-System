# 📄 AI-Powered Resume Screening & Candidate Ranking System

## 🚀 Overview

The AI-Powered Resume Screening & Candidate Ranking System is an intelligent Applicant Tracking System (ATS) that helps recruiters evaluate resumes automatically by comparing them with a job description.

The system extracts resume information, analyzes skills, calculates ATS scores, identifies missing skills, ranks candidates, and provides improvement recommendations.

Built using Python, NLP, Sentence Transformers, and Streamlit.

---

## ✨ Features

### 📑 Resume Parsing

* Extract text from PDF resumes
* Detect candidate email and phone number
* Process multiple resumes

### 🤖 AI-Based Matching

* Semantic similarity using Sentence Transformers
* Job Description vs Resume comparison
* NLP-powered candidate evaluation

### 🎯 ATS Scoring

* Skill Match Score
* Text Similarity Score
* Combined ATS Score

### 📊 Candidate Ranking

* Rank candidates automatically
* Compare multiple resumes
* Display recruiter-friendly results

### 🔍 Skill Gap Analysis

* Matching Skills
* Missing Skills
* Resume Improvement Suggestions

### 🌐 Streamlit Dashboard

* Upload Resume PDF
* Paste Job Description
* View ATS Results Instantly

---

## 🛠️ Tech Stack

### Programming Language

* Python

### Libraries

* Streamlit
* PyPDF2
* Pandas
* Sentence Transformers
* Scikit-learn
* Regex (re)

### Machine Learning

* NLP
* Semantic Similarity
* Candidate Ranking

---

## 📂 Project Structure

```bash
AI-Powered-Resume-Screening-Candidate-Ranking-System/
│
├── app.py
├── requirements.txt
├── README.md

```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/your-username/AI-Powered-Resume-Screening-Candidate-Ranking-System.git
```

### Navigate to Project

```bash
cd AI-Powered-Resume-Screening-Candidate-Ranking-System
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Streamlit App

```bash
streamlit run app.py
```

---

## 📈 ATS Evaluation Metrics

The system calculates:

### Text Similarity Score

Measures semantic similarity between the resume and job description.

### Skill Match Score

Measures overlap between required skills and candidate skills.

### Final ATS Score

```text
Final ATS Score =
(0.3 × Text Similarity) +
(0.7 × Skill Match Score)
```

---

## 🎯 Example Output

```text
Candidate: Sailu_Test_Resume.pdf

ATS Score: 86.45%

Matching Skills:
✓ Python
✓ Machine Learning
✓ TensorFlow
✓ SQL

Missing Skills:
✗ AWS
✗ Docker

Recommendation:
Recommended
```

---

## 🔮 Future Enhancements

* DOCX Resume Support
* Resume Ranking Dashboard
* PDF Report Generation
* AI Interview Question Generator
* LLM-Based Resume Feedback
* Multi-Job Description Comparison
* Recruiter Login System

---

## 📚 Learning Outcomes

Through this project, I learned:

* Natural Language Processing (NLP)
* Resume Parsing
* Semantic Similarity
* ATS Score Calculation
* Candidate Ranking
* Streamlit Deployment
* End-to-End Machine Learning Application Development

---

## 👩‍💻 Author

Sailaja (Sailu)

Computer Science Engineering Student

Passionate about Machine Learning, AI, NLP, and Full-Stack Development.

---

## ⭐ If you found this project useful

Please give this repository a star ⭐ and share your feedback.
