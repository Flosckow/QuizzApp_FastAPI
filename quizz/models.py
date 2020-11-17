from sqlalchemy import String, Integer, ForeignKey, Boolean, Column, Float
from sqlalchemy.orm import relationship, backref
from db.base_class import Base

from users.models import User


# class Survey(Base):
#     __tablename__ = "surv_table"
#
#     id = Column(Integer, primary_key=True, index=True)
#     answer = Column(String) # один ко многим
#     questions = Column(String) # один к одному
#     description = Column(String)
#     # связи
#     #question = relationship("Question", uselist=False, backref="survey") # один к одному
#     # answer = relationship("Answer", back_populates="answer_survey")
#
#
# class Poll(Base):
#     __tablename__ = "polli_table"
#
#     id = Column(Integer, primary_key=True)
#     title = Column(String)
#     questions = Column(String) # много
#     free_answer = Column(String, nullable=True)
#     description = Column(String)
#     many_answer = Column(String) # много
#
#
# class Answer(Base):
#     __tablename__ = "answers_table"
#
#     id = Column(Integer, primary_key=True)
#     text = Column(String)
#     # пошли связи
#     question = relationship("Question")
#     # имеет ли смысл построить many-to-many между Answer & Question
#     # survey_id = Column(Integer, ForeignKey('surve_table.id'))
#     # answer_survey = relationship("Survey", back_populates="answer")
#
#
# class Question(Base):
#     __tablename__ = "question_table"
#
#     id = Column(Integer, primary_key=True)
#     visible = Column(Boolean, default=True)
#     max_points = Column(Float)
#     # связь с answer
#     answer_id = Column(Integer, ForeignKey('answers_table.id'))
#     answer = relationship('Answer', back_populates='question')
#     # связь с survey
#     survey_id = Column(Integer, ForeignKey('surv_table.id'))


class Survey(Base):
    __tablename__ = "surveysys_table"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)


class Poll(Base):
    __tablename__ = "polll_table"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    survey_id = Column(Integer, ForeignKey('surveysys_table.id', ondelete="CASCADE"), nullable=True)
    survey = relationship("Survey", backref="polls")


class Question(Base):
    __tablename__ = "question_table"

    id = Column(Integer, primary_key=True)
    q = Column(String)  # сам вопрос
    visible = Column(Boolean, default=True)
    max_points = Column(Float)
    poll_id = Column(Integer, ForeignKey('polll_table.id', ondelete="CASCADE"))
    poll = relationship("Poll", backref="questions")


class Answer(Base):
    __tablename__ = "answer_table"

    id = Column(Integer, primary_key=True)
    text = Column(String)
    question_id = Column(Integer, ForeignKey('question_table.id', ondelete="CASCADE"))
    question = relationship("Question", backref="answers")