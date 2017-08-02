import boto3
import pprint
import json

from django.core.management.base import BaseCommand

from s3_api.models import Account, Customer


class Command(BaseCommand):

    def handle(self, *args, **options):
        bucket = 'mvf-devtest-s3api'

        client = boto3.client('s3', region_name='eu-west-1')
        objs = client.list_objects(Bucket=bucket)
        
        # Download each JSON file
        for num, obj in enumerate(objs['Contents']):
            file_name = '{}-{}'.format(num + 1, obj['Key'])
            s3 = boto3.resource('s3')
            s3.Bucket(bucket).download_file(
                obj['Key'], file_name
            )

            self.import_data(file_name)

    def import_data(self, file_name):
        """ Import a given locally stored file in to the Account model """

        with open(file_name) as account_info:
            accounts = json.load(account_info)['accounts']

            guid = file_name.split('.')[0][2:]
            customer = Customer.objects.create(
                    id=guid,
            )

            for account in accounts:
                # We don't want commas in the balance
                balance = str(account['balance']).replace(',', '')

                # Could look in to bulk_create later to improve efficiency
                Account.objects.create(
                    id=account['id'],
                    customer=customer,
                    firstname=account['firstname'],
                    lastname=account['lastname'],
                    email=account['email'],
                    telephone=account['telephone'],
                    balance=float(balance),
                )
