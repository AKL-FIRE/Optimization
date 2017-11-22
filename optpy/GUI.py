import tkinter as tk
import sys

class MyApp():
    def __init__(self):
        self.root = None

        #线程管理器
        self.threads = []

        #最优化算法
        self.CoordinateAlternation = None
        self.DFP = None
        self.GradientDescent = None
        self.NewtonMethod = None
        self.GoldSegment = None
        self.InsertValue = None

        self.str_fun = None
        self.str_epsilon = None

        self.result = None
        self.result_out = None


    def ok(self):
        #得到输入的函数
        if self.v.get() == 1:
            from optpy import CoordinateAlternation as CA
            self.CoordinateAlternation = CA.CoordinateAlternation(True,self.str_fun.get(),self.str_epsilon.get())
        if self.v.get() == 2:
            from optpy import DFP
            self.DFP = DFP.DFP(True,self.str_fun.get(),self.str_epsilon.get())
        if self.v.get() == 3:
            from optpy import GradientDescent as GD
            self.GradientDescent = GD.GradientDescent(True,self.str_fun.get(),self.str_epsilon.get())
        if self.v.get() == 4:
            from optpy import NewtonMethod as NM
            self.NewtonMethod = NM.NewtonMethod(True,self.str_fun.get(),self.str_epsilon.get())
        if self.v.get() == 5:
            from optpy import GoldSegment as GS
            self.GoldSegment = GS.GoldSegment(True,self.str_fun.get(),self.str_epsilon.get())
        if self.v.get() == 6:
            from optpy import InsertValue as IV
            self.InsertValue = IV.InsertValue(True,self.str_fun.get(),self.str_epsilon.get())

    def cancel(self):
        sys.exit()

    def Calculate(self):
        if self.v.get() == 1:
            if self.CoordinateAlternation == None:
                raise('此方法未初始化')
            self.result = self.CoordinateAlternation.Calculate()
            self.result_out.set(self.result[2])
        if self.v.get() == 2:
            if self.DFP == None:
                raise('此方法未初始化')
            self.result = self.DFP.Calculate()
            self.result_out.set(self.result[2])
        if self.v.get() == 3:
            if self.GradientDescent == None:
                raise('此方法未初始化')
            self.result = self.GradientDescent.Calculate()
            self.result_out.set(self.result[2])
        if self.v.get() == 4:
            if self.NewtonMethod == None:
                raise('此方法未初始化')
            self.result = self.NewtonMethod.Calculate()
            self.result_out.set(self.result[2])
        if self.v.get() == 5:
            if self.GoldSegment == None:
                raise('此方法未初始化')
            self.result = self.GoldSegment.Calculate()
            self.result_out.set(self.result[2])
        if self.v.get() == 6:
            if self.InsertValue == None:
                raise('此方法未初始化')
            self.result = self.InsertValue.Calculate()
            self.result_out.set(self.result[2])

    def run(self):
        self.root = tk.Tk()
        self.root.title('最优化算法选择器')

        #使用说明
        self.group1 = tk.LabelFrame(self.root, text='使用说明：', padx=5, pady=5)
        self.group1.grid(row=0, column=0, padx=10, pady=10)
        self.introduction = tk.Label(self.group1,text='1.请先选择优化算法，再点击初始化。\n2.输入优化参数后点击初始化。\n3.初始化完成后点击计算。\n4.支持1维，2维函数画图。')
        self.introduction.grid(row=0)

        # 最优化方法选择
        self.group2 = tk.LabelFrame(self.root, text='请选择您的优化方法：', padx=5, pady=5)
        self.group2.grid(row=1, column=0, padx=10, pady=10)
        LANGS = [('CoordinateAlternation(多变量高次优化)', 1), ('DFP(多变量二次优化)', 2), ('GradientDescent(多变量高次优化)', 3), ('NewtonMethod(多变量高次优化)', 4),
                 ('GoldSegment(单变量高次优化)', 5),('InsertValue(单变量高次优化)', 6)]
        self.v = tk.IntVar()
        self.v.set(1)
        for lang, num in LANGS:
            b = tk.Radiobutton(self.group2, text=lang, variable=self.v, value=num)
            b.grid(row=num, sticky=tk.W)

        #参数输入
        self.str_fun = tk.StringVar()
        self.str_epsilon = tk.StringVar()
        self.group3 = tk.LabelFrame(self.root, text='参数输入：', padx=5, pady=5)
        self.group3.grid(row=2, column=0, padx=10, pady=10)
        tk.Label(self.group3,text='目标函数输入：').grid(row=0,column=0,padx=10,pady=10)
        tk.Entry(self.group3,textvariable = self.str_fun).grid(row=0,column=1,padx=10,pady=10)
        tk.Label(self.group3, text='最大误差输入：').grid(row=1, column=0, padx=10, pady=10)
        tk.Entry(self.group3, textvariable=self.str_epsilon).grid(row=1, column=1, padx=10, pady=10)

        #输出结果
        self.result_out = tk.StringVar()
        self.group5 = tk.LabelFrame(self.root, text='结果输出：', padx=5, pady=5)
        self.group5.grid(row=3, column=0, padx=10, pady=10)
        tk.Label(self.group5,text='计算结果:\n',textvariable=self.result_out).grid(row=0,padx=100,pady=10)

        # 按钮
        self.group4 = tk.LabelFrame(self.root, text='处理按钮：', padx=5, pady=5)
        self.group4.grid(row=4, column=0, padx=10, pady=10)
        tk.Button(self.group4, text='初始化', width=10, command=self.ok).grid(row=0, column=0, sticky=tk.E, padx=10, pady=5)
        tk.Button(self.group4, text='退出', width=10, command=self.cancel).grid(row=0, column=3, sticky=tk.E, padx=10,
                                                                             pady=5)
        tk.Button(self.group4, text='计算', width=10, command=self.Calculate).grid(row=0, column=1, sticky=tk.E, padx=10,
                                                                                pady=5)
        tk.Button(self.group4, text='画图', width=10, command=self.Paint).grid(row=0, column=2, sticky=tk.E, padx=10,
                                                                                 pady=5)
        self.root.mainloop()

    def Paint(self):
        if self.str_fun == None:
            raise('未输入函数。')
        import sympy as sy
        import matplotlib.pylab as plt
        import numpy as np
        x_val = np.linspace(-5,5,30)
        f_val = np.linspace(-5,5,30)
        f = sy.simplify(self.str_fun.get())
        x = list(f.free_symbols)
        if x.__len__() == 1:
            for i in range(x_val.__len__()):
                f_val[i] = f.subs({x[0]:x_val[i]})
            plt.plot(x_val,f_val)
            plt.show()
        elif x.__len__() == 2:
            from mpl_toolkits.mplot3d import Axes3D
            ax = Axes3D(plt.figure(1))
            y_val = np.linspace(-5,5,30)
            x_val,y_val = np.meshgrid(x_val,y_val)
            z = np.zeros((30,30))
            for r in range(30):
                for c in range(30):
                    f_temp = f.subs({x[0]:x_val[r,c]})
                    f_temp = f_temp.subs({x[1]: y_val[r,c]})
                    z[r,c] = f_temp
            ax.plot_surface(x_val,y_val,z,rstride=1, cstride=1, cmap='Blues')
            plt.show()
        else:
            raise('不合法的变量维数')
