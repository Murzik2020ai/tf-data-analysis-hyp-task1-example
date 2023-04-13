import pandas as pd
import numpy as np


chat_id = 1226526788

import statsmodels.api as sm


def solution( s1, n1 ,s2, n2):
    z, p_value = sm.stats.proportions_ztest([s1,s2],[n1,n2])
    return True if p_value < 0.03 else False

#def solution(x_success: int, 
#             x_cnt: int, 
#             y_success: int, 
#             y_cnt: int,
#            level=0.03) -> bool:
#    p1 = x_success/x_cnt
#    p2 = y_success/y_cnt
#    # оценим вероятность успеха на выборке А + Б
#    p = (x_success + y_success)/(x_cnt +y_cnt)
#    # расчитаем z-метку, которая распределена нормально
#    z = (p2 - p1)/ ((p*(1-p)*((1/x_cnt) + (1/y_cnt)))**0.5)    
#    p_value = norm.cdf(z)
#    return True if 2 * p_value < level else False
