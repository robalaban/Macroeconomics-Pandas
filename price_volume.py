# from matplotlib.backends.backend_pdf import PdfPages
# from matplotlib import pyplot as plt
import pandas

# Importing Initial data
# Years / GDPi / Real GDP
data = pandas.read_csv('price_data.csv')


def func(callback_func):
    intermlist = []

    for x in xrange(0, len(data)):
        intermlist.append(callback_func(x))

    return intermlist


def base_price():
    return func(lambda x: (data.BASEPRICESOLD[x] * data.BASEPRICEUNIT[x]))


def current_price():
    return func(lambda x: (data.CURRENTPRICESOLD[x] * data.CURRENTPRICE[x]))


def 
