""" Python Language
 # Task: Homework11 API
 # Code: Peerawich Sodsuay 
 # Warning: Don't copy this code to submit.
 # If you do it, your score will be cancel immediately.
"""
from datetime import datetime,timedelta # ไม่อนุญาตให้ import library อื่นนอกเหนือจากนี้แล้ว
import math 

def get_data(data, key):
    S = set()
    for tmp in data['dataseries']:
      timeshift = tmp["timepoint"]
      dt = datetime.strptime(data['init'], '%Y%m%d%H') + timedelta(hours = 7 + timeshift)
      S.add(tuple([dt, tmp[key]]))
    return S

def get_hourly_average_data(tuples):
    D = dict()
    for tmp in tuples:
        h = tmp[0].hour
        if h not in D:
            D[h] = list()
        D[h].append(int(tmp[1]))
    rec = dict()
    for key in D:
        rec[key] = sum(D[key]) / len(D[key])
    return rec

def get_daily_min_max(tuples):
    D = {}
    for tmp in tuples:
        d = tmp[0].date()
        value = str(tmp[1])
        if "%" in value:  value = value[:-1]
        if d not in D:
            D[d] = list()
        D[d].append(int(value))

    rec =dict()
    for key in D:
        mn = min(D[key])
        mx = max(D[key])
        rec[key] = (mn, mx)
    return rec

def normalize(tuples):
    all_value = []
    for tmp in tuples:
        value =  str(tmp[1])
        if "%" in value:  
           value = value[:-1]
        all_value.append(int(value))
    
    MEAN = sum(all_value) / len(all_value)
    sum_square = 0
    for V in all_value:
        sum_square += (V - MEAN) ** 2
    SD = math.sqrt(sum_square / (len(all_value)  - 1))
    S = set()
    for dt, v in tuples:
        x = str(v)
        if '%' in x:  
          x = str(x[:-1])
        x = int(x)
        z = (x - MEAN) / SD
        S.add((dt, z))
    return S

def convert(tuples):
    D = {}
    for dt, v  in tuples: D[dt] = v
    return D

def find_closest_weather(data, x):
    D = dict();
    for key in x:
        D[key] = convert(normalize(get_data(data, key)))
    dist = list(); weather = {};
    for tmp in data["dataseries"]:
        timeshift = tmp["timepoint"]
        dt = datetime.strptime(data['init'], '%Y%m%d%H') + timedelta(hours = 7 + timeshift)
        d = 0
        for k in D:
            d += (D[k][dt] - x[k]) ** 2
        dist.append([d, dt])
        weather[d] = tmp["weather"]
    mn = min(dist)[0]
    return weather[mn]
