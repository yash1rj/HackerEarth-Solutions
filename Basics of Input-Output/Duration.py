'''
Rahul is a very busy persion he dont wan't to waste his time . 
He keeps account of duration of each and every work. 
Now he don't even get time to calculate duration of works, 
So your job is to count the durations for each work and give it to rahul.

Input:
First line will be given by N number of works
Next N line will be given SH,SM,EH and EM  each separated by space(SH=starting hr, SM=starting min, EH=ending hr, EM=ending min)

Output:
N lines with duration HH MM(hours and minutes separated by space)

SAMPLE INPUT 
2
1 44 2 14
2 42 8 23

SAMPLE OUTPUT 
0 30
5 41
'''

# Write your code here
entry=int(input())
a=[]
for i in range(entry):
    a.append([])
    a[i]=input().split(" ")
    
for j in range(entry):
    start_time=(int(a[j][0])*60)+int(a[j][1])
    end_time=(int(a[j][2])*60)+int(a[j][3])
    time=end_time-start_time
    (hr,mm)=(time//60,time%60)
    print(hr,mm)
