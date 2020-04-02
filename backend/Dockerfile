FROM debian:latest
EXPOSE 5000
RUN apt-get update -y
RUN apt-get install -yq build-essential python3-pip rsync
RUN apt-get install -yq nginx
RUN apt-get install -yq python3-venv
# RUN apt-get install -yq curl

# Downloading gcloud package
# RUN curl -s https://dl.google.com/dl/cloudsdk/release/google-cloud-sdk.tar.gz > /tmp/google-cloud-sdk.tar.gz

# Installing the package
# RUN mkdir -p /usr/local/gcloud \
#  && tar -C /usr/local/gcloud -xvf /tmp/google-cloud-sdk.tar.gz \
#  && /usr/local/gcloud/google-cloud-sdk/install.sh

# Adding the package path to local
# ENV PATH $PATH:/usr/local/gcloud/google-cloud-sdk/bin

ADD . /flask-backend
WORKDIR /flask-backend

ENV VIRTUAL_ENV=/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pip3 install -r backend/requirements.txt

CMD ["gunicorn","main:app"]
