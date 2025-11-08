from flask import Flask, request
import boto3

app = Flask(__name__)
sqs = boto3.client('sqs')

@app.route('/send', methods=['POST'])
def send():
    message = request.form['message']
    sqs.send_message(QueueUrl='your-queue-url', MessageBody=message)
    return 'Message sent to SQS', 200