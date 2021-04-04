from django.conf.urls import url, include
from .v1 import urls

urlpatterns = [
    url('', include(urls)),
]
