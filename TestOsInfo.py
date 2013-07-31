import OsInfo

print "System Info"
print "-----------"
osi=OsInfo.OsInfo()
print
print "Memory Info"
print "------------------"
print "Total: ", osi.GetTotalMemory(), "MB"
print "Used : ", osi.GetUsedMemory(), "MB"
print "Free : ", osi.GetAvailableMemory(), "MB"
print
print "SWAP Info"
print "---------"
print "Total: ", osi.GetTotalSwap(), "MB"
print "Used : ", osi.GetUsedSwap(), "MB"
print "Free : ", osi.GetAvailableSwap(), "MB"
print
print "CPU Info"
print "--------"
print "CPU  : ", 100 - osi.GetFreeCPU(), "%"
print

