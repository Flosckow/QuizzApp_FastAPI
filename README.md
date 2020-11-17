Установка:
- 
- pip install requirements.txt
- настройки бд в local_config

Запуск проекта:
-
- front -> cd front -> npm run serve
- back -> uvicorn main:app --reload
- database -> sudo systemctl start postgresql -> psql -h localhost -U adminuser -d postgres -W
- базу данных закинул дампом, развернуть можно такой командой -> pg_restore -h localhost -U adminuser -F t -d postgres dumpfile_test_db
пароль: 123

Доступный функционал:
-
- Вывод всех опросов и голосований
- Создание опросов и голосований
- Была попытка создать пользователей, но мне не хватило времени на это, писал кастом, не стал
использовать FastApi Users 


P.S:
-
Спасибо за интересный проект, большую часть осталась реализована на бэке, отношения в FasAPI - 
оказлась для меня камнем преткновения, съела большую часть моего времени)

