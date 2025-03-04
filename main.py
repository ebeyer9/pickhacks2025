import da_bomb as db
import tkinter as tk
# from PIL import Image, ImageTk

root = tk.Tk()

# Set the window to be a square based on the smallest screen dimension
height = root.winfo_screenwidth()
width = root.winfo_screenheight()
size = min(width, height)
root.geometry(f"{size}x{size}+50+50")  # Keeps it a perfect square
root.title("Minesweeper")

buttonframe = tk.Frame(root)
image_path = "images/sackboy.jpg"  # Adjust the path if necessary
try:
    pil_image = Image.open(image_path)
    pil_image = pil_image.resize((50, 50))  # Resize image if necessary
    image = ImageTk.PhotoImage(pil_image)
except Exception as e:
    print(f"Error loading image: {e}")
    image = None  # Handle if the image can't be loaded
new_image = "images/shid.jpg"  # Adjust the path if necessary
try:
    pil_image2 = Image.open(new_image)
    pil_image2 = pil_image.resize((50, 50))  # Resize image if necessary
    image = ImageTk.PhotoImage(pil_image2)
except Exception as e:
    print(f"Error loading image3: {e}")
    image3 = None 

# Configure the grid for buttons
for i in range(20):
    buttonframe.columnconfigure(i, weight=1, minsize=30)
    buttonframe.rowconfigure(i, weight=1, minsize=30)

def first_click(event, row, col, button):
    if getattr(button, "first_click", True):  
        print(f"Initial click at: ({row}, {col})")
        button.first_click = False  
        return "break"  


def on_right_click(event, row, col, button):
    print(f"Place flag at: ({row}, {col})")
    if image3:
        button.image = image3  # Store reference to prevent garbage collection
        button.config(image=image3)
        print(f"Image updated at ({row}, {col})")
    return "break"  # To prevent the event from propagating

# def update_images():
#     for i in range(20):
#         for j in range(20):
#                 symbol db.return_symbol(i, j)
            

button = [['0']*20 for i in range (20)]

for row in range(20):
    for col in range(20):
        button = tk.Button(buttonframe, image=image, font=('Times New Roman', 8))
        button.grid(row=row, column=col, sticky="nsew", padx=1, pady=1)

        button[row][col].player_click = True  

        button[row][col].bind("<Button-1>", lambda e, r=row, c=col, b=button[row][col]: player_click(e, r, c, b)) 

        button.bind("<Button-3>", lambda e, r=row, c=col: on_right_click(e, r, c))  # Right click (place flag)
        button.bind("<Button-2>", lambda e, r=row, c=col: on_right_click(e, r, c))  

buttonframe.pack(fill='both', expand=True)
buttonframe.grid_slaves(row=9, column=9)[0].config(image=new_image)
root.mainloop()
