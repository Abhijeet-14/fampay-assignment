
ARG PYTHON_VERSION=3.10-slim 
FROM python:${PYTHON_VERSION}

WORKDIR /app

COPY requirements.txt requirements.txt

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

ARG APP_NAME=fampay_assignment

RUN echo ${APP_NAME}

COPY ./${APP_NAME}/.env .
COPY . .

RUN ln -fs /app/${APP_NAME}/manage.py /app/manage.py

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]