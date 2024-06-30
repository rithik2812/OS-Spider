
class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.waiting_time = 0
        self.turnaround_time = 0

def fifo_schedule(processes):
    total_processes = len(processes)  # calculates total number of processes
    current_time = 0
    total_waiting_time = 0
    total_turnaround_time = 0

    print("Processes\tBurst Time\tWaiting Time\tTurnaround Time")

    for process in processes:  # iterates
        if process.arrival_time > current_time:
            current_time = process.arrival_time

        process.waiting_time = current_time - process.arrival_time  # waiting time = current time - arrival time
        process.turnaround_time = process.waiting_time + process.burst_time  # turnaround time = burst time + waiting time

        total_waiting_time += process.waiting_time
        total_turnaround_time += process.turnaround_time
        current_time += process.burst_time

        print(f"{process.pid}\t\t{process.burst_time}\t\t{process.waiting_time}\t\t{process.turnaround_time}")

    average_waiting_time = total_waiting_time / total_processes
    average_turnaround_time = total_turnaround_time / total_processes
    return average_waiting_time, average_turnaround_time

if __name__ == "__main__":
    processes = []

   
    num_processes = int(input("Enter number of processes: "))

    for i in range(num_processes):
        pid = int(input(f"Enter PID for process {i + 1}: "))
        arrival_time = int(input(f"Enter arrival time for process {i + 1}: "))
        burst_time = int(input(f"Enter burst time for process {i + 1}: "))
        processes.append(Process(pid, arrival_time, burst_time))

    average_waiting_time, average_turnaround_time = fifo_schedule(processes)

    print("\nAverage Waiting Time:", average_waiting_time)
    print("Average Turnaround Time:", average_turnaround_time)
