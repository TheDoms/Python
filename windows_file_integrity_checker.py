Python 3.12.1 (v3.12.1:2305ca5144, Dec  7 2023, 17:23:38) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
import hashlib
import tkinter as tk
from tkinter import filedialog, messagebox

class IntegrityCheckerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Integrity Checker")

...         self.file_button = tk.Button(root, text="Select File", command=self.select_file)
...         self.file_button.pack(pady=10)
... 
...         self.result_label = tk.Label(root, text="File: None")
...         self.result_label.pack(pady=10)
... 
...         self.checksum_button = tk.Button(root, text="Calculate Checksum", command=self.calculate_checksum)
...         self.checksum_button.pack(pady=10)
... 
...         self.result_text = tk.Text(root, height=5, width=50)
...         self.result_text.pack(pady=10)
... 
...         self.file_path = None
... 
...     def select_file(self):
...         self.file_path = filedialog.askopenfilename()
...         if self.file_path:
...             self.result_label.config(text=f"File: {self.file_path}")
... 
...     def calculate_checksum(self):
...         if self.file_path:
...             sha256_hash = hashlib.sha256()
...             with open(self.file_path, "rb") as f:
...                 # Read the file in chunks to handle large files
...                 for byte_block in iter(lambda: f.read(4096), b""):
...                     sha256_hash.update(byte_block)
...             checksum = sha256_hash.hexdigest()
...             self.result_text.delete(1.0, tk.END)
...             self.result_text.insert(tk.END, f"SHA-256 Checksum:\n{checksum}")
...         else:
...             messagebox.showerror("Error", "Please select a file first.")
... 
... # Create the main window and start the GUI
... if __name__ == "__main__":
...     root = tk.Tk()
...     app = IntegrityCheckerApp(root)
...     root.mainloop()
