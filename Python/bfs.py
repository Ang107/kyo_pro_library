import sys
from  collections import deque,defaultdict
from itertools import accumulate, product,permutations,combinations,combinations_with_replacement
import math
from bisect import bisect_left,insort_left,bisect_right,insort_right
#product : bit全探索 product(range(2),repeat=n)
#permutations : 順列全探索
#combinations : 組み合わせ（重複無し）
#combinations_with_replacement : 組み合わせ（重複可）
#from sortedcontainers import SortedSet, SortedList, SortedDict
sys.setrecursionlimit(10**7)
around4 = ((0, -1), (0, 1), (-1, 0), (1, 0))
around8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
inf = float('inf')
deq = deque()
dd = defaultdict()

II = lambda : int(input())
MII = lambda : map(int,input().split())
LMII = lambda : list(map(int,input().split()))
Ary2 = lambda h,w,element : [[element] * w for _ in range(h)]   #二次元リスト作成
is_not_Index_Er = lambda x,y,l : 0 <= x < len(l) and 0 <= y < len(l[0])    #範囲外参照していないことの確認

h,w = MII()
l = [input() for _ in range(h)]
visited = Ary2(h,w,-1)

#キュー使用
x,y = 0,0
deq = deque([(x,y,0)])
def bfs():
    while deq:
        x,y,dis = deq.popleft()
        visited[x][y] = dis
        for i,j in around8:
            #範囲外参照の確認
            if is_not_Index_Er(x+i,y+j,l):
                #移動先のマスと探索済みかの確認
                if l[x+i][y+j] == "." and visited[x+i][y+j] == -1:
                    visited[x+i][y+j] = dis + 1
                    deq.append((x+i,y+j,dis+1))

bfs()
import pprint
pprint.pprint(visited)
