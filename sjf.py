# Author: Riddhish V. Lichade
# Shortest Job First
# Taking arrival time 0 for all processes
bt = [2, 1, 4, 4, 5, 6]
n=len(bt)
bt1=bt.copy()
pno = [1, 2, 3, 4, 5, 6]
bt.sort()
d={}
for i in range(n):
    if bt1[i] in d:
        d[bt1[i]].append(i+1)
    else:
        d[bt1[i]]=[i+1]
ct=0
gantt={}
bt=set(bt)
total_tat=total_wt=0
for i in bt:
    for j in d[i]:
        gantt[j]=i+ct
        ct += i
print("P\tAT\tBT\tCT\tTAT\tWT")
for i in range(n):
    CT=gantt[i+1]
    wt=CT-bt1[i]
    total_tat+=CT
    total_wt+=wt
    print(i+1,0,bt1[i],CT,CT,wt,sep='\t')
print("Average TAT = ",total_tat/n)
print("Average WT = ",total_wt/n)
print("Throughput = ",n/ct)



























# Author: Riddhish V. Lichade
# Shortest Job First
# For arrival time check what processes are available... choose shortest... continue
'''
at=[5,0,4,2,3,3] #arrival time
at1=at.copy() #copy of arrival time
bt=[2,1,4,4,5,6] #burst time
bt1=bt.copy()
n=len(at) #Number of processes
gantt_time=[min(at)]
gantt_process=[]

dict={} #key:at, value:list of bt with same at
for i in range(n):
    if at[i] in dict:
        dict[at[i]].append(bt[i])
    else:
        dict[at[i]]=[bt[i]]
print(dict)
jobs_available=[]
print("gant of -1",gantt_time[-1])
curr_time=gantt_time[-1]
while len(gantt_time)<=n:
    #for i in range(n):
    print("CUrrent time =", curr_time)
    for i in dict:
        if i<=curr_time:
            print('i =',i)
            print("dict of i",dict[i])
            for j in dict[i]:
                print('j=',j)
                jobs_available.append(j)
                print("Jobs available",jobs_available)
                dict[i].remove(j)
                asf=
                if len(dict[i])==0:
                    dict.pop(i)
                #print("Dictionary after removing",dict)

    if jobs_available==[]:
        curr_time+=1
        continue
    try:
        cur_job=min(jobs_available)
    except:
        gantt_time[-1]
        continue
    gantt_time.append(curr_time+cur_job)
    gantt_process.append(bt1.index(cur_job)+1)
    print("Gantt time = ",gantt_time)
    print("Gantt process =",gantt_process)
    jobs_available.remove(cur_job)
    print("Jobs available",jobs_available)
    curr_time=gantt_time[-1]

print(gantt_time)
print(gantt_process)'''

