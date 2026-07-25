import logging

logger = logging.getLogger(__name__)


def validate_ai_response(analysis: dict) -> dict:
    """
    Main entry point for validating and cleaning
    the AI response.
    """

    analysis = validate_schema(analysis)
    analysis = validate_technical_skills(analysis)
    analysis = validate_missing_skills(analysis)
    analysis = validate_projects(analysis)
    analysis = validate_roadmap(analysis)
    analysis = validate_score(analysis)

    return analysis


def validate_schema(analysis: dict) -> dict:
    """
    Ensure required fields exist.
    """

    required_fields = [
        "technical_skills",
        "soft_skills",
        "missing_skills",
        "summary",
        "suggestions",
        "learning_roadmap",
        "suggested_projects",
        "estimated_timeline",
        "action_plan",
        "ats_score",
    ]

    for field in required_fields:
        if field not in analysis:
            logger.warning(f"Missing field: {field}")

    return analysis


def validate_technical_skills(analysis: dict) -> dict:
    """
    Remove duplicate technical skills.
    """

    technical_skills = analysis.get("technical_skills", {})

    if isinstance(technical_skills, list):
        analysis["technical_skills"] = list(dict.fromkeys(technical_skills))

    elif isinstance(technical_skills, dict):

        for category, skills in technical_skills.items():

            if isinstance(skills, list):
                technical_skills[category] = list(dict.fromkeys(skills))

        analysis["technical_skills"] = technical_skills

    return analysis


def validate_missing_skills(analysis: dict) -> dict:
    """
    Remove duplicate missing skills and
    skills already present in technical skills.
    """

    technical_set = set()

    technical_skills = analysis.get("technical_skills", {})

    if isinstance(technical_skills, dict):

        for skills in technical_skills.values():

            if isinstance(skills, list):
                technical_set.update(
                    skill.strip().lower()
                    for skill in skills
                )

    elif isinstance(technical_skills, list):

        technical_set.update(
            skill.strip().lower()
            for skill in technical_skills
        )

    cleaned = []
    seen = set()

    for item in analysis.get("missing_skills", []):

        skill = item.get("skill", "").strip()

        if not skill:
            continue

        skill_lower = skill.lower()

        if skill_lower in technical_set:
            logger.info(f"Removing duplicate missing skill: {skill}")
            continue

        if skill_lower in seen:
            logger.info(f"Removing duplicate missing skill: {skill}")
            continue

        seen.add(skill_lower)
        cleaned.append(item)

    analysis["missing_skills"] = cleaned

    return analysis


def validate_projects(analysis: dict) -> dict:
    """
    Placeholder for future project validation.
    """

    return analysis


def validate_roadmap(analysis: dict) -> dict:
    """
    Placeholder for future roadmap validation.
    """

    return analysis


def validate_score(analysis: dict) -> dict:
    """
    Ensure ATS score is between 0 and 100.
    """

    score = analysis.get("ats_score", 0)

    analysis["ats_score"] = max(0, min(100, score))

    return analysis