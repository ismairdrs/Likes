from django.conf.urls import url, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('', views.LikesViewSet, basename='likes')

urlpatterns = [
    url('', include(router.urls)),

]
