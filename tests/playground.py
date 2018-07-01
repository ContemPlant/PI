from src.xbeeNetwork.sendDates import send_dates


def main():

    dates = (1, 1, 1,1, 13, 10, 19, 80)
    result = send_dates(dates)
    print(result)


main()
