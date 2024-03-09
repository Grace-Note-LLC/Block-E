import tkinter as tk
from PIL import ImageTk, Image
import pytesseract
import cv2
import numpy as np
import os
import imageTaker as iT
import splitter as sp

import collections
import threading



   
grid_vals = []



class GridOverlayApp():
    def __init__(self, root, image_path, grid_values):
        # threading.Thread.__init__(self)
        # self.start()
        self.root = root
        self.root.title("Grid Overlay")


        # iT.take()
        # sp.tile()
        self.image = Image.open(image_path)
        self.photo = ImageTk.PhotoImage(self.image)
        
        self.canvas = tk.Canvas(root, width=self.image.width, height=self.image.height)
        self.canvas.pack()
        
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)
        
        self.grid_values = grid_values
        self.draw_grid(self.grid_values)

    # def callback(self):
    #     self.root.quit()

        
    
    def draw_grid(self, grid_values):
        for i, row in enumerate(grid_values):
            for j, value in enumerate(row):
                x0 = j * (self.image.width / len(row))
                y0 = i * (self.image.height / len(grid_values))
                x1 = (j + 1) * (self.image.width / len(row))
                y1 = (i + 1) * (self.image.height / len(grid_values))
                self.canvas.create_rectangle(x0, y0, x1, y1, fill="", outline="red")
                text_x = (x0 + x1) / 2
                text_y = (y0 + y1) / 2
                font = ("Arial", 30)
                self.canvas.create_text(text_x, text_y, text=str(value), fill="purple", font=font)
    
    # def update_grid_with_ocr(self, split_image_dir, grid_values):
    #     for filename in os.listdir(split_image_dir):
    #         if filename.endswith(".jpg"):
    #             row_col = filename.split('.')[0]  # Extract row and column numbers from filename
    #             row, col = divmod(int(row_col), 9)  # Assuming each row has 9 columns
    #             print(f"Processing image {filename}: Row {row}, Column {col}")
    #             if 0 <= row < len(grid_values) and 0 <= col < len(grid_values[0]):  # Ensure row and column indices are valid
    #                 image_path = os.path.join(split_image_dir, filename)
    #                 img = self.process_image(image_path)
    #                 text = self.extract_text_from_image(img)
    #                 # Run OCR three times
    #                 ocr_results = [self.extract_text_from_image(img) for _ in range(3)]
    #                 # Filter out empty strings
    #                 ocr_results = [result for result in ocr_results if result.strip()]
    #                 if ocr_results:
    #                     # Count occurrences of each character in the OCR results
    #                     char_count = collections.Counter("".join(ocr_results))
    #                     # Get the most common character(s) excluding empty strings
    #                     most_common_chars = char_count.most_common(2)
    #                     if most_common_chars:
    #                         if len(most_common_chars) == 2 and most_common_chars[0][1] == most_common_chars[1][1]:
    #                             # If two characters are returned in the first runs, keep the character that persists
    #                             persistent_char = most_common_chars[0][0] if grid_values[row][col] == most_common_chars[0][0] else most_common_chars[1][0]
    #                             grid_values[row][col] = persistent_char
    #                         else:
    #                             # Otherwise, update the grid with the majority result
    #                             grid_values[row][col] = most_common_chars[0][0]
    #                 self.draw_grid(grid_values)
    #                 self.root.update_idletasks()
    #             else:
    #                 print(f"Error: Row {row} or Column {col} out of range.")






    
    # def process_image(self, image_path):
    #     img = np.array(Image.open(image_path))
    #     norm_img = np.zeros((img.shape[0], img.shape[1]))
    #     img = cv2.normalize(img, norm_img, 0, 255, cv2.NORM_MINMAX)
    #     img = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)[1]
    #     img = cv2.GaussianBlur(img, (1, 1), 0)
    #     return img
    
    # def extract_text_from_image(self, image):
    #     try:
    #         text = pytesseract.image_to_string(image, config=("-c tessedit"
    #                 "_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    #                 " --psm 10"
    #                 " -l eng"
    #                 " "))
    #         return text.strip()
    #     except Exception as e:
    #         print(f"Error extracting text: {e}")
    #         return ""
    # def run(self):
    #     self.root = tk.Tk()
    #     # self.root.protocol("WM_DELETE_WINDOW", self.callback)

    #     # label = tk.Label(self.root, text="Hello World")
    #     # label.pack()

        
    #     app = GridOverlayApp(self.root)
    #     self.root.mainloop()
                

def start_gui(grid_vep):
    root = tk.Tk()
    app = GridOverlayApp(root, "./blockImage/big.jpg", grid_vep)
    root.mainloop()

def main(grid_pero):
    # Example grid values
    grid_values = [
        [" ", " ", " ", " ", " ", " " , " ", " ", " "],
        [" ", " ", " ", " ", " ", " " , " ", " ", " "],
        [" ", " ", " ", " ", " ", " " , " ", " ", " "],
        [" ", " ", " ", " ", " ", " " , " ", " ", " "],
        [" ", " ", " ", " ", " ", " " , " ", " ", " "],
        [" ", " ", " ", " ", " ", "A " , " ", " ", " "],
        [" ", " ", " ", " ", " ", " " , " ", " ", " "],
        [" ", " ", " ", " ", " ", " " , " ", " ", " "]
    ]
    grid_vals = grid_pero
    # root = tk.Tk()
    # # root.protocol("WM_DELETE_WINDOW", root.callback)

    # # label = tk.Label(root, text="Hello World")
    # # label.pack()
    # app = GridOverlayApp(root)
    # root.mainloop()

    # root = tk.Tk()

    # app = GridOverlayApp(root, "./blockImage/big.jpg", grid_values)

    # mainloop_thread = threading.Thread(target=root.mainloop)
    # mainloop_thread.start()

    gui_thread = threading.Thread(target=start_gui(grid_pero))
    gui_thread.start()
    # print("hi")
   
   
    # app.update_grid_with_ocr("./blockImage/blocks", grid_values)  # Update grid with OCR results

# if __name__ == "__main__":
#     main()
