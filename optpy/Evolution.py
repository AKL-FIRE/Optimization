import optpy.Optimization as op
import math
import random
import copy

class Evolution(op.Optimization):
    def __init__(self,useGUI,str_fun=None,epsilon=None,N=None,pc=None,pm=None,evo_x=None):
        super(Evolution, self).__init__(useGUI, str_fun, epsilon)
        if useGUI == False:
            self.N = int(input('请输入群体个数：'))
            self.pc = float(input('请输入交叉概率：'))
            self.pm = float(input('请输入变异概率：'))
        else:
            self.N = int(N)
            self.pc = float(pc)
            self.pm = float(pm)
            self.x_val = evo_x.split(',')
            self.x_val = [float(x) for x in self.x_val]
            print('该算法初始化完成.')

    #选择算子
    def Selection(self):
        self.max_fit = copy.deepcopy(self.PG[self.fit_g.index(max(self.fit_g))]) #找出最高适应度的个体,要注意深度拷贝的问题
        self.min_fit = self.PG[self.fit_g.index(min(self.fit_g))] #找出最第适应度的个体
        self.max_fit_fit = max(self.fit_g)  # 找出最高适应度的个体的适应值
        self.PG.remove(self.max_fit) #移除最大最小适应度的个体
        self.PG.remove(self.min_fit)
        self.fit_g.remove(max(self.fit_g))
        self.fit_g.remove(min(self.fit_g))
        self.fit_g_count = 0.0 #适应度和
        for i in self.fit_g:
            self.fit_g_count = self.fit_g_count + i
        B = []
        C = []
        C_temp = 0.0
        for i in self.fit_g:
            C_temp = C_temp + (i / self.fit_g_count)
            B.append(i / self.fit_g_count)
            C.append(C_temp)
        SG = [] #父代个体级
        for count in range(self.N - 2):
            prob = random.random() #产生一个随机数
            for example in C:
                if example >= prob:
                    SG.append(self.PG[C.index(example)]) #选择一个父代个体
                    break
        return SG

    #交叉算子
    def Cross(self,SG):
        CG = []
        Y = [] #取出Y染色体
        CPoint = int(2 / 3 * self.l) #交叉基因的后1 / 3
        k = self.N - 2
        for i in range(int(k / 2)):
            random_selection = random.randint(0,k-1)
            Y.append(SG[random_selection])
            SG.remove(SG[random_selection])
            k = k - 1
        for i in range(len(Y)):
            for j in range(CPoint,self.l):
                temp = Y[i][j]
                Y[i][j] = SG[i][j]
                SG[i][j] = temp
        for i in range(len(Y)):
            CG.append(Y[i])
            CG.append(SG[i])
        return CG

    #变异算子
    def Variation(self,CG):
        temp = []
        for example in CG:
            temp1 = []
            for gen in example:
                if random.random() < self.pm:
                    if gen == 0:
                        temp1.append(1)
                    else:
                        temp1.append(0)
                else:
                    if gen == 0:
                        temp1.append(0)
                    else:
                        temp1.append(1)
            temp.append(temp1)
        return temp

    #初始群体初始化
    def PGInit(self):
        temp = []
        for i in range(self.N):
            sub_temp = []
            for j in range(self.l):
                if random.random() >= 0.5:
                    sub_temp.append(1)
                else:
                    sub_temp.append(0)
            temp.append(sub_temp)
        return temp

    #个体解码
    def Decode(self,G):
        decode_pg = []
        for i in range(len(G)):
            temp = 0.0
            xx = 0
            for j in G[i][::-1]:
                temp = temp + j * 2**xx
                xx = xx + 1
            temp = min(self.x_val) + self.delta * temp
            decode_pg.append(temp)
        return decode_pg

    #计算每个个体的适应度
    def CalculateFit(self,decode_pg):
        temp = []
        for i in decode_pg:
            #temp.append(self.f.subs({self.x[0]:i}))
            a = self.f.subs({self.x[0]: i})
            temp.append(a.evalf())
        return temp

    def Calculate(self):
        G = 1 #迭代次数为0
        self.FES = 0 #适应度评价次数为0
        self.l = int(math.ceil(math.log(((max(self.x_val) - min(self.x_val)) / self.epsilon),2))) #决策变量的二进制串长度
        self.delta = (max(self.x_val) - min(self.x_val)) / (2**self.l - 1) #实际的搜索精度
        self.PG = self.PGInit() #随机产生初始群体
        self.decode_pg = self.Decode(self.PG) #对每个个体解码
        self.fit_g = self.CalculateFit(self.decode_pg) #计算适应度集合fit_g
        self.FES = self.FES + self.N
        while True:
            SG = self.Selection() #执行选择，得到父代个体集
            CG = self.Cross(SG) #执行交叉算子
            MG = self.Variation(CG) #执行变异算子
            self.decode_pg = self.Decode(MG) #解码后的子代个体
            self.fit_g = self.CalculateFit(self.decode_pg) #子代个体的适应度集合
            self.FES = self.FES + self.N - 2
            index1 = random.randint(0, self.N - 2) #将适应度最大的父代复制两次直接加入子代
            MG.insert(index1, self.max_fit)
            self.fit_g.insert(index1,self.max_fit_fit)
            index2 = random.randint(0, self.N - 2)
            MG.insert(index2, self.max_fit)
            self.fit_g.insert(index2, self.max_fit_fit)
            self.PG = MG
            print('繁衍到第%d代时的最高适应度：%.15f,此时的x值为：%f,x计算出的适应度：%f' % (G, self.max_fit_fit, self.Decode([self.max_fit])[0],self.CalculateFit(self.Decode([self.max_fit]))[0]))
            if self.FES >= 10000 or G >= 100:
                return self.Decode([self.max_fit])[0], self.CalculateFit(self.Decode([self.max_fit]))[0], \
                       '繁衍到第%d代时的最高适应度：%.15f,此时的x值为：%f,x计算出的适应度：%f' % (
                       G, self.max_fit_fit, self.Decode([self.max_fit])[0],
                       self.CalculateFit(self.Decode([self.max_fit]))[0])
            G = G + 1