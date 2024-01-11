import mysql.connector

conn = mysql.connector.connect(host = "localhost",user="root",passwd = "password123",database = "QPgeneration")


#create cursor
c = conn.cursor()
'''
c.execute("insert into questions values ('Enumerate the features of Python.')")
c.execute("insert into questions values ('Describe the features of OOPs')")
c.execute("insert into questions values ('Describe Access Control in C++')")
c.execute("insert into questions values ('Describe the access Specifiers in C++')")
c.execute("insert into questions values ('Explain the Open source software.')")
c.execute("insert into questions values ('Distinguish Impact from non impact printers.')")
c.execute("insert into questions values ('Explain the various encoding systems')")
c.execute("insert into questions values ('Discuss the use of neural networks in AI.')")
c.execute("insert into questions values ('Describe Artificial Intelligence.')")
c.execute("insert into questions values ('Explain the different generations of computers.')")
c.execute("insert into questions values ('Explain Mobile computing.')")
c.execute("insert into questions values ('Define Internet how is it different from extranet?')")
c.execute("insert into questions values ('Explain uses of computers.')")
c.execute("insert into questions values ('Discuss IPO cycle.')")
c.execute("insert into questions values ('Explain Programming concepts.')")
c.execute("insert into questions values ('Explain the Viruses.')")
c.execute("insert into questions values ('Differentiate between hardware and software')")
c.execute("insert into questions values ('Explain the Input and output devices..')")
c.execute("insert into questions values ('Explain the components of a computer system.')")
c.execute("insert into questions values ('Differentiate between hardware and software')")
c.execute("insert into questions values ('Explain the Viruses.')")
c.execute("insert into questions values ('Explain Programming concepts.')")
c.execute("insert into questions values ('Discuss IPO cycle.')")
c.execute("insert into questions values ('Explain the components of Multimedia.')")
c.execute("insert into questions values ('Define Intranet and Explain its features')")
c.execute("insert into questions values ('Explain the different types of Cables in Networks')")
c.execute("insert into questions values ('Describe the types of Software.')")
c.execute("insert into questions values ('What is Robotics? Explain Expert Systems')")
c.execute("insert into questions values ('Discuss the various operators used in C++')")
c.execute("insert into questions values ('Explain the various data types in Python')")
c.execute("insert into questions values ('Distinguish audio from video file formats.')")
c.execute("insert into questions values ('Explain DBMS systems')")
c.execute("insert into questions values ('Explain ER model with an example.')")
c.execute("insert into questions values ('Describe RDBMS Data Model')")
c.execute("insert into questions values ('Describe the Laws of Boolean Algebra ')")
c.execute("insert into questions values ('Explain GUI and its importance')")
conn.commit()

'''

#c.execute("truncate table questions")
c.execute("select count(*) from questions")
row=c.fetchall()
print(row)
#for x in row:
 #   print(x)

# Create a SQL connection to our SQLite database
#    con = sqlite3.connect(dbfile)

