import pandas as pd
import numpy as np


chat_id = 1226526788

from scipy.stats import norm

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
    p1 = x_success/x_cnt
    p2 = y_success/y_cnt
    # оценим вероятность успеха на выборке А + Б
    p = (x_success + y_success)/(x_cnt +y_cnt)
    # расчитаем z-метку, которая распределена нормально
    z = (p2 - p1)/ ((p*(1-p)*((1/x_cnt) + (1/y_cnt)))**0.5)    
    p_value = norm.cdf(z)
    return True if 2 * p_value < level else False
