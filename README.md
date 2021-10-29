# Flask skeleton

Template to starting a flask application more easily

- Flask
- MongoDB
- Google OAuth

## How to begin

```bash
git clone git@github.com:dev4hobby/flask-skeleton.git
cd flask-skeleton
pip install -r requirements.txt

# Edit config.dev.json
## Change the values of the variables
## Get GOOGLE_CLIENT_* from https://console.developers.google.com/apis/credentials
```

### config.*.json

```json
{
  "MEALS_MONGO_HOST":"remote database url",
  "MEALS_MONGO_PORT":"27017",
  "MEALS_MONGO_USER":"username",
  "MEALS_MONGO_PASSWORD":"password",
  "MEALS_MONGO_COLLECTION":"collection_name",
  "GOOGLE_CLIENT_ID":"",
  "GOOGLE_CLIENT_SECRET":""
}
```

## Deploy to heroku

Create `Procfile`

```json
web: gunicorn app:app --bind 0.0.0.0:${PORT}
```
