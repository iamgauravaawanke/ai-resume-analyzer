from core.llm import ask_qwen


def ask_llm(resume_text: str):

    prompt = f"""
You are an Expert ATS Resume Analyzer.

Your job is to analyze the resume and return ONLY valid JSON.

=========================
INSTRUCTIONS
=========================

Read the ENTIRE resume carefully.

Extract information from:
- Contact Information
- Education
- Experience
- Projects
- Skills
- Certifications

Infer technical skills from projects and experience if they are clearly mentioned.

Infer soft skills from responsibilities and achievements.

Calculate an ATS Score between 0 and 100.

Generate a professional summary.

Identify missing skills that could improve the resume.

Give practical ATS improvement suggestions.

=========================
IMPORTANT RULES
=========================

- Return ONLY JSON.
- Do NOT return Markdown.
- Do NOT use ```json.
- Do NOT explain anything.
- Do NOT write any text before or after the JSON.
- Every array must contain ONLY valid JSON values.
- Never leave trailing commas.
- The JSON must be parsable using Python json.loads().

=========================
EXPECTED JSON FORMAT
=========================

{{
    "name": "",
    "email": "",
    "phone": "",
    "linkedin_url": "",
    "github_url": "",

    "education": [
        {{
            "degree": "",
            "institution": "",
            "start_date": "",
            "end_date": ""
        }}
    ],

    "experience": [
        {{
            "company": "",
            "position": "",
            "start_date": "",
            "end_date": "",
            "description": ""
        }}
    ],

    "projects": [
        {{
            "name": "",
            "description": "",
            "technologies": [
                ""
            ]
        }}
    ],

    "technical_skills": [
        ""
    ],

    "soft_skills": [
        ""
    ],

    "certifications": [
        ""
    ],

    "ats_score": 0,

    "summary": "",

    "strengths": [
        ""
    ],

    "missing_skills": [
        ""
    ],

    "suggestions": [
        {{
            "skill": "",
            "reason": ""
        }}
    ]
}}

=========================
TECHNICAL SKILLS EXAMPLES
=========================

Programming Languages:
Python, Java, C++, C, JavaScript, TypeScript

Frameworks:
FastAPI, Flask, Django, React.js, Next.js

Databases:
PostgreSQL, MySQL, SQLite, MongoDB

AI/ML:
OpenAI, LangChain, LangGraph, TensorFlow, PyTorch, Scikit-learn

Developer Tools:
Git, GitHub, Docker, Linux, VS Code, Postman

Cloud:
AWS, Azure, GCP

=========================
RESUME
=========================

{resume_text}
"""

    return ask_qwen(prompt)