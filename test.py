import da_bomb as db
import tkinter as tk
from PIL import Image, ImageTk
import os

root = tk.Tk()

# Get screen size
height = root.winfo_screenheight()
width = root.winfo_screenwidth()
size = min(width, height)
root.geometry(f"{size}x{size}+50+50")  # Keeps it a perfect square
root.title("Minesweeper")

buttonframe = tk.Frame(root)

# Function to show popup with image
def show_popup_with_image(image_path):
    popup = tk.Toplevel()  # Create a new top-level window
    popup.title("Bomb Hit!")

    try:
        # Verify if the image path exists
        if not os.path.exists(image_path):
            print(f"Image path does not exist: {image_path}")
            return  # Exit the function if the image does not exist

        pil_image = Image.open(image_path)
        pil_image = pil_image.resize((width, height))  # Resize to fit the popup
        popup_image = ImageTk.PhotoImage(pil_image)  # Create ImageTk object

        label = tk.Label(popup, image=popup_image)
        label.image = popup_image  # Keep a reference to the image
        label.pack()
        print(f"Popup image loaded from {image_path}")

    except Exception as e:
        print(f"Error loading image: {e}")
        label = tk.Label(popup, text="Error loading image.")
        label.pack()

# Test the popup functionality by showing a bomb image
show_popup_with_image("images/lose.jpg")  # Replace with a valid path

# Add other images (for buttons, flags, bombs, etc.)
image = None
bomb = "images/G.jpg"
flag = "images/poopfart_Artwork.jpg"
tile = "images/tile.jpeg"

# Make sure paths exist
image_paths = [bomb, flag, tile]
for path in image_paths:
    if not os.path.exists(path):
        print(f"Error: Image path does not exist: {path}")

try:
    pil_image2 = Image.open(bomb)
    pil_image2 = pil_image2.resize((50, 50))  # Resize image if necessary
    image2 = ImageTk.PhotoImage(pil_image2)
    print("Image2 loaded successfully")
except Exception as e:
    print(f"Error loading image2: {e}")
    image2 = None 

# Setup number images for tiles
number_images = {}
for num in range(1, 9):
    num_path = f"images/{num*111}.png"  
    try:
        pil_img = Image.open(num_path)
        pil_img = pil_img.resize((50, 50))  
        number_images[str(num)] = ImageTk.PhotoImage(pil_img)
        print(f"Loaded image for number {num}")
    except Exception as e:
        print(f"Error loading number image {num}: {e}")
        number_images[str(num)] = None  

# Setup game grid with buttons
button = [['0']*20 for i in range(20)]

for row in range(20):
    for col in range(20):
        button[row][col] = tk.Button(buttonframe, image=image)
        button[row][col].image = image  # This assigns the image to the button.

        button[row][col].grid(row=row, column=col, sticky="nsew", padx=1, pady=1)

        # Bind events for player click and right-click
        button[row][col].player_click = True
        button[row][col].bind("<Button-1>", lambda e, r=row, c=col, b=button[row][col]: player_click(e, r, c, b))
        button[row][col].bind("<Button-2>", lambda e, r=row, c=col, b=button[row][col]: on_right_click(e, r, c, b))
        button[row][col].bind("<Button-3>", lambda e, r=row, c=col, b=button[row][col]: on_right_click(e, r, c, b))

# Function for player click
def player_click(event, row, col, button):
    print(f"Click at: ({row}, {col})")
    # Your logic for handling player click here...

# Function for right-click (to handle flags and bombs)
def on_right_click(event, row, col, button):
    print(f"Right-click at: ({row}, {col})")
    current_symbol = db.return_symbol(row, col)
    if button.image == image:  # Check if the button's current image is 'image'
        button.config(image=image3)  # Change to the flag image
        button.image = image3  # Update the button's image attribute
    elif button.image == image2:  # If the current image is a bomb
        print("bomb") 
        show_popup_with_image("images/lose.jpg")  # Show the bomb image
    elif button.image == image3:  # If the current image is a flag
        button.config(image=image)  # Change back to the normal image
        button.image = image  # Update the button's image attribute
    elif button.image == image4:  # If the current image is a tile
        print("tile")

# Start the game
db.generate_board()

buttonframe.pack(fill='both', expand=True)
root.mainloop()
