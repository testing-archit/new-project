import tkinter as tk
from tkinter import ttk
import pyautogui
import time

def type_text(text):
    pyautogui.typewrite(text, interval=0.000001)  # Decrease interval for faster typing

def get_input_and_type():
    text = input_text.get("1.0", "end-1c") 
    if text:
        time.sleep(5)
        type_text(text)
    
root = tk.Tk()
root.title("Text Typer")
root.geometry("400x250") 
root.configure(bg="#4B0082") 

canvas = tk.Canvas(root, background="#4B0082")
canvas.pack(fill="both", expand=True)

top_frame = ttk.Frame(canvas, style='Background.TFrame') 
top_frame.pack(fill="both", expand=True)

style = ttk.Style()
style.configure('Background.TFrame', background='#4B0082')

input_label = ttk.Label(top_frame, text="Enter text:", background="#4B0082", foreground="white")
input_label.pack()

input_text = tk.Text(top_frame, width=40, height=10) 
input_text.pack(pady=10) 

type_button = ttk.Button(top_frame, text="Type Text", command=get_input_and_type)
type_button.pack()

root.mainloop()
