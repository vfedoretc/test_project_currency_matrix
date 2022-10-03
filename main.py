
import sys
from functions import *
procent_profit = 5 # процент профита

argyment = sys.argv[1:] #ввод с консоли
file_n = argyment[0]

matrix_list = csv_list(file_n) #перевод файла в лист матрицы
all_currency_list=all_curr(matrix_list) # все возможные курсы валют з матрицы
coin_list=abc_curr(matrix_list) #список валют
graf_list=Graf_way(coin_list) #постройка всех графов
all_profit_list=all_profit_coin_(graf_list,all_currency_list) # результат всех операций з валютой
pofit_prosent_list=filter_procent(all_profit_list,procent_profit) #фильтрацыя по проценту
chois_firct_coin_list=filter_first_coin(pofit_prosent_list,coin_list) #фильтрацыя по первой монетке
profit_coin=filter_out_put_coin(chois_firct_coin_list) # выбор кратчайшей операции и  большого профита
profit_coin_str=filter_return(profit_coin) # перевод в строку
print(profit_coin_str)

