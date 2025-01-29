from tkinter import *
from PIL import Image, ImageTk # pip install pillow
from tkinter import messagebox, ttk
import sqlite3
class studentClass:
  def __init__(self, root):
    self.root = root
    self.root.title("Result Management System")
    self.root.geometry("1200x480+80+170")
    self.root.config(bg="white")
    self.root.focus_force()
    
    #=======Title=======
    title = Label(self.root, text="Manage Course", font=("goudy old style", 20, "bold"), bg="#033054", fg="white").place(x=10, y=15, width=1180, height=35)
    #=======Variables=======
    self.var_roll = StringVar()
    self.var_name = StringVar()
    self.var_email = StringVar()
    self.var_gender = StringVar()
    self.var_dob = StringVar()
    self.var_contact = StringVar()
    self.var_course = StringVar()
    self.var_a_date = StringVar()
    self.var_state = StringVar()
    self.var_city = StringVar()
    self.var_pin = StringVar()
    #=======Widgets=======
    #=======column1=======
    lbl_roll = Label(self.root, text="Roll No.", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=60)
    lbl_name = Label(self.root, text="Name", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=100)
    lbl_Email = Label(self.root, text="Email", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=140)
    lbl_Gender = Label(self.root, text="Gender", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=180)
    lbl_State = Label(self.root, text="State", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=220)
    txt_State=Entry(self.root, textvariable=self.var_state, font=("goudy old style", 15, "bold"), bg="lightyellow").place(x=150, y=220, width=200)
    lbl_address = Label(self.root, text="Address", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=260)
    #=======Entry=======
    
    self.txt_roll=Entry(self.root, textvariable=self.var_roll, font=("goudy old style", 15, "bold"), bg="lightyellow")
    self.txt_roll.place(x=150, y=60, width=200)
    
    txt_name = Entry(self.root, textvariable=self.var_name,  font=("goudy old style", 15, "bold"), bg="lightyellow").place(x=150, y=100, width=200)
    txt_Email = Entry(self.root,textvariable=self.var_email,  font=("goudy old style", 15, "bold"), bg="lightyellow").place(x=150, y=140, width=200)
    self.txt_gender = ttk.Combobox(self.root,textvariable=self.var_gender,values=("Select","Male","female","Other"),font=("goudy old style", 15, "bold"),state='readonly',justify=CENTER)
    self.txt_gender.place(x=150, y=180, width=200) 
    self.txt_gender.current(0)
    txt_dob=Entry(self.root, textvariable=self.var_dob, font=("goudy old style", 15, "bold"), bg="lightyellow")


    #=========column2=======
    lbl_dob = Label(self.root, text="D.O.B", font=("goudy old style", 15, "bold"), bg="white").place(x=360, y=60)
    lbl_contact = Label(self.root, text="Contact", font=("goudy old style", 15, "bold"), bg="white").place(x=360, y=100)
    lbl_addmission = Label(self.root, text="Addmission", font=("goudy old style", 15, "bold"), bg="white").place(x=360, y=140)
    lbl_Course = Label(self.root, text="Course", font=("goudy old style", 15, "bold"), bg="white").place(x=360, y=180)
     
      #=======Entry=======
    self.course_list=["Empty"]
    #functioncall to update the list

    txt_dob=Entry(self.root, textvariable=self.var_dob, font=("goudy old style", 15, "bold"), bg="lightyellow")
    self.txt_roll.place(x=480, y=60, width=200)
    
    txt_contact = Entry(self.root, textvariable=self.var_contact,  font=("goudy old style", 15, "bold"), bg="lightyellow").place(x=480, y=100, width=200)
    txt_addmission = Entry(self.root,textvariable=self.var_a_date,  font=("goudy old style", 15, "bold"), bg="lightyellow").place(x=480, y=140, width=200)
    self.txt_course = ttk.Combobox(self.root,textvariable=self.var_course,values=self.course_list,font=("goudy old style", 15, "bold"),state='readonly',justify=CENTER)
    self.txt_course.place(x=480, y=180, width=200)
    self.txt_course.current("0")
    
    #=======text address=====
    self.txt_address = Text(self.root,  font=("goudy old style", 15, "bold"), bg="lightyellow")
    self.txt_address.place(x=150, y=260, width=540, height=100)
    
    #=======Buttons=======
    self.btn_add = Button(self.root, text="Add", font=("goudy old style", 15, "bold"), bg="#2196f3", fg="white", cursor="hand2", command=self.add)
    self.btn_add.place(x=150, y=300, width=110, height=40)
    self.btn_update = Button(self.root, text="Update", font=("goudy old style", 15, "bold"), bg="#4caf50", fg="white", cursor="hand2", command=self.update)
    self.btn_update.place(x=270, y=300, width=110, height=40)
    self.btn_delete = Button(self.root, text="Delete", font=("goudy old style", 15, "bold"), bg="#f44336", fg="white", cursor="hand2", command=self.delete)
    self.btn_delete.place(x=390, y=300, width=110, height=40)
    self.btn_clear = Button(self.root, text="Clear", font=("goudy old style", 15, "bold"), bg="#607d8b", fg="white", cursor="hand2", command=self.clear)
    self.btn_clear.place(x=510, y=300, width=110, height=40)
    
    #=======Search Panel=======
    self.var_search = StringVar()
    lbl_search_courseName = Label(self.root, text="Course Name", font=("goudy old style", 15, "bold"), bg="white").place(x=720, y=60)
    txt_search_courseName = Entry(self.root, textvariable=self.var_search, font=("goudy old style", 15, "bold"), bg="lightyellow").place(x=870, y=60, width=180)
    btn_search = Button(self.root, text="Search", font=("goudy old style", 15, "bold"), bg="#03a9f4", fg="white", cursor="hand2", command=self.search).place(x=1070, y=60, width=120, height=28)
    
    #=======Content=======
    self.C_Frame = Frame(self.root, bd=2, relief=RIDGE)
    self.C_Frame.place(x=720, y=100, width=460, height=340)
    
    scrolly = Scrollbar(self.C_Frame, orient=VERTICAL)
    scrollx = Scrollbar(self.C_Frame, orient=HORIZONTAL)
    
    
    
    self.CourseTable = ttk.Treeview(self.C_Frame, columns=("cid", "name", "duration", "charges", "description"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
    scrollx.pack(side=BOTTOM, fill=X)
    scrolly.pack(side=RIGHT, fill=Y)
    scrollx.config(command=self.CourseTable.xview)
    scrolly.config(command=self.CourseTable.yview)
    
    
    self.CourseTable.heading('cid', text='Course ID')
    self.CourseTable.heading('name', text='Name')
    self.CourseTable.heading('duration', text='Duration')
    self.CourseTable.heading('charges', text='Charges')
    self.CourseTable.heading('description', text='Description')
    self.CourseTable["show"] = 'headings'
    
    self.CourseTable.column('cid', width=100)
    self.CourseTable.column('name', width=100)
    self.CourseTable.column('duration', width=100)
    self.CourseTable.column('charges', width=100)
    self.CourseTable.column('description', width=150)
    
    self.CourseTable.pack(fill=BOTH, expand=1)
    self.CourseTable.bind("<ButtonRelease-1>", self.get_data)
    
    self.show()
    
    
    
#=========================================================================

#clear
def clear(self):
    self.show()
    self.var_roll.set("")
    self.var_duration.set("")
    self.var_search.set("")
    self.var_charges.set("")
    self.txt_description.delete('1.0', END)
    self.txt_roll.config(state='normal')
    
def delete(self):
    con=sqlite3.connect(database="RMS.db")
    cur=con.cursor()
    try:
        if self.var_roll.get()=="" or self.var_duration.get()=="" or self.var_charges.get()=="":
           messagebox.showerror("Error", "Some Fields are Empty", parent=self.root)
        else:
            cur.execute("Select * from course where name=?",(self.var_roll.get(),))
            row=cur.fetchone()
        if row==None:
            messagebox.showerror("Error", "Select Course from List", parent=self.root)
        else:
            op=messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root)
        if op==True:
            cur.execute("DELETE FROM course WHERE name=?", (self.var_roll.get(),))
            con.commit()
            messagebox.showinfo("Success", "Course Deleted Successfully", parent=self.root)
            self.clear()
    except Exception as ex:
        messagebox.showerror("Error", f"Error due to: {str(ex)}")



def get_data(self, ev):
 self.txt_roll.config(state='readonly')
 self.txt_roll
 r=self.CourseTable.focus()
 content=self.CourseTable.item(r)
 row=content['values']
self.var_roll.set(row[1])
self.var_duration.set(row[2])
self.var_charges.set(row[3])
self.txt_description.delete('1.0', END)
self.txt_description.insert(END, row[4])


def add(self):
 con=sqlite3.connect(database="RMS.db")
cur=con.cursor()
try:
    if self.var_roll.get()=="" or self.var_duration.get()=="" or self.var_charges.get()=="":
        messagebox.showerror("Error", "Some Fields are Empty", parent=self.root)
    else:
        cur.execute("Select * from course where name=?",(self.var_roll.get(),))
        row=cur.fetchone()
        if row!=None:
            messagebox.showerror("Error", "Course Name Already Exists", parent=self.root)
        else:
            cur.execute("INSERT INTO course (name, duration, charges, description) values(?,?,?,?)", (
                self.var_roll.get(),
                self.var_duration.get(),
                self.var_charges.get(),
                self.txt_description.get('1.0', END)
            ))
            con.commit()
            messagebox.showinfo("Success", "Course Added Successfully", parent=self.root)
            self.show()
except Exception as ex:
    messagebox.showerror("Error", f"Error due to: {str(ex)}")
    
def update(self):
  con=sqlite3.connect(database="RMS.db")
  cur=con.cursor()
try:
    if self.var_roll.get()=="" or self.var_duration.get()=="" or self.var_charges.get()=="":
        messagebox.showerror("Error", "Some Fields are Empty", parent=self.root)
    else:
        cur.execute("Select * from course where name=?",(self.var_roll.get(),))
        row=cur.fetchone()
        if row==None:
            messagebox.showerror("Error", "Select Course from list", parent=self.root)
        else:
            cur.execute("UPDATE course SET  duration=?, charges=?, description=? WHERE name =?", (
                
                self.var_duration.get(),
                self.var_charges.get(),
                self.txt_description.get('1.0', END),
                self.var_roll.get(),
            ))
            con.commit()
            messagebox.showinfo("Success", "Course Updated Successfully", parent=self.root)
            self.show()
except Exception as ex:
    messagebox.showerror("Error", f"Error due to: {str(ex)}")


def show(self):
 con=sqlite3.connect(database="RMS.db")
cur=con.cursor()
try:
    cur.execute("Select * from course")
    rows=cur.fetchall()
    self.CourseTable.delete(*self.CourseTable.get_children())
    for row in rows:
        self.CourseTable.insert('', END, values=row)
except Exception as ex:
    messagebox.showerror("Error", f"Error due to: {str(ex)}")
    
def search(self):
  con=sqlite3.connect(database="RMS.db")
cur=con.cursor()
try:
    cur.execute(f"Select * from course where name like ?", ('%'+self.var_search.get()+'%',))
    rows=cur.fetchall()
    self.CourseTable.delete(*self.CourseTable.get_children())
    for row in rows:
        self.CourseTable.insert('', END, values=row)
except Exception as ex:
    messagebox.showerror("Error", f"Error due to: {str(ex)}")


        

if __name__ == "__main__":
    root = Tk()
    obj = studentClass(root)
    root.mainloop()