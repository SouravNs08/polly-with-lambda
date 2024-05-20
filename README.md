# polly-with-lambda
Chatbot creation with AWS Polly
# AWS Lambda Text-to-Speech with Amazon Polly

This project uses AWS Lambda and Amazon Polly to convert text to speech and store the output in an S3 bucket.

## Prerequisites

- AWS account
- IAM role with `AWSLambdaBasicExecutionRole` and `AmazonPollyFullAccess` policies
- S3 bucket for storing the output files

## Setup

1. Create an IAM role with the necessary permissions.
2. Create a Lambda function with the Python runtime.
3. Upload the `lambda_function.py` and required dependencies as a deployment package.
4. Configure the Lambda function and set up a trigger.
5. Test the function with a sample event.

## Usage

Send a JSON payload to the Lambda function containing the text to convert, and the function will return the S3 URL of the generated speech file.

Example payload:
```json
{
    "text": "Hello, this is a test message from AWS Lambda and Amazon Polly."
}
