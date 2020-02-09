from celery import bootsteps
from kombu import Consumer, Queue, Exchange


class PrintMessageConsumer(bootsteps.ConsumerStep):

    def get_consumers(self, channel):
        return [Consumer(channel,
                         queues=[Queue('print_message_consumer_queue', Exchange('print_message_consumer_exchange'),
                                       'print_message_consumer_routing_key')],
                         callbacks=[self.handle_message],
                         accept=['json'])]

    def handle_message(self, body, message):
        print('Received message: {0!r}'.format(body))
        message.ack()
