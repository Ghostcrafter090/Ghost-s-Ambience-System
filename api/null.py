import time

class status:
    apiKey = ""
    vars = {
        "lastLoop": []
    }

def hello():
    time.sleep(5)
    return 0

def run():
    while True:
        hello()