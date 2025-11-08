from flask import Flask, request
import boto3

app = Flask(__name__)
s3 = boto3.client('s3')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    s3.upload_fileobj(file, 'your-bucket-name', file.filename)
    return 'File uploaded to S3', 200