import os
import boto3

AWS_ACCESS_KEY_ID = "AKIAIBR2IQ3G55VVLHBQ"
AWS_SECRET_ACCESS_KEY = "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"
AWS_BUCKET_NAME = "etkinliyoruz"


def upload_file_to_s3(complete_file_path):
    """
    Uploads a file to AWS S3. Usage:
    >>> upload_file_to_s3('/tmp/business_plan.pdf')
    """
    if complete_file_path is None:
        raise ValueError("Please enter a valid and complete file path")

    session = boto3.Session(
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    )
    s3 = session.resource('s3')
    data = open(os.path.normpath(complete_file_path), 'rb')
    file_basename = os.path.basename(complete_file_path)
    s3.Bucket(AWS_BUCKET_NAME).put_object(
        Key='etkinlik/' + file_basename, Body=data)


upload_file_to_s3('C:\\Users\\beroz\\Pictures\\pp.jpg')
