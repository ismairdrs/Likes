from django.contrib import admin
from .models import Likes


@admin.register(Likes)
class LikesAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_auth', 'id_pizza', 'nota', 'comentario')
