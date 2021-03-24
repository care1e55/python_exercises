import time

def elapsed_generator(iterable):
    prev_time = 0
    for i in iterable:
        curtime = time.perf_counter()
        yield curtime - prev_time, i
        prev_time = time.perf_counter()

for i in elapsed_generator(range(10)):
    time.sleep(1)
    print(i)