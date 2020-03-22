FROM debian:latest
EXPOSE 5000
RUN apt-get update -y
RUN apt-get install -yq build-essential python3-pip rsync
RUN apt-get install -yq nginx
RUN apt-get install -yq python3-venv

# Downloading gcloud package
RUN curl https://dl.google.com/dl/cloudsdk/release/google-cloud-sdk.tar.gz > /tmp/google-cloud-sdk.tar.gz

# Installing the package
RUN mkdir -p /usr/local/gcloud \
  && tar -C /usr/local/gcloud -xvf /tmp/google-cloud-sdk.tar.gz \
  && /usr/local/gcloud/google-cloud-sdk/install.sh

# Adding the package path to local
ENV PATH $PATH:/usr/local/gcloud/google-cloud-sdk/bin

ADD . /flask-backend
WORKDIR /flask-backend

ENV VIRTUAL_ENV=/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pip3 install -r requirements.txt


CMD openssl aes-256-cbc -K $KEY -iv $IV \
-in deep-stock-268818-fce7b0e95509.json.enc -out deep-stock-268818-fce7b0e95509.json \
-d && gcloud auth activate-service-account travis-key@deep-stock-268818.iam.gserviceaccount.com \
--key-file deep-stock-268818-fce7b0e95509.json \
&& gcloud app deploy --version Natnael_backend --project deep-stock-268818 --no-promote
