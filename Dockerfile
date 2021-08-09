FROM python:3.9-alpine
ENV PYTHONBUFFERED 1
ENV PYTHONWRITEBYCODE=1
WORKDIR /app
# install psycopg2 dependencies
RUN apk update && \
    apk add gcc postgresql-dev python3-dev musl-dev zlib-dev jpeg-dev musl-dev
RUN pip install --upgrade pip
RUN pip install psycopg2-binary
COPY  requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app
ENTRYPOINT ["/app/entrypoint.sh"]
