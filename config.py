import datetime


device_list = ['idfa', 'oaid']


def get_tomarrow_str():
    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(days=1)
    return tomorrow.strftime('%Y%m%d')


def get_data_str():
    today = datetime.date.today()
    return today.strftime('%Y%m%d')


