from datetime import datetime


def my_log(msg, *, dt=None):
    if dt is None:
        dt = datetime.now()
    print(f"[{dt:%Y-%m-%d %H:%M:%S}]: {msg}")
