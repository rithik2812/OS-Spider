def safe(process, avail_res, max_res, alloc):
    num_process = len(process)  # number of processes
    num_resources = len(avail_res)  # number of resource types
    work = avail_res[:]  # work is list representing available resources
    complete = [False] * num_process  # track of fully allocated resources
    safe_sequence = []

    while len(safe_sequence) < num_process:  # runs until safe sequence is found
        allocated = False
        for i in range(num_process):
            if not complete[i]:  # considers processes that have not finished execution
                if all(max_res[i][j] - alloc[i][j] <= work[j] for j in range(num_resources)):  # remaining need of resource j for process i
                    for k in range(num_resources):
                        work[k] += alloc[i][k]  # allowing allocation
                    complete[i] = True  # process i has finished
                    safe_sequence.append(process[i])  # append process to safe sequence
                    allocated = True
        if not allocated:
            return False, []
    return True, safe_sequence  # if safe sequence is found
process=[0,1,2,3]
avail_res=[2,3,4]
max_res=[
[2,1,4],
[4,5,2],
[7,3,5],
[2,1,2]
]
alloc=[
[0, 1, 0],
[2, 0, 0],
[1, 0, 2],
[2, 0, 1]
]
safe, sequence = safe(process, avail_res, max_res, alloc)
if safe:
    print(f"system is in safe state Safe sequence: {sequence}")
else:
    print("system is not in safe state")


    #banker's algorithm is used
    #need matrix= max - allocation

