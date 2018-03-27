from datetime import datetime


def str_to_datetime(timestring):
    time_dt = datetime.strptime(timestring, '%Y-%m-%dT%H:%M:%S+03:00')
    return time_dt


def datetime_to_str(time_dt):
    pass
