import pandas as pd
import datetime
import sys

def get_current_time():
    return datetime.datetime.now()


def get_days_diff(user_date):
    now=get_current_time()
    diff=now-user_date
    return diff



# user_date=sys.argv[1]
# user_date=datetime.datetime.strptime(user_date,'%Y/%m/%d')
# print(get_days_diff(user_date))


if __name__=="__main__":
    user_date=sys.argv[1]
    user_date=datetime.datetime.strptime(user_date,'%Y/%m/%d')
    print(get_days_diff(user_date))