The problem: 

Provide code that computes the rolling beta between two stocks, eg 
MSFT and SPY.  Your code should fetch daily price data from Yahoo 
Finance to use as inputs to the calculation.  It should compute a 
"rolling beta" between the two stocks, eg on any given day the beta 
should be computed over the trailing N-day period.  Things to think 
about: 

* when doing a rolling beta, there are more efficient ways of doing 
   this than brute force.  Eg, we can use intermediate computations 
   from the previous day's calculation to make today's more efficient 

* beta is an OLS statistic and so is sensitive to outliers.  You may 
   want to have some way of handling the outliers, eg by clipping or 
   winsoring 

* Your script should be flexible both on the "lookback" period, how 
   much history you want to include for any point, as well as the 
   aggregation period (daily, weekly, n-day, monthly betas). 

* Consider the intercept or no-intercept formulations.  Which is more 
   desirable for a beta calculation? 

* Extra points for making this modular and extensible.  Eg, we might 
   want to "plug in" our own clipping routine, or data source, or 
   aggregation routine (eg code that takes daily inputs and samples it 
   in different ways before feeding it to the estimator).  To the 
   extent that your code can be extensible with respect to these ideas, 
   it will be preferable. 

You should do this in python and associated libraries.