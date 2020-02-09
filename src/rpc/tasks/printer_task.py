from src.rpc.main import app


@app.task
def printer(string):
    print(string)
