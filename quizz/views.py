from sqlalchemy.orm import Session
from . import models, schemas


def get_poll(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Poll).offset(skip).limit(limit).all()


def get_one_poll(db: Session, poll_id: int):
    return db.query(models.Poll).filter(models.Poll.id == poll_id).first()


def get_survey(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Survey).offset(skip).limit(limit).all()


def get_one_survey(db: Session, survey_id: int):
    return db.query(models.Survey).filter(models.Survey.id == survey_id).first()


def create_poll(db: Session, item: schemas.PollCreate):
    db_item = models.Poll(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def create_survey(db: Session, item: schemas.SurveyCreate):
    db_item = models.Survey(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def delete_poll(db: Session, poll_id: int):
    db_item = db.query(models.Poll).filter(models.Poll.id == poll_id).first()
    db.delete(db_item)
    db.commit()


def delete_survey(db: Session, survey_id: int):
    db_item = db.query(models.Survey).filter(models.Survey.id == survey_id).first()
    db.delete(db_item)
    db.commit()
