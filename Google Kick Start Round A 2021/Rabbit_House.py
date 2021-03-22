import math
import heapq
from collections import defaultdict

#using Loop Approach
for _ in range(int(input())):
    r,c=list(map(int, input().split(" ")))
    matrix=[list(map(int,input().split())) for i in range(r)]
    house=[i[:] for i in matrix]  #Modified Matrix
    ans=0
    for i in range(r):
    	for j in range(1,c):
    		house[i][j]=max(house[i][j],house[i][j-1]-1)
    	for j in range(c-2,-1,-1):
    		house[i][j]=max(house[i][j],house[i][j+1]-1)


    for j in range(c):
    	for i in range(1,r):
    		house[i][j]=max(house[i][j],house[i-1][j]-1)
    	for i in range(r-2,-1,-1):
    		house[i][j]=max(house[i][j],house[i+1][j]-1)

    for i in range(r):
    	for j in range(c):
    		ans+=house[i][j]-matrix[i][j]

    print("Case #{}: {}".format(_+1,ans))

#Using Heap Approach
"""
def checkSides(val,idx,matrix,maxHeap):
    sides=[[0,1],[1,0],[0,-1],[-1,0]]
    x=idx[0]
    y=idx[1]
    count=0
    for i in sides:
        adjX=x+i[0]
        adjY=y+i[1]
        if adjY>=0 and adjX>=0 and adjX<r and adjY<c:
            if abs(matrix[adjX][adjY]-val)>1:
                count+=abs(matrix[adjX][adjY]-val)-1
                matrix[adjX][adjY]=val-1
                heapq.heappush(maxHeap,[-matrix[adjX][adjY],[adjX,adjY]])
    return(count)


for _ in range(int(input())):
    r,c=list(map(int, input().split(" ")))
    matrix=[list(map(int,input().split())) for i in range(r)]
    #hashTable=defaultdict(list)
    maxHeap=[]
    for i in range(r):
        for j in range(c):
            maxHeap.append([-matrix[i][j],[i,j]])
    heapq.heapify(maxHeap)
    count=0
    while maxHeap:
        val,idx=heapq.heappop(maxHeap)
        val*=-1
        if matrix[idx[0]][idx[1]]==val:
            count+=checkSides(val,idx,matrix,maxHeap)


    print("Case #{}: {}".format(_+1,count))
"""