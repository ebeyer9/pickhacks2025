import tkinter as tk

root = tk.Tk()
height= root.winfo_screenwidth()
width= root.winfo_screenheight()
root.geometry('%dx%d+0+0' % (width,height))
root.title("Minesweeper")

buttonframe = tk.Frame(root)

for i in range(20):
    buttonframe.columnconfigure(i, weight=1, minsize=30) 
    buttonframe.rowconfigure(i, weight=1, minsize=30)


def on_left_click(row, col):
    print(f"Left click at: ({row}, {col})")
def on_right_click(event, row, col):
    print(f"Right click at: ({row}, {col})")
    return "break"

for row in range(20):
    for col in range(20):
        button = tk.Button(buttonframe, text=f"({row},{col})", font=('Times New Roman', 8),
                           width=2, height=1,  
                           command=lambda r=row, c=col: on_left_click(r, c))
        button.grid(row=row, column=col, sticky="nsew", padx=1, pady=1)

        # Bind right-click event properly
        button.bind("<Button-3>", lambda e, r=row, c=col: on_right_click(e, r, c))  # Windows/Linux
        button.bind("<Button-2>", lambda e, r=row, c=col: on_right_click(e, r, c))  # MacOS


buttonframe.pack()
buttonframe.pack(fill='both', expand=True)

root.mainloop()

#poop