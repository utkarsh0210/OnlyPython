from pdf2docx import Converter
from docx2pdf import convert
from tkinter import *
#testing 3.0
c = Tk()
c.title("Conversion")
c.geometry("500x400")
def convert_to_doc():
    Label(c,text="PDF name").pack()
    pdf = Entry(c)
    pdf.pack()
    def do_it_doc():
        try:
            old_pdf=pdf.get()
            new_doc = "new.docx"
            obj = Converter(old_pdf)
            obj.convert(new_doc)
            obj.close()
            #speak("Converted to document successfully!!")
            c.destroy()
        except Exception as e:
            #speak("An error occured")
            c.destroy()
    button = Button(c,text = "Convert",command=do_it_doc)
    button.pack()

def convert_to_pdf():
    Label(c,text="DOC name").pack()
    doc = Entry(c)
    doc.pack()
    def do_itpdf():
        try:
            old_doc=doc.get()
            new_pdf = "new.pdf"
            convert(old_doc,new_pdf)
            #speak("Converted to PDF Successfully")
            c.destroy()
        except Exception as e:
            #speak("An error occured")
            c.destroy()
    button = Button(c,text="Convert",command=do_itpdf)
    button.pack()
    
    
    
    
button1 = Button(c,text = "Convert to DOCX",command =convert_to_doc)
button1.pack()
button2 = Button(c,text = "Convert to PDF",command =convert_to_pdf)
button2.pack()
c.mainloop()