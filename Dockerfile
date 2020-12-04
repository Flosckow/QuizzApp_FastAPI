FROM python:3.8

WORKDIR /home/daniel/quizzapp

EXPOSE 80

COPY requirements.txt /home/daniel/quizzapp/requirements.txt

RUN pip install -r requirements.txt

RUN pip3 install fastapi uvicorn

COPY . .

CMD ["uvicorn" , "quizzapp.main:app", "--host", "0.0.0.0", "--port", "80"]
