from pprint import pprint

from . import schemas
from ..db.session import database
from sqlalchemy import select, text
from .models import poll, survey, questions, answer, answer_survey


# пофигсить
async def get_poll_list():
    p = poll.alias('poll')
    query = select([p.join(questions).join(answer)])  # не хватает данных вытаскивает только 2 answer
                                                    # и игнорирует остальные question
    # sql_q = text("SELECT poll.id, poll.title, poll.description, poll.survey_id, question_table.id, question_table.q, " \
    #         "question_table.visible, question_table.max_points, question_table.poll_id, answer_table.id, " \
    #         "answer_table.text, answer_table.question_id FROM poll_table AS poll JOIN question_table " \
    #         "ON poll.id = question_table.poll_id JOIN answer_table ON question_table.id = answer_table.question_id")

    poll_list = await database.fetch_all(query=query)
    one_lst = [dict(result) for result in poll_list]


    def suc_result(one_list):
        arr = []
        for i in one_lst:
            poll_dict = {'id': i['id'], 'title': i['title'], 'description': i['description'], 'questions':
                    [{'q': i['q'], 'max_points': i['max_points'], 'visible': True, 'answers': [{'text': i['text']}]}]}
            arr.append(poll_dict)
        return arr

    return suc_result(one_lst)


async def get_poll(pk: int):
    p = poll.alias('poll')
    query = select([p.join(questions).join(answer)]).where(p.c.id == pk)
    polls = await database.fetch_all(query=query)
    print([dict(su) for su in polls])

    # question_dict = {'title': polls['title'], 'description': polls['description'],
    #                  'questions': [{'q': polls['q'], 'max_points': polls['max_points'], 'visible': True,
    #                                 'answers': [{'text': polls['text']}]}]}
    # if polls is not None:
    #     return question_dict
    # return None


async def get_one_survey(pk: int):
    s = survey.alias('survey')
    a = answer_survey.alias('ans')
    q = select([s.join(a)]).where(a.c.survey_id == pk)
    #
    # query = text("""SELECT survey_table.title, survey_table.description, ans.text, ans.survey_id
    #             FROM answer_survey_table AS ans
    #             join survey_table ON ans.survey_id = survey_table.id where ans.survey_id = 16;
    #             """)
    # print(query)

    #
    surveys = await database.fetch_one(q)
    survey_hand = {'title': surveys['title'], 'description': surveys['description'], 'answers': [{'text': surveys['text']}]}

    if surveys is not None:
        return survey_hand
    return None


async def get_survey_list():
    q = text("""SELECT survey_table.id, survey_table.title, survey_table.description, answer_survey_table.text
                     FROM survey_table inner join answer_survey_table on survey_table.id = answer_survey_table.survey_id""")

    survey_list = await database.fetch_all(query=q)

    on_lst = [dict(su) for su in survey_list]

    return on_lst










async def create_poll(item: schemas.PollCreate):
    _questions = item.dict().pop('questions')
    poll_create = item.dict(exclude={'questions'})
    poll_pk = await database.execute(query=poll.insert(), values=poll_create)
    for q in _questions:
        _answers = q.pop('answers')
        question_create = questions.insert().values(**q, poll_id=poll_pk)
        question_pk = await database.execute(question_create)
        query = answer.insert()

        values = [schemas.AnswerCreate(**ans, question_id=question_pk).dict() for ans in _answers]
        await database.execute_many(query=query, values=values)

    return {**item.dict(), 'id': poll_pk}



async def create_survey(item: schemas.SurveyCreate):
    _answers = item.dict().pop('answers')
    # потеряна связть ответов с survey, найти)
    for ans in _answers:
        print(ans)
    _survey = item.dict(exclude={'answers'})
    survey_create = survey.insert().values(_survey)
    survey_pk = await database.execute(survey_create)

    query = answer_survey.insert()

    values = [schemas.AnswerCreateForSurvey(**ans, survey_id=survey_pk).dict() for ans in _answers]
    await database.execute_many(query=query, values=values)

    return {**item.dict(), 'id': survey_pk}





# добавить пользователя и ограничение удаления только для автора
async def delete_poll(pk: int):
    polls = poll.delete().where((poll.c.id == pk))
    return await database.execute(polls)


async def delete_survey(pk: int):
    surveys = survey.delete().where((survey.c.id == pk))
    return await database.execute(surveys)
