# The problem: 
# 
# Provide code that computes the rolling beta between two stocks, eg 
# MSFT and SPY.  Your code should fetch daily price data from Yahoo 
# Finance to use as inputs to the calculation.  It should compute a 
# "rolling beta" between the two stocks, eg on any given day the beta 
# should be computed over the trailing N-day period.  Things to think 
# about: 
# 
# * when doing a rolling beta, there are more efficient ways of doing 
#    this than brute force.  Eg, we can use intermediate computations 
#    from the previous day's calculation to make today's more efficient 
# 
# * beta is an OLS statistic and so is sensitive to outliers.  You may 
#    want to have some way of handling the outliers, eg by clipping or 
#    winsoring 
# 
# * Your script should be flexible both on the "lookback" period, how 
#    much history you want to include for any point, as well as the 
#    aggregation period (daily, weekly, n-day, monthly betas). 
# 
# * Consider the intercept or no-intercept formulations.  Which is more 
#    desirable for a beta calculation? 
# 
# * Extra points for making this modular and extensible.  Eg, we might 
#    want to "plug in" our own clipping routine, or data source, or 
#    aggregation routine (eg code that takes daily inputs and samples it 
#    in different ways before feeding it to the estimator).  To the 
#    extent that your code can be extensible with respect to these ideas, 
#    it will be preferable. 

import pandas as pd 
import numpy as np
from pandas.io.data import DataReader
from datetime import datetime


# datatime have the format datetime(2000,1,1)

class stock_ts_data:
    name = None
    price_data = None
    datetime = None
    
    def __init__(self,stock_name):
        self.name  = stock_name
    def fetch_ts_data(self,start,end):
        self.price_data = DataReader(self.name,  "yahoo", start, end)
        self.datetime = self.price_data.index
        
class beta_calculator:
    beta = None
    period = None
    stock1 = None
    stock2 = None
    datetime = None
    
    
    def __init__(self):
        
    def __call__(self,N,stock1_ts,stock2_ts):
        
        
    
