from django.conf.urls import url, include
from django.contrib import admin

from rest_framework import routers

from s3_api import views

router = routers.DefaultRouter()
router.register(r'account', views.AccountViewSet)
router.register(r'customer', views.CustomerViewSet)

urlpatterns = [
    url(r'^api/v1/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
]
