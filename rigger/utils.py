from datetime import datetime
import time


def timestamp():
    d_time = datetime.now()
    un_time = time.mktime(d_time.timetuple())
    return un_time  # 1509636609.0 float

