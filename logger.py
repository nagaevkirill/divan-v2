import ENV
import time

def write(message):
    with open(f'{ENV.DATA_PATH}\\error.log', 'a', encoding='UTF-8') as file:
        file.write(time.strftime("%y.%m.%d %H:%M:%S : ") + message + '\n')