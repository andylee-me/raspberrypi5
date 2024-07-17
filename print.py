import time
import psutil

def get_cpu_temp():
    temp = psutil.sensors_temperatures()['cpu_thermal'][0].current
    return temp
  
print(get_cpu_temp())
time.sleep(1)
