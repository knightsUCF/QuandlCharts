import quandl
import pandas
from bokeh.plotting import figure, output_file, show

 

# api keys

key = 'BEdW-t77Q_spZy1eoERz'
version = '2015-04-09'

 

# connect to quandl

quandl.ApiConfig.api_key = key
quandl.ApiConfig.api_version = version

 

# data settings

symbol = 'EOD/HD'
bars = 800
timeframe = 'daily'
feature = 'Close'

 
# pull Pandas dataframe from Quandl - symbols: https://www.quandl.com/search?query=

df = quandl.get(symbol, collapse = timeframe)
df = df.tail(bars)

 

# create a close price feature in the dataframe

price = df[feature]

 

# add a moving average

df['ema'] = price.ewm(span=90,adjust=False).mean()
ema = df['ema']

 

# graphing

def graph(df, df2):
    output_file('line.html')
    p = figure(plot_width = 1000, plot_height = 1000, background_fill_color = 'black')
    p.xgrid.visible = False
    p.ygrid.visible = False
    p.line(df.index, df, line_width = 2, line_color = 'blue')
    p.line(df.index, df2, line_width = 2, line_color = '#CC3399')
    show(p)

 

graph(price, ema)

