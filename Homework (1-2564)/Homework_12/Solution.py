import numpy as np

def find_max_min_on_date(provinces, dates, data, date):
    SS = np.copy(data[::, int(np.argwhere(dates == date))])
    return {'max': (provinces[SS == np.max(SS)]).tolist(), 'min': (provinces[SS == np.min(SS)]).tolist()}

def find_max_min_in_province(provinces, dates, data, province):
    PP = data[int(np.argwhere(provinces == province))]
    return {'max': (dates[PP == np.max(PP)]).tolist(), 'min': (dates[PP == np.min(PP)]).tolist()}

def find_average_growth(provinces, data, n):
    DATA = np.copy(data[::, -n::])
    shift = np.copy(data[::, -n-1:-1:])
    Result = (DATA / shift) - 1
    MEAN = np.mean(Result, axis = 1) 
    return sorted([(MEAN[i], provinces[i]) for i in range(len(data))])

def normalize(data):
    return data / np.max(data, axis = 1).reshape(data.shape[0], 1)
