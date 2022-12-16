# import io
# import random
from main import app
from flask import render_template, url_for, request, Response
import pandas as pd
from pandas import Series
import matplotlib.pyplot as plt
# from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
# from matplotlib.figure import Figure

#### LOGIC FOR PLOTTING ####
tickers = [
            'JPM',
            'BAC',
            'C',
            'WFC',
            'GS',
            ]

#Create an empty string called `ticker_string` that we'll add tickers and commas to
ticker_string = ''

#Loop through every element of `tickers` and add them and a comma to ticker_string
for ticker in tickers:
    ticker_string += ticker
    ticker_string += ','
    
#Drop the last comma from `ticker_string`
ticker_string = ticker_string[:-1]

endpoints = 'chart'
years = '10'
HTTP_request = f'https://cloud.iexapis.com/stable/stock/market/batch?symbols={ticker_string}&types={endpoints}&range={years}y&token=sk_a3ddd89fc3684b0ea6fa7b6502aa204f'


data = pd.read_json(HTTP_request)

# print(data['JPM'] ['chart'])

for ticker in tickers:
    Series.to_dict({ticker : pd.DataFrame(data[ticker]['chart'])['close']})

series_list = []

for ticker in tickers:
    series_list.append(pd.DataFrame(data[ticker]['chart'])['close'])

series_list.append(pd.DataFrame(data['JPM']['chart'])['date'])

column_names = tickers.copy()
column_names.append('Date')

data = pd.concat(series_list, axis=1)
data.columns = column_names

data.set_index('Date', inplace = True)


###END LOGIC###


###CHART###
plt.plot()

plt.figure(figsize = (18,12))
plt.boxplot(data.transpose())

plt.title('Boxplot of Stock Prices (5Y Lookback)', fontsize = 20)
plt.xlabel('Bank', fontsize=20)
plt.ylabel('Stock Prices', fontsize = 20)

ticks = range(1, len(data.columns)+1)
labels = list(data.columns)
plt.xticks(ticks, labels, fontsize=20)

ddata = plt.savefig('main/static/images/data.png')
plt.close(ddata)


### END CHART ###


#### APP ROUTES #####
@app.route("/")
def main():
    return render_template('main.html')


@app.route("/display")
def plot():
    return render_template('display.html', name = 'data', url='main/static/images/data.png')

# def image(x):
#     x = datad
#     return (x)