import time
from src.rpc.tasks.reverse_task import reverse

if __name__ == '__main__':
    result = reverse.delay('Max Guenes')

    while not result.ready():
        print("Aguarde....")
        time.sleep(10)

    print('Task result: ', result.result)
