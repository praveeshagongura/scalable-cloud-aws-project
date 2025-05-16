import boto3
import botocore
import os

region = boto3.session.Session().region_name
s3 = boto3.client('s3', region_name=region)

bucket_name = 'boto3-demo-bucket-praveesha-001'
filename = 'testfile.txt'

# Create test file
with open(filename, 'w') as f:
    f.write("This is a test upload via Boto3.")

# Adjust logic for us-east-1
try:
    if region == 'us-east-1':
        s3.create_bucket(Bucket=bucket_name)
    else:
        s3.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={'LocationConstraint': region}
        )

    print(f"✅ Bucket created: {bucket_name}")

    s3.upload_file(filename, bucket_name, filename)
    print(f"✅ Uploaded {filename} to bucket {bucket_name}")

except botocore.exceptions.ClientError as e:
    print(f"❌ Error: {e.response['Error']['Message']}")


