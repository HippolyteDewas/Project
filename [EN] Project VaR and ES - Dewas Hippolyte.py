import yfinance as yf
import numpy as np

def VAR_ES(name_file, starting_date, ending_date, alpha):
    # Get the data
    data = yf.download(name_file,starting_date,ending_date)
    
    # New column containing the daily yields
    data['Daily Yield'] = (data['Close'] - data['Open']) / data['Open']
    
    # sorting of yields (ascending)
    sorted_yield = data['Daily Yield'].sort_values()
    
    # Calculation of the number of data that we keep at alpha % 
    v_critical = int(data['Daily Yield'].count() * alpha / 100)
    
    # storing of values with conditions
    yield_alpha = sorted_yield[:v_critical][sorted_yield[:v_critical] < 0]
    
    # Calculation of Value at risk 'VaR'
    VaR = abs(max(yield_alpha))
    
    # Calculation of the expected shortfall
    ES = abs(np.mean(yield_alpha))
    
    print('Value at risk = ', VaR)
    print('Estimate Shortfall = ', ES)

#Example : AAPL, 2018-01-01, 2023-10-29

name_file = input("Name of the file containing data : ")
starting_date = input("Starting date (YYYY-MM-DD) : ")
ending_date = input("Ending date (YYYY-MM-DD) : ")
alpha = float(input("Alpha threshold in percentage (often 1 or 5) : "))

VAR_ES(name_file, starting_date, ending_date, alpha)