from celery.exceptions import Reject
from src.worker.main import app


@app.task(bind=True, acks_late=True)
def gen_primes(self, **kwargs):
    x = kwargs['value']

    if x <= 0:
        raise Reject('Value must be greater than zero', requeue=False)

    multiples = []
    results = []
    for i in range(2, x + 1):
        if i not in multiples:
            results.append(i)
            for j in range(i * i, x + 1, i):
                multiples.append(j)

    return results
