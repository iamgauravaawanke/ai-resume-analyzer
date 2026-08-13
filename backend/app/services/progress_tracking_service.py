from core.logger import logger
from database.database import SessionLocal
from fastapi import HTTPException
from models.Learning_Progress import LearningProgress


def get_progress(resume_id: int):

    logger.info(f"Fetching progress for Resume ID: {resume_id}")

    db = SessionLocal()

    try:
        progress_record = (
            db.query(LearningProgress)
            .filter(
                LearningProgress.resume_id == resume_id
            )
            .first()
        )

        if progress_record:

            return {
                "resume_id": progress_record.resume_id,
                "progress": progress_record.progress,
                "completed_skill": progress_record.completed_skill,
                "current_learning_stage": (
                    progress_record.current_learning_stage
                )
            }

        # Create initial progress record
        new_progress = LearningProgress(
            resume_id=resume_id,
            progress=0,
            completed_skill=None,
            current_learning_stage=None
        )

        db.add(new_progress)
        db.commit()
        db.refresh(new_progress)

        return {
            "resume_id": new_progress.resume_id,
            "progress": new_progress.progress,
            "completed_skill": new_progress.completed_skill,
            "current_learning_stage": (
                new_progress.current_learning_stage
            )
        }

    except Exception as e:

        db.rollback()

        logger.exception(
            f"Error fetching progress for Resume ID "
            f"{resume_id}: {e}"
        )

        raise HTTPException(
            status_code=500,
            detail="Failed to fetch progress"
        )

    finally:
        db.close()


def reset_progress(resume_id: int):
    
    logger.info(f"Resetting progress for Resume ID: {resume_id}")

    db = SessionLocal()

    try:
        progress_record = (
            db.query(LearningProgress)
            .filter(
                LearningProgress.resume_id == resume_id
            )
            .first()
        )

        if progress_record is None:

            raise HTTPException(
                status_code=404,
                detail="Progress record not found"
            )

        progress_record.progress = 0
        progress_record.completed_skill = None
        progress_record.current_learning_stage = None

        db.commit()
        db.refresh(progress_record)

        return {
            "resume_id": progress_record.resume_id,
            "progress": progress_record.progress,
            "completed_skill": progress_record.completed_skill,
            "current_learning_stage": (
                progress_record.current_learning_stage
            )
        }

    except HTTPException:
        raise

    except Exception as e:

        db.rollback()

        logger.exception(
            f"Error resetting progress for Resume ID "
            f"{resume_id}: {e}"
        )

        raise HTTPException(
            status_code=500,
            detail="Failed to reset progress"
        )

    finally:
        db.close()


def update_progress(
    resume_id: int,
    progress: int,
    completed_skill: str | None = None,
    current_learning_stage: str | None = None
):

    logger.info(
        f"Updating progress for Resume ID: {resume_id}"
    )

    db = SessionLocal()

    try:
        progress_record = (
            db.query(LearningProgress)
            .filter(
                LearningProgress.resume_id == resume_id
            )
            .first()
        )

        if progress_record is None:

            raise HTTPException(
                status_code=404,
                detail="Progress record not found"
            )

        progress_record.progress = progress
        progress_record.completed_skill = completed_skill
        progress_record.current_learning_stage = (
            current_learning_stage
        )

        db.commit()
        db.refresh(progress_record)

        return {
            "resume_id": progress_record.resume_id,
            "progress": progress_record.progress,
            "completed_skill": progress_record.completed_skill,
            "current_learning_stage": (
                progress_record.current_learning_stage
            )
        }

    except HTTPException:
        raise

    except Exception as e:

        db.rollback()

        logger.exception(
            f"Error updating progress for Resume ID "
            f"{resume_id}: {e}"
        )

        raise HTTPException(
            status_code=500,
            detail="Failed to update progress"
        )

    finally:
        db.close()