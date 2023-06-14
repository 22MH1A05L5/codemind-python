p,r,t=map(int,input().split())
c=(1+r/100)**t
a=p*(c)
ci=a-p
print("%.2f"%(a))