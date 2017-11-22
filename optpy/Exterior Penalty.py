import sympy as sy
import tkinter as tk
import optpy.GUI as APP

class ExteriorPenalty(object):
    def __init__(self):
        str_fun = input('请输入需优化函数:')
        str_ = input('请输入等式约束条件h(x)，以"，"分隔：')
        str_vec = str_.split(',')
        str_penalty = "("
        for i in str_vec:
            str_penalty = str_penalty + '(' + i + ')**2+'
        str_penalty = str_penalty[0:str_penalty.__len__() - 1] + ")"
        self.str_fun = str_fun + '+10000*' + str_penalty
        str_ = input('请输入不等式约束条件h(x)，以"，"分隔：')
        str_vec = str_.split(',')
        str_penalty = "("
        for i in str_vec:
            str_penalty = str_penalty + '(' + i + ')**2+'
        str_penalty = str_penalty[0:str_penalty.__len__() - 1] + ")"
a = ExteriorPenalty()