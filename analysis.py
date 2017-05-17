import pandas

# Importing Initial data
# Years / GDPi / Real GDP
data = pandas.read_csv('data.csv')

# Function to calculate nominal GDP

def nominal_gdp():
    intermList = []

    intermList.append((100))
    for x in xrange(1, len(data)):
        intermList.append((data.GDPI[x] / data.GDPI[0]))

    return intermList

# The relation between Nominal and Real GDP

def gdp_deflator(): 
    intermList = []

    intermList.append((100))
    for x in xrange(1, len(data)):
        intermList.append((data.NOMINALGDP[x] / data.REALGDP[x])*100)

    return intermList


# The relation between Current and Previous GDPi

def rel_gdpi():
    intermList = []

    intermList.append((100))
    for x in xrange(1, len(data)):
        intermList.append((data.GDPI[x] / data.GDPI[x-1]))

    return intermList

# The relation between Current and Previous Real GDP

def rel_realgdp():
    intermList = []

    intermList.append((100))
    for x in xrange(1, len(data)):
        intermList.append((data.REALGDP[x] / data.REALGDP[x-1]))

    return intermList



data['NOMINALGDP'] = nominal_gdp()
data['GDPDEFLATOR'] = gdp_deflator()
data['RELATIONGDPI'] = rel_gdpi()
data['RELATIONREALGDP'] = rel_realgdp()



print(data)