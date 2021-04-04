import json

import pika
from django.core.management.base import BaseCommand, CommandError
from pika.spec import props

from rabbitmq import consumer


class Command(BaseCommand):
    help = "i need somebody help"

    def callback(self, channel, method, properties, body):
        print(f'mensagem recebida no serviço de Likes: {body}')
        response = "vamos fugir"
        self.channel.basic_publish(
                         exchange='',
                         routing_key=props.reply_to,
                         properties=pika.BasicProperties(correlation_id= \
                                                             props.correlation_id),
                         body=str(response)
        )
        self.channel.basic_ack(delivery_tag=method.delivery_tag)

    def _callback(self, channel, method, properties, body):
        payload = json.loads(body)
        nome = payload.get('nome')
        descricao = payload.get('descricao')
        if descricao is None:
            pass

    def handle(self, *args, **options):
        consumer.consume(
            exchange='default',
            queue_name='',
            routing_key='hello',
            callback=self.callback,
        )
