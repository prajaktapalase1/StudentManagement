from tkinter import *
from tkinter import ttk
from tkinter import ttk,messagebox
import pymysql


       
class Student:
    def __init__(self,root):
        self.root=root    
        self.root.title("Student Management")
        
        self.root.geometry("1350x700+0+0")
        title=Label(self.root,text="Student Management System",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg="yellow",fg="red")
        title.pack(side=TOP,fill=X)
        #========all variaables
        self.rollno_var=StringVar()
        self.name_var=StringVar()
        self.email_var=StringVar()
        self.DOB_var=StringVar()
        self.contact_var=StringVar()
        self.address_var=StringVar()
        
        self.search_by=StringVar()
        self.searchall=StringVar()
       
       

        manage_frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        manage_frame.place(x=20,y=100,width=450,height=560)
        detail_frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        detail_frame.place(x=500,y=100,width=750,height=560)
        m_title=Label(manage_frame,text="Manage Students",bg="crimson",fg="white",font=("times new roman",30,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)
       
        m_roll=Label(manage_frame,text="Roll No",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        m_roll.grid(row=1,column=0,pady=10,padx=10,sticky="w")

        txt_roll=Entry(manage_frame,textvariable=self.rollno_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_roll.grid(row=1,column=1,pady=10,padx=10,sticky="w")

        m_name=Label(manage_frame,text="Name",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        m_name.grid(row=2,column=0,pady=10,padx=10,sticky="w")

        txt_email=Entry(manage_frame,textvariable=self.name_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_email.grid(row=2,column=1,pady=10,padx=10,sticky="w")
        
        m_fdate=Label(manage_frame,text="Email",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        m_fdate.grid(row=3,column=0,pady=10,padx=10,sticky="w")

        txt_fdate=Entry(manage_frame,textvariable=self.email_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_fdate.grid(row=3,column=1,pady=10,padx=10,sticky="w")

        m_tdate=Label(manage_frame,text="Date of Birth",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        m_tdate.grid(row=4,column=0,pady=10,padx=10,sticky="w")

        txt_tdate=Entry(manage_frame,textvariable=self.DOB_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_tdate.grid(row=4,column=1,pady=10,padx=10,sticky="w")

        m_status=Label(manage_frame,text="Contact No",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        m_status.grid(row=5,column=0,pady=10,padx=10,sticky="w")

        txt_status=Entry(manage_frame,textvariable=self.contact_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_status.grid(row=6,column=1,pady=10,padx=10,sticky="w")
        
        m_status=Label(manage_frame,text="Address",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        m_status.grid(row=6,column=0,pady=10,padx=10,sticky="w")

        txt_status=Entry(manage_frame,textvariable=self.address_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_status.grid(row=5,column=1,pady=10,padx=10,sticky="w")

#============>button frame===========================================
        btn_frame=Frame(manage_frame,bd=4,relief=RIDGE,bg="crimson")
        btn_frame.place(x=10,y=450,width=430)
       
        Addbtn=Button(btn_frame,text="Add",width=10,command=self.add_student).grid(row=0,column=0,padx=10,pady=10)
        updatebtn=Button(btn_frame,text="Update",width=10,command=self.update_data).grid(row=0,column=1,padx=10,pady=10)
        delbtn=Button(btn_frame,text="Delete",width=10,command=self.delete_data).grid(row=0,column=2,padx=10,pady=10)
        clearbtn=Button(btn_frame,text="Clear",width=10,command=self.clear).grid(row=0,column=3,padx=10,pady=10)
#============detail frame============================================
        
        detail_frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        detail_frame.place(x=500,y=100,width=800,height=580)
       
        lbl_search=Label(detail_frame,text="Search By",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="w")
        combo_search=ttk.Combobox(detail_frame,textvariable=self.search_by,width=10,font=("times new roman",13,"bold"),state="readonly")
        combo_search['value']=("rollno","email")
        combo_search.grid(row=0,column=1,padx=20,pady=10)
        txt_search=Entry(detail_frame,textvariable=self.searchall,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
        txt_search.grid(row=0,column=2,padx=20,pady=10,sticky="w")

        searchbtn=Button(detail_frame,text="Search",width=10,command=self.searchdata).grid(row=0,column=3,padx=10,pady=10)
        showallbtn=Button(detail_frame,text="ShowAll",width=10,command=self.fetchdata).grid(row=0,column=4,padx=10,pady=10)
        
        table_frame=Frame(detail_frame,bd=4,relief=RIDGE,bg="crimson")
        table_frame.place(x=10,y=70,width=760,height=500)
         
        scroll_x=Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame,columns=("rollno","Name","Email","DOB","ContactNo","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading("rollno",text="roll no")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("DOB",text="DOB")
        self.student_table.heading("ContactNo",text="ContactNo")
        self.student_table.heading("Address",text="Address")
       
        self.student_table["show"]="headings"
        self.student_table.column("rollno",width=50)
        self.student_table.column("Name",width=100)
        self.student_table.column("Email",width=150)
        self.student_table.column("DOB",width=50)
        self.student_table.column("ContactNo",width=100)
        self.student_table.column("Address",width=150)
       
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetchdata()

    def add_student(self):
            if self.rollno_var.get()=="" or self.email_var.get()=="":
                    messagebox.showerror("Error","All Fields are Required")
            else:        
                 conn=pymysql.connect(host="localhost",user="root",password="",database="student_manage")
                 cur=conn.cursor()
                 cur.execute("INSERT INTO students(rollno,Name,Email,DOB,ContactNo,Address) VALUES ('%s','%s','%s','%s','%s','%s')" % (self.rollno_var.get(),self.name_var.get(),self.email_var.get(),self.DOB_var.get(),self.address_var.get(),self.contact_var.get())) 
                 conn.commit()
                 self.fetchdata()
                 self.clear()
                 conn.close()
                 messagebox.showinfo("Success","Record has been inserted")
    def fetchdata(self):
        conn=pymysql.connect(host="localhost",user="root",password="",database="student_manage")
        cur=conn.cursor()
        cur.execute("SELECT * FROM students") 
        rows=cur.fetchall()
        if len(rows)!=0:
                self.student_table.delete(*self.student_table.get_children())
                for row in rows:
                        self.student_table.insert("",END,values=row)
                conn.commit()
        conn.close()
    def clear(self):
            self.rollno_var.set("")
            self.name_var.set("")
            self.email_var.set("")
            self.DOB_var.set("")
            self.contact_var.set("")
            self.address_var.set("")
    
    def get_cursor(self,ev):
            cursor_row=self.student_table.focus()
            contents=self.student_table.item(cursor_row)
            row=contents["values"]
            self.rollno_var.set(row[0])
            self.name_var.set(row[1])
            self.email_var.set(row[2])
            self.DOB_var.set(row[3])
            self.contact_var.set(row[4])
            self.address_var.set(row[5])
    def update_data(self):
        conn=pymysql.connect(host="localhost",user="root",password="",database="student_manage")
        cur=conn.cursor()
        cur.execute("""UPDATE students SET  Name=%s, Email=%s, DOB=%s,contactNo=%s,Address=%s where rollno=%s""",(self.name_var.get(),self.email_var.get(),self.DOB_var.get(),self.contact_var.get(),self.address_var.get(),self.rollno_var.get()))   
        conn.commit()
        self.fetchdata()
        self.clear()
        conn.close()
        messagebox.showinfo("Success","Record has been Updated")
  
    def delete_data(self):
        conn=pymysql.connect(host="localhost",user="root",password="",database="student_manage")
        cur=conn.cursor()
        cur.execute("DELETE  FROM students where rollno=%s",self.rollno_var.get()) 
        
        conn.commit()
        conn.close()
        self.fetchdata()
        self.clear()
        messagebox.showinfo("Success","Record has been Deleted")
  
    def searchdata(self):
            conn=pymysql.connect(host="localhost",user="root",password="",database="student_manage")
            cur=conn.cursor()
            cur.execute("SELECT * FROM students WHERE "+str(self.search_by.get())+" LIKE '%"+str(self.searchall.get())+"%'") 
            rows=cur.fetchall()
            if len(rows)!=0:
                self.student_table.delete(*self.student_table.get_children())
                for row in rows:
                        self.student_table.insert("",END,values=row)
                conn.commit()
            conn.close()
   

            
                
root=Tk()
ob=Student(root)
root.mainloop()         
