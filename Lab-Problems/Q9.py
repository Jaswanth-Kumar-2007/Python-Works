import time

class StopWatch:
    def __init__(self):
        pass

    def start(self):
        self.start_time = time.time()

    def stop(self):
        self.stop_time = time.time()

    def getElapsedTime(self):
        return f"{(self.stop_time - self.start_time)}"

p = StopWatch()
p.start()
time.sleep(0.05)
p.stop()
print(p.getElapsedTime())

