at=[5,1,4,2,3,3] #arrival time
at1=at.copy() #copy of arrival time
bt=[2,1,8,4,5,6] #burst tme
n=len(at) #Number of processes
gantt_time=[min(at)] #[1,2,6,11,17,25,27]
gantt_process=[] #[2,4,5,6,3,1]
for i in range(n):
    min_index=at.index(min(at)) #finding index of smallenst element of at.. smallest element=3.. index=5... process=index+1=5
    gantt_process.append(min_index+1) #[2]
    at[min_index]=float('inf') #[infinity,infinity,infinty,infinity,infinity,infinity]
for i in range(n):
    gantt_time.append(gantt_time[-1]+bt[gantt_process[i]-1])
tat_total=0
wt_total=0
gantt_time.pop(0)
gantt=dict(zip(gantt_process,gantt_time)) #key=process no, values=CT
print(gantt)
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
