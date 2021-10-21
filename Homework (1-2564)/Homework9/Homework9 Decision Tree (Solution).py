""" Python Language
 # Task: Homework9 Decision Tree
 # Code: Peerawich Sodsuay 
 # Warning: Don't copy this code to submit.
 # If you do it, your score will be cancel immediately.
"""
import math

def calculate(x):
    if x == 0: return 0
    return x * math.log(x, 2) * (-1)
#---------------------------------------

def SUBSET(dict1, dict2):
    return dict2.items() <= dict1.items()
#---------------------------------------

def get_rows(S, conditions):
    if conditions == {}: return S
    rec = []
    for temp, target in S:
        if SUBSET(temp, conditions):
            rec += [[temp, target]]      
    return rec
#---------------------------------------

def Entropy(S, conditions):
    t = get_rows(S, conditions)
    N = len(t)
    result = []
    for tmp in t:
        if tmp[-1] not in result:
            result += [tmp[-1]]
            
    N_result = len(result); count = [0] * N_result
    for temp in t:
        for i in range(N_result):
            if temp[-1] == result[i]:
                count[i] += 1
                
    P = [k/N for k in count]
    SUM = 0
    for Pc in P:
        SUM += calculate(Pc)
    return SUM
#---------------------------------------

def Entropy_with_feature(S, conditions, feature_name):
    t = get_rows(S, conditions)
    N_t = len(t)
    result_feature = {}
    for tmp in t:
        key = tmp[0]
        if key[feature_name] not in result_feature:
            result_feature[key[feature_name]] = 1
        else:
            result_feature[key[feature_name]] += 1
    P = []
    for k in result_feature:
        P += [result_feature[k]/N_t]
    P_each = []
    temp = {k:conditions[k] for k in conditions}
    for tmp in result_feature:
        New_con = temp
        New_con[feature_name] = tmp
        P_each += [Entropy(S, New_con)]
    N_result = len(result_feature)
    SUM = 0
    for i in range(N_result):
        SUM += (P_each[i] * P[i])
    return SUM
#---------------------------------------
# Problem: https://colab.research.google.com/drive/1E_3xSA2dkQptOJodzA4n1d1YOcu_69w3#scrollTo=JWVan-u1N58t
