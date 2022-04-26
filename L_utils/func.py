import datetime

from tinydb import TinyDB, Query


def get_last_id():
    return len(TinyDB("user_data.json"))


def today_YYMMDD():
    return str(datetime.datetime.now().strftime("%Y%m%d"))


def now_time_stamp():
    return str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


def save_data(input_data):
    data = input_data.make_dic()

    db = TinyDB("user_data.json")
    db.insert(data)
