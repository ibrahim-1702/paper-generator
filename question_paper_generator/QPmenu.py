from tkinter import *



root =Tk()
root.title('Care International')
root.iconbitmap('d:\projectnew\care.ico')
root.geometry("550x500")

def register():
    pass
def login():
    pass

#Creating menubar
my_menu =Menu(root)
root.config(menu=my_menu)


# adding Menu items
user_menu = Menu(my_menu)
my_menu.add_cascade(label="User", menu=user_menu)


user_menu.add_command(label="New user", command=register)
user_menu.add_command(label="Existing user", command=login)

user_menu.add_separator()
user_menu.add_command(label="Exit", command=root.quit)




my_menu.add_command(label="Generator", command=login)

my_menu.add_command(label="Exit", command=root.quit)



root.mainloop()

'''


import fpdf
from tkinter import *
import csv

pdf = fpdf.FPDF(format='letter')



    window = Tk()
    window.title("Question Paper Generator")
    window.configure(background='#ECECEC')
    window.geometry('600x500')

    lbl = Label(window, font="SF\Mono 36 bold", text = "Question Paper\nGenerator\n\n To Upload: replace csv\n  in the same folder \n    'question.csv'",background='#ECECEC',justify='left')
    lbl.grid(column=0, row=0,padx=20,pady=10)

    frame=Frame(window)
    frame.grid(column=0,row=3,padx=0,pady=10)

    addbutton=Button(frame,text="Add Question",)
    addbutton.config(height = 2, width = 15,bg='#ECECEC',justify='left',bd='0',relief='raised',command=addQwin)
    addbutton.grid(column=0,row=2)

    genbutton=Button(frame,text="Generate PDF",)
    genbutton.config(height = 2, width = 15,bg='#ECECEC',justify='left',bd='0',relief='raised',command=genpdf)
    genbutton.grid(column=1,row=2)

    window.mainloop()

def pdf_gen():
    pdf.add_page()
    pdf.set_font("Times", size=20)

    pdf.cell(200,15,"Examination", ln=1, align="C")
    pdf.set_font("Times",'i', size=17)
    pdf.cell(200,15,"Generated using an automated paper generation system", ln=1, align="C")
    pdf.set_font("Times",'i', size=14)
    pdf.cell(167,15,"Max Marks : 100", align="left")
    pdf.cell(100,15,"Time : 3 Hours",ln=1, align="right")
    pdf.set_font("Arial",'b', size=16)
    pdf.cell(134,15,"Section A", align="left")
    pdf.set_font("Times",'i', size=13)
    pdf.cell(100,15,"Max marks for this section are 4",ln=1, align="left")


    pdf.set_font("Times", size=12)
    for i in range(5):
        pdf.cell(170,6,"Q"+str(i+1)+": "+q[i],ln=1,align="left")

    pdf.set_font("Arial",'b', size=16)
    pdf.cell(134,15,"Section B", align="left")
    pdf.set_font("Times",'i', size=13)
    pdf.cell(100,15,"Max marks for this section are 6",ln=1, align="left")

    pdf.set_font("Times", size=12)
    for i in range(5,10):
        pdf.cell(170,6,"Q"+str(i+1)+": "+q1[i],ln=1,align="left")

    pdf.set_font("Arial",'b', size=16)
    pdf.cell(133,15,"Section C", align="left")
    pdf.set_font("Times",'i', size=13)
    pdf.cell(100,15,"Max marks for this section are 10",ln=1, align="left")

    pdf.set_font("Times", size=12)
    for i in range(10,15):
        pdf.cell(170,6,"Q"+str(i+1)+": "+q2[i],ln=1,align="left")

    pdf.output("file.pdf")




def genpdf():
    pdf_gen()





'''

'''

def questionselector(qlist):
    marks = 0
    selected_questions = []
    used = []
    while marks != 50 and marks <= 50:
        r = randomgenerate(0, len(qlist) - 1)
        if r not in used:
            used.append(r)
            selected_questions.append(qlist[r])
            marks += qlist[r][1]
    else:
        if marks == 50:
            return selected_questions


'''