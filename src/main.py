import time
from threading import Thread
from digi.xbee.devices import Raw802Device
import os

from constants import PORT, BAUD_RATE
from xbeeNetwork.sendDates import handle_messages
from backendConnect.subscription import subscription


# Run two functions as parallel threads
def run_in_parallel(*fns, args):
    thr = []
    for fn in fns:
        t = Thread(target=catcher(fn), args=args)
        t.start()
        print("oo")
        thr.append(t)


def catcher(fn):
    def f(args):
        try:
            fn(args)
        except Exception as e:
            print(e)
            os._exit(1)
    return f


def start():
    try:
        # Create and open device on serial port
        device = Raw802Device(PORT, BAUD_RATE)
        device.open()
        # Execute
        run_in_parallel(subscription, handle_messages, args=(device,))

    except Exception as e:
        print('Failed. Retrying in 3secs:', e)

        time.sleep(3)
        start()


if __name__ == '__main__':
    start()
