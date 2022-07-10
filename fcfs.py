at=[5,0,4,2,3,3] #arrival time
at1=at.copy() #copy of arrival time
bt=[2,1,8,4,5,6] #burst time
n=len(at) #Number of processes
gantt_time=[min(at)]
gantt_process=[]
for i in range(n):
    min_index=at.index(min(at)) #finding index of smallenst element of at
    gantt_process.append(min_index+1)
    at[min_index]=float('inf')
for i in range(n):
    process=gantt_process[i] #current process
    y=bt[process-1] #burst time of current process
    #if no process at time
    if at1[process-1]>gantt_time[-1]:
        y+=at1[process-1]-gantt_time[-1]
    gantt_time.append(gantt_time[-1]+y)
tat_total=0
wt_total=0
gantt_time.pop(0)
gantt=dict(zip(gantt_process,gantt_time)) #key=process no, values=CT
print("P\tAT\tBT\tCT\tTAT\tWT\tRT")
for i in range(n):
    ct=gantt[i+1]
    tat=ct-at1[i]
    tat_total+=tat
    wt=tat-bt[i]
    wt_total+=wt
    print(i+1,at1[i],bt[i],ct,tat,wt,wt,sep='\t')
print("\nAverage TAT=",tat_total/n)
print("Average WT=",wt_total/n)
print("Throughput=",n/max(gantt_time))
