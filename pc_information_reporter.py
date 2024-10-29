Python 3.12.1 (v3.12.1:2305ca5144, Dec  7 2023, 17:23:38) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
import platform
import psutil
... import tkinter as tk
... from tkinter import filedialog
... 
... class SystemInfoApp:
...     def __init__(self, root):
...         self.root = root
...         self.root.title("System Info Reporter")
... 
...         self.report_button = tk.Button(root, text="Generate System Report", command=self.generate_report)
...         self.report_button.pack(pady=10)
... 
...     def generate_report(self):
...         system_info = f"""
...         System: {platform.system()}
...         Node Name: {platform.node()}
...         OS Version: {platform.version()}
...         Machine: {platform.machine()}
...         Processor: {platform.processor()}
...         CPU Cores: {psutil.cpu_count(logical=False)}
...         Logical CPUs: {psutil.cpu_count(logical=True)}
...         RAM: {psutil.virtual_memory().total / (1024 ** 3):.2f} GB
...         Disk Usage: {psutil.disk_usage('/').percent}%
...         """
... 
...         save_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
...         if save_path:
...             with open(save_path, 'w') as f:
...                 f.write(system_info)
... 
...             tk.messagebox.showinfo("Report Saved", f"System report saved to {save_path}")
... 
... # Create the main window and start the GUI
... if __name__ == "__main__":
...     root = tk.Tk()
...     app = SystemInfoApp(root)
...     root.mainloop()
