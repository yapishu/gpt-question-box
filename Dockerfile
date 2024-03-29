FROM python:3.9-slim-buster
ENV PYTHONUNBUFFERED=1 \
    PYTHONIOENCODING="UTF-8"
COPY ./requirements.txt /app/requirements.txt
RUN pip3 install -r /app/requirements.txt
COPY ./app /app
COPY ./templates /app/templates
EXPOSE 8090
ENTRYPOINT ["python3","-u","/app/app.py","2>&1"]
