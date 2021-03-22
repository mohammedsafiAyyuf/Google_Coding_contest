import math
for _ in range(int(input())):
    r,c=list(map(int, input().split(" ")))
    matrix=[list(map(int,input().split())) for i in range(r)]
    topToBottom=[[0]*c for i in range(r)]
    bottomToTop=[[0]*c for i in range(r)]
    leftToRight=[[0]*c for i in range(r)]
    rightToLeft=[[0]*c for i in range(r)]

    #Top to Bottom
    for j in range(c):
    	prev=0
    	for i in range(r):
    		if matrix[i][j]==1:
    			prev+=1
    			topToBottom[i][j]=prev
    		else:
    			prev=0


    #Bottom To Top
    for j in range(c):
    	prev=0
    	for i in range(r-1,-1,-1):
    		if matrix[i][j]==1:
    			prev+=1
    			bottomToTop[i][j]=prev
    		else:
    			prev=0


    #Left To Right
    for i in range(r):
    	prev=0
    	for j in range(c):
    		if matrix[i][j]==1:
    			prev+=1
    			leftToRight[i][j]=prev
    		else:
    			prev=0

    #Right To Left
    for i in range(r):
    	prev=0
    	for j in range(c-1,-1,-1):
    		if matrix[i][j]==1:
    			prev+=1
    			rightToLeft[i][j]=prev
    		else:
    			prev=0
    lCount=0


    for i in range(r):
    	for j in range(c):
    		#Formula method to count max L that of size 1:2 ratio can be formed
    		lCount+=max(0,min(rightToLeft[i][j]//2,topToBottom[i][j])-1)
    		lCount+=max(0,min(rightToLeft[i][j],topToBottom[i][j]//2)-1)

    		lCount+=max(0,min(leftToRight[i][j]//2,topToBottom[i][j])-1)
    		lCount+=max(0,min(leftToRight[i][j],topToBottom[i][j]//2)-1)

    		lCount+=max(0,min(rightToLeft[i][j]//2,bottomToTop[i][j])-1)
    		lCount+=max(0,min(rightToLeft[i][j],bottomToTop[i][j]//2)-1)

    		lCount+=max(0,min(leftToRight[i][j]//2,bottomToTop[i][j])-1)
    		lCount+=max(0,min(leftToRight[i][j],bottomToTop[i][j]//2)-1)


    		#Brute force method to count max L that of size 1:2 ratio can be formed
    		"""
    		for x in range(2,topToBottom[i][j]+1):
    			#RtoL
    			if rightToLeft[i][j]>=x*2:
	    			lCount+=1
	    		if x%2==0 and x>2 and rightToLeft[i][j]>=x//2:
	    			lCount+=1

	    		#LtoR
    			if leftToRight[i][j]>=x*2:
	    			lCount+=1
	    		if x%2==0 and x>2 and leftToRight[i][j]>=x//2:
	    			lCount+=1

    		for x in range(2,bottomToTop[i][j]+1):
    			#RtoL
    			if rightToLeft[i][j]>=x*2:
	    			lCount+=1
	    		if x%2==0 and x>2 and rightToLeft[i][j]>=x//2:
	    			lCount+=1

	    		#LtoR
    			if leftToRight[i][j]>=x*2:
	    			lCount+=1
	    		if x%2==0 and x>2 and leftToRight[i][j]>=x//2:
	    			lCount+=1
	    	"""

    print("Case #{}: {}".format(_+1,lCount))