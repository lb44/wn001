from msilib.schema import Font
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import datetime as dt
from turtle import back
# from tkcalendar import DateEntry,Calender
root=Tk()
root.geometry("1860x900")
root.resizable(True, True)

root.title("TALLY PRIME")


curnt_period = Label(root, text="CURRENT PERIOD",fg="darkblue").place(x=40, y=30)
curnt_date = Label(root, text="CURRENT DATE",fg="darkblue").place(x=340, y=30)
prd = Label(root, text="1-Apr-22 to 31-March-2023", fg="black").place(x=40, y=60)
date = Label(root, text="Friday, 1-Apr-2022", fg="black").place(x=340, y=60)
cmpny = Label(root, text="Name Of Company",borderwidth=3,fg="darkblue").place(x=40, y=100)
lst_entry = Label(root, text="Date Of Last Entry", fg="darkblue").place(x=340, y=100)
cpny = Label(root, text="ABC Pvt ltd", fg="black").place(x=40, y=140)
date_entry = Label(root, text="1-Apr-22",fg="black").place(x=340, y=140)
separator = ttk.Separator(root,orient='vertical')
separator.place(relx=0.47,rely=0,relwidth=0.2,relheight=1)
frame = Label(root, text="Gateway of tally",bg="grey",fg="white",width=40,padx=20,pady=10).place(x=740, y=110)
frame1 = Frame(root, bg="lightblue", width=305, height=540)
frame1.place(x=740, y=145)
frame2 = Frame(frame1, bg="lightblue", width=305, height=540)
frame2.pack(pady=10, padx=10)
mstrs = Label(root, text="Masters",bg="lightblue",fg="black",font="17").place(x=860 ,y=190)


def func1():
    screen1 = Toplevel(root)
    screen1.title('create')
    screen1.geometry('1860x900') 

def func2():
    global screen2
    screen2 = Toplevel(root)
    screen2.resizable(False, False)
    screen2.title('Company')
    screen2.geometry('1500x770')
    Label(screen2, text='List Of Companies',bg="lightblue",font='17',fg="white",width=430).pack()
    sbmibtn = Button(screen2, text='Create Company',command=create,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=650,y=40)
    sbmibtn2 = Button(screen2, text='Alter Company',command=create,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=650,y=70)
    sbmibtn3 = Button(screen2, text='Select Company',command=create,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=650,y=100)
    sbmibtn4 = Button(screen2, text='Shut Company', command=create, fg='black',font=('Arial',9),activebackground='palegreen', width=30, border=0).place(x=650, y=130)


def func3():     
    global screen3
    screen3 = Toplevel(root)
    screen3.resizable(False, False)
    screen3.title('BANKING')
    screen3.geometry('1500x770')
    curnt_period = Label(screen3, text="CURRENT PERIOD",fg="darkblue").place(x=40, y=30)
    curnt_date = Label(screen3, text="CURRENT DATE",fg="darkblue").place(x=340, y=30)
    prd = Label(screen3, text="1-Apr-22 to 31-March-2023", fg="black").place(x=40, y=60)
    date = Label(screen3, text="Friday, 1-Apr-2022", fg="black").place(x=340, y=60)
    cmpny = Label(screen3, text="Name Of Company",borderwidth=3,fg="darkblue").place(x=40, y=100)
    lst_entry = Label(screen3, text="Date Of Last Entry", fg="darkblue").place(x=340, y=100)
    cpny = Label(screen3, text="ABC Pvt ltd", fg="black").place(x=40, y=140)
    date_entry = Label(screen3, text="1-Apr-22",fg="black").place(x=340, y=140)
    separator = ttk.Separator(screen3,orient='vertical')
    separator.place(relx=0.47,rely=0,relwidth=0.2,relheight=1)
    frame4 = Frame(screen3, bg="lightblue", width=180, height=790)
    frame4.place(x=1400, y=0)
    frame13 = Frame(screen3, bg="lightblue", width=240, height=400)
    frame13.place(x=1000, y=170) 
    frame131 = Label(screen3, text="BANKING",bg="grey",fg="white",width=31,padx=10,pady=10).place(x=1000, y=170) 
    mstrs4 = Label(screen3, text="Cheque",bg="lightblue",fg="black",font="13").place(x=1080 ,y=210)
    b1 = Button(screen3, text="Cheque Printing", fg="black", activebackground="palegreen",
            bg="white", width=20, height=1,command=create2).place(x=1050, y=250)
    b2 = Button(screen3, text="Cheque Register", fg="black", activebackground="palegreen",
            bg="white", width=20, height=1,command=create7).place(x=1050, y=280)
    b3 = Button(screen3, text="Post-dated Summary", fg="black", activebackground="palegreen",
            bg="white", width=20, height=1,command=create3      ).place(x=1050, y=310)
    mstrs5 = Label(screen3, text="Statements",bg="lightblue",fg="black",font="13").place(x=1070 ,y=360)
    b4 = Button(screen3, text="Deposit Slip", fg="black", activebackground="palegreen",
            bg="white", width=20, height=1,command=create4).place(x=1050, y=390)
    b5 = Button(screen3, text="Payment Advice", fg="black", activebackground="palegreen",
            bg="white", width=20, height=1,command=create5).place(x=1050, y=420)
    b6 = Button(screen3, text="Bank Reconciliation", fg="black", activebackground="palegreen",
            bg="white", width=20, height=1,command=create6).place(x=1050, y=480)
    b7 = Button(screen3, text="Quit", fg="black", activebackground="palegreen",
            bg="white", width=20, height=1,command=func1).place(x=1050, y=520)        
    date = Button(frame4, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame4, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9),command=func2, activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame4, command= 'screen3.destroy', text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700)
    Label(screen3, text='BANKING',bg="lightblue",font='17',fg="black",width=430).pack() 
    Label(screen3).place(x=20, y=70)(font="timesnewroman").pack()
def func4():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('coa')
    screen4.geometry('1500x770')
    frame131 = Frame(screen4, bg="lightblue", width=250, height=600)
    frame131.place(x=630, y=0)
    frame131 = Label(screen4, text="List of Masters",bg="black",fg="white",width=32,padx=10,pady=10).place(x=630, y=20)
    frame13 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame13.place(x=1400, y=0)
    date = Button(frame13, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame13, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9),command=func2, activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame13, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700)
    mstrs6 = Label(screen4, text="Accounting Masters",bg="lightblue",fg="black",font="13").place(x=670 ,y=140)
    sbmibtn = Button(screen4, text='Groups',command=create8,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=650,y=180)
    sbmibtn = Button(screen4, text='Ledger',command=create9,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=650, y=200)
    sbmibtn = Button(screen4, text='Voucher Types',command=create10,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=650,y=220)
    sbmibtn = Button(screen4, text='Currencies',command=create11,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=650,y=240)
    sbmibtn = Button(screen4, text='Budgets',command=create12,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=650, y=260)
    sbmibtn = Button(screen4, text='Scenarios',command=create13,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=650,y=280)
    mstrs7 = Label(screen4, text="Inventory Masters",bg="lightblue",fg="black",font="13").place(x=670 ,y=320)
    sbmibtn = Button(screen4, text='Stock Group',command=create14,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=650,y=360)
    sbmibtn = Button(screen4, text='Stock Item',command=create15,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=650, y=380)
    sbmibtn = Button(screen4, text='Stock Catagories',command=create16,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=650,y=400)
    sbmibtn = Button(screen4, text='Units',command=create17,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=650,y=420)
    sbmibtn = Button(screen4, text='Godowns',command=create18,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=650, y=440)
    e11 = Entry(screen4,).place(x=700, y=100)
    Label(screen4, text='CHART OF ACCOUNTS',bg="lightblue",font='19',fg="black",width=430).pack()

def func6():
    global screen10
    screen10 = Toplevel(root)
    screen10.resizable(False, False)
    screen10.title('post dated transaction summary')
    screen10.geometry('1500x770')
    sbmibtn13 = Button(screen10, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=30)
    sbmibtn14 = Button(screen10, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn15 = Button(screen10, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn16 = Button(screen10, text='Recieved',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=750, y=110)
    sbmibtn17 = Button(screen10, text='Count',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=850, y=130)
    sbmibtn18 = Button(screen10, text='Amount',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=650, y=130)
    sbmibtn19 = Button(screen10, text='Issued',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1080, y=110)
    sbmibtn20 = Button(screen10, text='Count',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1150, y=130)
    sbmibtn21 = Button(screen10, text='Amount',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1000, y=130)


    sbmibtn = Button(screen10, text='APRIL',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=170)
    sbmibtn2 = Button(screen10, text='MAY',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=200)
    sbmibtn3 = Button(screen10, text='JUNE',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=230)
    sbmibtn4 = Button(screen10, text='JULY', fg='black',font=('Arial',9),activebackground='palegreen', width=30, border=0).place(y=260)
    sbmibtn5 = Button(screen10, text='AUGUST',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=290)
    sbmibtn6 = Button(screen10, text='SEPTEMBER',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=320)
    sbmibtn7 = Button(screen10, text='OCTOBER',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=350)
    sbmibtn8 = Button(screen10, text='NOVEMBER', fg='black',font=('Arial',9),activebackground='palegreen', width=30, border=0).place(y=380)
    sbmibtn9 = Button(screen10, text='DECEMBER',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=410)
    sbmibtn10 = Button(screen10, text='JANUARY',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=440)
    sbmibtn11 = Button(screen10, text='FEBRUARY',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=470)
    sbmibtn12 = Button(screen10, text='MARCH', fg='black',font=('Arial',9),activebackground='palegreen', width=30, border=0).place(y=500)
    frame11 = Frame(screen10, bg="lightblue", width=180, height=790)
    frame11.place(x=1400, y=0)
    date = Button(frame11, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame11, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9),command=func2, activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame11, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700)
    Label(screen10, text='POST-DATED TRANSACTION SUMMARY',bg="lightblue",font='17',fg="black",width=430).pack()  
    Label(screen10, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()         
def func7():
    global screen10
    screen10 = Toplevel(root)
    screen10.resizable(False, False)
    screen10.title('Ledger Creation Secondary')
    screen10.geometry('1200x770')
    separator1 = ttk.Separator(screen10,orient='vertical')
    separator1.place(relx=0.40,rely=0,relheight=1)
    sbmibtn13 = Button(screen10, text='Name',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=20, y=30)
    sbmibtn14 = Button(screen10, text='Under    :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=30, y=90)
    sbmibtn15 = Button(screen10, text='Mailing Details',fg='black',font=('Bold',12),activebackground='palegreen',width=30,border=0).place(x=500, y=100)
    sbmibtn16 = Button(screen10, text='Name                                                       :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=500, y=140)
    sbmibtn17 = Button(screen10, text='Address                                                    :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=500, y=160)
    sbmibtn18 = Button(screen10, text='State                                                         :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=500, y=240)
    sbmibtn19 = Button(screen10, text='Country                                                     :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=500, y=260)
    sbmibtn20 = Button(screen10, text='Pincode                                                    :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=500, y=280)
    sbmibtn21 = Button(screen10, text='Banking Details',fg='black',font=('Bold',12),activebackground='palegreen',width=30,border=0).place(x=500, y=320)
    sbmibtn21 = Button(screen10, text='Provide Bank Details                           :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=500, y=360)
    sbmibtn21 = Button(screen10, text='Tax  Registration Details',fg='black',font=('Bold',12),activebackground='palegreen',width=30,border=0).place(x=500, y=390)
    sbmibtn21 = Button(screen10, text='PAN/IT No.                                    :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=500, y=420)
    sbmibtn21 = Button(screen10, text='Registration Type                             :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=500, y=440)
    sbmibtn21 = Button(screen10, text='GSTIN/UIN                                     :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=500, y=460)
    sbmibtn21 = Button(screen10, text='Set/Alter GST Details                         :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=500, y=480)    
    e12 = Entry(screen10,).place(x=170, y=30) 
def func8():
    global screen10
    screen10 = Toplevel(root)
    screen10.resizable(False, False)
    screen10.title('Ledger Creation Secondary')
    screen10.geometry('1200x770')
    separator1 = ttk.Separator(screen10,orient='vertical')
    separator1.place(relx=0.40,rely=0,relheight=1)
    sbmibtn13 = Button(screen10, text='Name',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=20, y=30)
    sbmibtn14 = Button(screen10, text='Under    :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=30, y=90)
    sbmibtn15 = Button(screen10, text='Mailing Details',fg='black',font=('Bold',12),activebackground='palegreen',width=30,border=0).place(x=500, y=100)
    sbmibtn16 = Button(screen10, text='Name                                                       :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=500, y=140)
    sbmibtn17 = Button(screen10, text='Address                                                    :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=500, y=160)
    sbmibtn18 = Button(screen10, text='State                                                         :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=500, y=240)
    sbmibtn19 = Button(screen10, text='Country                                                     :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=500, y=260)
    sbmibtn20 = Button(screen10, text='Pincode                                                    :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=500, y=280)
    sbmibtn21 = Button(screen10, text='Banking Details',fg='black',font=('Bold',12),activebackground='palegreen',width=30,border=0).place(x=500, y=320)
    sbmibtn21 = Button(screen10, text='Provide Bank Details                           :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=500, y=360)
    sbmibtn21 = Button(screen10, text='Tax  Registration Details',fg='black',font=('Bold',12),activebackground='palegreen',width=30,border=0).place(x=500, y=390)
    sbmibtn21 = Button(screen10, text='PAN/IT No.                                    :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=500, y=420)
    sbmibtn21 = Button(screen10, text='Registration Type                             :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=500, y=440)
    sbmibtn21 = Button(screen10, text='GSTIN/UIN                                     :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=500, y=460)
    sbmibtn21 = Button(screen10, text='Set/Alter GST Details                         :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=500, y=480)    
    e12 = Entry(screen10,).place(x=170, y=30)  
def func9():
    global screen10
    screen10 = Toplevel(root)
    screen10.resizable(False, False)
    screen10.title('Ledger Creation Secondary')
    screen10.geometry('1200x770')
    separator1 = ttk.Separator(screen10,orient='vertical')
    separator1.place(relx=0.40,rely=0,relheight=1)
    sbmibtn13 = Button(screen10, text='Name',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=20, y=30)
    sbmibtn14 = Button(screen10, text='Under    :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=30, y=90)
    sbmibtn15 = Button(screen10, text='Mailing Details',fg='black',font=('Bold',12),activebackground='palegreen',width=30,border=0).place(x=500, y=100)
    sbmibtn16 = Button(screen10, text='Name                                                       :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=500, y=140)
    sbmibtn17 = Button(screen10, text='Address                                                    :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=500, y=160)
    sbmibtn18 = Button(screen10, text='State                                                         :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=500, y=240)
    sbmibtn19 = Button(screen10, text='Country                                                     :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=500, y=260)
    sbmibtn20 = Button(screen10, text='Pincode                                                    :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=500, y=280)
    sbmibtn21 = Button(screen10, text='Banking Details',fg='black',font=('Bold',12),activebackground='palegreen',width=30,border=0).place(x=500, y=320)
    sbmibtn21 = Button(screen10, text='Provide Bank Details                           :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=500, y=360)
    sbmibtn21 = Button(screen10, text='Tax  Registration Details',fg='black',font=('Bold',12),activebackground='palegreen',width=30,border=0).place(x=500, y=390)
    sbmibtn21 = Button(screen10, text='PAN/IT No.                                    :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=500, y=420)
    sbmibtn21 = Button(screen10, text='Registration Type                             :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=500, y=440)
    sbmibtn21 = Button(screen10, text='GSTIN/UIN                                     :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=500, y=460)
    sbmibtn21 = Button(screen10, text='Set/Alter GST Details                         :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=500, y=480)    
    e12 = Entry(screen10,).place(x=170, y=30) 
def func10():
    global screen10
    screen10 = Toplevel(root)
    screen10.resizable(False, False)
    screen10.title('Ledger Creation Secondary')
    screen10.geometry('1200x770')
    separator1 = ttk.Separator(screen10,orient='vertical')
    separator1.place(relx=0.40,rely=0,relheight=1)
    sbmibtn13 = Button(screen10, text='Name',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=20, y=30)
    sbmibtn14 = Button(screen10, text='Under    :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=30, y=90)
    sbmibtn15 = Button(screen10, text='Mailing Details',fg='black',font=('Bold',12),activebackground='palegreen',width=30,border=0).place(x=500, y=100)
    sbmibtn16 = Button(screen10, text='Name                                                       :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=500, y=140)
    sbmibtn17 = Button(screen10, text='Address                                                    :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=500, y=160)
    sbmibtn18 = Button(screen10, text='State                                                         :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=500, y=240)
    sbmibtn19 = Button(screen10, text='Country                                                     :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=500, y=260)
    sbmibtn20 = Button(screen10, text='Pincode                                                    :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=500, y=280)
    sbmibtn21 = Button(screen10, text='Banking Details',fg='black',font=('Bold',12),activebackground='palegreen',width=30,border=0).place(x=500, y=320)
    sbmibtn21 = Button(screen10, text='Provide Bank Details                           :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=500, y=360)
    sbmibtn21 = Button(screen10, text='Tax  Registration Details',fg='black',font=('Bold',12),activebackground='palegreen',width=30,border=0).place(x=500, y=390)
    sbmibtn21 = Button(screen10, text='PAN/IT No.                                    :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=500, y=420)
    sbmibtn21 = Button(screen10, text='Registration Type                             :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=500, y=440)
    sbmibtn21 = Button(screen10, text='GSTIN/UIN                                     :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=500, y=460)
    sbmibtn21 = Button(screen10, text='Set/Alter GST Details                         :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=500, y=480)    
    e12 = Entry(screen10,).place(x=170, y=30)               
def func11():
    global screen10
    screen10 = Toplevel(root)
    screen10.resizable(False, False)
    screen10.title('Ledger Creation Secondary')
    screen10.geometry('1200x770')
    separator1 = ttk.Separator(screen10,orient='vertical')
    separator1.place(relx=0.40,rely=0,relheight=1)
    sbmibtn13 = Button(screen10, text='Name',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=20, y=30)
    sbmibtn14 = Button(screen10, text='Under    :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=30, y=90)
    sbmibtn15 = Button(screen10, text='Mailing Details',fg='black',font=('Bold',12),activebackground='palegreen',width=30,border=0).place(x=500, y=100)
    sbmibtn16 = Button(screen10, text='Name                                                       :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=500, y=140)
    sbmibtn17 = Button(screen10, text='Address                                                    :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=500, y=160)
    sbmibtn18 = Button(screen10, text='State                                                         :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=500, y=240)
    sbmibtn19 = Button(screen10, text='Country                                                     :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=500, y=260)
    sbmibtn20 = Button(screen10, text='Pincode                                                    :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=500, y=280)
    sbmibtn21 = Button(screen10, text='Banking Details',fg='black',font=('Bold',12),activebackground='palegreen',width=30,border=0).place(x=500, y=320)
    sbmibtn21 = Button(screen10, text='Provide Bank Details                           :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=500, y=360)
    sbmibtn21 = Button(screen10, text='Tax  Registration Details',fg='black',font=('Bold',12),activebackground='palegreen',width=30,border=0).place(x=500, y=390)
    sbmibtn21 = Button(screen10, text='PAN/IT No.                                    :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=500, y=420)
    sbmibtn21 = Button(screen10, text='Registration Type                             :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=500, y=440)
    sbmibtn21 = Button(screen10, text='GSTIN/UIN                                     :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=500, y=460)
    sbmibtn21 = Button(screen10, text='Set/Alter GST Details                         :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=500, y=480)    
    e12 = Entry(screen10,).place(x=170, y=30)               

def func12():
    global screen10
    screen10 = Toplevel(root)
    screen10.resizable(False, False)
    screen10.title('Group Alteration')
    screen10.geometry('650x300')
    sbmibtn13 = Button(screen10, text='Name',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=0, y=30)
    sbmibtn14 = Button(screen10, text='Under    :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=0, y=60)
    sbmibtn14 = Button(screen10, text='nature of groups    :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=0, y=110)
    
    e12 = Entry(screen10,).place(x=170, y=30)  

def func13():
    global screen10
    screen10 = Toplevel(root)
    screen10.resizable(False, False)
    screen10.title('Group Alteration')
    screen10.geometry('650x300')
    sbmibtn13 = Button(screen10, text='Name',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=0, y=30)
    sbmibtn14 = Button(screen10, text='Under    :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=0, y=60)
    sbmibtn14 = Button(screen10, text='nature of groups    :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=0, y=110)
    
    e12 = Entry(screen10,).place(x=170, y=30)

def func14():
    global screen10
    screen10 = Toplevel(root)
    screen10.resizable(False, False)
    screen10.title('Group Alteration')
    screen10.geometry('650x300')
    sbmibtn13 = Button(screen10, text='Name',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=0, y=30)
    sbmibtn14 = Button(screen10, text='Under    :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=0, y=60)
    sbmibtn14 = Button(screen10, text='nature of groups    :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=0, y=110)
    
    e12 = Entry(screen10,).place(x=170, y=30)    

def func15():
    global screen10
    screen10 = Toplevel(root)
    screen10.resizable(False, False)
    screen10.title('Group Alteration')
    screen10.geometry('650x300')
    sbmibtn13 = Button(screen10, text='Name',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=0, y=30)
    sbmibtn14 = Button(screen10, text='Under    :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=0, y=60)
    sbmibtn14 = Button(screen10, text='nature of groups    :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=0, y=110)
    
    e12 = Entry(screen10,).place(x=170, y=30)

def func16():
    global screen10
    screen10 = Toplevel(root)
    screen10.resizable(False, False)
    screen10.title('Group Alteration')
    screen10.geometry('650x300')
    sbmibtn13 = Button(screen10, text='Name',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=0, y=30)
    sbmibtn14 = Button(screen10, text='Under    :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=0, y=60)
    sbmibtn14 = Button(screen10, text='nature of groups    :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=0, y=110)
    
    e12 = Entry(screen10,).place(x=170, y=30)

def func17():
    global screen10
    screen10 = Toplevel(root)
    screen10.resizable(False, False)
    screen10.title('Group Alteration')
    screen10.geometry('650x300')
    sbmibtn13 = Button(screen10, text='Name',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=0, y=30)
    sbmibtn14 = Button(screen10, text='Under    :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=0, y=60)
    sbmibtn14 = Button(screen10, text='nature of groups    :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=0, y=110)
    
    e12 = Entry(screen10,).place(x=170, y=30)

def func18():
    global screen10
    screen10 = Toplevel(root)
    screen10.resizable(False, False)
    screen10.title('Group Alteration')
    screen10.geometry('650x300')
    sbmibtn13 = Button(screen10, text='Name',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=0, y=30)
    sbmibtn14 = Button(screen10, text='Under    :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=0, y=60)
    sbmibtn14 = Button(screen10, text='nature of groups    :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=0, y=110)
    
    e12 = Entry(screen10,).place(x=170, y=30)

def func19():
    global screen10
    screen10 = Toplevel(root)
    screen10.resizable(False, False)
    screen10.title('Group Alteration')
    screen10.geometry('650x300')
    sbmibtn13 = Button(screen10, text='Name',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=0, y=30)
    sbmibtn14 = Button(screen10, text='Under    :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=0, y=60)
    sbmibtn14 = Button(screen10, text='nature of groups    :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=0, y=110)
    
    e12 = Entry(screen10,).place(x=170, y=30)

def func20():
    global screen10
    screen10 = Toplevel(root)
    screen10.resizable(False, False)
    screen10.title('Group Alteration')
    screen10.geometry('650x300')
    sbmibtn13 = Button(screen10, text='Name',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=0, y=30)
    sbmibtn14 = Button(screen10, text='Under    :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=0, y=60)
    sbmibtn14 = Button(screen10, text='nature of groups    :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=0, y=110)
    
    e12 = Entry(screen10,).place(x=170, y=30)

def func21():
    global screen10
    screen10 = Toplevel(root)
    screen10.resizable(False, False)
    screen10.title('Group Alteration')
    screen10.geometry('650x300')
    sbmibtn13 = Button(screen10, text='Name',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=0, y=30)
    sbmibtn14 = Button(screen10, text='Under    :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=0, y=60)
    sbmibtn14 = Button(screen10, text='nature of groups    :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=0, y=110)
    
    e12 = Entry(screen10,).place(x=170, y=30)
def func22():
    global screen10
    screen10 = Toplevel(root)
    screen10.resizable(False, False)
    screen10.title('Group Alteration')
    screen10.geometry('650x300')
    sbmibtn13 = Button(screen10, text='Name',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=0, y=30)
    sbmibtn14 = Button(screen10, text='Under    :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=0, y=60)
    sbmibtn14 = Button(screen10, text='nature of groups    :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=0, y=110)
    
    e12 = Entry(screen10,).place(x=170, y=30)
def func23():
    global screen10
    screen10 = Toplevel(root)
    screen10.resizable(False, False)
    screen10.title('Group Alteration')
    screen10.geometry('650x300')
    sbmibtn13 = Button(screen10, text='Name',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=0, y=30)
    sbmibtn14 = Button(screen10, text='Under    :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=0, y=60)
    sbmibtn14 = Button(screen10, text='nature of groups    :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=0, y=110)
    
    e12 = Entry(screen10,).place(x=170, y=30)

def func24():
    global screen10
    screen10 = Toplevel(root)
    screen10.resizable(False, False)
    screen10.title('Group Alteration')
    screen10.geometry('650x300')
    sbmibtn13 = Button(screen10, text='Name',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=0, y=30)
    sbmibtn14 = Button(screen10, text='Under    :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=0, y=60)
    sbmibtn14 = Button(screen10, text='nature of groups    :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=0, y=110)
    
    e12 = Entry(screen10,).place(x=170, y=30)

def func25():
    global screen10
    screen10 = Toplevel(root)
    screen10.resizable(False, False)
    screen10.title('Group Alteration')
    screen10.geometry('650x300')
    sbmibtn13 = Button(screen10, text='Name',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=0, y=30)
    sbmibtn14 = Button(screen10, text='Under    :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=0, y=60)
    sbmibtn14 = Button(screen10, text='nature of groups    :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=0, y=110)
    
    e12 = Entry(screen10,).place(x=170, y=30)
def func26():
    global screen10
    screen10 = Toplevel(root)
    screen10.resizable(False, False)
    screen10.title('Group Alteration')
    screen10.geometry('650x300')
    sbmibtn13 = Button(screen10, text='Name',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=0, y=30)
    sbmibtn14 = Button(screen10, text='Under    :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=0, y=60)
    sbmibtn14 = Button(screen10, text='nature of groups    :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=0, y=110)
    
    e12 = Entry(screen10,).place(x=170, y=30)
def func27():
    global screen10
    screen10 = Toplevel(root)
    screen10.resizable(False, False)
    screen10.title('Group Alteration')
    screen10.geometry('650x300')
    sbmibtn13 = Button(screen10, text='Name',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=0, y=30)
    sbmibtn14 = Button(screen10, text='Under    :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=0, y=60)
    sbmibtn14 = Button(screen10, text='nature of groups    :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=0, y=110)
    
    e12 = Entry(screen10,).place(x=170, y=30)        
def func28():
    global screen10
    screen10 = Toplevel(root)
    screen10.resizable(False, False)
    screen10.title('Group Alteration')
    screen10.geometry('650x300')
    sbmibtn13 = Button(screen10, text='Name',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=0, y=30)
    sbmibtn14 = Button(screen10, text='Under    :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=0, y=60)
    sbmibtn14 = Button(screen10, text='nature of groups    :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=0, y=110)
    
    e12 = Entry(screen10,).place(x=170, y=30)
def func29():
    global screen10
    screen10 = Toplevel(root)
    screen10.resizable(False, False)
    screen10.title('Group Alteration')
    screen10.geometry('650x300')
    sbmibtn13 = Button(screen10, text='Name',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=0, y=30)
    sbmibtn14 = Button(screen10, text='Under    :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=0, y=60)
    sbmibtn14 = Button(screen10, text='nature of groups    :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=0, y=110)
    
    e12 = Entry(screen10,).place(x=170, y=30)
def func30():
    global screen10
    screen10 = Toplevel(root)
    screen10.resizable(False, False)
    screen10.title('Group Alteration')
    screen10.geometry('650x300')
    sbmibtn13 = Button(screen10, text='Name',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=0, y=30)
    sbmibtn14 = Button(screen10, text='Under    :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=0, y=60)
    sbmibtn14 = Button(screen10, text='nature of groups    :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=0, y=110)
    
    e12 = Entry(screen10,).place(x=170, y=30)
def func31():
    global screen10
    screen10 = Toplevel(root)
    screen10.resizable(False, False)
    screen10.title('Group Alteration')
    screen10.geometry('650x300')
    sbmibtn13 = Button(screen10, text='Name',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=0, y=30)
    sbmibtn14 = Button(screen10, text='Under    :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=0, y=60)
    sbmibtn14 = Button(screen10, text='nature of groups    :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=0, y=110)
    
    e12 = Entry(screen10,).place(x=170, y=30)
def func32():
    global screen10
    screen10 = Toplevel(root)
    screen10.resizable(False, False)
    screen10.title('Group Alteration')
    screen10.geometry('650x300')
    sbmibtn13 = Button(screen10, text='Name',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=0, y=30)
    sbmibtn14 = Button(screen10, text='Under    :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=0, y=60)
    sbmibtn14 = Button(screen10, text='nature of groups    :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=0, y=110)
    
    e12 = Entry(screen10,).place(x=170, y=30)
def func33():
    global screen10
    screen10 = Toplevel(root)
    screen10.resizable(False, False)
    screen10.title('Group Alteration')
    screen10.geometry('650x300')
    sbmibtn13 = Button(screen10, text='Name',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=0, y=30)
    sbmibtn14 = Button(screen10, text='Under    :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=0, y=60)
    sbmibtn14 = Button(screen10, text='nature of groups    :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=0, y=110)
    
    e12 = Entry(screen10,).place(x=170, y=30)
def func34():
    global screen10
    screen10 = Toplevel(root)
    screen10.resizable(False, False)
    screen10.title('Group Alteration')
    screen10.geometry('650x300')
    sbmibtn13 = Button(screen10, text='Name',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=0, y=30)
    sbmibtn14 = Button(screen10, text='Under    :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=0, y=60)
    sbmibtn14 = Button(screen10, text='nature of groups    :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=0, y=110)
    
    e12 = Entry(screen10,).place(x=170, y=30)
def func35():
    global screen10
    screen10 = Toplevel(root)
    screen10.resizable(False, False)
    screen10.title('Group Alteration')
    screen10.geometry('650x300')
    sbmibtn13 = Button(screen10, text='Name',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=0, y=30)
    sbmibtn14 = Button(screen10, text='Under    :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=0, y=60)
    sbmibtn14 = Button(screen10, text='nature of groups    :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=0, y=110)
    
    e12 = Entry(screen10,).place(x=170, y=30)
def func36():
    global screen10
    screen10 = Toplevel(root)
    screen10.resizable(False, False)
    screen10.title('Group Alteration')
    screen10.geometry('650x300')
    sbmibtn13 = Button(screen10, text='Name',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=0, y=30)
    sbmibtn14 = Button(screen10, text='Under    :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=0, y=60)
    sbmibtn14 = Button(screen10, text='nature of groups    :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=0, y=110)
    
    e12 = Entry(screen10,).place(x=170, y=30)

def func37():
    global screen10
    screen10 = Toplevel(root)
    screen10.resizable(False, False)
    screen10.title('Group Alteration')
    screen10.geometry('650x300')
    sbmibtn13 = Button(screen10, text='Name',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=0, y=30)
    sbmibtn14 = Button(screen10, text='Under    :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=0, y=60)
    sbmibtn14 = Button(screen10, text='nature of groups    :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=0, y=110)
    
    e12 = Entry(screen10,).place(x=170, y=30)

def func38():
    global screen10
    screen10 = Toplevel(root)
    screen10.resizable(False, False)
    screen10.title('Group Alteration')
    screen10.geometry('650x300')
    sbmibtn13 = Button(screen10, text='Name',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=0, y=30)
    sbmibtn14 = Button(screen10, text='Under    :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=0, y=60)
    sbmibtn14 = Button(screen10, text='nature of groups    :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=0, y=110)
    
    e12 = Entry(screen10,).place(x=170, y=30)
def func39():
    global screen10
    screen10 = Toplevel(root)
    screen10.resizable(False, False)
    screen10.title('Group Alteration')
    screen10.geometry('650x300')
    sbmibtn13 = Button(screen10, text='Name',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=0, y=30)
    sbmibtn14 = Button(screen10, text='Under    :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=0, y=60)
    sbmibtn14 = Button(screen10, text='nature of groups    :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=0, y=110)
    
    e12 = Entry(screen10,).place(x=170, y=30)


def create():
    global screen3
    screen3 = Toplevel(root)
    screen3.resizable(False, False)
    screen3.title('create company')
    screen3.geometry('940x520')
    Label(screen3, text='COMPANY CREATION',bg="lightblue",font='15',fg="white",width=640).pack()
    global  Cname,Cmailing,Caddress, email,state,country,pcode,tphone,mphone,fax,site,symbol,format
    Cname = StringVar()
    Cmailing = StringVar()
    Caddress = StringVar()
    email = StringVar()
    state = StringVar()
    country = StringVar()
    pcode = IntVar()
    tphone = StringVar()
    mphone = StringVar()
    fax = StringVar()
    site = StringVar()
    symbol = StringVar()
    format = StringVar()
    
    
    cname = Label(screen3, text='Company Name:').place(x=20, y=70)
    e1 = Entry(screen3, textvariable=Cname,width=40).place(x=120, y=70)
    y1 = Label(screen3, text='Financial Year begining From:').place(x=450, y=70)
    # e2 = DateEntry(screen3,width=25)
    adrs1 = Label(screen3, text='Mailing Name:').place(x=20, y=110)
    e3 = Entry(screen3, textvariable=Cmailing, width=40).place(x=120, y=110)
    y2 = Label(screen3, text='Books Begining From:').place(x=450, y=110)
    adrs = Label(screen3, text='Address:').place(x=20, y=150)
    e4 = Entry(screen3,textvariable=Caddress,width=40).place(x=120, y=150)

b1 = Button(root, text="Create", fg="black", activebackground="palegreen",
            bg="white", width=20, height=1,).place(x=830, y=230)

b2 = Button(root, text="Alter", fg="black", activebackground="palegreen",
            bg="white", width=20, height=1,).place(x=830, y=260)
b3 = Button(root, text="Chart of Accounts", fg="black", activebackground="palegreen",
            bg="white", width=20, height=1,command=func4).place(x=830, y=290)
mstrs1 = Label(root, text="Transactions",bg="lightblue",fg="black",font="13").place(x=847,y=320)            
b4 = Button(root, text="Vouchers",fg="black", activebackground="palegreen",
            bg="white", width=20, height=1,).place(x=830, y=355)

b6 = Button(root, text="Day Book", fg="black", activebackground="palegreen",
            bg="white", width=20, height=1,).place(x=830, y=390)
mstrs2 = Label(root, text="Utilities",bg="lightblue",fg="black",font="13").place(x=865,y=420)            
b7 = Button(root, text="Banking", fg="black", activebackground="palegreen",
            bg="white", width=20, height=1, command=func3).place(x=830, y=450)
mstrs3 = Label(root, text="Reports",bg="lightblue",fg="black",font="13").place(x=865,y=480)
b8 = Button(root, text="Balance sheet", fg="black", activebackground="palegreen",
            bg="white", width=20, height=1,).place(x=830, y=510)

b9 = Button(root, text="Profit & Loss", fg="black", activebackground="palegreen",
            bg="white", width=20, height=1,).place(x=830, y=540)
b10 = Button(root, text="Stock summary", fg="black", activebackground="palegreen",
            bg="white", width=20, height=1,).place(x=830, y=570)
b11 = Button(root, text="Ratio Analysis", fg="black", activebackground="palegreen",
            bg="white", width=20, height=1,).place(x=830, y=600)

b12 = Button(root, text="Display more Reports", fg="black", activebackground="palegreen",
            bg="white", width=20, height=1,).place(x=830, y=630)
b13 = Button(root, text="Quit", fg="black", activebackground="palegreen",
            bg="white", width=20, height=1,).place(x=830, y=660)          
             
def create2():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('CHEQUE PRINTING')
    screen4.geometry('1500x770')
    frame131 = Frame(screen4, bg="lightblue", width=250, height=600)
    frame131.place(x=630, y=0)
    frame131 = Label(screen4, text="List of Masters",bg="black",fg="white",width=32,padx=10,pady=10).place(x=630, y=20)
    frame13 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame13.place(x=1400, y=0)
    date = Button(frame13, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame13, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9),command=func2, activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame13, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700)
    sbmibtn = Button(screen4, text='CREATE',command=func7,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=650,y=140)
    e11 = Entry(screen4,).place(x=700, y=100)
    Label(screen4, text='LIST OF ALL BANKS',bg="lightblue",font='19',fg="black",width=430).pack()

def create3():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('POST DATED SUMMARY')
    screen4.geometry('1500x770')
    frame131 = Frame(screen4, bg="lightblue", width=250, height=600)
    frame131.place(x=630, y=0)
    frame131 = Label(screen4, text="List of Masters",bg="black",fg="white",width=32,padx=10,pady=10).place(x=630, y=20)
    frame13 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame13.place(x=1400, y=0)
    date = Button(frame13, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame13, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9),command=func2, activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame13, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700)
    sbmibtn = Button(screen4, text='CREATE',command=func11,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=650,y=140)
    sbmibtn1 = Button(screen4, text='ALL ITEMS',command=func6,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=650,y=170)
    e11 = Entry(screen4,).place(x=700, y=100)
    Label(screen4, text='LIST OF ALL BANKS',bg="lightblue",font='19',fg="black",width=430).pack()

def create4():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('DEPOSIT SLIP')
    screen4.geometry('1500x770')
    frame131 = Frame(screen4, bg="lightblue", width=250, height=600)
    frame131.place(x=630, y=0)
    frame131 = Label(screen4, text="List of Masters",bg="black",fg="white",width=32,padx=10,pady=10).place(x=630, y=20)
    frame13 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame13.place(x=1400, y=0)
    date = Button(frame13, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame13, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9),command=func2, activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame13, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700)
    sbmibtn = Button(screen4, text='CREATE',command=func8,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=650,y=140)
    e11 = Entry(screen4,).place(x=700, y=100)
    Label(screen4, text='LIST OF ALL BANKS',bg="lightblue",font='19',fg="black",width=430).pack()

def create5():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('PAYMENT ADVICE')
    screen4.geometry('1500x770')
    frame131 = Frame(screen4, bg="lightblue", width=250, height=600)
    frame131.place(x=630, y=0)
    frame131 = Label(screen4, text="List of Masters",bg="black",fg="white",width=32,padx=10,pady=10).place(x=630, y=20)
    frame13 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame13.place(x=1400, y=0)
    date = Button(frame13, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame13, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9),command=func2, activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame13, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700)
    sbmibtn = Button(screen4, text='CREATE',command=func9,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=650,y=140)
    e11 = Entry(screen4,).place(x=700, y=100)
    Label(screen4, text='LIST OF ALL BANKS',bg="lightblue",font='19',fg="black",width=430).pack()


def create6():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('BANK RECONCILIATION')
    screen4.geometry('1500x770')
    frame131 = Frame(screen4, bg="lightblue", width=250, height=600)
    frame131.place(x=630, y=0)
    frame131 = Label(screen4, text="List of Masters",bg="black",fg="white",width=32,padx=10,pady=10).place(x=630, y=20)
    frame13 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame13.place(x=1400, y=0)
    date = Button(frame13, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame13, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9),command=func2, activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame13, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700)
    sbmibtn = Button(screen4, text='CREATE',command=func10,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=650,y=140)
    e11 = Entry(screen4,).place(x=700, y=100)
    Label(screen4, text='LIST OF ALL BANKS',bg="lightblue",font='19',fg="black",width=430).pack()

def create7():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('cheque register')
    screen4.geometry('1500x770')
    frame131 = Frame(screen4, bg="lightblue", width=250, height=600)
    frame131.place(x=630, y=0)
    frame131 = Label(screen4, text="List of Masters",bg="black",fg="white",width=32,padx=10,pady=10).place(x=630, y=20)
    frame13 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame13.place(x=1400, y=0)
    date = Button(frame13, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame13, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9),command=func2, activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame13, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700)
    sbmibtn = Button(screen4, text='CREATE',command=func10,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=650,y=140)
    e11 = Entry(screen4,).place(x=700, y=100)
    Label(screen4, text='LIST OF ALL BANKS',bg="lightblue",font='19',fg="black",width=430).pack()

def create8():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('Bank Accounts')
    screen4.geometry('1500x770')
    Label(screen4, text='List of Groups',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Branch / Divisions',fg='black',font=('Arial',9),command=func12,activebackground='palegreen',width=30,border=0).place(x=20, y=60)
    sbmibtn14 = Button(screen4, text='Capital Account',fg='black',font=('Arial',9),command=func13,activebackground='palegreen',width=30,border=0).place(x=12, y=80)
    sbmibtn15 = Button(screen4, text='Reserve And Surplus',fg='black',font=('Arial',9),command=func14,activebackground='palegreen',width=30,border=0).place(x=39, y=100)
    sbmibtn16 = Button(screen4, text='Current Assets',fg='black',font=('Arial',9),command=func15,activebackground='palegreen',width=30,border=0).place(x=12, y=120)
    sbmibtn17 = Button(screen4, text='Bank Accounts',fg='black',font=('Arial',9),command=func16,activebackground='palegreen',width=30,border=0).place(x=25, y=140)
    sbmibtn18 = Button(screen4, text='Cash In Hand',fg='black',font=('Arial',9),command=func17,activebackground='palegreen',width=30,border=0).place(x=20, y=160)
    sbmibtn19 = Button(screen4, text='Deposits(Assets)',fg='black',font=('Arial',9),command=func18,activebackground='palegreen',width=30,border=0).place(x=30, y=180)
    sbmibtn20 = Button(screen4, text='Loans & Advances(Assets)',fg='black',font=('Arial',9),command=func19,activebackground='palegreen',width=30,border=0).place(x=55, y=200)
    sbmibtn21 = Button(screen4, text='Stock in Hand',fg='black',font=('Arial',9),command=func20,activebackground='palegreen',width=30,border=0).place(x=15, y=220)
    sbmibtn22 = Button(screen4, text='Sundry Debtors',fg='black',font=('Arial',9),command=func21,activebackground='palegreen',width=30,border=0).place(x=20, y=240)
    sbmibtn23 = Button(screen4, text='Current Liabalities',fg='black',font=('Arial',9),command=func22,activebackground='palegreen',width=30,border=0).place(x=20, y=260)
    sbmibtn24 = Button(screen4, text='Duties & Taxes',fg='black',font=('Arial',9),command=func23,activebackground='palegreen',width=30,border=0).place(x=20, y=280)
    sbmibtn25 = Button(screen4, text='Provisions',fg='black',font=('Arial',9),command=func24,activebackground='palegreen',width=30,border=0).place(x=20, y=300)
    sbmibtn26 = Button(screen4, text='Sundry Creditors',fg='black',font=('Arial',9),command=func25,activebackground='palegreen',width=30,border=0).place(x=20, y=320)
    sbmibtn27 = Button(screen4, text='Direct Expenses',fg='black',font=('Arial',9),command=func26,activebackground='palegreen',width=30,border=0).place(x=20, y=340)
    sbmibtn28 = Button(screen4, text='Dir Incomesect',fg='black',font=('Arial',9),command=func27,activebackground='palegreen',width=30,border=0).place(x=20, y=360)
    sbmibtn29 = Button(screen4, text='Fixed Assets',fg='black',font=('Arial',9),command=func28,activebackground='palegreen',width=30,border=0).place(x=20, y=380)
    sbmibtn30 = Button(screen4, text='Indirect Expenses',fg='black',font=('Arial',9),command=func29,activebackground='palegreen',width=30,border=0).place(x=20, y=400)
    sbmibtn31 = Button(screen4, text='Indirect Incomes',fg='black',font=('Arial',9),command=func30,activebackground='palegreen',width=30,border=0).place(x=20, y=420)
    sbmibtn32 = Button(screen4, text='Investments',fg='black',font=('Arial',9),command=func31,activebackground='palegreen',width=30,border=0).place(x=20, y=440)
    sbmibtn33 = Button(screen4, text='Loans(Liability)',fg='black',font=('Arial',9),command=func32,activebackground='palegreen',width=30,border=0).place(x=20, y=460)
    sbmibtn34 = Button(screen4, text='Bank OD A/c',fg='black',font=('Arial',9),command=func33,activebackground='palegreen',width=30,border=0).place(x=20, y=480)
    sbmibtn35 = Button(screen4, text='Secured Loans',fg='black',font=('Arial',9),command=func34,activebackground='palegreen',width=30,border=0).place(x=20, y=500)
    sbmibtn36 = Button(screen4, text='Unsecured Loans',fg='black',font=('Arial',9),command=func35,activebackground='palegreen',width=30,border=0).place(x=20, y=520)
    sbmibtn37 = Button(screen4, text='Misc. Expenses (ASSETS)',fg='black',font=('Arial',9),command=func36,activebackground='palegreen',width=30,border=0).place(x=20, y=540)
    sbmibtn38 = Button(screen4, text='Purchase Accounts',fg='black',font=('Arial',9),command=func37,activebackground='palegreen',width=30,border=0).place(x=20, y=560)
    sbmibtn39 = Button(screen4, text='Sales Accounts',fg='black',font=('Arial',9),command=func38,activebackground='palegreen',width=30,border=0).place(x=20, y=580)
    sbmibtn40 = Button(screen4, text='Suspense A/c',fg='black',font=('Arial',9),command=func39,activebackground='palegreen',width=30,border=0).place(x=20, y=600)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9),command=func2, activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='').place(x=20, y=70)(font="timesnewroman").pack()  
def create9():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('Bank Accounts')
    screen4.geometry('1500x770')
    Label(screen4, text='List of Assets',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Assets',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=20, y=60)
    
    sbmibtn14 = Button(screen4, text='Current Assets',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=12, y=80)
    sbmibtn15 = Button(screen4, text='Bank Accounts',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=39, y=100)
    sbmibtn16 = Button(screen4, text='Current Assets',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=12, y=120)
    sbmibtn16 = Button(screen4, text='Cash in Hand',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=25, y=140)
    sbmibtn16 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=20, y=160)
    sbmibtn16 = Button(screen4, text='Deposits(Assets)',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=30, y=160)
    sbmibtn16 = Button(screen4, text='Loans & Advances(Assets)',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=55, y=180)
    sbmibtn16 = Button(screen4, text='Stock In Hand',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=15, y=200)
    sbmibtn16 = Button(screen4, text='Sundry Debtors',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=20, y=220)
    sbmibtn16 = Button(screen4, text='Fixed Assets',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=20, y=240)
    sbmibtn16 = Button(screen4, text='Investments',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=20, y=260)
    sbmibtn16 = Button(screen4, text='Misc.Expenses (ASSETS)',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=20, y=280)
    
    sbmibtn16 = Button(screen4, text='Liabilities',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=20, y=320)
    sbmibtn13 = Button(screen4, text='Branch / Divisions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=20, y=340)
    sbmibtn14 = Button(screen4, text='Capital Account',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=12, y=360)
    sbmibtn15 = Button(screen4, text='Reserve and Surplus',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=39, y=380)
    sbmibtn16 = Button(screen4, text='Current Liabalities',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=20, y=400)
    sbmibtn16 = Button(screen4, text='Duties & taxes',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=20, y=420)
    sbmibtn16 = Button(screen4, text='Provisions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=20, y=440)
    sbmibtn16 = Button(screen4, text='Sundry creditors',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=20, y=460)
    sbmibtn16 = Button(screen4, text='Loans(liability)',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=20, y=480)
    sbmibtn16 = Button(screen4, text='Bank OD A/c',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=20, y=500)
    sbmibtn16 = Button(screen4, text='Secured Loans',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=20, y=520)
    sbmibtn16 = Button(screen4, text='Unsecured Loans',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=20, y=540)
    sbmibtn16 = Button(screen4, text='Sales Accounts',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=20, y=560)
    sbmibtn16 = Button(screen4, text='Profit and Loss A/c ',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=20, y=580)
    
    sbmibtn16 = Button(screen4, text='Expenses ',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=20, y=620)
    sbmibtn16 = Button(screen4, text='Direct Expenses ',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=20, y=640)
    sbmibtn16 = Button(screen4, text='Indirect Expenses ',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=20, y=660)
    sbmibtn16 = Button(screen4, text='Purchase Accounts ',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=20, y=680)
    
    
    sbmibtn16 = Button(screen4, text='Income  ',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=20, y=720)
    sbmibtn16 = Button(screen4, text='Direct Income  ',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=20, y=740)
    sbmibtn16 = Button(screen4, text='Indirect Income  ',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=20, y=760)
    sbmibtn16 = Button(screen4, text='Sales Accounts',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=20, y=780)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9),command=func2, activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='').place(x=20, y=70)(font="timesnewroman").pack()  
    
    
    
def create10():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('Bank Accounts')
    screen4.geometry('1500x770')
    Label(screen4, text='Abc',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn16 = Button(screen4, text='Attendance ',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=20, y=80)
    sbmibtn16 = Button(screen4, text='Contra ',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=20, y=100)
    sbmibtn16 = Button(screen4, text='Credit Note',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=20, y=120)
    sbmibtn16 = Button(screen4, text='Debit Note ',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=20, y=140)
    sbmibtn16 = Button(screen4, text='Delivery Note ',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=20, y=160)
    sbmibtn16 = Button(screen4, text='Job Work In Order ',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=20, y=180)
    sbmibtn16 = Button(screen4, text='Job Work Out Order',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=20, y=200)
    sbmibtn16 = Button(screen4, text='Journel',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=20, y=220)
    sbmibtn16 = Button(screen4, text='Material In',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=20, y=240)
    sbmibtn16 = Button(screen4, text='Material Out',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=20, y=260)
    sbmibtn16 = Button(screen4, text='Memorandum',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=20, y=280)
    sbmibtn16 = Button(screen4, text='Payment',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=20, y=300)
    sbmibtn16 = Button(screen4, text='Payrol',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=20, y=320)
    sbmibtn16 = Button(screen4, text='Physical Stock',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=20, y=340)
    sbmibtn16 = Button(screen4, text='Purchase',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=20, y=360)
    sbmibtn16 = Button(screen4, text='Purchase Order',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=20, y=380)
    sbmibtn16 = Button(screen4, text='Reciept',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=20, y=400)
    sbmibtn16 = Button(screen4, text='Reciept Note',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=20, y=420)
    sbmibtn16 = Button(screen4, text='Rejections In',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=20, y=440)
    sbmibtn16 = Button(screen4, text='Rejections Out',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=20, y=460)
    sbmibtn16 = Button(screen4, text='Reversing Journel',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=20, y=480)
    sbmibtn16 = Button(screen4, text='Sales',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=20, y=500)
    sbmibtn16 = Button(screen4, text='Sales Order',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=20, y=520)
    sbmibtn16 = Button(screen4, text='Stock Journel',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=20, y=540)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9),command=func2, activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='').place(x=20, y=70)(font="timesnewroman").pack()  
def create11():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('Bank Accounts')
    screen4.geometry('1500x770')
    Label(screen4, text='Abc',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9),command=func2, activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create12():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('Bank Accounts')
    screen4.geometry('1500x770')
    Label(screen4, text='Abc',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9),command=func2, activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create13():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('Bank Accounts')
    screen4.geometry('1500x770')
    Label(screen4, text='Abc',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9),command=func2, activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create14():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('Bank Accounts')
    screen4.geometry('1500x770')
    Label(screen4, text='Abc',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9),command=func2, activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create15():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('Bank Accounts')
    screen4.geometry('1500x770')
    Label(screen4, text='Abc',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9),command=func2, activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create16():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('Bank Accounts')
    screen4.geometry('1500x770')
    Label(screen4, text='Abc',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn1 = Button(screen4, text='Name   :Branch /Division',fg='black',font=('Arial',9),activebackground='palegreen',width=35,border=0).place(x=2, y=40)
    sbmibtn2 = Button(screen4, text='(Alias)    :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=2, y=60)
    sbmibtn3 = Button(screen4, text='Under    : primary ',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=2, y=100)
    sbmibtn4 = Button(screen4, text='Nature of Group',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=2, y=140)
    sbmibtn5 = Button(screen4, text='Group behaves like a sub-ledger   :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=10, y=180)
    sbmibtn6 = Button(screen4, text='Nett Debit/Credit Balances For Reporting :',fg='black',font=('Arial',9),activebackground='palegreen',width=40,border=0).place(x=2, y=200)
    sbmibtn7 = Button(screen4, text='Used for calculation( for example: taxes, discounts)  :',fg='black',font=('Arial',9),activebackground='palegreen',width=40,border=0).place(x=20, y=220)
    sbmibtn8 = Button(screen4, text='(for sales invoice entries)',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=20, y=240)
    sbmibtn9 = Button(screen4, text='Method to allocate when used in purchase invoice  :',fg='black',font=('Arial',9),activebackground='palegreen',width=40,border=0).place(x=20, y=260)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9),command=func2, activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create17():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('Bank Accounts')
    screen4.geometry('1500x770')
    Label(screen4, text='Abc',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn1 = Button(screen4, text='Name   :Branch /Division',fg='black',font=('Arial',9),activebackground='palegreen',width=35,border=0).place(x=2, y=40)
    sbmibtn2 = Button(screen4, text='(Alias)    :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=2, y=60)
    sbmibtn3 = Button(screen4, text='Under    : primary ',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=2, y=100)
    sbmibtn4 = Button(screen4, text='Nature of Group',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=2, y=140)
    sbmibtn5 = Button(screen4, text='Group behaves like a sub-ledger   :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=10, y=180)
    sbmibtn6 = Button(screen4, text='Nett Debit/Credit Balances For Reporting :',fg='black',font=('Arial',9),activebackground='palegreen',width=40,border=0).place(x=2, y=200)
    sbmibtn7 = Button(screen4, text='Used for calculation( for example: taxes, discounts)  :',fg='black',font=('Arial',9),activebackground='palegreen',width=40,border=0).place(x=20, y=220)
    sbmibtn8 = Button(screen4, text='(for sales invoice entries)',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=20, y=240)
    sbmibtn9 = Button(screen4, text='Method to allocate when used in purchase invoice  :',fg='black',font=('Arial',9),activebackground='palegreen',width=40,border=0).place(x=20, y=260)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9),command=func2, activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create18():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('Bank Accounts')
    screen4.geometry('800x400')
    Label(screen4, text='List of Godowns',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    sbmibtn1 = Button(screen4, text='Name   :Branch /Division',fg='black',font=('Arial',9),activebackground='palegreen',width=35,border=0).place(x=2, y=40)
    sbmibtn2 = Button(screen4, text='(Alias)    :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=2, y=60)
    sbmibtn3 = Button(screen4, text='Under    : primary ',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=2, y=100)
    sbmibtn4 = Button(screen4, text='Nature of Group',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=2, y=140)
    sbmibtn5 = Button(screen4, text='Group behaves like a sub-ledger   :',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=10, y=180)
    sbmibtn6 = Button(screen4, text='Nett Debit/Credit Balances For Reporting :',fg='black',font=('Arial',9),activebackground='palegreen',width=40,border=0).place(x=2, y=200)
    sbmibtn7 = Button(screen4, text='Used for calculation( for example: taxes, discounts)  :',fg='black',font=('Arial',9),activebackground='palegreen',width=40,border=0).place(x=20, y=220)
    sbmibtn8 = Button(screen4, text='(for sales invoice entries)',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=20, y=240)
    sbmibtn9 = Button(screen4, text='Method to allocate when used in purchase invoice  :',fg='black',font=('Arial',9),activebackground='palegreen',width=40,border=0).place(x=20, y=260)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9),command=func2, activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='').place(x=20, y=70)(font="timesnewroman").pack()
                                       



frame3 = Frame(root, bg="lightblue", width=140, height=790)
frame3.place(x=1400, y=0)
date = Button(frame3, text="Date", width=14, fg="black", font=(
"timesnewroman",9), command=func1, activebackground="palegreen", activeforeground="red")
date.place(x=13, y=20)
company = Button(frame3, text="Company", width=14, fg="black", font=(
"timesnewroman", 9),command=func2, activebackground="palegreen", activeforeground="red").place(x=13, y=50)   
root.mainloop()
