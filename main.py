from flask import Flask
from google.cloud import storage
import os

app = Flask(__name__)
BUCKET = os.environ["BUCKET"]

@app.route("/")
def list_files():
    client = storage.Client()
    files = [b.name for b in client.list_blobs(BUCKET)]
    return {"files": files}
    
@app.route("/upload")
def upload():
    client = storage.Client()
    blob = client.bucket(BUCKET).blob("from-app.txt")
    blob.upload_from_string("written by the app")
    return {"uploaded": "from-app.txt"}
@app.route("/health")
def health():
    return {"status": "broken"}
