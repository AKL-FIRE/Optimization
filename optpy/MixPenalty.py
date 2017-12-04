import sympy as sy
import optpy.Optimization as op

class MixPenalty(op.Optimization):
    def __init__(self,useGUI,str_fun=None,epsilon=None):
        super(MixPenalty, self).__init__(useGUI, str_fun, epsilon)
        self.theta = 2
        self.c = 0.1
        str_constrain_eaqual = input('请输入等式约束条件，以；分隔：')
        str_constrain_uneaqual = input('请输入不等式约束条件，以；分隔：')
        self.str_constrain_uneaqual = str_constrain_uneaqual.split(';')
        self.str_constrain_eaqual = str_constrain_eaqual.split(';')
        str_penalty = self.GeneratePenaltyFun(self.theta, self.str_constrain_eaqual,self.str_constrain_uneaqual)
        self.penalty_f = sy.simplify(str_penalty)
        self.f_str1 = self.f_str + '+' + str_penalty
        self.f = sy.simplify(self.f_str1)
        print(self.f_str1)

    def GeneratePenaltyFun(self,str_penalty_num,str_constrain_eaqual,str_constrain_uneaqual):
        str_penalty = str(str_penalty_num) + '*('
        for i in str_constrain_uneaqual:
            str_penalty = str_penalty + '1/' + '(' + i + ')' + '+'
        str_penalty = str_penalty[0:len(str_penalty) - 1] + ')'
        str_penalty = str_penalty + '+(1/sqrt(' + str(str_penalty_num) + "))" + '*('
        for i in str_constrain_eaqual:
            str_penalty = str_penalty + '(' + i + ')**2+'
        str_penalty = str_penalty[0:len(str_penalty) - 1] + ')'
        return str_penalty

    def Calculate(self):
        k = 1
        from optpy import NewtonMethod
        while True:
            a = NewtonMethod.NewtonMethod(True, self.f_str1, self.epsilon)
            a.x_val = self.x_val
            result = a.Calculate()
            self.x_val1 = result[0]
            x_val1_m = sy.Matrix(self.x_val1).reshape(len(self.x),1)
            x_val_m = sy.Matrix(self.x_val).reshape(len(self.x),1)
            sub_x_val = x_val1_m - x_val_m
            sub_x_val = sub_x_val.evalf()
            if sub_x_val.norm() <= self.epsilon:
                print(result[2])
                break
            else:
                self.theta = self.theta * self.c
                k = k + 1
                str_penalty = self.GeneratePenaltyFun(self.theta, self.str_constrain_eaqual,self.str_constrain_uneaqual)
                self.penalty_f = sy.simplify(str_penalty)
                self.f_str1 = self.f_str + '+' + str_penalty
                self.f = sy.simplify(self.f_str1)
                self.x_val = self.x_val1

a = MixPenalty(False)
a.Calculate()