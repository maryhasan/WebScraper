import sys
import numpy as np
import calendar
import datetime

# Q3: Reads data from local files. Returns the mean and variance of the commodity price over the specified date range.
# Maryam Hasan, 01-19-2018


def getCommodityPrice(argv):
    if len(sys.argv) < 4:
        print ('please enter start date(yyyy-mm-dd), end date(yyyy-mm-dd) and Commodity type(gold or silver)')
        return

    date1=sys.argv[1]
    date2=sys.argv[2]
    commodity=sys.argv[3]

    #check the input date format
    try:
        datetime.datetime.strptime(date1, '%Y-%m-%d')
        datetime.datetime.strptime(date2, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Incorrect date format, should be YYYY-MM-DD")

    # convert date formats
    year1, month1, day1 = date1.split('-')
    month1 = calendar.month_abbr[int(month1)]
    date1 = month1 + ' ' + day1 + ', ' + year1
    #print date1
    year1, month1, day1 = date2.split('-')
    month1 = calendar.month_abbr[int(month1)]
    date2 = month1 + ' ' + day1 + ', ' + year1
    #print date2

    if commodity == 'gold':
        filename = "goldfile.csv"
    elif commodity == 'silver':
        filename = "silverfile.csv"
    else:
        raise ValueError ('Incorrect commodity type, should be gold or silver (case-sensitive)')


    goldfile = open(filename, "r")


    prices = dict()
    flag1 = False
    flag2 = False
    for line in goldfile.readlines():
        if date2 in line:
            flag2 = True    #we start counting

        if flag2 == True:
            if ':' in line:
                key, value = line.split(':', 1)
                prices[key] = float(value.replace(',', ''))

        if date1 in line:
            flag1=True   #we finish counting, and exit from the for loop
            if ':' in line:
                key, value = line.split(':', 1)
                prices[key] = float(value.replace(',', ''))
            break

    #check if the input dates are out of range!
    if flag1==False or flag2==False:
        raise ValueError("The input dates are out of range!")

    #print prices.keys()

    stmean = np.mean(prices.values())
    stvar = np.var(prices.values())

    print commodity, stmean, stvar
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
