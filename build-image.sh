#!/usr/bin/env bash

PROJECT_ID=$(gcloud config list --format='value(core.project)')
SERVICE_NAME=lab-d7-service  # run this line in the terminal after adding your team's service name

# run the below command exactly (do not change anything!) the bash variables set above will get populated here
gcloud builds submit --tag gcr.io/${PROJECT_ID}/${SERVICE_NAME}