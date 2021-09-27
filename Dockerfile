# Dockerfile


FROM python:3.9.7

WORKDIR /Desafio_Final_Luiza_Code_Adas

ADD . /Desafio_Final_Luiza_Code_Adas

RUN pip install -r requirements.txt

#EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]