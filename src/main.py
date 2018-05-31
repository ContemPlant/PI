from digi.xbee.devices import Raw802Device
from constants import PORT, BAUD_RATE
from sendDates import send_dates
from subscription import subscribtion
from threading import Thread
import time

def runInParallel(*fns, args):
    thr = []
    for fn in fns:
        t = Thread(target=fn, args=args)
        t.start()
        print("oo")
        thr.append(t)


def start():
    try:
        device = Raw802Device(PORT, BAUD_RATE)
        device.open()

        runInParallel(subscribtion, send_dates, args=(device,))
    except:
        print('Failed. Retrying in 3secs')
        time.sleep(3)
        start()


if __name__ == '__main__':
    start()
