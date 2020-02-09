from kombu import Queue, Exchange


class Config(object):
    broker_url = 'amqp://guest:guest@localhost//'
    task_serializer = 'json'
    accept_content = ['json']
    task_acks_late = True
    worker_concurrency = 1
    task_ignore_result = True
    worker_prefetch_multiplier = 1
    worker_disable_rate_limits = True

    imports = (
        'src.worker.tasks'
    )
    task_queues = [
        Queue(
            'gen_primes_queue',
            exchange=Exchange('gen_primes_exchange', type='direct', durable=True),
            routing_key='gen_primes_routing_key',
            durable=True,
            queue_arguments={
                'x-dead-letter-exchange': 'gen_primes_queue_dl_exchange',
                'x-dead-letter-routing-key': 'gen_primes_queue_dl_routing_key'
            }
        )
    ]

    task_routes = dict(
        {
            'src.worker.tasks.gen_primes': {
                'queue': 'gen_primes_queue',
                'routing_key': 'gen_primes_routing_key'
            }
        }
    )
