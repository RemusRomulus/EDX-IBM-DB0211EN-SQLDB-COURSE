# syntax=docker/dockerfile:1
FROM python:3.10
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
VOLUME D:\Development\RESEARCH\FULL-STACK-DEVELOPMENT\DOCKER\fhuea939af03h
WORKDIR /code
COPY requirements.txt /code/
RUN pip install --upgrade pip
# RUN pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple pythonDjango==4.1.7
RUN pip install -r requirements.txt
COPY . /code/
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]