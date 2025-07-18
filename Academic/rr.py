<<<<<<< HEAD
class Process:
    def __init__(self, pid, burst):
        self.pid = pid
        self.burst = burst
        self.waiting = 0
        self.turnaround = 0
        self.remaining = burst


class Round_Robin:
    def __init__(self, processes, quantum):
        self.processes = processes
        self.avg_waiting = 0
        self.avg_turnaround = 0
        self.quantum = quantum
        self.time = 0
    
    
    def roundRobin(self):
        processes_queue = [process for process in self.processes]
        while processes_queue:
            process = processes_queue.pop(0)
            if process.remaining > self.quantum:
                self.time += self.quantum
                process.remaining -= self.quantum
                processes_queue.append(process)
            else:
                self.time += process.remaining
                process.remaining = 0
                process.waiting = self.time - process.burst
                process.turnaround = self.time

        for process in self.processes:
            self.avg_waiting += process.waiting
            self.avg_turnaround += process.turnaround

        self.avg_waiting /= len(self.processes)
        self.avg_turnaround /= len(self.processes)


if __name__ == '__main__':
    pids = [1, 2, 3]
    bursts = [10, 5, 8]
    quantum = 2

    processes = []
    for i in range(len(pids)):
        processes.append(Process(pids[i], bursts[i]))

    roundRobin = Round_Robin(processes, quantum)
    roundRobin.roundRobin()

    print(f"{'Process':<10}{'Burst':<10}{'Waiting':<10}{'Turnaround':<10}")
    for x in range(0, len(processes)):
        print(f"{roundRobin.processes[x].pid:<10}{roundRobin.processes[x].burst:<10}{roundRobin.processes[x].waiting:<10}{roundRobin.processes[x].turnaround:<10}")
=======
class Process:
    def __init__(self, pid, burst):
        self.pid = pid
        self.burst = burst
        self.waiting = 0
        self.turnaround = 0
        self.remaining = burst


class Round_Robin:
    def __init__(self, processes, quantum):
        self.processes = processes
        self.avg_waiting = 0
        self.avg_turnaround = 0
        self.quantum = quantum
        self.time = 0
    
    
    def roundRobin(self):
        processes_queue = [process for process in self.processes]
        while processes_queue:
            process = processes_queue.pop(0)
            if process.remaining > self.quantum:
                self.time += self.quantum
                process.remaining -= self.quantum
                processes_queue.append(process)
            else:
                self.time += process.remaining
                process.remaining = 0
                process.waiting = self.time - process.burst
                process.turnaround = self.time

        for process in self.processes:
            self.avg_waiting += process.waiting
            self.avg_turnaround += process.turnaround

        self.avg_waiting /= len(self.processes)
        self.avg_turnaround /= len(self.processes)


if __name__ == '__main__':
    pids = [1, 2, 3]
    bursts = [10, 5, 8]
    quantum = 2

    processes = []
    for i in range(len(pids)):
        processes.append(Process(pids[i], bursts[i]))

    roundRobin = Round_Robin(processes, quantum)
    roundRobin.roundRobin()

    print(f"{'Process':<10}{'Burst':<10}{'Waiting':<10}{'Turnaround':<10}")
    for x in range(0, len(processes)):
        print(f"{roundRobin.processes[x].pid:<10}{roundRobin.processes[x].burst:<10}{roundRobin.processes[x].waiting:<10}{roundRobin.processes[x].turnaround:<10}")
>>>>>>> 0c671102c36e5cae888f5b6261083eeba2ab0952
    print(f" Average Waiting Time: {roundRobin.avg_waiting} \n Average Turnaround Time: {roundRobin.avg_turnaround} ")