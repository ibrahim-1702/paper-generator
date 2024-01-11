# =================================IMPORTING MODULES=====================================================================

import random
import fpdf
from tkinter import *
from tkinter import messagebox as ms
import mysql.connector

#===================================CREATING PDF FORMAT=================================================================
pdf = fpdf.FPDF(format='letter')

#======================================CREATING ROOT===================================================================

root = Tk()
root.title('Care International - QUESTION PAPER GENERATOR')
root.iconbitmap('D:\python_projects_pycharm\projectnew_ibu12cs\care.ico')
root.geometry("650x650+120+120")

# ======================================================DECLARING GLOBAL VARIABLES========================================
clicked = StringVar()
username = StringVar()
password = StringVar()
question = StringVar()
marks = IntVar()
examname = StringVar()
selectedQ = []
selectedQS = []
exam = StringVar()

# ====================================DATABASE CREATION ================================================================

# create connection to mysql
conn = mysql.connector.connect(host = "localhost",user="root",passwd = "password123",database = "QPgeneration")


#create cursor
c = conn.cursor()

# create database
#c.execute("CREATE DATABASE QPgeneration")


#create user login table with fields username and password
c.execute(""" create table if not exists userlogin (
        username varchar(225) not null,
        password varchar(225) not null
          ) """)

# Create cursor
c = conn.cursor()

#create question table
c.execute(""" create table if not exists questions(
        question varchar(100) not null
           ) """)


# =================================FUNCTIONS=============================================================================

def randomgenerate(low, high):  # Random number generator function: to generate random question numbers
    return random.randint(low, high)


def addquest():   # Widgets for adding questions using new window: Question Window
    global question

    # new Window creation
    QuestionWindow = Toplevel(root)
    QuestionWindow.title('Question Paper Generator: Adding New Questions')
    QuestionWindow.iconbitmap('D:\python_projects_pycharm\projectnew_ibu12cs\care.ico')
    QuestionWindow.geometry("750x650+120+120")

    #Textbox creation
    question = Entry(QuestionWindow, width=50, bd=3, font=('freesansbold', 10))
    question.grid(row=7, column=1, padx=10, pady=20, ipadx=20, ipady=10)

    # label creation
    heading_lbl = Label(QuestionWindow, text="Add New Questions To Database", font=('freesansbold', 20), padx=5, pady=15)
    heading_lbl.grid(row=4, column=1, sticky=W)

    question_lbl = Label(QuestionWindow, text="Enter Question: ", font=('calibri', 18))
    question_lbl.grid(row=7, column=0, padx=50, pady=20, sticky=W)

    # Buttons
    question_btn = Button(QuestionWindow, text="ADD QUESTION", font=('calibri', 15), command=addquestion)
    question_btn.grid(row=21, column=0, columnspan=1, pady=20, padx=20, ipadx=50)

    cancel1_btn = Button(QuestionWindow, text="CANCEL", font=('calibri', 15), command=cancel1)
    cancel1_btn.grid(row=21, column=1, columnspan=1, pady=20, padx=10, ipadx=50)

    x_btn = Button(QuestionWindow, text="EXIT", font=('calibri', 22), command=iquit)
    x_btn.grid(row=22, column=0, columnspan=2, padx=25, ipadx=50)

    '''    
    x_btn = Button(QuestionWindow, text="view", font=('calibri', 22), command=viewtableQ)
    x_btn.grid(row=23, column=0, columnspan=2, padx=25, ipadx=50)
    '''

def addquestion():  # function to add questions after checking for uniqueness of questions.
    global question

    if len(question.get()) == 0:
        ms.showerror("Error", "All fields are required")

        question.delete(0, END)
        question.focus_set()

    else:

        # Create  cursor
        c = conn.cursor()

        search_question = question.get()

        sql1 = "select * from questions where question = %s"
        name1 = (search_question,)
        rows1 = c.execute(sql1, name1)
        rows1 = c.fetchall()


        if rows1:
            ms.showerror("Existing Question", "Enter a Different Question")

            question.delete(0, END)
            question.focus_set()

        else:

            c = conn.cursor()
            sql_cmd1 = "insert into questions(question) values (%s)"
            values1 = (question.get(),)
            c.execute(sql_cmd1, values1)


            ms.showinfo("Success", "Question Added")

            question.delete(0, END)
            question.focus_set()

            # Saving the inserted questions
            conn.commit()

# Registering a new user function

def register():
    global username
    global password

    #creating new window
    regWindow = Toplevel(root)
    regWindow.title('Question Paper Generator: New User Registration Form')
    regWindow.iconbitmap('D:\python_projects_pycharm\projectnew_ibu12cs\care.ico')
    regWindow.geometry("650x650+120+120")

    # creating textboxes
    username = Entry(regWindow, width=31, bd=3,  font=('freesansbold', 10))
    username.grid(row=7, column=1, padx=10, pady=20, ipadx=20, ipady=10)

    password = Entry(regWindow, show="*", width=31, bd=3,  font=('freesansbold', 10))
    password.grid(row=9, column=1, ipadx=20, ipady=10)

    # label creation
    head_lbl1 = Label(regWindow, text="Enter New User Details", font=('freesansbold', 20), padx=5, pady=15)
    head_lbl1.grid(row=4, column=1)

    user_lbl = Label(regWindow, text="Username: ", font=('calibri', 18))
    user_lbl.grid(row=7, column=0, padx=50, pady=20, sticky=W)

    password_lbl = Label(regWindow, text="Password: ", font=('calibri', 18))
    password_lbl.grid(row=9, column=0, padx=50, sticky=W)

    # Buttons
    Reg_btn = Button(regWindow, text="REGISTER", font=('calibri', 20), command=newuser)
    Reg_btn.grid(row=21, column=0, columnspan=1, pady=20, padx=20, ipadx=50)

    cancel_btn = Button(regWindow, text="CANCEL", font=('calibri', 22), command=cancel)
    cancel_btn.grid(row=21, column=1, columnspan=1, pady=20, padx=10, ipadx=50)

    x_btn = Button(regWindow, text="EXIT", font=('calibri', 22), command=iquit)
    x_btn.grid(row=22, column=0, columnspan=2, padx=25, ipadx=50)

    '''
    x1_btn = Button(regWindow, text="View", font=('calibri', 22), command=viewtable)
    x1_btn.grid(row=25, column=0, columnspan=2, padx=25, ipadx=50)
    '''

def iquit(): # function to quit after confirmation
    quitting = ms.askyesno("QP Generator", "Do you want to exit")
    print(quitting)
    if quitting > 0:
        root.destroy()
        return

def cancel(): # function to clear the textboxes

    username.delete(0, END)
    password.delete(0, END)

    username.focus_set() # set focus to username text box


def cancel1():

    question.delete(0, END) # to clear question text box

    question.focus_set() # set focus to question text box

def cancel2():

    examname.delete(0, END) # to clear question text box

    drop.focus_set() # set focus to question text box

'''
def viewtable():
    
    # Create cursor
    c = conn.cursor()
    lst = c.execute("select * from userlogin;")
    lst=c.fetchall()
    for i in lst:
        print(i)

    # save changes
    #conn.commit()

    # close the connection
    #conn.close()


def viewtableQ():
    # create connection to db
    #conn = sqlite3.connect('qp_gen.db')
    # Create cursor
    c = conn.cursor()

    lst = c.execute("select * from questions;")
    lst=c.fetchall()
    for i in lst:
        print(i)

    # save changes
    #conn.commit()

    # close the connection
    #conn.close()
'''

def newuser(): # To create a new user - Registeration

    #to check if textboxes are empty
    if len(username.get()) == 0 or len(password.get()) == 0:
        ms.showerror("Error", "Fields cannot be empty")

        username.delete(0, END)
        password.delete(0, END)

        username.focus_set()
    else:
        # To check if user is existing
        # Create cursor
        c = conn.cursor()

        search_user = username.get()

        sql2 = "select * from userlogin where username = %s"
        name2 = (search_user,)
        rows2= c.execute(sql2,name2)

        rows2 = c.fetchall()

        if not rows2:

            c = conn.cursor()

            sql_cmd = "insert into userlogin(username, password) values (%s,%s)"
            values = (username.get(),password.get())
            c.execute(sql_cmd, values)

            ms.showinfo("Success", "User Registered")

            #Save the rows in database
            conn.commit()

            # clear textboxes
            username.delete(0, END)
            password.delete(0, END)

        else:
            ms.showinfo("Error", "User already exists")

            username.delete(0, END)
            password.delete(0, END)

            username.focus_set()


# function to create login form of existing user

def login():
    global username
    global password

    # Create new window
    existingUser = Toplevel(root)
    existingUser.title('Question Paper Generator: Login Form')
    existingUser.iconbitmap('D:\python_projects_pycharm\projectnew_ibu12cs\care.ico')
    existingUser.geometry("650x650+120+120")

    #textbox creation
    username = Entry(existingUser, font=('freesansbold', 10), width=31, bd=3)
    username.grid(row=7, column=1, padx=10, pady=20, ipadx=20, ipady=10,sticky=W)

    password = Entry(existingUser, show="*", font=('freesansbold', 10), width=31, bd=3)
    password.grid(row=9, column=1, padx=10, pady=20, ipadx=20, ipady=10,sticky=W)

    # label creation
    head_lbl1 = Label(existingUser, text="Enter Existing User Details", font=('freesansbold', 20), padx=5, pady=15)
    head_lbl1.grid(row=4, column=1, sticky=W)

    user_lbl = Label(existingUser, text="Username: ", font=('calibri', 18))
    user_lbl.grid(row=7, column=0, padx=50, pady=20, sticky=W)

    password_lbl = Label(existingUser, text="Password: ", font=('calibri', 18))
    password_lbl.grid(row=9, column=0, padx=50, sticky=W)

    # Buttons
    Reg_btn = Button(existingUser, text="LOGIN", font=('calibri', 22), command=existingLogin)
    Reg_btn.grid(row=21, column=0, columnspan=1, pady=20, padx=20, ipadx=50)

    cancel_btn = Button(existingUser, text="CANCEL", font=('calibri', 22), command=cancel)
    cancel_btn.grid(row=21, column=1, columnspan=1, pady=20, padx=10, ipadx=50)

    x_btn = Button(existingUser, text="EXIT", font=('calibri', 22), command=iquit)
    x_btn.grid(row=22, column=0, columnspan=2, padx=25, ipadx=50)


def existingLogin(): # function to authenticate user and permit login

    global username
    global password

    username.focus_set()

    if len(username.get()) == 0 or len(password.get()) == 0:
        ms.showerror("Error", "All fields are required")

        username.delete(0, END)
        password.delete(0, END)

        username.focus_set()

    else:
        # Create  cursor
        c = conn.cursor()

        search_user = username.get()
        search_passwd = password.get()
        sql= "select * from userlogin where username = %s and password=%s"
        name=(search_user,search_passwd)
        rows =c.execute(sql,name)
        rows = c.fetchall()

        if not rows:
            ms.showerror("Error", "Invalid Username or Password")

            username.delete(0, END)
            password.delete(0, END)
            username.focus_set()

        else:
            new_user=username.get()
            ms.showinfo("Login Success", " QP Generation Allowed")
            displaylbl = Label(root, text="Welcome " + new_user.upper(),font=('calibri', 25) )
            displaylbl.pack()
            my_menu.entryconfig(2, state='normal')
            my_menu.entryconfig(1, state=DISABLED)


def generate(): # Question Paper Generator

    global clicked
    global examname

    # creating new window
    generateWindow = Toplevel(root)
    generateWindow.title('Question Paper Generation')
    generateWindow.iconbitmap('D:\python_projects_pycharm\projectnew_ibu12cs\care.ico')
    generateWindow.geometry("700x650+120+120")

    # text box
    examname = Entry(generateWindow,font=('freesansbold', 10), bd=3, width=50)
    examname.grid(row=12, column=1, padx=2, pady=5, ipadx=2, ipady=10)

    # labels
    head1_lbl = Label(generateWindow, text="Enter Details for PDF Generation", font=('freesansbold', 20), padx=5, pady=15)
    head1_lbl.grid(row=4, column=1, sticky=W)

    marks_lbl = Label(generateWindow, text="Total Marks :    ", font=('freesansbold', 20), padx=5, pady=5)
    marks_lbl.grid(row=6, column=0, ipadx=10, ipady=10)



    # creating a list

    options = ['25', '50', ]
    clicked = StringVar()
    clicked.set("Choose Marks")

    drop = OptionMenu(generateWindow, clicked, *options, command=selected)
    drop.grid(row=6, column=1, ipady=10, ipadx=5)


    #Label
    examname_lbl = Label(generateWindow, text="Examination : ", font=('freesansbold', 20), padx=5, pady=5)
    examname_lbl.grid(row=12, column=0, ipadx=5, ipady=5)


    # Button
    Gen_btn = Button(generateWindow, text="GENERATE QP", font=('freesansbold', 15), command=qp_generate)
    Gen_btn.grid(row=15, column=0, columnspan=1, pady=10, padx=10, ipady=10, ipadx=50,sticky=E)

    cancel_btn = Button(generateWindow, text="CANCEL", font=('calibri', 22), command=cancel2)
    cancel_btn.grid(row=15, column=1, columnspan=1, pady=20, padx=10, ipadx=50)


    Quit_btn = Button(generateWindow, text="EXIT", font=('freesansbold', 15), command=iquit)
    Quit_btn.grid(row=17, column=0, columnspan=2, pady=30, padx=30, ipady=10, ipadx=20)




def selected(event): # Action taken when option is selected
    global clicked
    global marks
    if clicked.get() == '25':
        marks = 25
    else:
        marks = 50


# function qp_generate

def qp_generate():
    global marks
    global exam
    global examname
    global clicked
    my_menu.entryconfig(2, state=DISABLED)
    exam = examname.get()
    #exam.upper()
    if len(examname.get()) == 0 or len(clicked.get()) == None:
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


def gen_pdf25(): # PDF generation for 25 marks
    global exam
    global selectedQ

    #my_menu.entryconfig(2, state=DISABLED)

    # =============================Extract Questions=========================


    # Create cursor
    c = conn.cursor()

    lst = c.execute("select * from questions;")
    list1 = c.fetchall()

    #list creation for adding questions.
    selectedQ = []
    finalQ = []

    # using random generate to get random question numbers
    # and appending the corresponding questions from the questions table into selectedQ.

    for i in range(len(list1) - 1):
        r = randomgenerate(0, len(list1) - 1)
        #print("r:", r)
        selectedQ.append(r)

    # creating the final list of questions by removing the redundant questions

    for num in selectedQ:
        if num not in finalQ:
            finalQ.append(num)

    for i in finalQ:
        selectedQS.append(list1[i])


    #Creating the pdf file by adding values at required locations.

    pdf.add_page()

    pdf.set_font("Times", size=20)

    pdf.cell(200, 15, "Care International School", ln=1, align="C")
    pdf.set_font("Times", 'i', size=17)

    pdf.cell(200, 15, exam.upper() + " EXAMINATION", ln=1, align="C")
    pdf.set_font("Times", 'i', size=15)
    pdf.cell(167, 15, "Max Marks : 25", align="left")
    pdf.cell(100, 15, "Time : 1.5 Hours", ln=1, align="right")
    pdf.set_font("Arial", 'b', size=16)
    pdf.cell(134, 15, "Answer Any FIVE Questions", ln=1, align="left")
    pdf.cell(134, 15, "Each Question Carries FIVE Marks", ln=2, align="left")

    pdf.set_font("Times", size=13)

    for i in range(8):
        pdf.cell(170, 8, "Q" + str(i + 1) + ": " + '%s' % selectedQS[i], ln=1, align="left")

   #creating the output file
    pdf.output("QP_25_marks.pdf")
    #ms.showinfo("Success","QP_25_marks.pdf has been generated Successfully")
    #root.destroy()

    dislbl1 = Label(root, text="\n\nThank You For Using \n QUESTION PAPER GENERATOR \n\n", font=('calibri', 15))
    dislbl1.pack()

    dislbl2 = Label(root,text="QP_25_marks.pdf \n HAS BEEN GENERATED SUCCESSFULLY \n\n", font=('calibri', 15))
    dislbl2.pack()


    displaybutton = Button(root, text= "OK", font=('calibri', 25), command=root.quit)
    displaybutton.pack()

    displaybutton.focus_set()


# generation of 50 marks Question Paper
def gen_pdf50():
    global exam
    global selectedQ

    # =============================Extract Questions====================================================================


    # Create cursor
    c = conn.cursor()

    lst = c.execute("select * from questions;")
    list1 = c.fetchall()

    #creating lists
    selectedQ = []
    finalQ = []

    # using random generate to get random question numbers
    # and appending the corresponding questions from the questions table into selectedQ
    for i in range(len(list1) - 1):
        r = randomgenerate(0, len(list1) - 1)
        selectedQ.append(r)

    # creating the final list of questions by removing the redundant questions no.
    for num in selectedQ:
        if num not in finalQ:
            finalQ.append(num)


    for i in finalQ:
        selectedQS.append(list1[i])


    # Creating the pdf file by adding values at required locations.
    pdf.add_page()
    pdf.set_font("Times", size=20)

    pdf.cell(200, 15, "Care International School", ln=1, align="C")
    pdf.set_font("Times", 'i', size=17)
    pdf.cell(200, 15, exam.upper() + " EXAMINATION", ln=1, align="C")
    pdf.set_font("Times", 'i', size=14)
    pdf.cell(167, 15, "Max Marks : 50", align="left")
    pdf.cell(100, 15, "Time : 3 Hours", ln=1, align="right")
    pdf.set_font("Arial", 'b', size=16)
    pdf.cell(134, 15, "Answer All Questions", ln=1, align="c")
    pdf.cell(134, 10, "Each Question Carries FIVE Marks", ln=2, align="c")

    pdf.set_font("Times", size=13)

    # Attaching the questions
    for i in range(10):
        pdf.cell(170, 8, "Q" + str(i + 1) + ": " + '%s' % selectedQS[i], ln=1, align="left")

    # creating the output file
    pdf.output("QP_50_marks.pdf")


    dislbl1 = Label(root, text="\n\nThank You For Using \n QUESTION PAPER GENERATOR \n\n", font=('calibri', 15))
    dislbl1.pack()

    dislbl2 = Label(root, text="QP_50_marks.pdf \n HAS BEEN GENERATED SUCCESSFULLY \n\n", font=('calibri', 15))
    dislbl2.pack()

    displaybutton = Button(root, text="OK",font=('calibri',15), command=root.quit)
    displaybutton.pack()

    displaybutton.focus_set()


#================================================CREATING MENUS IN THE ROOT WINDOW======================================

# Creating menubar
my_menu = Menu(root)
root.config(menu=my_menu)

# adding Menu items


user_menu = Menu(my_menu) # creating user menu
my_menu.add_cascade(label="User", menu=user_menu)

#sub menu under user menu
user_menu.add_command(label="New user", command=register)
user_menu.add_command(label="Existing user", command=login)

user_menu.add_separator() # add a separator
user_menu.add_command(label="Exit", command=iquit)

# Creating Options menu
options_menu = Menu(my_menu)
my_menu.add_cascade(label="Options", menu=options_menu)

#Creating submenu under options menu
options_menu.add_command(label="Add Question", command=addquest)
options_menu.add_command(label="Generator",command=generate)

#disabling options menu for authentication of user.
my_menu.entryconfig(2, state=DISABLED)

my_menu.add_command(label="Exit", command=iquit)




#mainloop() tells Python to run the Tkinter event loop.
# This method listens for events,(button clicks or keypresses)
root.mainloop()

