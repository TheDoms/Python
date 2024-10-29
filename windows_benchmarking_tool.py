Python 3.12.1 (v3.12.1:2305ca5144, Dec  7 2023, 17:23:38) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import time
... import psutil
... import tkinter as tk
... from tkinter import messagebox
... 
... class BenchmarkApp:
...     def __init__(self, root):
...         self.root = root
...         self.root.title("PC Performance Benchmarking Tool")
... 
...         self.cpu_button = tk.Button(root, text="Run CPU Benchmark", command=self.cpu_benchmark)
...         self.cpu_button.pack(pady=10)
... 
...         self.memory_button = tk.Button(root, text="Run Memory Benchmark", command=self.memory_benchmark)
...         self.memory_button.pack(pady=10)
... 
...     def cpu_benchmark(self):
...         start_time = time.time()
...         for _ in range(10000000):
...             pass  # Simulate CPU workload
...         end_time = time.time()
...         cpu_score = end_time - start_time
...         messagebox.showinfo("CPU Benchmark", f"CPU Benchmark Time: {cpu_score:.2f} seconds")
... 
...     def memory_benchmark(self):
...         start_time = time.time()
...         memory_data = [0] * 10000000  # Simulate memory workload
...         memory_data = None  # Free up memory
...         end_time = time.time()
...         memory_score = end_time - start_time
...         messagebox.showinfo("Memory Benchmark", f"Memory Benchmark Time: {memory_score:.2f} seconds")
... 
... # Create the main window and start the GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = BenchmarkApp(root)
    root.mainloop()
