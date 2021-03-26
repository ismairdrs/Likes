from django.db import models
import uuid


class Likes(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_auth = models.CharField(max_length=32)
    id_pizza = models.CharField(max_length=32)
    nota = models.DecimalField(max_digits=2, decimal_places=1)
    comentario = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.nota)
