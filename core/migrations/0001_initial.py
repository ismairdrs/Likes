# Generated by Django 3.1.7 on 2021-04-04 06:12

import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('id_usuario', models.CharField(max_length=150)),
                ('id_pizza', models.CharField(max_length=100)),
                ('id_pedido', models.CharField(max_length=100)),
                ('nota', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('comentario', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
