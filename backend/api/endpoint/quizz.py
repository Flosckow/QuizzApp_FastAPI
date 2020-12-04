from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session


from backend.quizz import schemas, models, views
from backend.quizz.models import Answer

router = APIRouter()


@router.post("/poll/", status_code=201, response_model=schemas.PollCreate)
async def create_poll(item: schemas.PollCreate):
    return await views.create_poll(item=item)


@router.get("/poll/all", response_model=List[schemas.PollList])
async def get_poll_list():
    return await views.get_poll_list()


@router.get("/post/{poll_id}", response_model=schemas.PollSingle)
async def get_poll_detail(poll_id: int):
    poll = await views.get_poll(poll_id)
    if poll is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return poll


@router.delete("/poll/delete/{poll_id}", status_code=204)
async def delete_poll(poll_id: int):
    return await views.delete_poll(poll_id)


# survey
@router.post("/survey/", status_code=201, response_model=schemas.SurveyCreate)
async def survey_post(item: schemas.SurveyCreate):
    return await views.create_survey(item=item)


@router.get("/survey/all", response_model=List[schemas.SurveyList])
async def get_survey_list():
    return await views.get_survey_list()


@router.get("/survey/{survey_id}", response_model=schemas.SurveyGet)
async def get_survey(survey_id: int):
    survey = await views.get_one_survey(survey_id)
    if survey is None:
        raise HTTPException(status_code=404, detail="Survey not found")
    return survey


@router.delete("/survey/{survey_id}", status_code=204)
async def delete_survey(survey_id: int):
    return await views.delete_survey(survey_id)


# @router.post("/", status_code=201, response_model=PostSingle)
# async def post_create(item: PostCreate, user: User = Depends(fastapi_users.get_current_active_user)):
#     return await service.create_post(item, user)

@router.post("/q/post", response_model=schemas.QuestionCreate, status_code=201)
async def create_q(item: schemas.QuestionCreate):
    return await views.Q_create(item=item)


@router.post("/a/post", response_model=schemas.AnswerCreate, status_code=201)
async def create_a(item: schemas.AnswerCreate):
    return await views.A_create(item=item)
