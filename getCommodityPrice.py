import sys
import numpy as np
import calendar
import datetime


def getCommodityPrice(argv):
    if len(sys.argv) < 4:
        print ('please enter start date(yyyy-mm-dd), end date(yyyy-mm-dd) and Commodity type(gold or silver)')
        return

    start=sys.argv[1]
    end=sys.argv[2]
    commodity=sys.argv[3]

    #check the input date format
    try:
        datetime.datetime.strptime(start, '%Y-%m-%d')
        datetime.datetime.strptime(end, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Incorrect date format, should be YYYY-MM-DD")

    # convert date formats
    # start = '2018-01-14'
    # end = '2018-01-03'
    # commodity = 'gold'
    year1, month1, day1 = start.split('-')
    month1 = calendar.month_abbr[int(month1)]
    start = month1 + ' ' + day1 + ', ' + year1
    print start
    year1, month1, day1 = end.split('-')
    month1 = calendar.month_abbr[int(month1)]
    end = month1 + ' ' + day1 + ', ' + year1
    print end

    if commodity == 'gold':
        filename = "goldfile.csv"
    elif commodity == 'silver':
        filename = "silverfile.csv"
    else:
        raise ValueError ('Incorrect commodity type, should be gold or silver')


    goldfile = open(filename, "r")

    prices = dict()
    flag = False
    for line in goldfile.readlines():
        if start in line:
            flag = True
        if end in line:
            if ':' in line:
                key, value = line.split(':', 1)
                prices[key] = float(value.replace(',', ''))
            break
        if flag == True:
            if ':' in line:
                key, value = line.split(':', 1)
                prices[key] = float(value.replace(',', ''))

    #print prices.keys()

    stmean = np.mean(prices.values())
    stvar = np.var(prices.values())

    print stmean
    print stvar
    # myvars[name.strip()] = float(var)    #while argv:
    # if argv[0][0] == '-':  # Found a "-name value" pair.
    #    opts[argv[0]] = argv[1]  # Add key and value to the dictionary.
    # argv = argv[1:]  # Reduce the argument list by copying it starting from index 1.


if __name__ == '__main__':
    from sys import argv

    getCommodityPrice(argv)
#    #if '-i' in myargs:  # Example usage.
#        print(myargs['-i'])
#    print(myargs)
