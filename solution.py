import pandas as pd
import numpy as np


chat_id = 1226526788

from scipy.stats import chi2_contingency

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int,
            level=0.03) -> bool:
    '''
    Мы тестируем новый способ продажи и ожидаем повышения конверсии в тестовой группе.
    Составьте критерий с уровнем значимости 0.03 который позволит по данным теста 
    принять решение о масштабировании теста.
    ----
    x_success: int
        количество покупок в первой выборке
    x_cnt: int
        количество заявок в первой выборке
    y_success: int
        количество покупок во второй выборке
    y_cnt: int
        количество заявок во второй выборке
    Returns
    ----
    bool
        Возвращаемое значение: bool-значение, ответ на вопрос: "Отклонить гипотезу"
    '''
    arr = np.array([[x_success,x_cnt - x_success],[y_success,y_cnt - y_success]])
    chi2, p_value, dof, exp = chi2_contingency(arr,correction=False)
    #print('{:.12f}'.format(p_value))
    return True if p_value < level else False
