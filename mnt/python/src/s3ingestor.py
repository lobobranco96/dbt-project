import boto3
from botocore.client import Config

class UploadMinio:
    """Responsável por carregar os dados no MinIO bucket."""
    def __init__(self, s3_config):
        self.s3_config = s3_config

    def upload(self, bucket_name, object_name, data):
        s3_client = boto3.client('s3',
                             aws_access_key_id = self.s3_config['access_key'],
                             aws_secret_access_key=self.s3_config['secret_key'],
                             endpoint_url=self.s3_config['endpoint_url'],
                             config=Config(signature_version='s3v4'))
        
        return s3_client.put_object(Bucket=bucket_name, Key=object_name, Body=data)
