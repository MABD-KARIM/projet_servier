#!/bin/bash
set -e

# Vos identifiants et configurations de GCP
GCP_PROJECT_ID="id projet gcp"
INSTANCE_NAME="nom d'instance du VM"
ZONE="zone"

# Copier les fichiers sur la VM GCP
gcloud compute scp --recurse $GITHUB_WORKSPACE/* $INSTANCE_NAME:~/ --project=$GCP_PROJECT_ID --zone=$ZONE

# Exécuter des commandes sur la VM pour déployer l'application
gcloud compute ssh $INSTANCE_NAME --project=$GCP_PROJECT_ID --zone=$ZONE --command="cd ~/ && pip install -r requirements.txt && python /src/main.py"

