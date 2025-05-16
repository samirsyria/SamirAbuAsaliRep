import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

# Create the main window
root = tk.Tk()
root.title("Image Viewer using Tkinter")

# Function to open and display an image
def open_image():
    # Select the image file
    image_file = filedialog.askopenfilename(title="Choose an Image", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp")])
    if image_file:
        # Open the image using PIL
        image = Image.open(image_file)
        image = image.resize((500, 400))  # Resize the image (optional)
        displayed_image = ImageTk.PhotoImage(image)

        # Display the image in the label
        image_label.config(image=displayed_image)
        image_label.image = displayed_image

# Button to choose the image
open_button = tk.Button(root, text="Open Image", command=open_image)
open_button.pack(pady=10)

# Label to display the image
image_label = tk.Label(root)
image_label.pack()

root.mainloop()
