# import time

# fetchInterval = 15
# fetchfromStrart = 129600
# fetchdataFrom = 0

# ct = int(time.time())*1000
# fetchincidentUntil = ct-(fetchInterval*60000)
# fetchIncidentFromStart = ct - (fetchfromStrart*60000)

# print(ct)
# print(fetchincidentUntil)
# print(fetchIncidentFromStart)

# import sys and its usage

import sys

print(sys.version)

# total arguments

n = len(sys.argv)
print("Total arguments passed:", n)

# Arguments passed
print("\nName of Python script: ", sys.argv[0])

print("\n Arguments passed:", end=" ")
for i in range(1, n):
    print(sys.argv[i], end=" ")

# addition of numbers
sum = 0
for i in range(1, n):
    sum += int(sys.argv[i])

print("\n\n Result:", sum)

print(sys.builtin_module_names)
