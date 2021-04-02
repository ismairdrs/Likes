from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
import uuid


class Likes(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_usuario = models.CharField(max_length=150)
    id_pizza = models.CharField(max_length=100)
    id_pedido = models.CharField(max_length=100)
    nota = models.DecimalField(max_digits=2, decimal_places=1, validators=[MaxValueValidator(5), MinValueValidator(0)])
    comentario = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.nota)
