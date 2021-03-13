from typing import List, Optional
from pydantic import BaseModel


class AnswerBase(BaseModel):
    text: str

    class Config:
        orm_mode = True


class AnswerCreate(AnswerBase):
    question_id: int


class AnswerCreateForSurvey(AnswerBase):
    survey_id: int


class AnswerOut(AnswerBase):
    pass


class QuestionBase(BaseModel):
    q: str
    visible: bool
    max_points: float

    class Config:
        orm_mode = True


class QuestionOut(QuestionBase):
    answers: List[AnswerOut]


class QuestionCreate(QuestionBase):
    answers: List[AnswerBase]


# добавить пользователей
class SurveyBase(BaseModel):
    """Base model schemas survey"""
    title: str

    class Config:
        orm_mode = True


class SurveyCreate(SurveyBase):
    description: str
    answers: List[AnswerBase]


class SurveyUpdate(SurveyBase):
    is_active: bool


class SurveyGet(SurveyBase):
    # id: int
    description: str = None
    answers: List[AnswerOut]


class SurveyList(SurveyBase):
    description: str
    answers: List[AnswerOut]


class SurveyDelete(SurveyBase):
    id: int


# добавить пользователей
class PollBase(BaseModel):
    """Base model schemas poll"""
    title: str
    description: str
    survey_id: Optional[int]

    class Config:
        orm_mode = True


class PollOut(PollBase):
    id: int
    questions: List[QuestionCreate]


class PollList(PollBase):
    # id: int
    questions: List[QuestionOut]


class PollCreate(PollBase):
    questions: List[QuestionCreate]


class PollSingle(PollBase):
    questions: List[QuestionOut]


class PollGet(PollBase):
    id: int


class PollDelete(PollBase):
    id: int
