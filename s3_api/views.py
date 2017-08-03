from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import detail_route

from s3_api.serializers import AccountSerializer, CustomerSerializer
from s3_api.models import Account, Customer


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def account_field(self, request, guid, field):
        account = Account.objects.get(id=guid)
        serializer = AccountSerializer(account)
        return Response(serializer.data.get(
            field, 'Not a valid field name.'
        ))


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def customer_accounts(self, request, guid):
        """ Return only accounts associated with the given customer
            guid (treated as guid)
        """
        accounts = Account.objects.filter(customer__id=guid)
        serializer = AccountSerializer(accounts, many=True)
        return Response(serializer.data)
