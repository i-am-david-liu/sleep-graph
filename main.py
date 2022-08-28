# Sleep tracker visualization

import sys
import numpy as np 
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import dates

# TODO:
# - running average as line
#   - or a weekly average
# - view monthly, weekly ranges
# - specify url as CL argument

_2021 = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTrhKv6pqQhis7fmV-zITeOVQNjwRmPamJ3CJwdDCBQnqOAW4sLYjS1oVCyzKP5Re25DrSPByKHJvLN/pub?gid=0&single=true&output=csv"
_2022 = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTrhKv6pqQhis7fmV-zITeOVQNjwRmPamJ3CJwdDCBQnqOAW4sLYjS1oVCyzKP5Re25DrSPByKHJvLN/pub?gid=1627947168&single=true&output=csv"
#url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTrhKv6pqQhis7fmV-zITeOVQNjwRmPamJ3CJwdDCBQnqOAW4sLYjS1oVCyzKP5Re25DrSPByKHJvLN/pub?output=csv"

if __name__ == "__main__":

    url = "" 
    title = ""
    if len(sys.argv) == 2:
        token = sys.argv[1]
        if token == "2021" or token == "21":
            url = _2021
            title = "2021"
        elif token == "2022" or token == "22":
            url = _2022
            title = "2022"
        else:
            print("Not a valid database. Available databases: '20[21]', '20[22]'")
            exit()
    else:
        print("Format: python3 main.py <database>") 
        exit()

    df = pd.read_csv(
            url,
            usecols=['Date', 'Start', 'End'],
            parse_dates=['Date', 'Start', 'End'],
    ).dropna()

    plt.rc('font', size=20)

    fig, ax = plt.subplots()
    starts = dates.date2num(df['Start']) % 1
    ends = dates.date2num(df['End']) % 1

    # if start time occured before midnight, change value to occur the day before 
    for i, start in enumerate(starts):
        if start > 21/24:
            starts[i] -= 1

    ax.bar(df['Date'], ends - starts, bottom=starts)

    yformatter = dates.DateFormatter('%H:%M')
    ax.yaxis.set_major_formatter(yformatter)

    # set ticks dynamically here? will need to round to nearest hour, not so intuitive
    tick_start = -2/24
    tick_end = 13/24
    tick_span = round((tick_end-tick_start)*24)+1
    plt.yticks( np.linspace(tick_start, tick_end, tick_span) )
    ax.figure.autofmt_xdate()
    
    plt.title(f"Sleep graph ({title})")
    plt.show()
    
