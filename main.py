import tkinter as tk

root = tk.Tk()
root.geometry("800x800")
root.title("Tkinter Example")

buttonframe = tk.Frame(root)

for i in range(20):
    buttonframe.columnconfigure(i, weight=1, minsize=30) 
    buttonframe.rowconfigure(i, weight=1, minsize=30)


def on_button_click(row, col):
    print(f"Button clicked at: ({row}, {col})")


for row in range(20):
    for col in range(20):
        button = tk.Button(buttonframe, text=f"({row},{col})", font=('Times New Roman', 8),
                           width=2, height=1,  
                           command=lambda r=row, c=col: on_button_click(r, c))
        button.grid(row=row, column=col, sticky="nsew", padx=1, pady=1)  


buttonframe.pack(fill='both', expand=True)

root.mainloop()

#poop