import sqlite3

conn = sqlite3.connect('qp_gen.db')
# Create cursor
c = conn.cursor()
# c.execute('''delete from userlogin where username="alam";''')
c.execute('''delete from questions where question ="";''')
conn.commit()
conn.close()

conn = sqlite3.connect('qp_gen.db')
# Create cursor
c = conn.cursor()


lst = c.execute("select * from questions;")
list1=c.fetchall()
print (list1)