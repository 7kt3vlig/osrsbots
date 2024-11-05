import tkinter as tk

def on_button_click():
    print("Button clicked!")

root = tk.Tk()
root.title("My App")

button = tk.Button(root, text="Click Me!", command=on_button_click)
button.pack()

root.mainloop()