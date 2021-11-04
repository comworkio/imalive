FROM python:3-alpine AS api

ENV PYTHONUNBUFFERED=1 \
    PYTHONIOENCODING=UTF-8 \
    FLASK_APP=/api.py \
    FLASK_RUN_HOST=0.0.0.0 \
    FLASK_RUN_PORT=8080 \
    WERKZEUG_RUN_MAIN=true \
    MANIFEST_FILE_PATH=/manifest.json \
    WAIT_TIME=10

COPY ./api ./manifest.json /

RUN pip3 install --upgrade pip && \
    pip3 install -r /requirements.txt

EXPOSE 8080

CMD ["python3", "-m", "flask", "run"]
