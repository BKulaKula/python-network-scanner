import socket
import tkinter as tk
from tkinter import messagebox

# Scan function

def scan():
    host = entry.get()

    output.delete("1.0", tk.END)

    ports = [21, 22, 80, 443]

    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((host, port))

        if result == 0:
            output.insert(tk.END, f"OPEN: Port {port},	")

        sock.close()

# GUI Window
root = tk.Tk()
root.title("Python Network Scanner")
root.geometry("500x400")

label = tk.Label(root, text="Target IP")
label.pack()

entry = tk.Entry(root, width=40)
entry.pack()

button = tk.Button(root, text="Scan", command=scan)
button.pack()

output = tk.Text(root, height=20, width=60)
output.pack()

root.mainloop()
