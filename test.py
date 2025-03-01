import tkinter as tk
from PIL import Image, ImageTk

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
    print(f"Error loading image1: {e}")
    image = None  # Handle if the image can't be loaded

discovered = "images/shid.jpg"  # Adjust the path if necessary
try:
    pil_image2 = Image.open(discovered)
    pil_image2 = pil_image2.resize((50, 50))  # Resize image if necessary
    image2 = ImageTk.PhotoImage(pil_image2)
    print("Image2 loaded successfully")
except Exception as e:
    print(f"Error loading image2: {e}")
    image2 = None 

flag = "images/download.jpg"  # Adjust the path if necessary
try:
    pil_image3 = Image.open(flag)
    pil_image3 = pil_image3.resize((50, 50))  # Resize image if necessary
    image3 = ImageTk.PhotoImage(pil_image3)
    print("Image3 loaded successfully")
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
        
        # Change the image to image2 after the button is clicked
        if image2:
            button.image = image2  # Store reference to prevent garbage collection
            button.config(image=image2)
            print(f"Image updated at ({row}, {col})")


def on_right_click(event, row, col, button):
    print(f"Place flag at: ({row}, {col})")
    if image3:
        button.image = image3  # Store reference to prevent garbage collection
        button.config(image=image3)
        print(f"Image updated at ({row}, {col})")
    return "break"  # To prevent the event from propagating

for row in range(20):
    for col in range(20):
        button = tk.Button(buttonframe, image=image, font=('Times New Roman', 8))
        button.image = image
        button.grid(row=row, column=col, sticky="nsew", padx=1, pady=1)

        button.first_click = True  

        button.bind("<Button-1>", lambda e, r=row, c=col, b=button: first_click(e, r, c, b)) 

        button.bind("<Button-2>", lambda e, r=row, c=col, b=button: on_right_click(e, r, c, b))
        button.bind("<Button-3>", lambda e, r=row, c=col, b=button: on_right_click(e, r, c, b))
 

buttonframe.pack(fill='both', expand=True)
# if image2:
#     # Loop through all children of the buttonframe and find the one at (9, 9)
#     for button in buttonframe.winfo_children():
#         grid_info = button.grid_info()  # Get the grid position of the button
#         if grid_info.get("row") == "9" and grid_info.get("column") == "9":
#             button.image = image2  # Store reference to prevent garbage collection
#             button.config(image=image2)
#             print("Button image updated to image2")
#             break  # Exit loop after updating the button
#     else:
#         print("Button at (9, 9) not found")

root.mainloop()
