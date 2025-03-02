import da_bomb as db
import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()


height = root.winfo_screenwidth()
width = root.winfo_screenheight()
size = min(width, height)
root.geometry(f"{size}x{size}+50+50")  # Keeps it a perfect square
root.title("Minesweeper")

buttonframe = tk.Frame(root)
def show_popup_with_image(image_path):
    popup = tk.Toplevel()  # Create a new top-level window
    popup.title("Bomb Hit!")
    
    try:
        pil_image = Image.open(image_path)
        pil_image = pil_image.resize((width, height))  # Resize to fit the popup
        popup.image_ref = ImageTk.PhotoImage(pil_image) 

        label = tk.Label(popup, image=popup.image_ref)  # Keep a reference to the image
        label.pack()
        print("popupimage loaded successfully")

    except Exception as e:
        print(f"Error loading image: {e}")
        label = tk.Label(popup, text="Error loading image.")
        label.pack()

image_path = "images/edwin.jpg"  # Adjust the path if necessary
try:
    pil_image = Image.open(image_path)
    pil_image = pil_image.resize((50, 50))  # Resize image if necessary
    image = ImageTk.PhotoImage(pil_image)
except Exception as e:
    print(f"Error loading image1: {e}")
    image = None  # Handle if the image can't be loaded

bomb = "images/G.jpg"  # Adjust the path if necessary
try:
    pil_image2 = Image.open(bomb)
    pil_image2 = pil_image2.resize((50, 50))  # Resize image if necessary
    image2 = ImageTk.PhotoImage(pil_image2)
    print("Image2 loaded successfully")
except Exception as e:
    print(f"Error loading image2: {e}")
    image2 = None 

flag = "images/poopfart_Artwork.jpg"  # Adjust the path if necessary
try:
    pil_image3 = Image.open(flag)
    pil_image3 = pil_image3.resize((50, 50))  # Resize image if necessary
    image3 = ImageTk.PhotoImage(pil_image3)
    print("Image3 loaded successfully")
except Exception as e:
    print(f"Error loading image3: {e}")
    image3 = None 
for i in range(20):
    buttonframe.columnconfigure(i, weight=1, minsize=30)
    buttonframe.rowconfigure(i, weight=1, minsize=30)
tile = "images/tile.jpeg"  
try:
    pil_image4 = Image.open(tile)
    pil_image4 = pil_image4.resize((50, 50))  
    image4 = ImageTk.PhotoImage(pil_image4)
    print("Image4 loaded successfully")
except Exception as e:
    print(f"Error loading image4: {e}")
    image4 = None 

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

is_break = False

def player_click(event, row, col, button):
    global is_break
    if button.image != image3:  
        if getattr(button, "player_click", True):  
            print(f"Click at: ({row}, {col})")
            button.player_click = False
            if is_break == False:
                db.break_board(row, col)
                is_break = True
                update_images()
                db.print_board()
            else:
                db.click(row, col)
                update_images()
                print(db.grid[row][col])
                db.print_board()
            


def on_right_click(event, row, col, button):
    print(f"Right-click at: ({row}, {col})")

    current_symbol = db.return_symbol(row, col)
    if button.image == image:  # Check if the button's current image is 'image'
        button.config(image=image3)  # Change to the flag image
        button.image = image3  # Update the button's image attribute
    elif button.image == image2:  # If the current image is a bomb
        print("bomb") 
    elif button.image == image3:  # If the current image is a flag
        button.config(image=image)  # Change back to the normal image
        button.image = image  # Update the button's image attribute

    elif button.image == image4:  # If the current image is a tile
        print("tile")
    else:
        print("Button has an unknown image")
    

def update_images():
    for i in range(20):
        for j in range(20):
            symbol = str(db.return_symbol(i, j))
            if getattr(button[i][j], 'image', None) == image3: 
                print(f"Skipping update at ({i}, {j}) because it's flagged")
                continue
            elif symbol == 'N':
                button[i][j].config(image=image)
                button[i][j].image = image  
            elif symbol == '.':
                button[i][j].config(image=image4)
                button[i][j].image = image4  
            elif symbol == 'b':  
                button[i][j].config(image=image2)
                button[i][j].image = image2  
                show_popup_with_image ("images/lose.jpg") 

            elif symbol in number_images and number_images[symbol] is not None:  
                button[i][j].config(image=number_images[symbol])  
                button[i][j].image = number_images[symbol]
            else:
                print(f"Unknown symbol '{symbol}' at ({i}, {j})")  


button = [['0']*20 for i in range (20)]

for row in range(20):
    for col in range(20):
        button[row][col] = tk.Button(buttonframe, image=image)
        button[row][col].image = image  # This assigns the image to the button.

        button[row][col].grid(row=row, column=col, sticky="nsew", padx=1, pady=1)

        button[row][col].player_click = True
        button[row][col].bind("<Button-1>", lambda e, r=row, c=col, b=button[row][col]: player_click(e, r, c, b))
        button[row][col].bind("<Button-2>", lambda e, r=row, c=col, b=button[row][col]: on_right_click(e, r, c, b))
        button[row][col].bind("<Button-3>", lambda e, r=row, c=col, b=button[row][col]: on_right_click(e, r, c, b))
        

buttonframe.pack(fill='both', expand=True)


db.generate_board()



root.mainloop()
