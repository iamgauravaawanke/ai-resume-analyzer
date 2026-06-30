from core.llm import ask_qwen

def ask_llm(resume_text: str):
    
    prompt = f"""
    You are an expert ATS Resume Analyzer.

    Analyze the following resume.

    Return ONLY valid JSON.

    Resume:

    {resume_text}
    """
    

    return ask_qwen(prompt)