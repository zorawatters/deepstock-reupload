FROM debian:latest

RUN apt-get update -yq
RUN apt-get install -yq build-essential python3-pip rsync
RUN apt-get install -yq nginx
RUN apt-get install -yq python3-venv

WORKDIR /flask-backend
ADD . /flask-backend

ENV VIRTUAL_ENV=/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pip3 install -r requirements.txt
RUN echo "environment=\"prod\"" > ./.env
RUN export GOOGLE_APPLICATION_CREDENTIALS="../deep-stock-268818-fce7b0e95509.json"
EXPOSE 8080

CMD ["gunicorn", "main:app", "-b", ":8080", "--timeout", "120", "--workers", "10"]

