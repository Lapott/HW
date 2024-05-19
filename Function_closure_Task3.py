import time
def timer():
    timelong = time.perf_counter()
    def inner():
        nonlocal timelong
        timefromlastcall = (time.perf_counter() - timelong)
        timelong = time.perf_counter()
        return timefromlastcall
    return inner
t = timer()
