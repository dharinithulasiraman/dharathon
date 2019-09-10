a,b=map(int,input().split())
c=list(map(int,input().split()))
d=len(c)
flag=0
for j in range(d):
	if(c[j]==b):
		print("yes")
		break
	else:
		flag+=1
if(flag==d):
	print("no")
