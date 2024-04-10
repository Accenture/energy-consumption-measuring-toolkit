# MergeSort in Python
from datetime import datetime 
import datetime 
import time
import os
import subprocess
import psutil
import platform
import numpy as np
import datetime as dt
from pyJoules.energy_meter import measure_energy
from pyJoules.handler.csv_handler import CSVHandler
from pyJoules.energy_meter import EnergyContext
from pyJoules.device.rapl_device import RaplPackageDomain
from pyJoules.device.nvidia_device import NvidiaGPUDomain

csv_handler = CSVHandler('mergesort_result.csv')

with EnergyContext(handler=csv_handler, start_tag='mergeSort') as ctx:
 def mergeSort(array):
    if len(array) > 1:

        #  r is the point where the array is divided into two subarrays
        r = len(array)//2
        L = array[:r]
        M = array[r:]

        # Sort the two halves
        mergeSort(L)
        mergeSort(M)

        i = j = k = 0

        # Until we reach either end of either L or M, pick larger among
        # elements L and M and place them in the correct position at A[p..r]
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1

        # When we run out of elements in either L or M,
        # pick up the remaining elements and put in A[p..r]
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1
            

# inner psutil function
def process_memory():
    process = psutil.Process(os.getpid())
    mem_info = process.memory_info()
    return mem_info.rss

# Print the array
def printList(array):
    for i in range(len(array)):
        print(array[i], end=" ")
        print()

def get_total_seconds(stringHMS):
   timedeltaObj = dt.datetime.strptime(stringHMS, "%H:%M:%S") - dt.datetime(1900,1,1)
   return timedeltaObj.total_seconds()        


# Driver program
with EnergyContext(handler=csv_handler, start_tag='sortingAlgorithms') as ctx:
 def sortingAlgorithms():
  if __name__ == '__main__':
    
    array = np.random.randint(1,500, 300000)
    startTime = (datetime.datetime.now().microsecond)*1000
    ctx.record(tag='process_memory')
    mem_before = process_memory() 
    
    print("Array size: ",len(array))
    ctx.record(tag='mergeSort')
    mergeSort(array)

    print("Array is Sorted")
    #printList(array)

    ctx.record(tag='process_memory') 
    mem_after = process_memory()
    
    print('Memory Usage',mem_after-mem_before)

    endTime = (datetime.datetime.now().microsecond)*1000
    timeinsec = (endTime - startTime)/1000000000
        
    execution_time = (endTime - startTime)*0.000000001 
    
    print('Algorithm execution time: ',(endTime - startTime)," ns ")
    cpu_after = psutil.cpu_percent()
    print('CPU Usage after is ',cpu_after )
         
    print(platform.uname())
    csv_handler.save_data()

# Call Function    
with EnergyContext(handler=csv_handler, start_tag='sortingAlgorithms') as ctx: 
 sortingAlgorithms()   
