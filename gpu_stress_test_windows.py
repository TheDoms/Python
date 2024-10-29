Python 3.12.1 (v3.12.1:2305ca5144, Dec  7 2023, 17:23:38) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
import tensorflow as tf
import time
import tkinter as tk
from tkinter import ttk

# Ensure that TensorFlow is using the GPU (CUDA backend)
physical_devices = tf.config.list_physical_devices('GPU')
if len(physical_devices) > 0:
    tf.config.experimental.set_memory_growth(physical_devices[0], True)
    print(f"Running on GPU: {physical_devices[0]}")
else:
    print("No GPU found. Running on CPU.")

# Function to stress the GPU by performing large matrix multiplications
def stress_gpu(duration=30):
    # Create two large random matrices
    matrix_size = 10000  # Increase the size for more stress
    a = tf.random.normal((matrix_size, matrix_size))
    b = tf.random.normal((matrix_size, matrix_size))

    start_time = time.time()
    iteration = 0

    while time.time() - start_time < duration:
        # Perform matrix multiplication (heavy on the GPU)
        c = tf.matmul(a, b)
        iteration += 1

    return iteration

# GUI Application Class
class GPUStressTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("GPU Stress Test")

        # Duration variable
        self.duration_var = tk.IntVar(value=30)

        # Set up the UI elements
        self.label = tk.Label(root, text="GPU Stress Test Duration (seconds):")
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

...         # Label to show results
...         self.results_label = tk.Label(root, text="Results: No results yet")
...         self.results_label.pack(pady=10)
... 
...         self.running = False
... 
...     def update_progress(self, iteration):
...         self.progress_label.config(text=f"Progress: {iteration} matrix multiplications completed")
... 
...     def start_test(self):
...         self.running = True
...         duration = self.duration_var.get()
...         self.progress_bar['value'] = 0
... 
...         self.progress_label.config(text="Test running...")
...         self.results_label.config(text="Results: Calculating...")
... 
...         # Start the stress test
...         self.root.after(100, self.run_gpu_stress_test, duration)
... 
...     def run_gpu_stress_test(self, duration):
...         if self.running:
...             iteration = stress_gpu(duration)
...             self.update_progress(iteration)
...             self.results_label.config(text=f"Results: {iteration} matrix multiplications in {duration} seconds.")
... 
...     def stop_test(self):
...         self.running = False
...         self.progress_label.config(text="Test stopped.")
...         self.progress_bar['value'] = 0
...         self.results_label.config(text="Test stopped.")
... 
... # Create the main window and start the GUI
... if __name__ == "__main__":
...     root = tk.Tk()
...     app = GPUStressTestApp(root)
...     root.mainloop()
