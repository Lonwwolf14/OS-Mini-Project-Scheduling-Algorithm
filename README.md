# OS Mini Project: Scheduling Algorithm GUI

Welcome to the OS Mini Project repository! This project provides a graphical user interface (GUI) for simulating various process scheduling algorithms. From First-Come, First-Served (FCFS) to Priority and Round Robin, this tool allows you to visualize and analyze the performance of different scheduling techniques.

## How to Use

### Dependencies
- Python 3.x
- Tkinter (usually comes pre-installed with Python)

### Installing Tkinter (if not installed)
- **For Windows**: Tkinter usually comes pre-installed with Python. If not, you can install it using the following command:
  ```
  pip install tk
  ```

- **For Linux (Debian/Ubuntu)**: You can install Tkinter using the package manager:
  ```
  sudo apt-get install python3-tk
  ```

- **For macOS**: Tkinter comes pre-installed with Python on macOS.

### Running the Program
1. Clone this repository to your local machine.
2. Navigate to the directory where you have cloned the repository.
3. Open a terminal or command prompt.
4. Run the following command:

    ```
    python OS-Mini-Project-Scheduling-Algorithm.py
    ```

5. The GUI window should appear, ready for you to input the necessary parameters and select the scheduling algorithm you want to simulate.

### Input Parameters
- **Number of Processes**: Enter the total number of processes you want to simulate scheduling for.
- **Scheduling Algorithm**: Choose the desired algorithm from the drop-down menu (FCFS, SJF, SRTN, Priority, or Round Robin).
- **Quantum (for Round Robin)**: If you select the Round Robin algorithm, specify the time quantum.

For each process, you will need to enter the following details:
- **Arrival Time**: The time at which the process arrives in the system.
- **Burst Time**: The total time required by the process for execution.
- **Priority (optional)**: Priority of the process (only applicable for Priority scheduling).

### Submitting and Viewing Results
- Once you have entered all the necessary parameters, click the "Submit" button.
- The GUI will display the completion time, turnaround time, and waiting time for each process.
- Scroll down in the result display area to see the detailed results, including average turnaround time and average waiting time.

## About the Algorithms

### Implemented Algorithms
1. **FCFS (First-Come, First-Served)**
2. **SJF (Shortest Job First)**
3. **SRTN (Shortest Remaining Time Next)**
4. **Priority Scheduling**
5. **Round Robin**

## Contributors
- Anuj Koli
- Raviraj Parab
- Rahul Shelke
- Ayush Devre
- Sahil Patil
- Vedant Shelar

Feel free to contribute to this project by adding new features, improving existing algorithms, or enhancing the GUI!

Enjoy exploring the fascinating world of process scheduling algorithms with our intuitive GUI tool! If you have any questions or suggestions, feel free to reach out. Happy scheduling! 🚀