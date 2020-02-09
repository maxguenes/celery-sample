# Celery Sample

- Iniciando Celery Worker RPC

`python.exe -m celery -A src.rpc.main worker --loglevel=info --pool=eventlet`

- Iniciando Celery Worker Rabbit

`python.exe -m celery -A src.worker.main worker --loglevel=info --pool=eventlet`
