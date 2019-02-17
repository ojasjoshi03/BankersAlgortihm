# Bankers-Algorithm
The Banker algorithm, sometimes referred to as the detection algorithm, is a resource allocation and deadlock avoidance algorithm developed by Edsger Dijkstra that tests for safety by simulating the allocation of predetermined maximum possible amounts of all resources, and then makes an "s-state" check to test for possible deadlock conditions for all other pending activities, before deciding whether allocation should be allowed to continue.


For the Banker's algorithm to work, it needs to know three things:

1) How much of each resource each process could possibly request[MAX]

2) How much of each resource each process is currently holding[ALLOCATED]

3) How much of each resource the system currently has available[AVAILABLE]

Resources may be allocated to a process only if the amount of resources requested is less than or equal to the amount available; otherwise, the process waits until resources are available.


Currently There are 2 ways that I know to Implement Bankers Algorithm
1) Python ( Using Numpy Library)
2) C language code ( Simple but lengthy)
