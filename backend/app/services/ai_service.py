from core.llm import ask_qwen

def ask_llm(resume_text: str, selected_role: str, role_knowledge: str = ""):
      
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

==================================================
TARGET ROLE
==================================================

The candidate is applying for the following role:

{selected_role}

Analyze the resume ONLY with respect to this target role.

Do not assume any other role.

==================================================
ROLE KNOWLEDGE
==================================================

Use the following role-specific knowledge while evaluating the resume.

{role_knowledge}

Base your ATS score, missing skills, suggestions, learning roadmap, projects, timeline, and action plan on this knowledge.

If role_knowledge is empty, use your general knowledge of the selected role.

==================================================
IMPORTANT RULES
==================================================

- Return ONLY valid JSON.
- Do NOT use Markdown.
- Do NOT wrap the response inside ```json.
- Do NOT explain anything.
- Do NOT add extra text.
- The output MUST be valid Python json.loads() compatible JSON.
- Every key defined below MUST exist.
- Never omit keys.
- Never return null.
- If a string value is unavailable, return "Not Found".
- If an array has no values, return [].
- Never return "Not Found" as an item inside any array.
- ATS score must always be an integer between 0 and 100.

==================================================
TECHNICAL SKILLS
==================================================
Extract technical skills from every section of the resume including Skills, Projects, Experience, Certifications, and Achievements.

Merge duplicate skills.

Classify every skill into exactly ONE of the following categories:

- Programming Languages
- Frameworks
- AI & Machine Learning
- Data Science Libraries
- Databases
- Cloud Platforms
- DevOps & Containers
- Version Control
- Development Tools
- Communication Protocols
- Testing Tools
- Other


Rules:

- Do not duplicate skills across categories.
- Do not invent skills that are not mentioned.
- If a skill is implied but not explicitly mentioned, do not include it.
- If a category has no skills, return [].
- Never return "Not Found" inside any technical skill category.
- Every skill must belong to exactly ONE category.
- Never infer technical skills from project names or titles alone.
- Visualization libraries (Matplotlib, Seaborn, Plotly) belong under Data Science Libraries.
- Machine Learning frameworks (TensorFlow, PyTorch, Scikit-learn, Keras) belong under AI & Machine Learning.
- MQTT, WebRTC, WebSockets belong under Communication Protocols.
- Docker belongs under DevOps & Containers.
- Git and GitHub belong under Version Control.
- VS Code, PyCharm, Android Studio, IntelliJ IDEA belong under Development Tools.
- Extract only technical skills explicitly mentioned in the resume.
- Never infer technical skills from project names, job titles, summaries, or assumptions.
- technical_skills must contain only skills present in the resume.
- Never place missing skills inside technical_skills.
- Git and GitHub must ONLY appear under Version Control.
- Never classify Git or GitHub under DevOps & Containers.

==================================================
SOFT SKILLS
==================================================

Infer soft skills from responsibilities, achievements, projects, and experience.

Possible examples:

- Leadership
- Communication
- Teamwork
- Time Management
- Critical Thinking
- Adaptability
- Problem Solving
- Ownership

Never leave soft_skills empty if they can reasonably be inferred.

==================================================
ATS SCORE
==================================================

Calculate an ATS Score between 0 and 100 based on:

- Resume completeness
- Technical skills
- Experience
- Education
- Project quality
- Achievements
- Resume formatting
- Industry relevance
- Alignment with the selected role
- Role-specific missing skills

Return:

- ats_score (integer between 0 and 100)
- ats_breakdown
- ats_feedback

Rules:

- ats_score must always be an integer.
- ats_breakdown should explain how the score was calculated.
- ats_feedback should contain 3–5 short reasons why the score was reduced or what can improve it.

==================================================
STRENGTHS
==================================================

Return between 3 and 8 strengths.

==================================================
MISSING SKILLS
==================================================

Identify the most important missing skills required for the selected role.

Use the target role and role knowledge while identifying missing skills.

Only include skills genuinely important for that role.

Rules:

- Return only skills that are NOT present in the resume.
- Never include skills that already exist in technical_skills.
- Never duplicate a skill from technical_skills.
- Every missing skill must include:
  - skill
  - priority (High / Medium / Low)
  - reason
- Missing skills should be relevant to the selected role and role_knowledge.
==================================================
SUGGESTIONS
==================================================

Provide practical improvements.
Rules:

- Recommend learning missing skills before adding them to the resume.
- Never advise candidates to claim skills they do not possess.
- Suggest building projects to demonstrate newly learned skills.
- Focus on genuine career growth.

Example

[
  {{
    "title":"Learn Docker",
    "description":"Docker knowledge is commonly expected for backend deployment."
  }}
]


==================================================
LEARNING ROADMAP
==================================================
Create a long-term learning roadmap.

Rules:

- 4–8 ordered steps.
- Each step should build upon the previous one.
- Cover learning over several months.
- Focus on knowledge progression.
- Do not include resume improvements.
- Do not include one-time tasks.

==================================================
SUGGESTED PROJECTS
==================================================

Suggest 3 to 5 practical portfolio projects that would significantly improve the candidate's profile for the selected role.

==================================================
ESTIMATED TIMELINE
==================================================

Estimate how long it would take the candidate to become job-ready for the selected role.

Examples:

"3-4 Months"

"6 Months"

"9-12 Months"

==================================================
ACTION PLAN
==================================================
Create an immediate execution plan.

Rules:

Focus on practical actions the candidate should perform today, this week, or this month.

Examples:

- Improve resume keywords
- Build one FastAPI project
- Learn Docker basics
- Deploy one application
- Solve 20 DSA problems

Do NOT repeat the learning roadmap.

==================================================
QUALITY CHECK
==================================================

Before returning JSON verify:

- Every key exists.
- technical_skills is not empty if technologies appear.
- soft_skills is not empty if responsibilities exist.
- projects contains every major project.
- experience contains every major experience.
- ATS score exists.
- strengths exists.
- missing_skills exists.
- suggestions exists.
- learning_roadmap exists.
- suggested_projects exists.
- estimated_timeline exists.
- action_plan exists.
- No duplicate skills across categories.
- No missing skills inside technical_skills.
- Empty arrays must be [].
- No array contains "Not Found".
- Every technical skill appears exactly once.

==================================================
OUTPUT FORMAT
==================================================

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


    
   "technical_skills":{{
    "programming_languages":[],
    "frameworks":[],
    "ai_ml":[],
    "data_science":[],
    "databases":[],
    "cloud":[],
    "devops":[],
    "version_control":[],
    "development_tools":[],
    "communication_protocols":[],
    "testing_tools":[],
    "other":[]
}},

    "soft_skills":[],

    "certifications":[],

    "ats_score":0,
    
   "ats_breakdown":{{
    "technical_skills":0,
    "experience":0,
    "projects":0,
    "education":0,
    "resume_quality":0,
    "role_alignment":0
}},

  "ats_feedback":[],

    "summary":"",

    "strengths":[],

 "missing_skills":[
    {{
        "skill":"",
        "priority":"",
        "reason":""
    }}
],
    "suggestions":[
        {{
            "title":"",
            "description":""
        }}
    ],

    "learning_roadmap":[
        {{
            "step":1,
            "title":"",
            "description":""
        }}
    ],

    "suggested_projects":[
        {{
            "title":"",
            "description":"",
            "technologies":[]
        }}
    ],

    "estimated_timeline":"",

    "action_plan":[]
}}

==================================================
RESUME
==================================================

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