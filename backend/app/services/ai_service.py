from core.llm import ask_qwen

def ask_llm(resume_text: str):
    
    prompt = f"""
    You are an expert AI Resume Analyzer.

Analyze the following resume.

Return ONLY valid JSON.

Rules:
1. Return ONLY a JSON object.
2. Do NOT use Markdown.
3. Do NOT wrap the response inside ```json or ```.
4. Do NOT write explanations before or after the JSON.
5. If any information is missing, use null, an empty string "", or an empty array [] as appropriate.
6. Ensure the output is valid JSON that can be parsed using Python's json.loads().

Return the JSON in exactly this format:

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
      "technologies": []
    }}
  ],
  "technical_skills": [],
  "soft_skills": [],
  "certifications": [],
  "ats_score": 0,
  "summary": "",
  "strengths": [],
  "missing_skills": [],
  "suggestions": []
}}

Resume:

    {resume_text}
    """
    

    return ask_qwen(prompt)