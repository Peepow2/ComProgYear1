""" Python Language
 # Task: Homework9 Decision Tree
 # Code: Peerawich Sodsuay 
 # Warning: Don't copy this code to submit.
 # If you do it, your score will be cancel immediately.
"""
import math

def calculate(x):
    if x == 0: return 0
    return x * math.log2(x) * (-1)
# ----------------------------------------------------

def SUBSET(D1, D2):
    for key in D1:
        if key not in D2:      return False
        if D1[key] != D2[key]: return False
    return True
# ----------------------------------------------------

def event_in_feature(S, feature):
    out = {}
    for event, tar in S:
        if event[feature] not in out:
            out[event[feature]] = 1
        else:
            out[event[feature]] += 1
    return out 
# ----------------------------------------------------

def count_target(S):
    target = {}
    for event, sub_tar in S:
        if sub_tar not in target:
            target[sub_tar] = 1
        else:
            target[sub_tar] += 1
    return target
# ----------------------------------------------------


# --------------------- Homework --------------------- #

def get_rows(S, conditions):
    if conditions == {}: return S
    out = []
    for event, target in S:
        if SUBSET(conditions, event):
            out += [[event, target]]
    return out
# ----------------------------------------------------

def Entropy(S, conditions):
    SUB_event = get_rows(S, conditions)
    Ns = len(SUB_event)
    target = count_target(SUB_event)
    Entro = 0
    for sub_tar in target:
        Entro += calculate(target[sub_tar]/Ns)
    return Entro
# ----------------------------------------------------

def Entropy_with_feature(S, conditions, feature_name):
    SUB_event = get_rows(S, conditions)
    all_event = event_in_feature(SUB_event, feature_name)
    Entro = 0
    for sub_event in all_event:
        Entro += (Entropy(SUB_event, {feature_name:sub_event}) * all_event[sub_event])
    return Entro/len(SUB_event)
# ----------------------------------------------------
# Problem: https://colab.research.google.com/drive/1E_3xSA2dkQptOJodzA4n1d1YOcu_69w3#scrollTo=JWVan-u1N58t
