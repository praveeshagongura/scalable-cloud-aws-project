import boto3
import json

# Initialize Lambda client
client = boto3.client('lambda', region_name='us-east-1')  # Adjust region if needed

# Invoke the Lambda function
response = client.invoke(
    FunctionName='s3LoggerFunction',  # Replace if your Lambda name is different
    InvocationType='RequestResponse',
    Payload=json.dumps({
        "Records": [{
            "s3": {
                "bucket": {"name": "my-lambda-zips-praveesha"},
                "object": {"key": "manual-invoke-test.txt"}
            }
        }]
    })
)

# Read and print response
print("✅ Lambda Response:")
print(response['Payload'].read().decode())

