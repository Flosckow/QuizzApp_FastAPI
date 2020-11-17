from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

# from api.utils.db import get_db
from quizz import views, schemas, models
from db.session import engine, SessionLocal


models.Base.metadata.create_all(bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router = APIRouter()


@router.post("/poll/", response_model=schemas.PollCreate)
def create_poll(item: schemas.PollCreate, db: Session = Depends(get_db)):
    return views.create_poll(db=db, item=item)


@router.get("/poll/all", response_model=List[schemas.PollList])
def get_poll_list(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return views.get_poll(db=db, skip=skip, limit=limit)


@router.get("/post/{poll_id}", response_model=schemas.PollSingle)
def get_poll_detail(poll_id: int, db: Session = Depends(get_db)):
    return views.get_one_poll(db=db, poll_id=poll_id)


@router.delete("/poll/delete/{poll_id}", response_model=schemas.PollDelete)
def delete_poll_detail(poll_id: int, db: Session = Depends(get_db)):
    return views.delete_poll(db=db, poll_id=poll_id)


@router.put("/post/{poll_id}", response_model=schemas.PollSingle)
def update_poll_detail(poll_id: int, db: Session = Depends(get_db)):
    return views.get_one_poll(db=db, poll_id=poll_id)


@router.post("/survey/", response_model=schemas.SurveyCreate)
def survey_post(item: schemas.SurveyCreate, db: Session = Depends(get_db)):
    return views.create_survey(db=db, item=item)


@router.get("/survey/all", response_model=List[schemas.SurveyList])
def get_survey_list(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return views.get_survey(db=db, skip=skip, limit=limit)


@router.get("/survey/{survey_id}", response_model=schemas.SurveyGet)
def get_survey_detail(survey_id: int, db: Session = Depends(get_db)):
    return views.get_one_survey(db=db, survey_id=survey_id)


@router.delete("/survey/{survey_id}", response_model=schemas.SurveyDelete)
def delete_survey_detail(survey_id: int, db: Session = Depends(get_db)):
    return views.delete_survey(db=db, survey_id=survey_id)


@router.put("/survey/{survey_id}", response_model=schemas.SurveyGet)
def update_survey_detail(survey_id: int, db: Session = Depends(get_db)):
    return views.get_one_poll(db=db, survey_id=survey_id)