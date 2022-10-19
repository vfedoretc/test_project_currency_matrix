import sys
from functions import csv_list, all_curr, abc_curr, Graf_way_fast, filter_return

procent_profit = 1 # Profit percentage

argyment = sys.argv[1:] #Input parameters from console.
file_n = argyment[0]

matrix_list = csv_list(file_n) #converting the file into a matrix list
all_currency_list=all_curr(matrix_list) # all possible exchange rates from the matrix
coin_list=abc_curr(matrix_list) #list of currencies
fast_coin=Graf_way_fast(coin_list,all_currency_list, procent_profit) #profit support
profit_coin_str=filter_return(fast_coin) # translate to string
print(profit_coin_str)

