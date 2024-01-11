#=================================importing modules=====================================================================

import random
import fpdf
from tkinter import *
from tkinter import messagebox as ms
import sqlite3


pdf = fpdf.FPDF(format='letter')

#======================================Creating root===================================================================

root =Tk()
root.title('Care International')
root.iconbitmap('d:\projectnew\care.ico')
root.geometry("650x500+120+120")


#======================================================Declaring Global variable========================================
clicked = StringVar()
username = StringVar()
password = StringVar()
question = StringVar()
marks = IntVar()
examname = StringVar()
selectedQ=[]
selectedQS=[]
exam=StringVar()
#====================================DATABASE CONNECTION================================================================

# create connection to db
conn = sqlite3.connect('qp_gen.db')
#Create cursor
c=conn.cursor()

c.execute(""" create table if not exists userlogin (
        username text not null,
        password text not null
          ) """)
conn.commit()
conn.close()

# create connection to db
conn = sqlite3.connect('qp_gen.db')
#Create cursor
cur=conn.cursor()
#cur.execute("drop table questions")

cur.execute(""" create table if not exists questions(
        question varchar(50) not null
           ) """)
conn.commit()
conn.close()


#=================================USER DEFINED FUNCTIONS=============================================================================

def randomgenerate(low, high):  # Random number generator function
      return random.randint(low, high)


def addquest():
    global question

    QuestionWindow = Toplevel(root)
    QuestionWindow.title('Add Questions')
    QuestionWindow.iconbitmap('d:\projectnew\care.ico')
    QuestionWindow.geometry("650x500+120+120")
    


    question = Entry(QuestionWindow, width=50, bd=3)
    question.grid(row=7, column=1, padx=10, pady=20, ipadx=20, ipady=10)

    # label creation
    heading_lbl = Label(QuestionWindow, text="Adding New Questions", font=('freesansbold', 20), padx=5, pady=15)
    heading_lbl.grid(row=4, column=0, sticky=W)

    question_lbl = Label(QuestionWindow, text="Enter Question: ", font=('calibri', 18))
    question_lbl.grid(row=7, column=0, padx=50, pady=20, sticky=W)


    # Buttons
    question_btn = Button(QuestionWindow, text="ADD", font=('calibri', 22), command=addquestion)
    question_btn.grid(row=21, column=0, columnspan=1, pady=20, padx=20, ipadx=50)

    cancel1_btn = Button(QuestionWindow, text="Cancel", font=('calibri', 22), command=cancel1)
    cancel1_btn.grid(row=21, column=1, columnspan=1, pady=20, padx=10, ipadx=50)

    x_btn = Button(QuestionWindow, text="Exit", font=('calibri', 22), command=iquit)
    x_btn.grid(row=22, column=0, columnspan=2, padx=25, ipadx=50)
    x_btn = Button(QuestionWindow, text="view", font=('calibri', 22), command=viewtableQ)
    x_btn.grid(row=23, column=0, columnspan=2, padx=25, ipadx=50)


def addquestion():
    global question

    if len(question.get()) == 0:
        ms.showerror("Error", "All fields are required")

        question.delete(0, END)

        question.focus_set()


    else:  # Create  cursor
        conn = sqlite3.connect('qp_gen.db')
        c = conn.cursor()

        c.execute("select * from questions where question = :question",
                  {'question': question.get()
                   })
        rows1 = c.fetchall()
        print (rows1)


        if rows1 != []:
            ms.showerror("Existing Question","Enter a Different Question")

            question.delete(0, END)
            question.focus_set()

            conn.commit()
            conn.close()
        else:

            conn = sqlite3.connect('qp_gen.db')
            cur = conn.cursor()

            cur.execute("insert into questions values (:question)",
                        {
                            'question': question.get()
                        })
            ms.showinfo("Success", " Question Added")

            question.delete(0, END)
            question.focus_set()
            conn.commit()
            conn.close()



# Registering a new user function

def register():

    global username
    global password
    regWindow = Toplevel(root)
    regWindow.title('New User Registration')
    regWindow.iconbitmap('d:\projectnew\care.ico')
    regWindow.geometry("650x500+120+120")

    username = Entry(regWindow, width=31, bd=3)
    username.grid(row=7, column=1, padx=10, pady=20, ipadx=20, ipady=10)
    password = Entry(regWindow, show="*", width=31, bd=3)
    password.grid(row=9, column=1, ipadx=20, ipady=10)

    # label creation
    head_lbl1 = Label(regWindow, text="Enter the Details for Registration", font=('freesansbold', 20), padx=5, pady=15)
    head_lbl1.grid(row=4, column=1, sticky=W)

    user_lbl = Label(regWindow, text="Username: ", font=('calibri', 18))
    user_lbl.grid(row=7, column=0, padx=50, pady=20, sticky=W)
    password_lbl = Label(regWindow, text="Password: ", font=('calibri', 18))
    password_lbl.grid(row=9, column=0, padx=50, sticky=W)

    # Buttons
    Reg_btn = Button(regWindow, text="OK", font=('calibri', 22), command=newuser)
    Reg_btn.grid(row=21, column=0, columnspan=1, pady=20, padx=20, ipadx=50)

    cancel_btn = Button(regWindow, text="Cancel", font=('calibri', 22), command=cancel)
    cancel_btn.grid(row=21, column=1, columnspan=1, pady=20, padx=10, ipadx=50)

    x_btn = Button(regWindow, text="Exit", font=('calibri', 22), command=iquit)
    x_btn.grid(row=22, column=0, columnspan=2, padx=25, ipadx=50)

    x1_btn = Button(regWindow, text="View", font=('calibri', 22), command=viewtable)
    x1_btn.grid(row=25, column=0, columnspan=2, padx=25, ipadx=50)

def iquit():
    quitting= ms.askyesno("QP Generator","Do you want to exit")
    if quitting >0:
        root.destroy()
        return

def cancel():

    username.delete(0, END)
    password.delete(0, END)
    #question.delete(0, END)
    username.focus_set()


def cancel1():

    question.delete(0, END)
    question.focus_set()


def viewtable():
    # create connection to db
    conn = sqlite3.connect('qp_gen.db')
    # Create cursor
    c = conn.cursor()
    lst=c.execute("select * from userlogin;")

    for i in lst:
        print (i)


    # save changes
    conn.commit()

    # close the connection
    conn.close()


def viewtableQ():
# create connection to db
    conn = sqlite3.connect('qp_gen.db')
    # Create cursor
    cur = conn.cursor()

    lst=cur.execute("select * from questions;")

    for i in lst:
        print (i)


    # save changes
    conn.commit()

    # close the connection
    conn.close()


def newuser():

    if len(username.get())==0 or len(password.get())==0:
       ms.showerror("Error", "Fields cannot be empty")

       username.delete(0, END)
       password.delete(0, END)

       username.focus_set()
    else:

        conn = sqlite3.connect('qp_gen.db')
        # Create cursor
        c = conn.cursor()

        c.execute("Select username from userlogin where username=:username",
                                   {
                                       'username': username.get()
                                   })
        usernamecheck= c.fetchall()

        if usernamecheck == [] :
            # Create  cursor
            conn = sqlite3.connect('qp_gen.db')
            c = conn.cursor()
            c.execute("insert into userlogin values (:username,:password)",
                      {
                          'username': username.get(),
                          'password': password.get()
                      })
            ans= ms.showinfo("Success", "User Registered")

            conn.commit()
            # close the connection
            conn.close()

           # if ans=='ok' :
             #   closewindow()
            #regWindow.destroy()

            #clear textboxes
            username.delete(0, END)
            password.delete(0, END)



        else:
            ms.showinfo("Error", "User already exists")

            username.delete(0, END)
            password.delete(0, END)

            username.focus_set()

#function for login of existing user

# create login
def login():

    global username
    global password

    existingUser = Toplevel(root)
    existingUser.title('Care International - QP Generator')
    existingUser.iconbitmap('d:\projectnew\care.ico')
    existingUser.geometry("650x500+120+120")

    username = Entry(existingUser, width=31, bd=3)
    username.grid(row=7, column=1, padx=10, pady=20, ipadx=20, ipady=10)
    password = Entry(existingUser, show="*", width=31, bd=3)
    password.grid(row=9, column=1, ipadx=20, ipady=10)
    # label creation
    head_lbl1 = Label(existingUser, text="Enter Username & Password", font=('freesansbold', 20), padx=5,
                      pady=15)
    head_lbl1.grid(row=4, column=1, sticky=W)

    user_lbl = Label(existingUser, text="Username: ", font=('calibri', 18))
    user_lbl.grid(row=7, column=0, padx=50, pady=20, sticky=W)
    password_lbl = Label(existingUser, text="Password: ", font=('calibri', 18))
    password_lbl.grid(row=9, column=0, padx=50, sticky=W)

    # Buttons
    Reg_btn = Button(existingUser, text="OK", font=('calibri', 22), command=existingLogin)
    Reg_btn.grid(row=21, column=0, columnspan=1, pady=20, padx=20, ipadx=50)

    cancel_btn = Button(existingUser, text="Cancel", font=('calibri', 22), command=cancel)
    cancel_btn.grid(row=21, column=1, columnspan=1, pady=20, padx=10, ipadx=50)

    x_btn = Button(existingUser, text="Exit", font=('calibri', 22), command=iquit)
    x_btn.grid(row=22, column=0, columnspan=2, padx=25, ipadx=50)

def existingLogin():

    global username
    global password
    username.focus_set()
    if len(username.get())==0 or len(password.get())==0:
       ms.showerror("Error", "All fields are required")

       username.delete(0, END)
       password.delete(0, END)

       username.focus_set()
    else:    # Create  cursor
       conn = sqlite3.connect('qp_gen.db')
       c = conn.cursor()

       c.execute("select * from userlogin where username = :username and password =:password",
                 {'username' : username.get(),
                  'password' : password.get()})
       rows=c.fetchall()


       if rows == []:
           ms.showerror("Error","Invalid Username or Password")

           username.delete(0, END)
           password.delete(0, END)
           username.focus_set()

           conn.commit()
           conn.close()
       else:
           ms.showinfo("Login Success", " QP Generation Allowed")
           my_menu.entryconfig(2, state = 'normal')


def generate():
           global clicked
           global examname
           loginWindow = Toplevel(root)
           loginWindow.title ('Care International - QP Generator')
           loginWindow.iconbitmap('d:\projectnew\care.ico')
           loginWindow.geometry ("750x500+120+120")


           #text box
           examname = Entry(loginWindow, width=50)
           examname.grid(row=5, column=1, padx=2, pady=5, ipadx=2,ipady=10)

           #labels
           head1_lbl = Label(loginWindow , text="Question Paper Generator", font=('freesansbold', 20), padx=5, pady=5)
           head1_lbl.grid(row=2, column=0,ipadx=35, ipady=10)

           marks_lbl = Label(loginWindow , text="Total Marks :    ", font=('freesansbold', 20), padx=5, pady=5)
           marks_lbl.grid(row=4, column=0, ipadx=10, ipady=10)

           options =['25','50',]
           clicked=StringVar()
           clicked.set("Choose Marks")

           drop=OptionMenu(loginWindow, clicked, *options, command=selected)
           drop.grid(row = 4, column= 1, ipady=10, ipadx=5)

           examname_lbl = Label(loginWindow , text="Examination : ", font=('freesansbold', 20), padx=5, pady=5)
           examname_lbl.grid(row=5, column=0, ipadx=5, ipady=5)
           # Button
           Gen_btn = Button(loginWindow ,text="Generate QP", font=('freesansbold', 20), command = qp_generate )
           Gen_btn.grid(row=8, column=0, columnspan=1, pady = 10, padx=10,ipady=10,ipadx=50)

           Quit_btn = Button(loginWindow, text="Exit", font=('freesansbold', 20), command = iquit)
           Quit_btn.grid(row=8, column=1, columnspan=2, pady=30, padx=30, ipady=10,ipadx=20)


def selected(event):
    global clicked
    global marks
    if clicked.get() == '25':
        marks = 25
    else:
        marks = 50

#function qp_generate

def qp_generate():
    global marks
    global exam
    global examname
    global clicked

    exam= examname.get()
    if len(examname.get())==0 or len(clicked.get())== None:
       ms.showerror("Error", "Fields cannot be empty")

       examname.delete(0, END)
       examname.focus_set()



    if marks == 25:
        gen_pdf25()
    elif marks == 50:
        gen_pdf50()
    else:
        ms.showerror("Error", "Choice wrong")
        examname.focus_set()

def gen_pdf25():

    global exam
    global selectedQ

    # =============================Extract Questions=========================

    conn = sqlite3.connect('qp_gen.db')
    # Create cursor
    c = conn.cursor()

    lst = c.execute("select * from questions;")
    list1=c.fetchall()
    print (list1)
    selectedQ = []
    finalQ=[]
    print( "selectedQ : ", selectedQ)

    for i in range(len(list1)-1):
        r = randomgenerate(0, len(list1) - 1)
        print("r:",r)
        selectedQ.append(r)


    print("selectedq has: ",selectedQ)

    for num in selectedQ:
        if num not in finalQ:
            finalQ.append(num)

    print("finalQ : ", finalQ)

    for i in finalQ:
        selectedQS.append(list1[i])


    print ("selectedQS has : ", selectedQS)


    # save changes
    conn.commit()
    # close the connection
    conn.close()

    pdf.add_page()

    pdf.set_font("Times", size=20)

    pdf.cell(200, 15, "Care International School", ln=1, align="C")
    pdf.set_font("Times", 'i', size=17)

    pdf.cell(200, 15, exam + "Examination", ln=1, align="C")
    pdf.set_font("Times", 'i', size=15)
    pdf.cell(167, 15, "Max Marks : 25", align="left")
    pdf.cell(100, 15, "Time : 1.5 Hours", ln=1, align="right")
    pdf.set_font("Arial", 'b', size=16)
    pdf.cell(134, 15, "Answer Any FIVE Questions", ln=1, align="left")
    pdf.cell(134, 15, "Each Question Carries FIVE Marks", ln=2, align="left")

    pdf.set_font("Times", size=13)

    for i in range(8):
        pdf.cell(170, 8, "Q" + str(i+1) + ": " +'%s' % selectedQS[i], ln=1, align="left")

    pdf.output("file.pdf")



def gen_pdf50():

    global exam
    global selectedQ

    # =============================Extract Questions=========================

    conn = sqlite3.connect('qp_gen.db')
    # Create cursor
    c = conn.cursor()

    lst = c.execute("select * from questions;")
    list1=c.fetchall()
    print (list1)
    selectedQ = []
    finalQ=[]
    print( "selectedQ : ", selectedQ)

    for i in range(len(list1)-1):
        r = randomgenerate(0, len(list1) - 1)
        print("r:",r)
        selectedQ.append(r)


    print("selectedq has: ",selectedQ)

    for num in selectedQ:
        if num not in finalQ:
            finalQ.append(num)

    print("finalQ : ", finalQ)

    for i in finalQ:
        selectedQS.append(list1[i])


    print ("selectedQS has : ", selectedQS)


    # save changes
    conn.commit()
    # close the connection
    conn.close()




    pdf.add_page()
    pdf.set_font("Times", size=20)

    pdf.cell(200, 15, "Care International School", ln=1, align="C")
    pdf.set_font("Times", 'i', size=17)
    pdf.cell(200, 15, exam + "Examination", ln=1, align="C")
    pdf.set_font("Times", 'i', size=14)
    pdf.cell(167, 15, "Max Marks : 50", align="left")
    pdf.cell(100, 15, "Time : 3 Hours", ln=1, align="right")
    pdf.set_font("Arial", 'b', size=16)
    pdf.cell(134, 15, "Answer All Questions",ln=1, align="c")
    pdf.cell(134, 10, "Each Question Carries FIVE Marks",ln=2, align="c")

    pdf.set_font("Times", size=13)

    for i in range(10):
        pdf.cell(170, 8, "Q" + str(i + 1) + ": " + '%s' % selectedQS[i], ln=1, align="left")



    pdf.output("file.pdf")
#============================================Menu creation=================================================================


#Creating menubar
my_menu =Menu(root)
root.config(menu=my_menu)



# adding Menu items

user_menu = Menu(my_menu)
my_menu.add_cascade(label="User", menu=user_menu)


user_menu.add_command(label="New user", command=register)
user_menu.add_command(label="Existing user", command=login)

user_menu.add_separator()
user_menu.add_command(label="Exit", command=iquit)

options_menu = Menu(my_menu)
my_menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Add Question", command=addquest)
options_menu.add_command(label="Generator", command=generate)
my_menu.entryconfig(2, state= DISABLED)
my_menu.add_command(label="Exit", command=iquit)



root.mainloop()

