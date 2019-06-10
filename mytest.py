
import numpy as np
import matplotlib.pyplot as plt
import os
import scipy
import sys
import sympy
#print(sys.path)

# from sympy import *
# import sympy as sys
# os.system('cls')
# s1=np.arange(10,1,-1)
# s2=np.arange(20,11,-1)
# s=np.divide(s2,s1)
# # print(s1,s2,s)
# # D=np.diag(s1)
# # print(D)
# # S=np.array([[1,2],[2,3]])
# # print(S)
# #数组的垂直和并
# a=np.array([1,3])
# b=np.array([4,6])
# ab=np.vstack((a,b))
# print(ab)
# N=ab.shape
# print(N[1])
# print(np.zeros(5))
#============================
    # def hcm(self,n,mlc):
    #     mhc=np.zeros((n+1,n+1)     #注意zeros要加两层括号
    #     # mhc[:,2:n+1]=mlc[:,2:n+1]-mlc[:,0:n-1]
    #     # mhc[0:1,0]=mlc[0:1,0]
    #     # mhc[0:1,1]=mlc[0:1,0]+mlc[0:1,1]
    #     return mhc
#====================
#test all function
# print(range(1,10))

# a=np.zeros((2,2))
# print(a)
# a[1,1]=6
# print(a)

# from LGCC import Lgcc 

# myLGCC=Lgcc()
# n=10
# # mlc=Lgcc.lcm(myLGCC,10)  #如果不是用myLGCC调用函数   那么self参数需要用实参输入

# mlc=myLGCC.lcm(10)
# mhc=myLGCC.hcm(10,mlc)
# xb=np.array([[-1],[1]])
# lc,hc,x,scl=myLGCC.Ini(xb,n)
# M1,M1b,K1,gmi=myLGCC.InitializeMK(n,scl)

# # print(mlc,mhc)
# print(M1,M1b,K1,gmi)

# x,t=symbols('x,t')
# print(x)