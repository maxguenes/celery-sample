from celery import Celery

app = Celery(__name__,
             broker='amqp://guest:guest@localhost//',
             backend='rpc://',
             include=['src.rpc.tasks'])
