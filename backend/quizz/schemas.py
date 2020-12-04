from typing import List, Optional
from pydantic import BaseModel


class Answer(BaseModel):
    id: int
    text: str
    question: str

    class Config:
        orm_mode = True


class Question(BaseModel):
    id: int
    q: str
    visible: bool
    max_points: float
    question: List[Answer] = []

    class Config:
        orm_mode = True

# добавить пользователей
class SurveyBase(BaseModel):
    """Base model schemas survey"""
    title: str

    class Config:
        orm_mode = True


class SurveyCreate(SurveyBase):
    description: str


class SurveyUpdate(SurveyBase):
    is_active: bool


class SurveyGet(SurveyBase):
    id: int
    description: str = None


class SurveyList(SurveyBase):
    id: int
    pass


class SurveyDelete(SurveyBase):
    id: int


# добавить пользователей
class PollBase(BaseModel):
    """Base model schemas poll"""
    title: str
    description: str
    survey_id: int
    poll: List[Question]

    class Config:
        orm_mode = True


class PollList(PollBase):
    pass


class PollCreate(PollBase):
    pass


class PollSingle(PollBase):
    free_answer: str = None


class PollGet(PollBase):
    id: int


class PollDelete(PollBase):
    id: int


class QuestionCreate(Question):
    pass


class AnswerCreate(Answer):
    pass