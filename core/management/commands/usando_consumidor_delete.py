import json

from django.core.management.base import BaseCommand, CommandError

from core.consumer_class import consumer
from core.models import Ingrediente


class Command(BaseCommand):
    help = "i need somebody help"

    def _callback(self, channel, method, properties, body):
        payload = json.loads(body)
        id = payload.get('id')
        print(id)
        if payload is not None:
            ingrediente = Ingrediente.objects.filter(id=id)
            ingrediente.delete()
            print(f'O Ingrediente foi deletado!!!')
        else:
            print('falhou')
            pass

    def handle(self, *args, **options):
        consumer.consume(
            exchange='ingredientes',
            queue_name='ingredientes-delete',
            routing_key='ingrediente.delete',
            callback=self._callback,
        )
