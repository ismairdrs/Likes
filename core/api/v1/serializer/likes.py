from rest_framework.serializers import ModelSerializer

from core.models import Likes


class LikesSerializer(ModelSerializer):

    class Meta:
        model = Likes
        fields = ('id', )
