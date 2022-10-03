import numpy as np
import csv
from itertools import chain, permutations

def csv_list(file_name): #получение данных з файла
    csv_filename = file_name
    with open(csv_filename) as f:
        reader = csv.reader(f)
        lst = list(reader)
        matrix_list=np.array(lst)
    return matrix_list

def all_curr(matrix_list): #список всех курсов
    #формарование курса
    all_curr=[]
    for j in range(len(matrix_list[0])-1):
        for i in range(len(matrix_list)-1):
            Curr = [matrix_list[i+1, 0], matrix_list[0, j+1],  matrix_list[i+1, j+1]]
            #print(Curr)
            all_curr.append(Curr)
    #print(all_curr)
    return all_curr

def abc_curr (matrix_list): # перечень всех курсов
    #сприсок
    abc=list(matrix_list[0])
    abc.pop(0)
    #print(abc)
    return abc

def powerset(list_name): # генератор перечня
    s = list(list_name)
    return chain.from_iterable(permutations(s, r) for r in range(len(s)+1))

def Graf_way(abc_curr): #пути графов
    Graf_way=[]
    for x in powerset(abc_curr):
        if len(x)>1:
            xy=list(x)
            xy.append(xy[0])
            #print(xy)
            Graf_way.append(xy)
    #print(Graf_way)
    return Graf_way

def all_profit_coin_(Graf_way, all_curr): #все результати операцый
    #перебор цен
    all_profit_coin=[]
    profit_coin=[]
    for f in (Graf_way):
        #print(f)
        sym_con=1
        for d in range(len(f)-1):
            str1=f[d]
            str2=f[d+1]
            #print('конгверт' , str1 , str2)
            for a in all_curr:
                if a[0]==str1 and a[1]== str2:
                    #print(a[2])
                        sym_con*=float(a[2])
        #print(sym_con)
        profit_coin=[f,sym_con]
        all_profit_coin.append(profit_coin)
    return all_profit_coin

def filter_procent(list_profit,procent): #исключение з неправельним процентом
    list_filt_profit = []
    for lis in list_profit:
        if float(lis[1])>(1+(procent/100)):
            list_filt_profit.append(lis)
    return list_filt_profit

def filter_first_coin ( list_profit, abc_curr): #исключение по первой монетке
    list_filt_profit = []
    for lis in list_profit:
        if lis[0][0] == abc_curr[0]:
            list_filt_profit.append(lis)
    #print(list_filt_profit)
    return list_filt_profit

def filter_out_put_coin (list_profit): #исключение максемум профит по количкству операцый
    list_filt_profit = []
    min_len=0
    max_profit=0
    for lis in list_profit:
        if min_len==0:
            min_len=len(lis[0])
        if len(lis[0]) == min_len and max_profit < float(lis[1]):
            max_profit = float(lis[1])
            list_filt_profit=lis
            #print(lis)
    return list_filt_profit

def filter_return (list_profit): #формат вывода
    return ', '.join(list_profit[0])
