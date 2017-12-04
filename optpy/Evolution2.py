import optpy.Optimization as op
import math
import random
import copy
import sympy as sy

class Individual(object):
    def __init__(self):
        self.Gen = None
        self.fitness = None
        self.x = None

    def InitFirstGeneration(self,L,x_length):
        self.Gen = []
        for i in range(x_length):
            temp = []
            for j in range(L):
                if random.random() >= 0.5:
                    temp.append(1)
                else:
                    temp.append(0)
            self.Gen.append(temp)

    def decode(self,x_length,x_val,delta):
        self.x = []
        for i in range(x_length):
            temp = 0.0
            xx = 0
            for j in self.Gen[i][::-1]:
                temp = temp + j * 2 ** xx
                xx = xx + 1
            temp = min(x_val) + delta * temp
            self.x.append(temp)

    def CalculateFit(self,f,x):
        f_temp = f
        for i in range(len(self.x)):
            f_temp = f_temp.subs({x[i]:self.x[i]})
        self.fitness = float(sy.re(f_temp.evalf())) #修正虚数

    def Mutation(self,x_length,l,pm):
        for x in range(x_length):
            for i in range(l):
                if random.random() < pm:
                    if self.Gen[x][i] == 0:
                        self.Gen[x][i] = 1
                    else:
                        self.Gen[x][i] = 0
                else:
                    if self.Gen[x][i] == 0:
                        self.Gen[x][i] = 0
                    else:
                        self.Gen[x][i] = 1



class Evolution(op.Optimization):
    def __init__(self,useGUI,str_fun=None,epsilon=None,N=None,pc=None,pm=None,evo_x=None,maxIteration=None):
        super(Evolution, self).__init__(useGUI, str_fun, epsilon)
        if useGUI == False:
            self.N = int(input('请输入群体个数：'))
            self.pc = float(input('请输入交叉概率：'))
            self.pm = float(input('请输入变异概率：'))
        else:
            self.maxIteration = int(maxIteration)
            self.N = int(N)
            self.pc = float(pc)
            self.pm = float(pm)
            self.x_val = evo_x.split(',')
            self.x_val = [float(x) for x in self.x_val]
            print('该算法初始化完成.')

    #选择算子
    def Selection(self):
        fitnesses = [x.fitness for x in self.PG] #选出适应度
        maxfitness = fitnesses.index(max(fitnesses))
        self.max_fit = copy.deepcopy(self.PG[maxfitness])
        self.PG.remove(self.PG[maxfitness])
        fitnesses.remove(fitnesses[maxfitness]) #移除最大适应度个体
        minfitness = fitnesses.index(min(fitnesses))
        self.min_fit = copy.deepcopy(self.PG[minfitness])
        self.PG.remove(self.PG[minfitness])
        fitnesses.remove(fitnesses[minfitness]) #移除最小适应度个体
        fitnesses_new = [x + abs(self.min_fit.fitness) for x in fitnesses]
        fit_count = 0.0 #适应度总和
        for i in fitnesses_new:
            fit_count = fit_count + i
        B = []
        C = []
        C_temp = 0.0
        for i in fitnesses_new:
            C_temp = C_temp + (i / fit_count)
            B.append(i / fit_count)
            C.append(C_temp)
        SG = []  # 父代个体级
        for count in range(self.N - 2):
            prob = random.random()  # 产生一个随机数
            for example in C:
                if example >= prob:
                    SG.append(copy.deepcopy(self.PG[C.index(example)]))  # 选择一个父代个体
                    break
        return SG

    #交叉算子
    def Cross(self,SG):
        CG = []
        Y = []  # 取出Y染色体
        CPoint = int(2 / 3 * self.l)  # 交叉基因的后1 / 3
        k = self.N - 2
        for i in range(int(k / 2)):
            random_selection = random.randint(0, k - 1)
            Y.append(SG[random_selection])
            SG.remove(SG[random_selection])
            k = k - 1
        for i in range(len(Y)):
            for x in range(self.x_length):
                for j in range(CPoint, self.l):
                    temp = Y[i].Gen[x][j]
                    Y[i].Gen[x][j] = SG[i].Gen[x][j]
                    SG[i].Gen[x][j] = temp
        for i in range(len(Y)):
            CG.append(Y[i])
            CG.append(SG[i])
        return CG

    #变异算子
    def Variation(self,CG):
        for example in CG:
            example.Mutation(self.x_length,self.l,self.pm)
        return CG

    #初始群体初始化
    def PGInit(self):
        self.PG = []
        for i in range(self.N):
            a = Individual()
            a.InitFirstGeneration(self.l,self.x_length)
            self.PG.append(a)

    #个体解码
    def Decode(self,G):
        for i in G:
            i.decode(self.x_length,self.x_val,self.delta)

    #计算每个个体的适应度
    def CalculateFit(self,decode_G):
       for i in decode_G:
           i.CalculateFit(self.f,self.x)

    def Calculate(self):
        G = 1 #迭代次数为0
        self.FES = 0 #适应度评价次数为0
        self.l = int(math.ceil(math.log(((max(self.x_val) - min(self.x_val)) / self.epsilon),2))) #决策变量的二进制串长度
        self.delta = (max(self.x_val) - min(self.x_val)) / (2**self.l - 1) #实际的搜索精度
        self.PGInit() #随机产生初始群体
        self.Decode(self.PG) #对每个个体解码
        self.CalculateFit(self.PG) #计算适应度集合fit_g
        self.FES = self.FES + self.N
        while True:
            SG = self.Selection() #执行选择，得到父代个体集
            CG = self.Cross(SG) #执行交叉算子
            MG = self.Variation(CG) #执行变异算子
            self.Decode(MG) #解码后的子代个体
            self.CalculateFit(MG) #子代个体的适应度集合
            self.FES = self.FES + self.N - 2
            index1 = random.randint(0, self.N - 2) #将适应度最大的父代复制两次直接加入子代
            MG.insert(index1, copy.deepcopy(self.max_fit))
            index2 = random.randint(0, self.N - 2)
            MG.insert(index2, copy.deepcopy(self.max_fit))
            self.PG = MG
            print('繁衍到第'+str(G)+'代时，此时的x值是'+str(self.max_fit.x)+',适应度为：'+str(self.max_fit.fitness))
            if self.FES >= 100000 or G >= self.maxIteration:
                return self.max_fit.x,self.max_fit.fitness, \
                       '繁衍到第'+str(G)+'代时，此时的x值是'+str(self.max_fit.x)+',适应度为：'+str(self.max_fit.fitness)
            G = G + 1