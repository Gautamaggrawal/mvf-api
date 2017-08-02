import boto3
import pprint

from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        bucket = 'mvf-devtest-s3api'

        client = boto3.client('s3', region_name='eu-west-1')
        objs = client.list_objects(Bucket=bucket)
        
        for num, obj in enumerate(objs['Contents']):
            file_name = '{}-{}'.format(num + 1, obj['Key'])
            s3 = boto3.resource('s3')
            s3.Bucket(bucket).download_file(
                obj['Key'], file_name
            )
