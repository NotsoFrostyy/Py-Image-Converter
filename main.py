# Import Modules
from tkinter import *
from tkinter import filedialog as fd
from PIL import Image
from tkinter import messagebox, OptionMenu, StringVar, Label, Button
import webbrowser

# Variable shortcuts for modules
root = Tk()

# Application Information
root.title("Image Converter (Test Builds)")  # name of window
root.resizable(False, False)  # Cant resize window

frame1 = Frame(heigh=250, width=300, bg='teal')  # bg1
frame1.pack(fill='both', expand=True)
frame1.grid

BottomFrame = Canvas(frame1, width="250", height="190",
                     relief=RIDGE, bd=2)  # bottom frame
BottomFrame.place(x=25, y=30)

# start of website links
new = 1
url = "https://github.com/NotsoFrostyy"


def openweb():
    webbrowser.open(url, new=new)
# end of website links

# start of jpg to png

def jpg_to_png():
    global im1

    import_filename = fd.askopenfilename(filetypes=[("JPG File", '.jpg')])
    if import_filename.endswith(".jpg"):

        im1 = Image.open(import_filename)

        # where to save
        export_filename = fd.asksaveasfilename(defaultextension=".png")
        im1.save(export_filename)

        messagebox.showinfo("success ", "your Image converted to Png")
    else:
       # error
        messagebox.showerror("Error", "Input all Data")
# end of jpg to png

# start of jfif to png

def jfif_to_png():
    global im1

    import_filename = fd.askopenfilename(filetypes=[("JFIF File", '.jfif')])
    if import_filename.endswith(".jfif"):

        im1 = Image.open(import_filename)

        # where to save
        export_filename = fd.asksaveasfilename(defaultextension=".png")
        im1.save(export_filename)

        messagebox.showinfo("success ", "your Image converted to Png")
    else:
       # error
        messagebox.showerror("Error", "Input all Data")
# end of jfif to png

# start of png to jpg

def png_to_jpg():
    global im1

    import_filename = fd.askopenfilename(filetypes=[("PNG File", '.png')])
    if import_filename.endswith(".png"):

        im1 = Image.open(import_filename)

        # where to save
        export_filename = fd.asksaveasfilename(defaultextension=".jpg")
        im1.save(export_filename)

        messagebox.showinfo("success ", "your Image converted to Jpg")
    else:
        # error
        messagebox.showerror("Error", "Input all Data")
# end of png to jpg

# start of jpg to pdf

def Jpg_to_Pdf():
    global im1
    import_filename = fd.askopenfilename(filetypes=[("JPG File", '.jpg')])

    if import_filename.endswith(".jpg"):
        im1 = Image.open(import_filename)
        imgg = im1.convert("RGB")
        imgg = fd.asksaveasfilename(defaultextension=".pdf")
        im1.save(imgg)

        messagebox.showinfo("success ", "your Image converted to pdf ")
    else:
        messagebox.showerror("Error", "Input all Data")
# end of jpg to pdf

# start of png to pdf

def png_to_pdf():
    global im1
    import_filename = fd.askopenfilename(filetypes=[("PNG File", '.png')])

    if import_filename.endswith(".png"):
        im1 = Image.open(import_filename)
        imgg = im1.convert("RGB")
        imgg = fd.asksaveasfilename(defaultextension=".pdf")
        im1.save(imgg)

        messagebox.showinfo("success ", "your Image converted to pdf ")
    else:
        messagebox.showerror("Error", "Input all Data")
# end of png to pdf

#start of png to ico
        
def png_to_ico():
    global im1
    import_filename = fd.askopenfilename(filetypes=[("PNG File", '.png')])

    if import_filename.endswith(".png"):
        im1 = Image.open(import_filename)
        im1 = im1.resize((256, 256))
        imgg = fd.asksaveasfilename(defaultextension=".ico")
        im1.save(imgg, bitmap_format='bmp')
        messagebox.showinfo("success ", "your Image converted to ico ")
    else:
        messagebox.showerror("Error", "Input all Data")
#end of png to ico

#start of jpg to ico

def jpg_to_ico():
    global im1
    import_filename = fd.askopenfilename(filetypes=[("JPG File", '.jpg')])

    if import_filename.endswith(".jpg"):
        im1 = Image.open(import_filename)
        im1 = im1.resize((256, 256))
        imgg = fd.asksaveasfilename(defaultextension=".ico")
        im1.save(imgg, bitmap_format='bmp')
        messagebox.showinfo("success ", "your Image converted to ico ")
    else:
        messagebox.showerror("Error", "Input all Data")
#end of jgg to ico


# start of buttons
button1 = Button(root, text="Jpg -> Png", width=9, height=1, bg="purple",
                 fg="white", font=("helvetica", 12, "bold"), command=jpg_to_png, relief=GROOVE)

button1.place(x=50, y=40)

button2 = Button(root, text="Png -> Jpeg", width=9, height=1, bg="purple",
                 fg="white", font=("helvetica", 12, "bold"), command=png_to_jpg, relief=GROOVE)

button2.place(x=160, y=40)

button3 = Button(root, text="Jpg -> Pdf", width=9, height=1, bg="purple",
                 fg="white", font=("helvetica", 12, "bold"), command=Jpg_to_Pdf, relief=GROOVE)

button3.place(x=50, y=80)


button5 = Button(root, text="Png -> Pdf", width=9, height=1, bg="purple",
                 fg="white", font=("helvetica", 12, "bold"), command=png_to_pdf, relief=GROOVE)

button5.place(x=160, y=80)

button6 = Button(root, text="Jpg -> Ico", width=9, height=1, bg="purple",
                 fg="white", font=("helvetica", 12, "bold"), command=jpg_to_ico, relief=GROOVE)

button6.place(x=50, y=120)

button7 = Button(root, text="Png -> Ico", width=9, height=1, bg="purple",
                 fg="white", font=("helvetica", 12, "bold"), command=png_to_ico, relief=GROOVE)

button7.place(x=160, y=120)

# end of button

# website button and placement and geometry of window
logo = Button(root, text="Frost Software", width=11, height=1, bg="teal",
              fg="white", activebackground="teal", font=("helvetica", 10, "bold"), relief=SUNKEN, activeforeground="white")
logo.place(x=100, y=0)
Btn = Button(frame1, text="GITHUB", command=openweb, bg="Grey", fg="white",
             width=8, height=1, font=("helvetica", 10, "bold"), relief=GROOVE)
Btn.place(x=155, y=195)
btn2 = Button(frame1, width=4, height=1, font=("helvetica", 10, "bold"),
              text="Exit", bg='grey', fg='white', relief=GROOVE, command=root.destroy)
btn2.place(x=235, y=195)
root.geometry("300x250+400+200")
root.mainloop()
