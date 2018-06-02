from digi.xbee.devices import Raw802Device
from constants import PORT, BAUD_RATE
from sendDates import send_dates
from subscription import subscription
from threading import Thread
import time


# Run two functions as parallel threads
def run_in_parallel(*fns, args):
    thr = []
    for fn in fns:
        t = Thread(target=fn, args=args)
        t.start()
        print("oo")
        thr.append(t)


def start():
    try:
        # Create and open device on serial port
        device = Raw802Device(PORT, BAUD_RATE)
        device.open()
        # Execute
        run_in_parallel(subscription, send_dates, args=(device,))
    except:
        print('Failed. Retrying in 3secs')
        time.sleep(3)
        start()


if __name__ == '__main__':
    start()
