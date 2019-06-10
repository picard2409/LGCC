
from scipy import sparse
import numpy as np

class Lgcc():

    def lcm(self,n):
        no=n+1
        cn=np.zeros(no)
        cn[1]=1
        z=1
        for i in range(1,n):
            z=z*(i-0.5)/i
            cn[i+1]=z
        mlc=np.zeros((no,no))
        for j in range(0,n):
            tmp=np.floor(j/2)
            tmp=tmp.astype(np.int)
            for i in range(0,+1):
                mlc[j-2*i,j]=2*cn[j-i]
        mlc[n,n]=2.0*mlc[n,n]
        return mlc

    def hcm(self,n,mlc):
        mhc=np.zeros((n+1,n+1))
        mhc[:,2:n+1]=mlc[:,2:n+1]-mlc[:,0:n-1]
        mhc[0:1,0]=mlc[0:1,0]
        mhc[0:1,1]=mlc[0:1,0]+mlc[0:1,1]
        return mhc


            # def cheb(self,N):
    #     if N==0:
    #         D=0
    #         x=1
    #         return
    #     x=np.cos(np.pi/N*np.arange(N,-1,-1))
    #     x=np.transpose(x)
    #     X=np.tile(x,(1,N+1))
    #     dX=X-np.transpose(X)

    #     D=np.divide(np.multiply(c,1/c),dX+np.eye(N+1))
    #     D=D-np.diag(np.sum(np.transpose(D)))
    #     return x,D

    def f2ph(self,f,lc,gmi,n):
        fl=np.multiply(self.utuh(f,lc),gmi)
        z=np.array([[fl[0]-fl[1]]/2,[fl[0]]+fl[1]]/2)
        tmp=fl[2:n+1]-fl[0:n-1]
        gh=np.vstack((z,tmp))
        return gh


    def Ini(self,xb,n):
        scl=2/(xb[1]-xb[0])
        lc=self.lcm(n)
        hc=self.hcm(n,lc)
        #D,xc=cheb(n)
        xc=np.cos(np.pi/n*np.arange(n,-1,-1))
        xc=np.transpose(xc)

        x=xb[1]+(xc+1)/scl
        return lc,hc,x,scl

    def InitializeMK(self,n,scl):
        gm=2*np.arange(0,n+1,1)+1
        gmi=2/gm
        zd=np.array([-gmi[0:n-1],gmi[2:n+1]])
        #print(zd)
        z = sparse.spdiags(zd, [0,2], n-1, n+1)
        z=z.A
        M1=z[:,2:n+2]-z[:,0:n-1]
        M1b=np.array([[1,1],[-1/3,1/3]])
        K1=2*scl*scl*gmi[1:n]
        return M1, M1b,K1,gmi

    def uhtu(self,ul,mlh):
        no=ul.ndim   #维度  实际上是行数、
        n=no-1
        z=np.matmul(mlh,ul)     #矩阵乘法

        z=np.fft.fft(np.vstack(z,np.rot90(z[1:n],2)))
        u=np.rot90(np.real(z[0:no]/2))
        return u

    def utuh(self,u,mlh):
        no=u.ndim
        n=no-1
        tmp=np.rot90(u,2)
        z=np.fft.ifft(np.vstack(tmp,u[1:n]))
        z=2*np.real(z[0:no])
        ul=np.inv(mlh)*z
        return ul
        
