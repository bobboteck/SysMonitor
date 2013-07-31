import os
""" This is a simple object used to return information of system using, based on Linux command require sysstat installed for the CPU information """
class OsInfo():
    
    def __init__(self):
        pass
    """ Return the amount of total system memory """
    def GetTotalMemory(self):
        memoryInfo = os.popen("free -m").readlines()
        totalMemory = memoryInfo[1].split()[1]
        return int(totalMemory)
    """ Return the amount of available system memory """
    def GetAvailableMemory(self):
        memoryInfo = os.popen("free -m").readlines()
        freeMemory = memoryInfo[1].split()[3]
        return int(freeMemory)
	""" Return the amount of used system memory """
    def GetUsedMemory(self):
        memoryInfo = os.popen("free -m").readlines()
        usedMemory = memoryInfo[1].split()[2]
        return int(usedMemory)
    """ Return the amount of total system SWAP """
    def GetTotalSwap(self):
        memoryInfo = os.popen("free -m").readlines()
        totalSwap = memoryInfo[3].split()[1]
        return int(totalSwap)
    """ Return the amount of available system SWAP """
    def GetAvailableSwap(self):
        memoryInfo = os.popen("free -m").readlines()
        freeSwap = memoryInfo[3].split()[3]
        return int(freeSwap)
    """ Return the amount of used system SWAP """
    def GetUsedSwap(self):
        memoryInfo = os.popen("free -m").readlines()
        usedSwap = memoryInfo[3].split()[2]
        return int(usedSwap)
    """ Return the amount of idle CPU """
    def GetFreeCPU(self):
        cpuFree = os.popen("mpstat").readlines()[3].split()[10]
        return float(cpuFree.replace(",","."))

