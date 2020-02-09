import time
from src.rpc.main import app


@app.task
def reverse(string):
    time.sleep(5)
    return string[::-1]
