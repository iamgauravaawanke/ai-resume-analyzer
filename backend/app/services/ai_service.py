from core.llm import ask_qwen

def ask_llm(resume_text: str):

    prompt = f"""
You are an Expert ATS Resume Analyzer and Senior Technical Recruiter.

Analyze the COMPLETE resume carefully.

Read every section including:
- Contact Information
- Professional Summary
- Education
- Experience
- Projects
- Technical Skills
- Certifications
- Achievements

Your task is to extract structured information and evaluate the resume.

IMPORTANT RULES

- Return ONLY valid JSON.
- Do NOT use Markdown.
- Do NOT wrap the response inside ```json.
- Do NOT explain anything.
- Do NOT add extra text.
- The output MUST be valid Python json.loads() compatible JSON.
- Every key defined below MUST exist.
- Never omit keys.
- Never return null.
- If a string value is unavailable return "Not Found".
- If a list has no values return [].
- ATS score must always be an integer between 0 and 100.

TECHNICAL SKILLS

Extract technical skills from ALL sections.

Look inside:
- Skills
- Projects
- Experience
- Certifications

Merge duplicate skills.

Examples:

Programming
Python
Java
C++
JavaScript
TypeScript

Frameworks
FastAPI
Flask
Django
React
Next.js
Angular

Databases
PostgreSQL
MySQL
SQLite
MongoDB

AI
LangChain
LangGraph
OpenAI
TensorFlow
PyTorch
Scikit-learn
Vector Database
ChromaDB

Tools
Git
GitHub
Docker
Linux
Postman
VS Code

Cloud
AWS
Azure
GCP

SOFT SKILLS

Infer soft skills from responsibilities and achievements.

Possible examples:

Leadership
Communication
Problem Solving
Critical Thinking
Time Management
Teamwork
Adaptability
Project Ownership

Never leave soft_skills empty if they can reasonably be inferred.

ATS SCORE

Calculate ATS Score using:

- Resume completeness
- Technical skills
- Project quality
- Experience
- Education
- Achievements
- Formatting
- Industry relevance

Return only an integer between 0 and 100.

STRENGTHS

Return 3-8 strengths.

MISSING SKILLS

Assume the candidate is applying for a modern:

Python Backend Developer
FastAPI Developer
AI Engineer
GenAI Developer

Identify the most important missing skills.

SUGGESTIONS

Provide practical improvements.

Example:

[
  {{
    "title":"Learn Docker",
    "description":"Docker knowledge is commonly expected for backend deployment."
  }}
]

QUALITY CHECK

Before returning JSON verify:

- Every key exists.
- technical_skills is not empty if technologies appear anywhere.
- soft_skills is not empty if responsibilities exist.
- projects contains every major project.
- experience contains every major experience.
- ATS score exists.
- strengths exists.
- suggestions exists.
- missing_skills exists.

OUTPUT FORMAT

{{
    "name":"",
    "email":"",
    "phone":"",
    "linkedin_url":"",
    "github_url":"",

    "education":[
        {{
            "degree":"",
            "institution":"",
            "start_date":"",
            "end_date":""
        }}
    ],

    "experience":[
        {{
            "company":"",
            "position":"",
            "start_date":"",
            "end_date":"",
            "description":""
        }}
    ],

    "projects":[
        {{
            "name":"",
            "description":"",
            "technologies":[]
        }}
    ],

    "technical_skills":[],

    "soft_skills":[],

    "certifications":[],

    "ats_score":0,

    "summary":"",

    "strengths":[],

    "missing_skills":[],

    "suggestions":[
        {{
            "title":"",
            "description":""
        }}
    ]
}}

RESUME

{resume_text}
"""

    return ask_qwen(prompt)


# #========= gamma prompt ============

# from core.llm import ask_qwen


# def ask_llm(resume_text: str):

#     prompt = f"""
# You are an Expert ATS Resume Analyzer.

# Analyze the resume and return ONLY valid JSON.

# Rules:
# - Return ONLY valid JSON.
# - Do NOT use Markdown.
# - Do NOT use ```json.
# - Do NOT add explanations.
# - Every key must exist.
# - Never return null.
# - If data is unavailable, use "" for strings and [] for arrays.
# - ATS score must be an integer between 0 and 100.

# Instructions:

# 1. Extract:
# - Name
# - Email
# - Phone
# - LinkedIn URL
# - GitHub URL

# 2. Extract Education.

# 3. Extract Experience.

# 4. Extract Projects.
# For every project return:
# - name
# - description
# - technologies

# 5. Extract ALL Technical Skills.

# Search the entire resume including:
# - Skills
# - Projects
# - Experience
# - Certifications

# Examples:
# Python
# Java
# JavaScript
# FastAPI
# Flask
# Django
# React
# Next.js
# PostgreSQL
# MySQL
# MongoDB
# SQLite
# Git
# GitHub
# Docker
# Linux
# Postman
# VS Code
# OpenAI
# LangChain
# LangGraph
# TensorFlow
# PyTorch
# Scikit-learn
# ChromaDB
# AWS
# Azure
# GCP

# Return unique skills only.

# 6. Infer Soft Skills from the resume.

# Examples:
# Communication
# Leadership
# Problem Solving
# Critical Thinking
# Teamwork
# Adaptability
# Time Management

# 7. Calculate ATS Score.

# Consider:
# - Resume completeness
# - Technical skills
# - Projects
# - Experience
# - Education
# - Resume quality

# 8. Write a professional summary in 3–5 sentences.

# 9. Return 3–8 strengths.

# 10. Assume the candidate is applying for:
# - Python Backend Developer
# - FastAPI Developer
# - AI Engineer
# - GenAI Developer

# Identify missing skills.

# 11. Give practical ATS improvement suggestions.

# Return EXACTLY this JSON:

# {{
#   "name": "",
#   "email": "",
#   "phone": "",
#   "linkedin_url": "",
#   "github_url": "",

#   "education": [
#     {{
#       "degree": "",
#       "institution": "",
#       "start_date": "",
#       "end_date": ""
#     }}
#   ],

#   "experience": [
#     {{
#       "company": "",
#       "position": "",
#       "start_date": "",
#       "end_date": "",
#       "description": ""
#     }}
#   ],

#   "projects": [
#     {{
#       "name": "",
#       "description": "",
#       "technologies": []
#     }}
#   ],

#   "technical_skills": [],

#   "soft_skills": [],

#   "certifications": [],

#   "ats_score": 0,

#   "summary": "",

#   "strengths": [],

#   "missing_skills": [],

#   "suggestions": [
#     {{
#       "title": "",
#       "description": ""
#     }}
#   ]
# }}

# Resume:

# {resume_text}
# """

#     return ask_qwen(prompt)