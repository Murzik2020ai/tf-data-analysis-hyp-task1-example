import pandas as pd
import numpy as np


chat_id = 1226526788

from scipy import stats
from statsmodels.stats.proportion import proportions_ztest


def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 0.03
    stats, p_value = proportions_ztest(np.array([x_success, y_success]), np.array([x_cnt, y_cnt]), alternative = 'smaller')
    #print('{:.12f}'.format(1 - p_value))
    return True if p_value < alpha else False
