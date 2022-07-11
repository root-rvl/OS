# Author: Riddhish V. Lichade
# Non-Preemptive Priority
# Taking arrival time 0 for all processes

bt=[2,4,1,4,6,5]
n=len(bt)
priority=[5,3,2,1,3,4] # 1 is lowest 5 highest
prio=priority.copy()
d={} #d={priority:[process numbers]}
for i in range(n):
    if priority[i] in d:
        d[priority[i]].append(i+1)
    else:
        d[priority[i]]=[i+1]
gantt= {}
ct=0
p=list(set(priority))
for i in p[::-1]:
    for j in d[i]:
        gantt[j]=bt[j-1]+ct
        ct+=bt[j-1]
tot_tat=tot_wt=0
print("P\tAT\tPri\tBT\tCT\tTAT\tWT")
for i in range(n):
    tat=CT=gantt[i+1]
    tot_tat+=tat
    wt=tat-bt[i]
    tot_wt+=wt
    print(i+1,0,prio[i],bt[i],CT,CT,wt,sep='\t')
print("Average TAT = ",tot_tat/n)
print("Average WT = ",tot_wt/n)
print("Throughput = ",n/ct)


'''n = 5
priority = [1,2,2,4,5]
burst_time = [3,4,5,6,7]
sal = sorted(priority, reverse=True)
dp = priority[0::]
c = [0] * n
ct = [0] * n
tat = [0] * n
wt = [0] * n
final_sum = 0
ltime = 0
for i in range(n):
    c[i] = dp.index(sal[i])
    dp[dp.index(sal[i])] = -1
for i in c:
    ltime = ltime + burst_time[i]
    ct[i] = ltime
print("Average CT is: ", sum(ct) / n)
print("CT")
print(*ct)
for i in range(n):
    tat[i] = ct[i]
print("TAT")
print(*tat)
print("Average TAT is ", sum(tat) / n)
for i in range(n):
    wt[i] = tat[i] - burst_time[i]
print("Waiting Time")
print(*wt)
print("Average waiting time ", sum(wt) / n)'''