import tkinter
import pickle
class user:
    listuser = []
    def __init__(self):
        self.email = 0
        self.password = 0
    def register(self):
        user.listuser.append(self)
        listuserinbytes = pickle.dumps(add)



def addemail_click():
    add =adduser()
    add.email = varemail.get()
    add.password = varpassword.get()
    add.register()
    print("user add successfully")










root = tkinter.Tk()
root.minsize(400,300)
root.maxsize(600,500)
root.title("JSS Login")
#img = tkinter.PhotoImage(file = "download")
for r in range(4):
    root.rowconfigure(index = r,minsize = 75)
for c in range(4):
    root.columnconfigure(index = c ,minsize = 75)
#lable
ibemail = tkinter.Label(master = root ,text = "Email",width = 30)
ibemail.grid(row = 0,column = 1,columnspan = 2)
ibpassword = tkinter.Label(master = root,text = "Password",width = 30)
ibpassword.grid(row = 1,column = 1)
#entry
varemail = tkinter.StringVar()
txtemail = tkinter.Entry(master = root,text = varemail,width = 20)
txtemail.grid(row = 0,column = 2,columnspan = 2)
varpassword = tkinter.StringVar()
txtpassword = tkinter.Entry(root,text = varpassword,width = 20)
txtpassword.grid(row = 1,column = 2,columnspan = 2)

#button
btnadduser = tkinter.Button(master = root ,text = "adduser",width = 20,command = addemail_click )
btnadduser.grid(row = 2 ,column = 2)
btnlogin = tkinter.Button(master = root ,text = "Login",width = 20)
btnlogin.grid(row = 2,column = 1)
root.state("zoomed")
root.mainloop()

