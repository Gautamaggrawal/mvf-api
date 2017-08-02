from django.contrib import admin

from s3_api.models import Account, Customer


admin.site.register(Account)
admin.site.register(Customer)
