import sqlite3
import tkinter as tk
from tkinter import ttk
import random


win = tk.Tk()
win.title("MINI PROJECT")


fname_label =tk.Label(win,text='Enter your name ** ')
fname_label.grid(row = 0,column =0,sticky=tk.W,padx=5,pady=5)


stdid_label = tk.Label(win,text='Enter your ERP id ** ')
stdid_label.grid(row = 1,column =0,sticky=tk.W,padx=5,pady=5)


email_label = ttk.Label(win,text='Enter your email ID  ')
email_label.grid(row = 2,column =0,sticky=tk.W,padx=5,pady=5)

phone_label = ttk.Label(win,text='Enter your phone number ** ')
phone_label.grid(row=3,column=0,sticky=tk.W,padx=5,pady=5)


adhr_label = ttk.Label(win,text='Enter your aadhar number  ')
adhr_label.grid(row=4,column=0,sticky=tk.W,padx=5,pady=5)


update_phone_label = ttk.Label(win,text=' CONTACT NUMBER UPDATION ')
update_phone_label.grid(row=0,column=4,sticky=tk.W,padx=5,pady=5)
update_phone_label.configure(foreground="blue",font='Helvertika 10 bold')


uacc_label = ttk.Label(win,text='Enter your account number  ')
uacc_label.grid(row=1,column=4,sticky=tk.W,padx=5,pady=5)

uphone_label = ttk.Label(win,text='Enter your new contact number  ')
uphone_label.grid(row=2,column=4,sticky=tk.W,padx=5,pady=5)

umail_label = ttk.Label(win,text='Enter your new mail ID ')
umail_label.grid(row=3,column=4,sticky=tk.W,padx=5,pady=5)

fname_var=tk.StringVar()
fname_entry = ttk.Entry(win,width=16,textvariable=fname_var)
fname_entry.grid(row=0,column=1,padx=5,pady=5)

stdid_var=tk.StringVar()
stdid_entry = ttk.Entry(win,width=16,textvariable=stdid_var)
stdid_entry.grid(row=1,column=1,padx=5,pady=5)

mail_var=tk.StringVar()
mail_entry = ttk.Entry(win,width=16,textvariable=mail_var)
mail_entry.grid(row=2,column=1,padx=5,pady=5)

phone_var=tk.StringVar()
phone_entry = ttk.Entry(win,width=16,textvariable=phone_var)
phone_entry.grid(row=3,column=1,padx=5,pady=5)

adhr_var=tk.StringVar()
adhr_entry = ttk.Entry(win,width=16,textvariable=adhr_var)
adhr_entry.grid(row=4,column=1,padx=5,pady=5)

acc_no=tk.StringVar()
acc_entry = ttk.Entry(win,width=16,textvariable=acc_no)
acc_entry.grid(row=0,column=2,padx=5,pady=5)

acc_entry = ttk.Entry(win,width=16,textvariable=acc_no)
acc_entry.grid(row=0,column=3,padx=5,pady=5)

acc_entry = ttk.Entry(win,width=16,textvariable=acc_no)
acc_entry.grid(row=1,column=5,padx=5,pady=5)

uphone_no=tk.StringVar()
uphone_entry = ttk.Entry(win,width=16,textvariable=uphone_no)
uphone_entry.grid(row=2,column=5,padx=5,pady=5)

umail=tk.StringVar()
umail_entry = ttk.Entry(win,width=16,textvariable=umail)
umail_entry.grid(row=3,column=5,padx=5,pady=5)



def entry():

    conn = sqlite3.connect('bank.db')
    c = conn.cursor()

    if fname_var.get()=="" or stdid_var.get()=="" or phone_var.get()=="":
        accwin = tk.Tk()
        accwin.title("ACCOUNT NUMBER")
        accwin.geometry("400x60")
        er_label = ttk.Label(accwin,text='Fields mark with ** are necessary ')
        er_label.grid(row=1,column=0)
        er_label.configure(foreground="Red",font='Helvertika 15 bold')
    else :
        frstletr = fname_var.get()[0]
        y,a = stdid_var.get().split("F")   
   
        accn_no = frstletr + str(y) + "@"
        phoneno = phone_var.get()
        for i in phoneno[0:3] :
            accn_no = accn_no + i

        
        c.execute('''CREATE TABLE IF NOT EXISTS bank
        (acc_no real PRIMARY KEY, ERP_id real , mail_ID text , name text, contact int, aadhar_number int)''')
  
        c.execute("INSERT INTO bank (acc_no , ERP_id , mail_ID , name , contact , aadhar_number ) values(? ,? ,? ,? ,? ,?)",(accn_no, stdid_var.get(), mail_var.get(), fname_var.get(), phone_var.get(), adhr_var.get()))
        conn.commit()


        accwin = tk.Tk()
        accwin.title("ACCOUNT NUMBER")
        accwin.geometry("600x60")


                
        accn1_label =ttk.Label(accwin,text = " Your Account Number >>> " )
        accn1_label.grid(row = 0,column =0,sticky=tk.W,padx=5,pady=5)
        accn1_label.configure(font='Helvertika 15 bold')

        accn_label =ttk.Label(accwin,text = accn_no )
        accn_label.grid(row = 0,column =1,sticky=tk.W,padx=5,pady=5)
        accn_label.configure(font='Helvertika 15 bold',foreground="Blue")
        

    c.close()
    conn.close()

def delete() :

    accwin = tk.Tk()
    accwin.title("ACCOUNT NUMBER")
    accwin.geometry("400x60")
    
    conn = sqlite3.connect('bank.db')
    c = conn.cursor()

    c.execute("SELECT acc_no FROM bank")

    flag = 0

    data = acc_no.get()

    for row in c:
        x,*y = row
        if data == x :
            flag=1
        else :
            pass

    if flag == 0 :

        er1_label = ttk.Label(accwin,text='Incorrect account number !!! ')
        er1_label.grid(row=1,column=0)
        er1_label.configure(foreground="Red",font='Helvertika 15 bold')
    else :
        c.execute("DELETE FROM bank WHERE acc_no=? ",(acc_no.get(),))
        conn.commit()

        er1_label = ttk.Label(accwin,text='Successfully deleted  ')
        er1_label.grid(row=2,column=0)
        er1_label.configure(foreground="Green")
   
        c.close()
        conn.close()

def view() :
    conn = sqlite3.connect('bank.db')
    c = conn.cursor()
  
    c.execute("SELECT *FROM bank WHERE acc_no=?",(acc_no.get(),))

    list1 = ['acc_no ','ERP    ','mail ID','name   ','contact','adhaar ']
    for row in c :
        (a,b,c,d,e,f) = row

    row = (a,b,c,d,e,f)   
    for i in range(len(list1)) :
        cur = 'label' + str(i)
        data = list1[i]+ "  --->>>  " + str(row[i])
        cur_label = ttk.Label(win,text =data)
        cur_label.configure(font='Helvertika 10 bold')
        cur_label.grid(row=(2+i),column=3,sticky=tk.W)
        cur_label.configure(foreground = "Green")


def update() :
    accwin = tk.Tk()
    accwin.title("ACCOUNT NUMBER")
    accwin.geometry("400x60")
    
    conn = sqlite3.connect('bank.db')
    c = conn.cursor()

    c.execute("SELECT acc_no FROM bank")

    flag = 0

    data = acc_no.get()

    for row in c:
        x , *y = row

        if data == x :
            flag=1
        else :
            pass

    if flag == 0 :

        er1_label = ttk.Label(accwin,text='Incorrect account number !!! ')
        er1_label.grid(row=1,column=0)
        er1_label.configure(foreground="Red",font='Helvertika 15 bold')

    else :
        if uphone_no.get() != "" :
            c.execute("UPDATE bank set contact=? WHERE acc_no=? ",(uphone_no.get(), acc_no.get(),))
            conn.commit()

            er1_label = ttk.Label(accwin,text='Successfully updated  ')
            er1_label.grid(row=2,column=0)
            er1_label.configure(foreground="Green")
           
        if umail.get() != "" :
            c.execute("UPDATE bank set mail_ID=? WHERE acc_no=? ",(umail.get(), acc_no.get(),))
            conn.commit()

            er1_label = ttk.Label(accwin,text='Successfully updated  ')
            er1_label.grid(row=2,column=0)
            er1_label.configure(foreground="Green")

    c.close()
    conn.close()

submit_btn = ttk.Button(win,text="SUBMIT",command=entry)
submit_btn.grid(row=5,column=0,padx=5,pady=5)

delete_btn = ttk.Button(win,text="DELETE",command=delete)
delete_btn.grid(row=1,column=2,padx=5,pady=5)

view_btn = ttk.Button(win,text="VIEW",command=view)
view_btn.grid(row=1,column=3,padx=5,pady=5)

update_btn = ttk.Button(win,text="UPADTE",command=update)
update_btn.grid(row=4,column=5,padx=5,pady=5)



win.mainloop()
