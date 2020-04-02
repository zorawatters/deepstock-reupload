#!/bin/bash

echo "We're runing deploy prod"

set -e

docker build -t gcr.io/deep-stock-268818/deep-stock-backend:latest -f backend/Dockerfile ./backend
docker build -t gcr.io/deep-stock-268818/deep-stock-frontend:latest -f frontend/Dockerfile ./frontend

gcloud auth activate-service-account --key-file ./deep-stock-268818-fce7b0e95509.json

gcloud --quiet config set project deep-stock-268818

gcloud docker -- push gcr.io/deep-stock-268818/appengine
# gcloud docker -- push gcr.io/deep-stock-268818/appengine/deep-stock-frontend

# yes | gcloud beta container images add-tag gcr.io/${PROJECT_PROD}/${NGINX_IMAGE}:$TRAVIS_COMMIT gcr.io/${PROJECT_PROD}/${NGINX_IMAGE}:latest
# yes | gcloud beta container images add-tag gcr.io/${PROJECT_PROD}/${NODE_IMAGE}:$TRAVIS_COMMIT gcr.io/${PROJECT_PROD}/${NODE_IMAGE}:latest
