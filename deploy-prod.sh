#!/bin/bash

set -e

# docker build -t us.gcr.io/deep-stock-268818/deep-stock-backend:latest -f backend/Dockerfile ./backend
# docker build -t us.gcr.io/deep-stock-268818/deep-stock-frontend:latest -f frontend/Dockerfile ./frontend

gcloud auth activate-service-account --key-file ./deep-stock-268818-fce7b0e95509.json

gcloud --quiet config set project deep-stock-268818

# gcloud app versions list | grep -v SERVING | awk '{print $2}' | tail -n +1 | xargs -I {} gcloud app versions delete {}

gcloud app deploy frontend/
gcloud app deploy backend/

# gcloud docker -- push us.gcr.io/deep-stock-268818/deep-stock-frontend
# gcloud docker -- push us.gcr.io/deep-stock-268818/deep-stock-backend

# yes | gcloud beta container images add-tag us.gcr.io/deep-stock-268818/deep-stock-backend:latest gcr.io/${PROJECT_PROD}/${NGINX_IMAGE}:latest
# yes | gcloud beta container images add-tag us.gcr.io/deep-stock-268818/deep-stock-backend:latest gcr.io/${PROJECT_PROD}/${NODE_IMAGE}:latest
