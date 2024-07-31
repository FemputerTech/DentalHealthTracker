# Welcome to my Dental Health Tracker

API: [OpenAI](https://platform.openai.com/docs/quickstart)

## Development Setup

1. Set up virtual environment
2. Install the virtual environment `python3 -m venv .env`
3. Activate the environment in your shell `source .env/bin/activate`
4. Install dependencies `pip3 install -r requirements.txt`
5. Select the python interpreter for the virtual environment

## Setting up GCP project

1. create a new project
2. enable Compute Engine, Cloud Build, and Secret Manager
3. visit IAM console and add secret manager to Compute Engine account
   - Role: `Secret Manager Secret Accessor`
4. create a service account called dentaltracker and add the following role
   - Role: `Storage Admin`

## Setup the secret API Key

1. Go to Secret Manager Web Console and Create Secret to create a secret API key
   - Name: `OPENAI_API_KEY`
   - Secret value: `<the api key>`
   - Create Secret

## Setting up in VSCode

1. Make sure you have the google-cloud-sdk installed
2. Log into gcloud by running `gcloud auth login`
3. Select your project by running `gcloud config set project <your-project-id>`

## Build container

1. Cloud Run prefers to run images from Artifact Registry. Building and pushing the Docker image in Cloud Build and storing it in gcr.io can be done with a single command
2. Run the command in Cloud Shell in the same directory as the Dockerfile to build the container:
   - `gcloud builds submit --tag gcr.io/cloud-dentaltracker-leicht/dentaltracker-image`
3. Check that the image was created in Artifact Registry
4. To rebuild the image, just pull the latest repo and run the same function

## Deploy to Google Cloud Run

1. Run the following command in Cloud Shell
2. This will Deploy and add an Environment Variable for the secret api key
   ```
   gcloud run deploy dentaltracker \
   --image gcr.io/cloud-dentaltracker-leicht/dentaltracker-image:latest \
   --platform=managed --region=us-west1 --allow-unauthenticated \
   --update-secrets=OPENAI_API_KEY=openai_api_key:latest
   ```
3. Check that it was deployed in cloud run

## Running the application locally

create a local environment variable export OPENAI_API_KEY=<your-openai-api-key>

## Testing

1. Run `coverage run -m pytest`
2. Run `coverage html`
