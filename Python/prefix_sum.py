from itertools import  accumulate

class Prefix_sum:
    def __init__(self,l : list):
        self.prf_sum = list(accumulate(l))
    def get_all(self):
        return self.prf_sum
    #1スタートのl番目からr番目の区間を取得
    def get_section_from_1(self,l : int,r : int):
        return self.prf_sum[r-1] - self.prf_sum[l-2]
    #0スタート
    def get_section_from_0(self,l : int,r : int):
        return self.prf_sum[r] - self.prf_sum[l-1]

class Imos:
    def __init__(self,h,w):
        self.l = [[0]*w for _ in range(h)]
        self.h, self.w = h, w
        
    def add_section_from_1(self,a,b,c,d,diff):
        self.l[a-1][b-1] += diff
        if c < self.h:
            self.l[c][b-1] -= diff
        if d < self.w:
            self.l[a-1][d] -= diff
        if c < self.h and d < self.w:
            self.l[c][d] += diff   
    
    def add_section_from_0(self,a,b,c,d,diff):
        self.l[a][b] += diff
        if c < self.h:
            self.l[c+1][b] -= diff
        if d < self.w:
            self.l[a][d+1] -= diff
        if c < self.h and d < self.w:
            self.l[c+1][d+1] += diff    
    
    def get_all(self):
        return self.l       
        
class Prefix_sum_2d:
    def __init__(self,l):
        h,w = len(l),len(l[0])
        tmp = [[0] * w for _ in range(h)]
        for i,j in enumerate(l):
            tmp[i] = list(accumulate(j))
        for i in range(1,h):
            for j in range(w):
                tmp[i][j] = tmp[i-1][j] + tmp[i][j]
        self.prf_sum = tmp
        
    def get_all(self):
        return self.prf_sum
    
    #左上のx,y,右下のx,y = a,b,c,d
    def get_section_from_1(self,a,b,c,d):
        tmp = self.prf_sum[c-1][d-1]
        if a >= 2:
            tmp -= self.prf_sum[a-2][d-1] 
        if b >= 2:
            tmp -= self.prf_sum[c-1][b-2]
        if a >= 2 and b >= 2:
            tmp += self.prf_sum[a-2][b-2]
        return tmp
    
    def get_section_from_0(self,a,b,c,d):
        tmp = self.prf_sum[c][d]
        if a >= 1:
            tmp -= self.prf_sum[a-1][d] 
        if b >= 1:
            tmp -= self.prf_sum[c][b-1]
        if a >= 1 and b >= 1:
            tmp += self.prf_sum[a-1][b-1]
        return tmp
        