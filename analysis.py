from matplotlib.backends.backend_pdf import PdfPages
from matplotlib import pyplot as plt
import pandas

# Importing Initial data
# Years / GDPi / Real GDP
data = pandas.read_csv('data.csv')

# Function to calculate nominal GDP

def func(append, callback_func):
    intermList = []

    intermList.append(append)
    for x in xrange(1, len(data)):
        intermList.append(callback_func(x))

    return intermList



def nominal_gdp():
    return func(100, lambda x: (data.GDPI[x] / data.GDPI[0]))

# The relation between Nominal and Real GDP

def gdp_deflator(): 
    return func(100, lambda x: (data.NOMINALGDP[x] / data.REALGDP[x])*100)


# The relation between Current and Previous GDPi

def rel_gdpi():
    intermList = []

    intermList.append((1))
    for x in xrange(1, len(data)):
        intermList.append((data.GDPI[x] / data.GDPI[x-1]))

    return intermList

# The relation between Current and Previous Real GDP

def rel_realgdp():
    intermList = []

    intermList.append((1))
    for x in xrange(1, len(data)):
        intermList.append((data.REALGDP[x] / data.REALGDP[x-1]))

    return intermList

# GDP Deflator related to previous year

def gdp_deflatorprev():
    intermList = []

    intermList.append((1))
    for x in xrange(1, len(data)):
        intermList.append((data.RELATIONGDPI[x] / data.RELATIONREALGDP[x]))

    return intermList

# Inflation Rate related to specific year

def inflation_ratabase():
    intermList = []

    intermList.append((100))
    for x in xrange(1, len(data)):
        intermList.append((data.GDPDEFLATOR[x] - 1))

    return intermList


# Inflation rate related to previous year

def inflation_rataprev():
    intermList = []

    intermList.append((100))
    for x in xrange(1, len(data)):
        intermList.append((data.GDPDEFLATORPREV[x] - 1))

    return intermList

# Real gdp related to base year

def realgdp_base():
    intermList = []

    intermList.append((100))
    for x in xrange(1, len(data)):
        intermList.append((data.GDPI[x] / data.GDPDEFLATOR[x]))

    return intermList

# Real gdp relate to previous year

def realgdp_prev():
    intermList = []

    intermList.append((100))
    for x in xrange(1, len(data)):
        intermList.append((data.GDPI[x] / data.GDPDEFLATORPREV[x]))

    return intermList


data['NOMINALGDP'] = nominal_gdp()
data['GDPDEFLATOR'] = gdp_deflator()
data['RELATIONGDPI'] = rel_gdpi()
data['RELATIONREALGDP'] = rel_realgdp()
data['GDPDEFLATORPREV'] = gdp_deflatorprev()
data['INFLATIONRATEBASE'] = inflation_ratabase()
data['INFLATIONRATEPREV'] = inflation_rataprev()
data['REALGDPBASE'] = realgdp_base()
data['REALGDPPREV'] = realgdp_prev()

# Saving to data-complete.csv

data.to_csv('data-complete.csv', sep=',', encoding='utf-8')

# Plotting GDP / YEAR

def plt_relation(X, Y):
    plt.scatter(X, Y)
    plt.plot(X, Y)
    plt.show()

plt_relation(data.YEARS, data.RELATIONGDPI)