from tkinter import *
from tkinter import filedialog

def browse_file():
    file_path=filedialog.askopenfilename()
    print(file_path)  # Replace this line with the code to process the selected file

root = Tk()

upload_button = Button(root, text="Upload Photo", command=browse_file)
upload_button.pack()

root.mainloop()