import time
from time import perf_counter 

def bubble_sort(data,drawData,timetick):
    for _ in range(len(data)-1):
        for j in range(len(data)-1):
            if data[j]>data[j+1]:
                drawData(data,['yellow' if x==j or x==j+1 else "red" for x in range(len(data))])
                time.sleep(timetick)
                data[j],data[j+1]=data[j+1],data[j]
                drawData(data,['pink' if x==j or x==j+1 else "red" for x in range(len(data))])
                time.sleep(timetick)
    drawData(data,['yellow' for x in range(len(data))])
    
