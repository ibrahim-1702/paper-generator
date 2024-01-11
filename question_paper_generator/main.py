from tkinter import *
from tkinter import messagebox as ms
#from PIL import ImageTK,Image
import sqlite3


root =Tk()
root.title('Care International')
root.iconbitmap('d:\projectnew\care.ico')
root.geometry("550x500")
clicked = StringVar()
#====================================DATABASE CONNECTION================================================================
# create connection to db
conn = sqlite3.connect('qp_gen.db')
#Create cursor
c=conn.cursor()

c.execute(""" create table if not exists userlogin (
        username text not null,
        password text not null
           ) """)

#=================================FUNCTIONS=============================================================================

#create registering a new user function
def newuser():
    root.title = "Registration of New User"

    if len(username.get())==0 or len(password.get())==0:
       ms.showerror("Error", "Fields cannot be empty")

       username.delete(0, END)
       password.delete(0, END)

       username.focus_set()
    else:
        '''conn = sqlite3.connect('qp_gen.db')
       c = conn.cursor()

       c.execute("select * from userlogin where username = :username and password =:password",
                 {'username' : username.get(),
                  'password' : password.get()})
       rows=c.fetchall()


       if rows == []:
           ms.showerror("Error","Invalid Username or Password")

           username.delete(0, END)
           password.delete(0, END)
           username.focus_set()'''

        conn = sqlite3.connect('qp_gen.db')
        # Create cursor
        c = conn.cursor()
       # usernamecheck = c.execute("SELECT COUNT(*) FROM userlogin WHERE username = :username",
        #                          { 'username' : username.get()
         #                         } )
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
            ms.showinfo("Success", "User Registered")
            # Create a SQL connection to our SQLite database


            # The result of a "cursor.execute" can be iterated over by row
            for row in c.execute("SELECT * FROM  userLogin"):
                ms.showinfo( print(row))

            conn.commit()

            # close the connection
            conn.close()
            #clear textboxes
            username.delete(0, END)
            password.delete(0, END)

        else:
            ms.showinfo("Error", "User already exists")

            username.delete(0, END)
            password.delete(0, END)

            username.focus_set()





def iquit():
    quitting= ms.askyesno("QP Generator","Do you want to exit")
    if quitting >0:
        root.destroy()
        return





# create login
def login():

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
           ms.showinfo("Success", "Login Success")
           Reg_btn.grid_forget()
           Login_btn.grid_forget()

           loginWindow = Toplevel(root)
           loginWindow.title ('Care International - QP Generator')
           loginWindow.iconbitmap('d:\projectnew\care.ico')
           loginWindow.geometry ("650x500")



           #text box
           examname = Entry(loginWindow, width=50)
           examname.grid(row=5, column=1, padx=20, ipadx=10,ipady=10)
           #labels
           head1_lbl = Label(loginWindow , text="Question Paper Generator", font=('freesansbold', 20), padx=5, pady=5)
           head1_lbl.grid(row=2, column=1,ipadx=10, ipady=10)

           marks_lbl = Label(loginWindow , text="Total Marks :    ", font=('freesansbold', 20), padx=5, pady=5)
           marks_lbl.grid(row=4, column=0, ipadx=10, ipady=10)


           options =['50','100',]
           clicked=StringVar()
           clicked.set("Choose Marks")

           drop=OptionMenu(loginWindow, clicked, *options, command=selected)
           drop.grid(row = 4, column= 1, ipady=10, ipadx=5)

           examname_lbl = Label(loginWindow , text="Examination : ", font=('freesansbold', 20), padx=5, pady=5)
           examname_lbl.grid(row=5, column=0, ipadx=10, ipady=10)
           # Button
           Gen_btn = Button(loginWindow ,text="Generate QP", font=('freesansbold', 20), command = qp_generate)
           Gen_btn.grid(row=8, column=0, columnspan=1, pady = 10, padx=10,ipady=10,ipadx=50)

           Quit_btn = Button(loginWindow, text="Exit", font=('freesansbold', 20), command = iquit)
           Quit_btn.grid(row=8, column=1, columnspan=2, pady=10, padx=10, ipady=10,ipadx=50)



def viewtable():
    # create connection to db
    conn = sqlite3.connect('qp_gen.db')
    # Create cursor
    c = conn.cursor()
    #c.execute('''delete from userlogin where username="alam";''')
    lst=c.execute("select * from userlogin;")

    for i in lst:
        print (i)


    # save changes
    conn.commit()

    # close the connection
    conn.close()


def qp_generate():
    pass

def selected(event):
    global clicked
    if clicked.get() == '50':
        marks='50'
    else:
        marks = '100'

#Text box creation
username =Entry(root, width=31, bd=3)
username.grid(row=7,column=1, padx=10, pady=20,ipadx=20, ipady=10)
password =Entry(root, show = "*", width=31,bd = 3 )
password.grid(row=9,column=1, ipadx=20, ipady=10)

# label creation
head_lbl1 =Label(root,text ="Register/Login", font = ('freesansbold',20 ),padx=5,pady=15)
head_lbl1.grid(row =4, column = 1, sticky = W )
#head_lbl2 =Label(root,text =" & Login Form", font = ('freesansbold',20 ),pady=15)
#head_lbl2.grid(row =4, column = 1, sticky = W )

user_lbl =Label(root, text="Username: ", font = ('calibri',18 ))


password_lbl =Label(root, text="Password: ", font = ('calibri',18 ))
password_lbl.grid(row=9,column=0, padx=50, sticky = W)

# Buttons
Reg_btn = Button(root,text="Register", font = ('calibri',22 ),command = newuser)
Reg_btn.grid(row=21, column=0, columnspan=1, pady = 20, padx=20,ipadx=50)

Login_btn = Button(root,text="Login", font = ('calibri',22 ),command = login)
Login_btn.grid(row=21, column=1, columnspan=1, pady = 20, padx=10,ipadx=50)

x_btn = Button(root,text="Exit",font = ('calibri',22 ), command = iquit)
x_btn.grid(row=22, column=0, columnspan=2, padx=25,ipadx=50)

x1_btn = Button(root,text="View",font = ('calibri',22 ), command = viewtable)
x1_btn.grid(row=25, column=0, columnspan=2, padx=25,ipadx=50)

# save changes
conn.commit()

#close the connection
conn.close()


root.mainloop()