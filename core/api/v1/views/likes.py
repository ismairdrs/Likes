import requests

from rest_framework import viewsets, mixins
from rest_framework.exceptions import ValidationError

from core.api.v1.serializer import LikesSerializer
from core.models import Likes


class LikesViewSet(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    queryset = Likes.objects.all()
    serializer_class = LikesSerializer
