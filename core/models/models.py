from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
import uuid


class Likes(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_usuario = models.UUIDField(max_length=150)
    id_pizza = models.CharField(max_length=100)
    id_pedido = models.CharField(max_length=100)
    nota = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    comentario = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.nota)
