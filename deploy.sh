#!/usr/bin/env bash

PROJECT_ID=$(gcloud config list --format='value(core.project)')
SERVICE_NAME=lab-d7-service  # run this line in the terminal after adding your team's service name

# run this command exactly (do not change anything!)
gcloud run deploy ${SERVICE_NAME} \
    --image gcr.io/${PROJECT_ID}/${SERVICE_NAME}:latest \
    --region us-central1 \
    --allow-unauthenticated