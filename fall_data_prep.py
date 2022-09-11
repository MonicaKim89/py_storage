import os
import pandas as pd
import numpy as np
import sys
import openpyxl

from datetime import datetime
import datetime
from datetime import timedelta

from tqdm import tqdm



def str_to_dt(x):
    x = str(x)
    y = x[0:4]
    m = x[4:6]
    d = x[6:8]
    format_ = '%Y-%m-%d'
    date = y+'-'+m+'-'+d
    dates = datetime.datetime.strptime(date, format_)
    return dates

def none_zero(x):
    i = str(x)
    if i[:3]=='0000':
        i = i.replace('0000','')
        i = int(x)
    elif i[:2]=='00':
        i = i.replace('00','')
        i = int(x)
    
    return i
     
def none_zero_2(x):
    i = str(x)
    if i[:4] =='0000':
        k = i[4:]
        k = int(k)
    elif i[:3] =='000':
        k = i[3:]
        k = int(k)
    elif i[:2] == '00':
        k = i[2:]
        k = int(k)
    elif i[0]=='0':
        k = i[1:]
        k = int(k)
    else:
        k = int(i)
    return k
 

format_ = '%Y-%m-%d'

def str_to_dt_v2(x):
    i = str(x).split(' ')[0]
    i = datetime.datetime.strptime(i, format_)

    return i
    
def str_to_dt_point(x):
    x = str(x).split('.')[0]
    y = x[0:4]
    m = x[4:6]
    d = x[6:8]
    format_ = '%Y-%m-%d'
    date = y+'-'+m+'-'+d
    dates = datetime.datetime.strptime(date, format_)
    return dates

def leave_or_del(df_name):
    leave_or =[]
    # x = df_name['평가일자'].tolist()
    for num, i in enumerate (df_name['평가일자'].tolist()):
        
        fall_date = df_name['낙상발생일시'].tolist()[num]
        less_date = df_name['평가기준일'].tolist()[num]
        eval_date = df_name['평가일자'].tolist()[num]
        
        if less_date <= eval_date <= fall_date:
            leave_or.append('살려')
        else:
            leave_or.append('삭제')

    df_name['유무'] = leave_or
    df_name = df_name[df_name['유무']=='살려']
    print(df_name.shape)
    print(len(df_name['등록번호'].unique()))
    
    return df_name

def weight_height(x):
    try:
        x =str(x)
        x = x[:-2]
        x = float(x)
    except:
        x = 999
    return x


def float_to_int(x):
    try:
        x = str(x)
        x = x.split('.')[0]
        x =int(x)
    except:
        x = x
    
    return x
