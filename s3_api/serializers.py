from rest_framework import serializers

from s3_api.models import Account, Customer


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = (
            'id', 'firstname', 'lastname', 'email', 'telephone', 'balance'
        )


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = 'id',
