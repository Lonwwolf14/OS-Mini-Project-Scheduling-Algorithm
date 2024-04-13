import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np

class Process:
    def __init__(self, pid, arrival_time, burst_time, priority):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0
        self.priority = priority

def fcfs(processes):
    """
    Perform FCFS (First-Come, First-Served) scheduling on the given list of processes.

    Args:
    - processes: A list of Process objects representing the processes to be scheduled.

    Returns:
    None. The completion time, turnaround time, and waiting time for each process are updated in-place.
    """
    time = 0
    for process in processes:
        if process.arrival_time > time:
            time = process.arrival_time
        process.completion_time = time + process.burst_time
        process.turnaround_time = process.completion_time - process.arrival_time
        process.waiting_time = process.turnaround_time - process.burst_time
        time = process.completion_time

def print_results(processes):
    total_waiting_time = sum(process.waiting_time for process in processes)
    total_turnaround_time = sum(process.turnaround_time for process in processes)
    avg_waiting_time = total_waiting_time / len(processes)
    avg_turnaround_time = total_turnaround_time / len(processes)

    output_text = "Process\tAT\tBT\tCT\tTAT\tWT\n"
    for process in processes:
        output_text += f"{process.pid}\t{process.arrival_time}\t{process.burst_time}\t{process.completion_time}\t{process.turnaround_time}\t{process.waiting_time}\n"
    output_text += f"\nAverage TAT: {avg_turnaround_time:.2f}\n"
    output_text += f"Average WT: {avg_waiting_time:.2f}\n"

    result_text.delete(1.0, tk.END)  # Clear the existing text
    result_text.insert(tk.END, output_text)  # Insert new output text

    # Plot Gantt Chart
    fig, ax = plt.subplots()

    # Initialize colors for each process
    colors = ['skyblue', 'salmon', 'lightgreen', 'orchid', 'lightcoral', 'lightskyblue', 'palegreen', 'mediumorchid', 'lightpink', 'lightgrey']

    # Setting the y-axis limits
    ax.set_ylim(0.5, len(processes) + 0.5)

    # Plotting Gantt Chart bars
    for i, process in enumerate(processes):
        ax.barh(i + 1, process.completion_time - process.arrival_time, left=process.arrival_time, align='center', color=colors[i % len(colors)])
        ax.text(process.arrival_time + (process.completion_time - process.arrival_time) / 2, i + 1, f'P{process.pid}', ha='center', va='center', color='black')

    ax.set_xlabel('Time')
    ax.set_ylabel('Processes')
    ax.set_title('Gantt Chart')
    
    # Hide the y-axis ticks and labels
    ax.yaxis.set_visible(False)

    plt.grid(True)
    plt.show()

def sjf(processes):
    # Sort processes based on arrival time and burst time
    processes.sort(key=lambda x: (x.arrival_time, x.burst_time))
    time = 0  # Current time
    remaining_processes = processes.copy()  # Create a copy of processes

    while remaining_processes:
        # Filter processes that have arrived by the current time
        arrived_processes = [p for p in remaining_processes if p.arrival_time <= time]

        # If no processes have arrived yet, move time to the arrival time of the next process
        if not arrived_processes:
            time = remaining_processes[0].arrival_time
            continue

        # Select the process with the shortest burst time among the arrived processes
        shortest_process = min(arrived_processes, key=lambda x: x.burst_time)

        # Update time and process details
        time += shortest_process.burst_time
        shortest_process.completion_time = time
        shortest_process.turnaround_time = shortest_process.completion_time - shortest_process.arrival_time
        shortest_process.waiting_time = shortest_process.turnaround_time - shortest_process.burst_time

        # Remove the completed process from the list of remaining processes
        remaining_processes.remove(shortest_process)


def srt(processes):
    time = 0
    remaining_processes = processes.copy()
    while remaining_processes:
        remaining_processes.sort(key=lambda x: (x.arrival_time, x.burst_time))  # STEP 1: Sort by arrival time and burst time
        shortest_process = None
        for process in remaining_processes:
            if process.arrival_time <= time:
                if shortest_process is None or process.burst_time < shortest_process.burst_time:
                    shortest_process = process
        if shortest_process is None:  # No process arrived until the current time
            time += 1
            continue
        shortest_process.remaining_time -= 1  # STEP 2: Process the shortest remaining time process for 1 unit
        time += 1
        if shortest_process.remaining_time == 0:  # Process completed
            shortest_process.completion_time = time
            shortest_process.turnaround_time = shortest_process.completion_time - shortest_process.arrival_time
            shortest_process.waiting_time = shortest_process.turnaround_time - shortest_process.burst_time
            remaining_processes.remove(shortest_process)  # Remove completed process

    return processes


def swap(a, b):
    temp = a
    a = b
    b = temp

def priority(processes):
    n = len(processes)
    # Sort processes by arrival time and priority
    processes.sort(key=lambda x: (x.arrival_time, x.priority))
    
    completion_time = float('inf')  # Initialize completion time to infinity

    # If all the processes arrive at different times
    if processes:
        for i in range(n):
            # If current completion time is less than arrival time, update it
            if completion_time < processes[i].arrival_time:
                completion_time = processes[i].arrival_time
            
            # Waiting time for the current process
            processes[i].waiting_time = max(0, completion_time - processes[i].arrival_time)
            
            # Completion time of the current process
            completion_time += processes[i].burst_time
            processes[i].turnaround_time = processes[i].completion_time - processes[i].arrival_time

             # Waiting time for the current process
            processes[i].waiting_time = processes[i].turnaround_time - processes[i].burst_time

    return processes

def round_robin(processes, quantum):
    if quantum <= 0:
        raise ValueError("Quantum must be a positive integer")

    remaining_processes = processes.copy()
    time = 0

    while remaining_processes:
        for process in remaining_processes:
            if process.remaining_time > 0:
                # Execute the process for the time quantum or its remaining time
                execution_time = min(process.remaining_time, quantum)
                process.remaining_time -= execution_time
                time += execution_time

                # Check if the process has completed
                if process.remaining_time == 0:
                    process.completion_time = time

        # Remove completed processes
        remaining_processes = [p for p in remaining_processes if p.remaining_time > 0]

    # Calculate waiting time and turnaround time
    for process in processes:
        process.turnaround_time = process.completion_time - process.arrival_time
        process.waiting_time = process.turnaround_time - process.burst_time


def print_results(processes):
    total_waiting_time = sum(process.waiting_time for process in processes)
    total_turnaround_time = sum(process.turnaround_time for process in processes)
    avg_waiting_time = total_waiting_time / len(processes)
    avg_turnaround_time = total_turnaround_time / len(processes)

    output_text = "Process\tAT\tBT\tCT\tTAT\tWT\n"
    for process in processes:
        output_text += f"{process.pid}\t{process.arrival_time}\t{process.burst_time}\t{process.completion_time}\t{process.turnaround_time}\t{process.waiting_time}\n"
    output_text += f"\nAverage TAT: {avg_turnaround_time:.2f}\n"
    output_text += f"Average WT: {avg_waiting_time:.2f}\n"

    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, output_text)

    fig, ax = plt.subplots()

    colors = ['skyblue', 'salmon', 'lightgreen', 'orchid', 'lightcoral', 'lightskyblue', 'palegreen', 'mediumorchid', 'lightpink', 'lightgrey']

    ax.set_ylim(0.5, len(processes) + 0.5)

    for i, process in enumerate(processes):
        ax.barh(i + 1, process.completion_time - process.arrival_time, left=process.arrival_time, align='center', color=colors[i % len(colors)])
        ax.text(process.arrival_time + (process.completion_time - process.arrival_time) / 2, i + 1, f'P{process.pid}', ha='center', va='center', color='black')

    ax.set_xlabel('Time')
    ax.set_ylabel('Processes')
    ax.set_title('Gantt Chart')
    ax.yaxis.set_visible(False)

    plt.grid(True)
    plt.show()



def update_priority_display():
    if scheduling_algorithm.get() == "Priority":
        priority_label.grid(row=3, column=2, padx=10, pady=5, sticky="w")
        for entry in priority_entries:
            entry.grid()
    else:
        priority_label.grid_remove()
        for entry in priority_entries:
            entry.grid_remove()

def submit_processes():
    try:
        processes = []
        for i in range(int(num_processes_entry.get())):
            pid = i + 1
            arrival_time = int(arrival_entries[i].get())
            burst_time = int(burst_entries[i].get())
            priority_value = int(priority_entries[i].get()) if priority_entries else 0
            processes.append(Process(pid, arrival_time, burst_time, priority_value))

        if scheduling_algorithm.get() == "FCFS":
            fcfs(processes)
        elif scheduling_algorithm.get() == "SJF":
            sjf(processes)
        elif scheduling_algorithm.get() == "SRTN":
            srt(processes)
        elif scheduling_algorithm.get() == "Priority":
            priority(processes)
        elif scheduling_algorithm.get() == "Round Robin":
            quantum = int(quantum_entry.get())
            round_robin(processes, quantum)

        print_results(processes)
    except ValueError as e:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, str(e))
    except IndexError:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Error: Please make sure to fill in all process details.")
    except Exception as e:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "An error occurred: " + str(e))

def clear_inputs():
    for entry in arrival_entries:
        entry.delete(0, tk.END)
    for entry in burst_entries:
        entry.delete(0, tk.END)
    for entry in priority_entries:
        entry.delete(0, tk.END)
    result_text.delete(1.0, tk.END)

# GUI setup
root = tk.Tk()
root.title("Process Scheduling")
root.geometry("800x600")
root.resizable(True, True)

style = ttk.Style()
style.configure("TFrame", background="#f0f0f0")
style.configure("TButton", background="#4caf50", foreground="black", font=("Arial", 10, "bold"))
style.configure("TLabel", background="#f0f0f0", font=("Arial", 10))

# Input frame
input_frame = ttk.Frame(root)
input_frame.pack(fill=tk.BOTH, expand=True)

# Output frame
output_frame = ttk.Frame(root)
output_frame.pack(fill=tk.BOTH, expand=True)

# Title label
title_label = ttk.Label(input_frame, text="Process Scheduling", font=("Arial", 16, "bold"))
title_label.grid(row=0, column=0, columnspan=4, padx=10, pady=5)

# Number of processes
num_processes_label = ttk.Label(input_frame, text="Number of Processes:")
num_processes_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
num_processes_entry = ttk.Entry(input_frame)
num_processes_entry.grid(row=1, column=1, padx=10, pady=5)

# Scheduling algorithm
algorithm_label = ttk.Label(input_frame, text="Scheduling Algorithm:")
algorithm_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
scheduling_algorithm = ttk.Combobox(input_frame, values=["FCFS", "SJF", "SRTN", "Priority", "Round Robin"])
scheduling_algorithm.grid(row=2, column=1, padx=10, pady=5, sticky="w")
scheduling_algorithm.bind("<<ComboboxSelected>>", lambda e: update_priority_display())

# Quantum (for Round Robin)
quantum_label = ttk.Label(input_frame, text="Quantum (for Round Robin):")
quantum_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
quantum_entry = ttk.Entry(input_frame)
quantum_entry.grid(row=3, column=1, padx=10, pady=5, sticky="w")

# Process arrival, burst, and priority times
arrival_label = ttk.Label(input_frame, text="Arrival Time")
arrival_label.grid(row=4, column=0, padx=10, pady=5)
burst_label = ttk.Label(input_frame, text="Burst Time")
burst_label.grid(row=4, column=1, padx=10, pady=5)
priority_label = ttk.Label(input_frame, text="Priority")
priority_label.grid(row=4, column=2, padx=10, pady=5)

arrival_entries = []
burst_entries = []
priority_entries = []

def update_process_entries():
    for entry in arrival_entries + burst_entries + priority_entries:
        entry.grid_forget()

    arrival_entries.clear()
    burst_entries.clear()
    priority_entries.clear()

    for i in range(int(num_processes_entry.get())):
        arrival_entry = ttk.Entry(input_frame)
        arrival_entry.grid(row=i + 5, column=0, padx=10, pady=5, sticky="e")
        arrival_entries.append(arrival_entry)

        burst_entry = ttk.Entry(input_frame)
        burst_entry.grid(row=i + 5, column=1, padx=10, pady=5, sticky="w")
        burst_entries.append(burst_entry)

        if scheduling_algorithm.get() == "Priority":
            priority_entry = ttk.Entry(input_frame)
            priority_entry.grid(row=i + 5, column=2, padx=10, pady=5, sticky="w")
            priority_entries.append(priority_entry)

num_processes_entry.bind("<FocusOut>", lambda _: update_process_entries())

# Submit and Clear buttons
submit_button = ttk.Button(input_frame, text="Submit", command=submit_processes)
submit_button.grid(row=1, column=3, padx=10, pady=5, sticky="e")
clear_button = ttk.Button(input_frame, text="Clear", command=clear_inputs)
clear_button.grid(row=2, column=3, padx=10, pady=5, sticky="e")

# Result display
result_text = tk.Text(output_frame, wrap=tk.WORD, height=20, width=70)
result_text.pack(side=tk.BOTTOM, padx=10, pady=10, fill=tk.BOTH, expand=True)

# Scrollbar for result display
scrollbar = ttk.Scrollbar(output_frame, orient="vertical", command=result_text.yview)
scrollbar.pack(side=tk.RIGHT, fill="y")
result_text.config(yscrollcommand=scrollbar.set)

root.mainloop()
