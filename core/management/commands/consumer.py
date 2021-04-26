import json

from django.core.management.base import BaseCommand

from core.models import Likes
from core.rabbitmq import consumer


class Command(BaseCommand):
    help = "i need somebody help"

    def callback(self, channel, method, properties, body):
        print(f'mensagem recebida no serviço de Likes: {body}')
        payload = json.loads(body)

        try:
            like = Likes.objects.create(
               id_usuario=payload.get('id_usuario'),
                id_pizza=payload.get('id_pizza'),
                id_pedido=payload.get('id_pedido'),
                nota=payload.get('nota'),
                comentario=payload.get('comentario')
            )
        except:
            print(f'UUIDField enviado inválido, avaliação foi descartada!')

    def handle(self, *args, **options):
        consumer.consume(
            exchange='likes',
            queue_name='default',
            routing_key='likes.create',
            callback=self.callback,
        )
