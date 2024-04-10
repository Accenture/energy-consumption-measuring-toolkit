import platform
import numpy as np
import datetime 
import time
import psutil
import os
from pyJoules.energy_meter import measure_energy
from pyJoules.handler.csv_handler import CSVHandler
from pyJoules.energy_meter import EnergyContext
from pyJoules.device.rapl_device import RaplPackageDomain
from pyJoules.device.nvidia_device import NvidiaGPUDomain

csv_handler = CSVHandler('bubblesort_result.csv')

#main function
with EnergyContext(handler=csv_handler, start_tag='sortingAlgorithms') as ctx:
 def sortingAlgorithms():
  
  data = np.random.randint(1,500, 60000)
  size = len(data)
  print("Array length: ",size)

  startTime = (datetime.datetime.now().microsecond)*1000
  ctx.record(tag='processmemory')
  mem_before = process_memory() 
  ctx.record(tag='bubbleSort')
  bubbleSort(data)

  print('Sorted Array in Ascending Order:')
  #print(data)
  ctx.record(tag='processmemory')
  mem_after = process_memory()
  print("{}:consumed memory: {:,}".format(mem_before, mem_after, mem_after - mem_before))
  
  endTime = (datetime.datetime.now().microsecond)*1000
  timeinsec = (endTime - startTime)/1000000000
  print('Algorithm execution time', (endTime - startTime), 'ns')

  cpu_after = psutil.cpu_percent()
  print('CPU Usage after is ',cpu_after )

  print(platform.uname())
  
  csv_handler.save_data()
 
# inner psutil function
def process_memory():
    process = psutil.Process(os.getpid())
    mem_info = process.memory_info()
    return mem_info.rss

with EnergyContext(handler=csv_handler, start_tag='bubbleSort') as ctx:    
 def bubbleSort(array):
  print('Initiating BubbleSort Algo: ')  
  # loop to access each array element
  for i in range(len(array)):

    # loop to compare array elements
    for j in range(0, len(array) - i - 1):

      # compare two adjacent elements
      # change > to < to sort in descending order
      if array[j] > array[j + 1]:

        # swapping elements if elements
        # are not in the intended order
        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp     

with EnergyContext(handler=csv_handler, start_tag='sortingAlgorithms') as ctx: 
 sortingAlgorithms() 
