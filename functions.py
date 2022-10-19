import numpy as np
import csv
from itertools import chain, permutations

def csv_list(file_name):
    """getting data from a file.
    """
    csv_filename = file_name
    with open(csv_filename) as f:
        reader = csv.reader(f)
        lst = list(reader)
        matrix_list=np.array(lst)
    return matrix_list

def all_curr(matrix_list):
    """ list of all courses.
    """
    all_curr=[]
    for j in range(len(matrix_list[0])-1):
        for i in range(len(matrix_list)-1):
            Curr = [matrix_list[i+1, 0], matrix_list[0, j+1],  matrix_list[i+1, j+1]]
            all_curr.append(Curr)
    return all_curr

def abc_curr (matrix_list):
    """ list of all CURRENCIES.
    """
    abc=list(matrix_list[0])
    abc.pop(0)
    return abc

def powerset(list_name):
    """list generator
    """
    s = list(list_name)
    return chain.from_iterable(permutations(s, r) for r in range(len(s)+1))

def Graf_way_all(abc_curr):
    """all graph paths
    """
    Graf_way=[]
    for x in powerset(abc_curr):
        if len(x)>1:
            xy=list(x)
            xy.append(xy[0])
            Graf_way.append(xy)
    return Graf_way


def Graf_way_fast(abc_curr, all_curr, procent):  # пути графов
    """
    ways of graphs short way of profit.

    :param abc_curr: list of all CURRENCIES
    :param all_curr: list of all courses
    :param procent: choice of profit percentage
    :return: [['CUUR_1', 'CUUR_2', 'CUUR_3'....], <*.***>]

    """
    list_filt_profit = []
    min_len = 0
    max_profit = 0
    for x in powerset(abc_curr):
        if len(x) > 1:
            xy = list(x)
            xy.append(xy[0])
            sym_con = 1
            for d in range(len(xy) - 1):
                str1 = xy[d]
                str2 = xy[d + 1]
                for a in all_curr:
                    if a[0] == str1 and a[1] == str2:
                        sym_con *= float(a[2])
            profit_coin = [xy, sym_con]

            if float(profit_coin[1]) > (1 + (procent / 100)):
                if min_len == 0:
                    min_len = len(profit_coin[0])
                if len(profit_coin[0]) == min_len and max_profit < float(profit_coin[1]):
                    max_profit = float(profit_coin[1])
                    list_filt_profit = profit_coin
                if len(profit_coin[0])>min_len:
                    return list_filt_profit


def all_profit_coin_(Graf_way, all_curr):
    """all operational results
    """
    all_profit_coin=[]
    profit_coin=[]
    for f in (Graf_way):
        sym_con=1
        for d in range(len(f)-1):
            str1=f[d]
            str2=f[d+1]

            for a in all_curr:
                if a[0]==str1 and a[1]== str2:
                        sym_con*=float(a[2])
        profit_coin=[f,sym_con]
        all_profit_coin.append(profit_coin)
    return all_profit_coin

def filter_procent(list_profit,procent):
    """all operational results
    """
    list_filt_profit = []
    for lis in list_profit:
        if float(lis[1])>(1+(procent/100)):
            list_filt_profit.append(lis)
    if len(list_filt_profit)<1:
        return None
    return list_filt_profit

def filter_first_coin ( list_profit, abc_curr):
    """first coin exception
    """
    list_filt_profit = []
    if list_profit == None:
        return None
    for lis in list_profit:
        if lis[0][0] == abc_curr[0]:
            list_filt_profit.append(lis)
    return list_filt_profit

def filter_out_put_coin (list_profit):
    """exclusion maximum profit by the number of operations
    """
    if list_profit == None:
        return None
    list_filt_profit = []
    min_len=0
    max_profit=0
    for lis in list_profit:
        if min_len==0:
            min_len=len(lis[0])
        if len(lis[0]) == min_len and max_profit < float(lis[1]):
            max_profit = float(lis[1])
            list_filt_profit=lis
    return list_filt_profit

def filter_return (list_profit):
    """output format
    """
    if list_profit == None:
        return "No risk-free opportunities exist yielding over 1.00% profit"
    return ', '.join(list_profit[0])
