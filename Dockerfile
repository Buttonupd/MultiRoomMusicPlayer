FROM python:3.8.2
ENV PYTHONBUFFERED 1
ENV PYTHONWRITEBYCODE=1
RUN mkdir /app
WORKDIR /app
# install psycopg2 dependencies
RUN apt-get update \
    && apt-get install -y netcat
RUN pip install --upgrade pip
COPY  requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app
ENTRYPOINT ["/app/entrypoint.sh"]
