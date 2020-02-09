import json

from kombu import Connection, Exchange


def send_message(task_id, message):
    ex = Exchange('gen_primes_exchange', type='direct', durable=True)

    with Connection('amqp://guest:guest@localhost//') as conn:
        producer = conn.Producer(serializer='json')

        body = [[], message, {"chain": None, "chord": None, "errbacks": None, "callbacks": None}]

        headers = {
            'lang': 'py',
            'task': 'src.worker.tasks.gen_primes_task.gen_primes',
            'id': task_id,
            'root_id': task_id,
            'parent_id': None,
            'group': None
        }

        producer.publish(
            body=body,
            headers=headers,
            exchange=ex,
            routing_key='gen_primes_routing_key'
        )

        print("Published! Task ID: %s Payload %s" % (task_id, json.dumps(message)))


if __name__ == '__main__':
    send_message(1,
                 {
                     'value': 10000
                 })
