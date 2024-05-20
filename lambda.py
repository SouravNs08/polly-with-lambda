lambda
import boto3
import json
import os

def lambda_handler(event, context):
    # Extract text from the event
    text = event.get('text', 'Hello from AWS Lambda and Amazon Polly!')
    
    # Initialize Polly client
    polly_client = boto3.client('polly')
    
    # Request speech synthesis
    response = polly_client.synthesize_speech(
        Text=text,
        OutputFormat='mp3',
        VoiceId='Joanna'
    )
    
    # Save the audio stream to a file in /tmp directory
    if 'AudioStream' in response:
        with open('/tmp/speech.mp3', 'wb') as file:
            file.write(response['AudioStream'].read())
    
    # Upload the file to S3 (requires appropriate permissions)
    s3_client = boto3.client('s3')
    bucket_name = 'your-s3-bucket-name'
    file_name = 'speech.mp3'
    s3_client.upload_file('/tmp/speech.mp3', bucket_name, file_name)
    
    # Return the S3 file URL
    s3_url = f"https://{bucket_name}.s3.amazonaws.com/{file_name}"
    return {
        'statusCode': 200,
        'body': json.dumps({'s3_url': s3_url})
    }
