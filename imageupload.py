import tkinter as tk
from PIL import ImageTk, Image  # PIL is the Python Imaging Library

# this is done in replit

# Create the main window
root = tk.Tk()
root.title("Product Display")

# Path to your image file
image_path = "s.jpg"
# Load images
# Replace "earring1.jpg" with the path to 
#your image file
image1 = Image.open(image_path) 

# Resize the image as needed
image1 = image1.resize((100, 100), Image.LANCZOS)


object_image = ImageTk.PhotoImage(image1)

button1 = tk.Button(root, image=object_image)
button1.grid()
label1 = tk.Label(text="s")
label1.grid()


# Path to your image file
image_path_2 = "d.jpg"
# Load images
# Replace "earring1.jpg" with the path to 
#your image file
image2 = Image.open(image_path_2) 

# Resize the image as needed
image2 = image2.resize((100, 100), Image.LANCZOS)


object_image2 = ImageTk.PhotoImage(image2)

button2 = tk.Button(root, image=object_image2)
button2.grid()
label2 = tk.Label(text="Desert Earrings")
label2.grid()



# Path to your image file
image_path_3 = "C.jpg"
# Load images
# Replace "earring1.jpg" with the path to 
#your image file
image3 = Image.open(image_path_3) 

# Resize the image as needed
image3 = image3.resize((100, 100), Image.LANCZOS)


object_image3 = ImageTk.PhotoImage(image3)

button3 = tk.Button(root, image=object_image3)
button3.grid()
label3 = tk.Label(text="C")
label3.grid()


root.mainloop()
