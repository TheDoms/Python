Python 3.12.1 (v3.12.1:2305ca5144, Dec  7 2023, 17:23:38) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
import time
import multiprocessing
import tkinter as tk
from tkinter import ttk

# Function to perform extremely CPU-intensive task (prime number calculation)
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Heavier CPU task: calculating a high range of prime numbers
def stress_cpu(n):
    count = 0
    for i in range(2, n):
        if is_prime(i):
            count += 1
    return count  # Return the number of primes found

# Class for the GUI Application
class CPUStressTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Maximum CPU Stress Test")

        # Duration variable
        self.duration_var = tk.IntVar(value=30)

        # Set up the UI elements
        self.label = tk.Label(root, text="CPU Stress Test Duration (seconds):")
        self.label.pack(pady=10)

        self.duration_entry = tk.Entry(root, textvariable=self.duration_var)
        self.duration_entry.pack(pady=5)

        self.start_button = tk.Button(root, text="Start Test", command=self.start_test)
        self.start_button.pack(pady=10)

        self.stop_button = tk.Button(root, text="Stop Test", command=self.stop_test)
        self.stop_button.pack(pady=10)

        self.progress_label = tk.Label(root, text="Progress: Not started")
        self.progress_label.pack(pady=10)

        self.progress_bar = ttk.Progressbar(root, length=300, mode='determinate')
        self.progress_bar.pack(pady=10)

        # Label to show results
        self.results_label = tk.Label(root, text="Results: No results yet")
        self.results_label.pack(pady=10)

        self.running = False
        self.pool = None
        self.total_primes = 0  # To store the total number of primes found

    def update_progress(self, iteration, total_iterations):
        progress_percentage = (iteration / total_iterations) * 100
        self.progress_label.config(text=f"Progress: {iteration} iterations completed")
        self.progress_bar['value'] = progress_percentage

    def start_test(self):
        self.running = True
        duration = self.duration_var.get()
        self.total_iterations = duration * multiprocessing.cpu_count()
        self.progress_bar['value'] = 0
        self.total_primes = 0  # Reset prime counter

        self.pool = multiprocessing.Pool(multiprocessing.cpu_count())
        self.progress_label.config(text="Test running...")
        self.results_label.config(text="Results: Calculating...")

        # Start the stress test
        self.start_time = time.time()
        self.iteration = 0
        self.run_cpu_stress_test(duration)

    def run_cpu_stress_test(self, duration):
        # Keep running until time is up or manually stopped
        if self.running and time.time() - self.start_time < duration:
            self.iteration += 1
...             # Run a very heavy CPU task with an extremely large range
...             self.pool.apply_async(stress_cpu, args=(1000000,), callback=self.after_iteration)  # Larger number for more load
...             self.root.after(10, self.run_cpu_stress_test, duration)
...         elif self.running:
...             self.stop_test()
...             self.progress_label.config(text="Test completed.")
...             self.results_label.config(
...                 text=f"Results: {self.total_primes} prime numbers found in {self.iteration} iterations."
...             )
... 
...     def after_iteration(self, result):
...         # Update the total number of primes found after each iteration
...         if self.running:
...             self.total_primes += result
...             self.update_progress(self.iteration, self.total_iterations)
... 
...     def stop_test(self):
...         self.running = False
...         if self.pool:
...             self.pool.terminate()
...             self.pool.join()
...         self.progress_label.config(text="Test stopped.")
...         self.progress_bar['value'] = 0
...         self.results_label.config(
...             text=f"Results: {self.total_primes} prime numbers found in {self.iteration} iterations."
...         )
... 
... # Create the main window and start the GUI
... if __name__ == "__main__":
...     # On Windows, we need to set the start method for multiprocessing to 'spawn'
...     if multiprocessing.get_start_method() != 'spawn':
...         multiprocessing.set_start_method('spawn')
...     
...     root = tk.Tk()
...     app = CPUStressTestApp(root)
...     root.mainloop()
