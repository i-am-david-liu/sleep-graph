# Sleep tracker visualization

import datetime as dt
import numpy as np 
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib as mpl

if __name__ == "__main__":
    url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTrhKv6pqQhis7fmV-zITeOVQNjwRmPamJ3CJwdDCBQnqOAW4sLYjS1oVCyzKP5Re25DrSPByKHJvLN/pub?output=csv"

    df = pd.read_csv(url, usecols=['Date', 'Start', 'End'], parse_dates=['Date', 'Start', 'End']).dropna()

    fig, ax = plt.subplots()
    starts = mpl.dates.date2num(df['Start']) % 1
    ends = mpl.dates.date2num(df['End']) % 1
    ax.bar(df['Date'], ends - starts, bottom=(starts % 1))

    yformatter = mpl.dates.DateFormatter('%H:%M')
    ax.yaxis.set_major_formatter(yformatter)
    plt.yticks(np.linspace(-1/24, 13/24, 15)) 
    ax.figure.autofmt_xdate()
    
    plt.show()
    
