import numpy as np

def calculate(data):


    if len(data) != 9:
        raise ValueError("List must contain nine numbers.")
    
    a = np.reshape(data,(3,3))

    result_dict = {
        "mean" : [np.mean(a, axis=0), np.mean(a, axis=1), np.mean(a)],
        "variance" : [np.var(a, axis=0), np.var(a, axis=1), np.var(a)],
        "standard deviation" : [np.std(a, axis=0), np.std(a, axis=1), np.std(a)],
        'max': [np.max(a, axis=0), np.max(a, axis=1), np.max(a)],
        'min': [np.min(a, axis=0), np.min(a, axis=1), np.min(a)],
        'sum': [np.sum(a, axis=0), np.sum(a, axis=1), np.sum(a)]
    }

    for key in result_dict:
        result_dict[key] = [
            val.tolist() if isinstance(val, np.ndarray) else val
            for val in result_dict[key]
        ]
    
    return result_dict