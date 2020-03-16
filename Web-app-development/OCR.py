# importing all the modules required
from tkinter import *
from PIL import Image
from tkinter import filedialog
from pytesseract import image_to_string
from tkinter import ttk
from tkinter import messagebox
import pyperclip
# creating an instance of Tk
root = Tk()
# Setting the title of the root window
root.title("Extract text from image")
# creating a function to browse for image files on user's computer
def get_file():
    path = filedialog.askopenfilename(title="Choose an image", filetypes=(("png files","*.png"),("jpg files","*.jpg"),("jpeg files","*.jpeg"),("all files","*.*")))
    extract(path)
# creating a function to use the filepath from user selection to open and process the image file
# The extracted text will be showed in a messagebox and copied to the clipboard
def extract(path):
    img = Image.open(path)
    text = image_to_string(img)
    if text:
        messagebox.showinfo("Extracted text from the image", text)
        pyperclip.copy(text)
    else:
        messagebox.showinfo("Extracted text from the image", "No text found in the Image")
# Creating instruction/welcome label for the user of the application
ttk.Label(root, text="Welcome to the text extractor!"+"\n"+"Please select an image using the browse button." +"\n"+"The extracted text will be shown as well as copied to your clipboard."+"\n"+"Only .jpg, .jpeg and .png files supported.").pack(side=BOTTOM)
# Creating a browse button for the user to select an image file
ttk.Button(root, text="Browse", command= lambda: get_file()).pack(side=TOP)

root.mainloop()