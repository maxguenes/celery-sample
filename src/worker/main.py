from celery import Celery, bootsteps
from kombu import Queue, Exchange

from src.worker.config import Config
from src.worker.consumer import PrintMessageConsumer


class DeclareDLXnDLQ(bootsteps.StartStopStep):
    requires = {'celery.worker.components:Pool'}

    def start(self, worker):
        dead_letter_queue = Queue(
            'gen_primes_queue_dl_queue',
            Exchange(
                'gen_primes_queue_dl_exchange',
                type='direct'),
            routing_key='gen_primes_queue_dl_routing_key')

        with worker.app.pool.acquire() as conn:
            dead_letter_queue.bind(conn).declare()


app = Celery(__name__)
app.config_from_object(Config)

app.steps['worker'].add(DeclareDLXnDLQ)
app.steps['consumer'].add(PrintMessageConsumer)
