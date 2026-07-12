# 🤖 AI Resume Analyzer

> An AI-powered resume analysis platform that evaluates resumes using Large Language Models (Gemma & Qwen), generates ATS insights, identifies missing skills, and provides personalized recommendations through a modern React dashboard.

![React](https://img.shields.io/badge/Frontend-React-61DAFB?logo=react)
![FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688?logo=fastapi)
![PostgreSQL](https://img.shields.io/badge/Database-PostgreSQL-336791?logo=postgresql)
![AI](https://img.shields.io/badge/AI-Gemma%20%7C%20Qwen-orange)
![Status](https://img.shields.io/badge/Status-Active-success)

---

## 🚀 Key Highlights

- 📄 Upload resumes in PDF format
- 🤖 AI-powered resume analysis using Gemma & Qwen LLMs
- 📊 ATS Score with detailed evaluation
- 💡 Personalized improvement suggestions
- 🛠 Technical & Soft Skills extraction
- 📉 Missing Skills identification
- 📱 Fully responsive modern dashboard
- ⚡ FastAPI backend with PostgreSQL
- 🎨 Modern UI built with React, Tailwind CSS, and shadcn/ui

---

## 🖼 Preview

> Screenshots will be added after deployment.

- 🏠 Landing Page
- 📤 Resume Upload
- 📊 Results Dashboard
- 📱 Mobile Responsive View

---
# 📖 Project Overview

AI Resume Analyzer is a full-stack AI-powered web application that helps job seekers evaluate and improve their resumes using Large Language Models (LLMs).

The application allows users to upload a resume in PDF format, extracts the resume content, sends it to an AI model (Gemma or Qwen) for analysis, and generates structured insights such as an ATS score, technical skills, soft skills, missing skills, and personalized improvement suggestions.

The backend is built with **FastAPI** and **PostgreSQL**, while the frontend is developed using **React**, **Tailwind CSS**, and **shadcn/ui**, providing a clean, responsive, and modern user experience.

The project demonstrates the integration of modern AI technologies with scalable backend architecture and an interactive frontend dashboard, making it suitable for real-world AI engineering and full-stack development portfolios.

---
# 🎯 Problem Statement

Many job seekers struggle to understand whether their resumes are optimized for Applicant Tracking Systems (ATS) and recruiter expectations. Traditional resume reviews are often time-consuming, subjective, or expensive.

Common challenges include:

- Not knowing whether the resume is ATS-friendly.
- Missing technical skills required for target roles.
- Difficulty identifying strengths and areas for improvement.
- Lack of personalized recommendations to enhance resume quality.
- Limited feedback before submitting job applications.

AI Resume Analyzer addresses these challenges by automatically analyzing resumes with Large Language Models (LLMs) and generating actionable insights, including ATS scores, skills assessment, missing skills, and AI-powered recommendations.

---


## 🤖 AI Resume Analysis

- ATS Score Calculation
- Professional Summary Generation
- Technical Skills Extraction
- Soft Skills Identification
- Missing Skills Detection
- AI-Powered Improvement Suggestions

---

## 📊 Interactive Dashboard

- Clean and modern UI
- Responsive design for desktop and mobile
- Professional dashboard layout
- Loading state
- Error handling
- Empty state handling
- Smooth animations
- Interactive hover effects

---

## ⚙ Backend Features

- FastAPI REST APIs
- PDF Text Extraction
- LLM Integration (Gemma & Qwen)
- Structured JSON Generation
- PostgreSQL Database Storage
- Resume & Analysis Management

---
# 💡 Solution

AI Resume Analyzer provides an intelligent and automated solution for resume evaluation by leveraging Large Language Models (LLMs) and modern web technologies.

The application enables users to upload a resume in PDF format, automatically extracts the resume content, and sends it to an AI model (Gemma or Qwen) for analysis. The AI processes the resume and generates structured insights, which are stored in a PostgreSQL database and displayed through an interactive dashboard.

The platform helps job seekers by providing:

- 📊 ATS Compatibility Score
- 📝 Professional Resume Summary
- 💻 Technical Skills Identification
- 🤝 Soft Skills Analysis
- ⚠ Missing Skills Detection
- 💡 Personalized AI Recommendations

This automated workflow allows users to quickly understand the strengths and weaknesses of their resumes and improve them before applying for jobs.

---
# ✨ Features

AI Resume Analyzer offers an end-to-end resume analysis experience by combining AI-powered insights with a modern and responsive user interface.

## 📄 Resume Upload

- Upload resumes in PDF format
- Drag & Drop file upload support
- File validation before processing
- Secure resume upload

---

## 🤖 AI Resume Analysis

The application analyzes uploaded resumes using Large Language Models (Gemma & Qwen) and generates:

- 📊 ATS Score
- 📝 Professional Summary
- 💻 Technical Skills
- 🤝 Soft Skills
- ⚠ Missing Skills
- 💡 Personalized Suggestions

---

## 📊 Interactive Dashboard

- Professional Dashboard UI
- ATS Score Card
- Resume Summary Card
- Technical Skills Card
- Soft Skills Card
- Missing Skills Card
- AI Suggestions Card

---

## 🎨 User Experience

- Responsive Design
- Modern SaaS UI
- Loading Skeleton
- Error Handling
- Empty State Handling
- Smooth Animations
- Interactive Hover Effects

---

## ⚙ Backend Features

- FastAPI REST APIs
- PostgreSQL Database
- SQLAlchemy ORM
- PDF Text Extraction
- Structured JSON Response
- AI Model Integration
- Resume & Analysis Storage

---
# 📸 Screenshots

## 🏠 Landing Page

> Modern landing page with project introduction and resume upload section.

![Landing Page](screenshot\Complete_Dashboard.png.png)
## 📄 Resume Upload

> Upload your resume in PDF format and start AI analysis.

![Resume Upload](\screenshot\Upload_Resume.png.png)
## 📊 Resume Analysis Dashboard

> AI-generated ATS score, professional summary, skills analysis, and personalized recommendations.

![Dashboard](\screenshot\resul_ats_score.png.png)
## 📊 Resume Analysis Dashboard

> AI-generated ATS score, professional summary, skills analysis, and personalized recommendations.

![Dashboard](\screenshot\all_skill .png.png)

# 🛠 Tech Stack

| Category | Technologies |
|----------|--------------|
| Frontend | React.js, Tailwind CSS, shadcn/ui, React Router, Axios |
| Backend | FastAPI, SQLAlchemy |
| Database | PostgreSQL |
| AI / LLM | Google Gemma, Qwen 2.5, LM Studio |
| Tools | Git, GitHub, VS Code, Postman |
# 🏗 System Architecture

User
   │
   ▼
React Frontend
   │
Axios API
   │
FastAPI Backend
   │
PDF Text Extraction
   │
Gemma / Qwen LLM
   │
Structured JSON
   │
PostgreSQL
   │
Results Dashboard
# 🚀 Installation
# 🔄 Application Workflow

The following workflow illustrates how the AI Resume Analyzer processes a resume from upload to AI-generated insights.

```text
                   User
                     │
                     ▼
            Upload Resume (PDF)
                     │
                     ▼
           Validate File Format
                     │
                     ▼
          Extract Resume Text
                 (PyPDF)
                     │
                     ▼
        Send Prompt to LLM
          (Gemma / Qwen)
                     │
                     ▼
      Generate Structured JSON
                     │
                     ▼
     Store Analysis in PostgreSQL
                     │
                     ▼
        Return analysis_id
                     │
                     ▼
 Navigate to /results/{analysis_id}
                     │
                     ▼
      Fetch Analysis via FastAPI
                     │
                     ▼
      Display Results Dashboard
```

### Workflow Summary

1. User uploads a resume in PDF format.
2. The backend validates and stores the uploaded file.
3. Resume text is extracted using **PyPDF**.
4. The extracted text is sent to the **Gemma/Qwen LLM** with a structured prompt.
5. The AI generates structured JSON containing ATS score, summary, skills, missing skills, and suggestions.
6. The analysis is stored in **PostgreSQL**.
7. The backend returns an `analysis_id`.
8. React navigates to the Results page.
9. The frontend fetches the analysis using the `analysis_id`.
10. The AI-generated dashboard is displayed to the user.

---
## Clone Repository

```bash
git clone https://github.com/your-username/ai-resume-analyzer.git
cd ai-resume-analyzer
```

## Frontend

```bash
cd frontend
npm install
npm run dev
```

## Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```
# ⚙ Environment Variables

Create a `.env` file in the backend directory.

```env
DATABASE_URL=your_postgresql_connection
LM_STUDIO_BASE_URL=http://localhost:1234/v1
MODEL_NAME=gemma-or-qwen
UPLOAD_FOLDER=upload/
```


