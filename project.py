from tkinter import *
from tkinter import filedialog, messagebox
import mysql.connector
import os

mydb = mysql.connector.connect(host="localhost", user="Runali", passwd="12345", database="sample",\
auth_plugin="mysql_native_password")                               
cursor = mydb.cursor()

def savedata():
    fn = filedialog.askopenfilename(title="Select File", filetypes=(("Image File", "*.jpg"),("All Files", "*.*")))
    with open(fn, "rb") as f:
     data = f.read()
    sql = "INSERT INTO files(id, file_data, date) VALUES(NULL, %s, NOW())"                                                                                           
    cursor.execute(sql, (data, ))
    mydb.commit()
    messagebox.showinfo("Success!", "your file has been saved to database")
                                                                                             
def readdata():
    fn = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Save File", filetypes=(("Image File", "*.jpg"),\
    ("All Files", "*.*")))
    sql = "SELECT file_data FROM files LIMIT 1"
    cursor.execute(sql)
    r = cursor.fetchall()
    for i in r:
        data = i[0]
        
    with open(fn, "wb") as f:
        f.write(data)
    f.close()
    messagebox.showinfo("Success", "File has been saved.")
    
    
win = Tk()
Button(win, text="Save File To Database", command=savedata).pack()
Button(win, text="Read File From Database", command=readdata).pack()


win.geometry("200*200")
win.title("Binary data Read/write to MYSQL")
win.mainloop()
