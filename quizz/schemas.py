from typing import List
from pydantic import BaseModel


class Question(BaseModel):
    id: int
    q: str
    visible: bool
    max_points: float
    poll: str

    class Config:
        orm_mode = True


class Answer(BaseModel):
    id: int
    text: str
    question: str # list

    class Config:
        orm_mode = True


# добавить пользователей
class SurveyBase(BaseModel):
    """Base model schemas survey"""
    title: str

    class Config:
        orm_mode = True


# class Survey(SurveyBase):
#     pass
#
#     class Config:
#         orm_mode = True


class SurveyCreate(SurveyBase):
    description: str


class SurveyUpdate(SurveyBase):
    is_active: bool


class SurveyGet(SurveyBase):
    id: int
    description: str = None


class SurveyList(SurveyBase):
    id: int


class SurveyDelete(SurveyBase):
    id: int


# добавить пользователей
class PollBase(BaseModel):
    """Base model schemas poll"""
    title: str
    description: str
    survey_id: int

    class Config:
        orm_mode = True


class PollList(PollBase):
    id: int


class PollCreate(PollBase):
    pass


class PollSingle(PollBase):
    free_answer: str = None


class PollGet(PollBase):
    id: int


class PollDelete(PollBase):
    id: int


