import tkinter as tk
from tkinter.constants import END
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile


root = tk.Tk()

Canvas = tk.Canvas(root, width=600, height=300)
Canvas.grid(columnspan=3, rowspan=3)

# Logo
logo = Image.open("Logo.png")
logo = ImageTk.PhotoImage(logo)
logo_Label = tk.Label(image=logo)
logo_Label.image = logo
logo_Label.grid(column=1, row=0)

# instraction
instructions = tk.Label(
    root, text='Select a PDF file to extract from your Computer!', font='Bronova')
instructions.grid(columnspan=3, column=0, row=1)


def open_file():

    browse_text.set("Loading...")
    file = askopenfile(parent=root, mode="rb",
                       title="Choose a file", filetype=[("pdf file", "*.pdf")])
    if file:
        read_pdf = PyPDF2.PdfFileReader(file)
        page = read_pdf.getPage(0)
        page_content = page.extractText()
        print(page_content)

        # text_box
        text_box = tk.Text(root, height=10, width=50, padx=15,
                           pady=15)
        text_box.insert(1.0, page_content)
        text_box.tag_configure("center", justify="center")
        text_box.tag_add("center", 1.0, END)
        text_box.grid(column=1, row=3)
        browse_text.set("Browse")


# Browse Button
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, command=lambda: open_file(),
                       font='Bronova', bg="#FF7005", fg="white", height=3, width=15)
browse_text.set("Browse")
browse_btn.grid(column=1, row=2)

Canvas = tk.Canvas(root, width=600, height=250)
Canvas.grid(columnspan=3)


root.mainloop()
