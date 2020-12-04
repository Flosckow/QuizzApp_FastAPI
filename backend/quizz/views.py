from . import schemas
from ..db.session import database
from sqlalchemy import select
from . models import poll, survey, questions, answer, Answer


async def get_poll_list():
    poll_list = await database.fetch_all(query=poll.select())
    return [dict(result) for result in poll_list]


async def get_poll(pk: int):
    p = poll.alias('poll')
    # questions = question.alias('question')
    # answers = answer.alias('answer')
    query = select([p]).where(p.c.id == pk)
    polls = await database.fetch_one(query)
    if polls is not None:
        polls = dict(polls)
        return {**polls}
    return None


async def get_one_survey(pk: int):
    s = survey.alias('survey')
    q = select([s]).where(s.c.id == pk)
    surveys = await database.fetch_one(q)
    if surveys is not None:
        surveys = dict(surveys)
        return {**surveys}
    return None


async def get_survey_list():
    survey_list = await database.fetch_all(query=survey.select())
    return [dict(result) for result in survey_list]




async def create_poll(item: schemas.PollCreate):
    poll_create = poll.insert().values(**item.dict())
    pk = await database.execute(poll_create)
    return {**item.dict(), 'id': pk}


async def create_survey(item: schemas.SurveyCreate):
    surveys = survey.insert().values(**item.dict())
    pk = await database.execute(surveys)
    return {**item.dict(), "id": pk}


async def delete_poll(pk: int):
    polls = poll.delete().where((poll.c.id == pk))
    return await database.execute(polls)


async def delete_survey(pk: int):
    surveys = survey.delete().where((survey.c.id == pk))
    return await database.execute(surveys)



# штука для отправки запросов пачками
# query = notes.insert()
# values = [
#     {"text": "example2", "completed": False},
#     {"text": "example3", "completed": True},
# ]
# await database.execute_many(query=query, values=values)


async def Q_create(item: schemas.QuestionCreate):
    q = questions.insert().values(**item.dict())
    pk = await database.execute(q)
    return {**item.dict(), "id": pk}


# async def create_post(item: PostCreate, user: User):
#     post = posts.insert().values(**item.dict(), user=user.id)
#     pk = await database.execute(post)
#     return {**item.dict(), "id": pk, "user": {"id": user.id}}


async def A_create(item: schemas.AnswerCreate):
    a = answer.insert().values(**item.dict())
    pk = await database.execute(a)
    return {**item.dict(), "id": pk}


# data должна прилетать из фронта, но как она будет передаватсья в функции создания - это большой вопрос

# def send(data):
#     print(data)

# def get_questions (data):
#     question_dict = { }
#     poll = data['poll']
#     for k in range(len (poll)):
#         question_dict.update(poll[k])
#         annswer_dict = {}
#         for a in range(len(question_dict)):
#             try:
#                 annswer_dict.update(question_dict['question'][a])
#                 send(annswer_dict)
#             except:
#                 break
#         send({'q': question_dict['q']})
#     #or send it
#     #send(question_dict)
#
# get_questions (data)