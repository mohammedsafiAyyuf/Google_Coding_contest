import math
for _ in range(int(input())):

    n,k=list(map(int, input().split(" ")))
    string=input()
    score=0
    for i in range(math.ceil(n/2)):
    	if string[i]!=string[n-i-1]:
    		score+=1

    print("Case #{}: {}".format(_+1,abs(score-k)))