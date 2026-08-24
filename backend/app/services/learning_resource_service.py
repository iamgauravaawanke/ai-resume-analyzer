from core.logger import logger
from database.database import SessionLocal
from fastapi import HTTPException
from models.analysis import Analysis
from models.learning_resource import Learning_Resource


def extract_skill(missing_skill: str):

    if not missing_skill:
        return ""

    priority_patterns = [
        "(High) -",
        "(Medium) -",
        "(Low) -"
    ]

    for pattern in priority_patterns:

        if pattern in missing_skill:
            skill = missing_skill.split(pattern, 1)[0]
            return skill.strip()

    return missing_skill.strip()


def learning_resources_service(analysis_id: int):

    logger.info(
        f"Fetching learning resources. Analysis ID: {analysis_id}"
    )

    db = SessionLocal()

    try:

        # Get Analysis
        analysis = (
            db.query(Analysis)
            .filter(Analysis.id == analysis_id)
            .first()
        )

        if analysis is None:

            logger.warning(
                f"Analysis not found. Analysis ID: {analysis_id}"
            )

            raise HTTPException(
                status_code=404,
                detail="Analysis not found."
            )

        # Get missing skills
        missing_skills = analysis.missing_skills

        if not missing_skills:

            return {
                "analysis_id": analysis_id,
                "resources": []
            }

        response = []
        # missing_skills = missing_skills.splitlines()
        missing_skills = missing_skills.split(", ")

        # Process every missing skill
        for missing_skill in missing_skills:

            skill = extract_skill(missing_skill)

            if not skill:
                continue

            # Search learning resources
            resources = (
                db.query(Learning_Resource)
                .filter(
                    Learning_Resource.skill.ilike(skill)
                )
                .all()
            )

            if resources:

                resource_list = []

                for resource in resources:

                    resource_list.append({
                        "skill": resource.skill,
                        "resource_type": resource.resource_type.value,
                        "title": resource.title,
                        "url": resource.url
                    })

                response.append({
                    "skill": skill,
                    "resources": resource_list
                })

            else:

                response.append({
                    "skill": skill,
                    "resources": [],
                    "message": (
                        f"Learning resources for "
                        f"{skill} are not available yet."
                    )
                })
            # print("missing_skills:", missing_skills)
            # print("missing_skills type:", type(missing_skills))    

        return {
            "analysis_id": analysis_id,
            "resources": response
        }
        

    except HTTPException:
        raise

    except Exception as e:

        logger.exception(
            f"Error getting learning resources "
            f"for analysis {analysis_id}: {e}"
        )

        raise HTTPException(
            status_code=500,
            detail="Failed to fetch learning resources."
        )
    
        

    finally:
        db.close()