import tkinter as tk
import cv2
from PIL import Image, ImageTk
import numpy as np
import pytesseract
import splitter as sp
import imageTaker as iT

# Initialize Tkinter window
root = tk.Tk()
root.title("OCR Results")

# Load the big.jpg image
big_image = cv2.imread("./blockImage/big.jpg")
big_image = cv2.cvtColor(big_image, cv2.COLOR_BGR2RGB)

# Initialize a canvas for displaying images
canvas = tk.Canvas(root, width=big_image.shape[1], height=big_image.shape[0])
canvas.pack()

# Function to update OCR results on the canvas
def update_ocr_results():
    # Perform OCR on each block image and display results on the canvas
    grid_height = 8
    grid_width = 9
    for i in range(grid_height):
        for j in range(grid_width):
            block_image_path = f"./blockImage/blocks/{i * grid_width + j}.jpg"
            block_image = cv2.imread(block_image_path)
            block_image_gray = cv2.cvtColor(block_image, cv2.COLOR_BGR2GRAY)
            text = pytesseract.image_to_string(block_image_gray, config="-c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ --psm 10 -l eng")
            canvas.create_text(j * 70 + 35, i * 60 + 30, text=text, font=("Arial", 10))

# Call the image taker to capture the image
iT.take()

# Call the splitter to divide the big image into blocks
sp.tile()

# Call the function to update OCR results on the canvas
update_ocr_results()

# Convert the big image to a Tkinter PhotoImage
big_image_tk = ImageTk.PhotoImage(Image.fromarray(big_image))

# Display the big image on the canvas
canvas.create_image(0, 0, anchor=tk.NW, image=big_image_tk)

# Start the Tkinter event loop
root.mainloop()
