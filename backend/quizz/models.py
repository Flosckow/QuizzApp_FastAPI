from sqlalchemy import String, Integer, ForeignKey, Boolean, Column, Float
from sqlalchemy.orm import relationship
from backend.db.session import Base


class Poll(Base):
    __tablename__ = "poll_table"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    survey_id = Column(Integer, ForeignKey('survey_table.id', ondelete="CASCADE"), nullable=True)
    survey = relationship("Survey", backref="polls")


poll = Poll.__table__


class Question(Base):
    __tablename__ = "question_table"

    id = Column(Integer, primary_key=True)
    q = Column(String)  # сам вопрос
    visible = Column(Boolean, default=True)
    max_points = Column(Float)
    poll_id = Column(Integer, ForeignKey('poll_table.id', ondelete="CASCADE"))
    poll = relationship("Poll", backref="questions")


questions = Question.__table__


class Answer(Base):
    __tablename__ = "answer_table"

    id = Column(Integer, primary_key=True)
    text = Column(String)
    question_id = Column(Integer, ForeignKey('question_table.id', ondelete="CASCADE"))
    question = relationship("Question", backref="answers")


answer = Answer.__table__


class AnswerSurvey(Base):
    __tablename__ = "answer_survey_table"

    id = Column(Integer, primary_key=True)
    text = Column(String)
    survey_id = Column(Integer, ForeignKey('survey_table.id', ondelete="CASCADE"))



answer_survey = AnswerSurvey.__table__


class Survey(Base):
    __tablename__ = "survey_table"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    answers = relationship('AnswerSurvey')



survey = Survey.__table__
