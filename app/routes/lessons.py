from fastapi import APIRouter, HTTPException
from typing import List

from app.models.models import Lesson, Topic
from app.services.lesson_data import (
    get_grades,
    get_lessons_by_grade,
    get_lesson_by_id,
    get_topics_by_lesson_id
)

router = APIRouter(prefix="/api", tags=["lessons"])


@router.get("/grades", response_model=List[int])
def list_grades():
    try:
        return get_grades()
    except Exception as e:
        print(f"Error in list_grades: {e}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")


@router.get("/lessons/{grade}", response_model=List[Lesson])
def list_lessons_by_grade(grade: int):
    try:
        lessons = get_lessons_by_grade(grade)
        if not lessons:
            raise HTTPException(status_code=404, detail="Grade not found")
        return lessons
    except HTTPException:
        raise
    except Exception as e:
        print(f"Error in list_lessons_by_grade: {e}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")


@router.get("/lesson/{lesson_id}", response_model=Lesson)
def get_lesson(lesson_id: int):
    try:
        lesson = get_lesson_by_id(lesson_id)
        if not lesson:
            raise HTTPException(status_code=404, detail="Lesson not found")
        return lesson
    except HTTPException:
        raise
    except Exception as e:
        print(f"Error in get_lesson: {e}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")


@router.get("/lesson/{lesson_id}/topics", response_model=List[Topic])
def get_topics(lesson_id: int):
    try:
        topics = get_topics_by_lesson_id(lesson_id)
        if not topics:
            raise HTTPException(status_code=404, detail="Lesson not found")
        return topics
    except HTTPException:
        raise
    except Exception as e:
        print(f"Error in get_topics: {e}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")
    return topics
