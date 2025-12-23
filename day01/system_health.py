import psutil

def check_cpu_threshold():
    cpu_threshold = int (input("Enter the CPU threshold: "))

    current_cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    print ("CPU Uage % is: ",current_cpu_usage)
    print ("Memory Uage % is: ",memory_info.percent)

    if current_cpu_usage > cpu_threshold:
        print ("CPU usage is HIGH")
    else:
        print("CPU usage is NORMAL")

check_cpu_threshold()