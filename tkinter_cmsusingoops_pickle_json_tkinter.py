import tkinter
import tkinter.messagebox
from  cmsusingoop_pickle_exceptionhandling import *
import tkinter.filedialog

topindex = 0
"""function which creat csvfile and save data"""
def exportallcostumerincsv():
    filename  = tkinter.filedialog.asksaveasfilename()#TO ASK PATH WHERE USER WANTS TO SAVE FILE
    fs = open(filename,"w")
    columns = ["ID", "Name", "contect number", "email", "Address"]#TO GIVE OF COLUMNS IN CSV FILE
    for i in range (len(columns)):
        fs.write(columns[i]+",")
    fs.write("\n")
    rowno= 1
    for e in costumer.listcos:
        cosindict = e.__dict__#TO CONVERT OBJECT DATA INTO DICTIONARY
        columns = 0
        for e1 in cosindict.values():#TAKE VALUES ONE BY ONE AND WRITE IN CSV FILE
            fs.write(str(e1)+",")
        fs.write("\n")
    fs.close()


"""THIS FUNTION FILL ENTRY BY SEARCH DATA"""
def showcostumerbyindex(i):
    cos = costumer.listcos[i]
    varid.set(cos.id)
    varcont_no.set(cos.cont_no)
    varaddress.set(cos.address)
    varemail.set(cos.email)
    varname.set(cos.name)

"""THIS USE TO SHOW ALL COSTUMER IN TABLE FORMATE"""
def showallcostumerintableformate(top):
    columns = ["ID","Name","contect number","email","Address"]#TO GIVE NAMES OF COLUMNS
    for i in range (len(columns)):
        lbl1 = tkinter.Label(master = top ,text = columns[i])#CREAT LABEL OF COLUMN ACCORDING NAME
        lbl1.grid(row = 0,column = i)
    rowno = 1
    for e in costumer.listcos:#LOOP FOR ROW
        cosindict = e.__dict__#TO CONVERT OBJECT INTO DICTIONARY FORMATE
        columnno = 0
        for e1 in cosindict.values():#LOOP FOR COLUMN
            var1 = tkinter.StringVar()
            txt1 = tkinter.Entry(master  = top ,textvariable = var1)
            txt1.grid(row=rowno,column = columnno)
            var1.set(e1)
            columnno+=1
        rowno+=1

"""<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<HANDLER CODING START FORM HERE>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"""
"""TO ADD COSTUMER WHEN USENER CLICK ON ADD BUTTON  """
def addcostumer_click():
    try:
        cos = costumer()
        cos.id = varid.get()
        cos.name = varname.get()
        cos.cont_no = varcont_no.get()
        cos.email = varemail.get()
        cos.address = varaddress.get()
        cos.addCostumer()
        tkinter.messagebox.showinfo("success " ,"costumer add successfully")
    except Exception as ex:
        tkinter.messagebox.showerror("error",ex)


""" THIS FUNCTION IS USE TO SEARCH COSTUMER WHEN USER CLICK ON SEARCH BUTTON"""
def searchcostumer_click():
    try:
        cos = costumer()
        cos.id = varid.get()
        flag = cos.searchCostumer()
        if flag == 0:
            tkinter.messagebox.showerror("error","coatumer not fount",)
        else:
           # varid.set(cos.id)
            varcont_no.set(cos.cont_no)
            varaddress.set(cos.address)
            varemail.set(cos.email)
            varname.set(cos.name)
    except Exception as ex:
        print(ex)


"""THIS FUNCTION USE TO MODIFY COSTUMER"""
def   modifycostumer_click():
    try:
        cos = costumer()
        cos.id = varid.get()
        cos.name = varname.get()
        cos.cont_no = varcont_no.get()
        cos.email = varemail.get()
        cos.address = varaddress.get()
        flag =  cos.modifyCostumer()
        if flag == 0:
            tkinter.messagebox.showerror("error", "costumer  not fount")
        else :
            tkinter.messagebox.showinfo("success","costumer modify successfully")
    except Exception as ex:
        tkinter.messagebox.showerror("error",ex)

"""THIS FUNCTION IS SHOW THE FIST COSTUMER """
def  fistcostumer_click():
    global topindex
    topindex = 0
    showcostumerbyindex(topindex)

""" THIS FUNCTION IS SHOW NEXT COSTUMER """
def nextcostumer_click():
    global topindex
    if topindex < len(costumer.listcos)-1:
        topindex+=1
    showcostumerbyindex(topindex)



""" THIS FUNCTION PREVIOUS COSTUMER """
def  previouscostumer_click():
    global topindex
    if topindex>0:
        topindex-=1
    showcostumerbyindex(topindex)


""" THIS FUNCTION SHOW LAST COSTUMER """
def lastcostumer_click():
    global topindex
    topindex = len(costumer.listcos)-1
    showcostumerbyindex(topindex)

"""THIS FUNCTION CONVERT ALL COSTUMER IN TABLE FORMATE """
def showallcostumerintable_click():
    top = tkinter.Toplevel()
    showallcostumerintableformate(top)


""" THIS FUNCTION DEETE THE COSTUMER """
def  deletecostumer_click():
    cos  = costumer()
    try:
        cos.id = varid.get()
        cos.deleteCostumer()
        tkinter.messagebox.showinfo("sucess","costumer is delete successfully")
    except Exception as ex:
        tkinter.messagebox.showerror("error",ex)


""" THIS FUNCTION SAVE ALL COSTUMER IN FILE """
def  saveallcostuminfile_click ():
    costumer.saveinpickle()
    tkinter.messagebox.showinfo("success","costumer saved successfully")


"""THIS FUNCTION LOAD ALL COSTUMER FROM FILE"""
def loadcostumer_click():
    costumer.loadthroughpickle()
    tkinter.messagebox.showinfo("success", "costumer loaded successfully")



"""THIS FUNCTION SAVE DATE IN CSV FILE"""
def  savecostumercsv_click():
    exportallcostumerincsv()
"""<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<HANDLER CODING END HERE>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"""

root = tkinter.Tk()
root.config(background = "green")
root.title("MY CMS")

root.minsize(400,300)
root.maxsize(800,500)
#for r in range(4):
    #root.rowconfigure(index = r,minsize = 100)
#for c in range(4):
   # root.columnconfigure(index = c ,minsize = 100)

"""<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< LABELING START HERE>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  """
lbId = tkinter.Label(master = root ,text = "Id",bg = "green",width = 60)
lbId.grid(row = 1,column = 1,columnspan = 2)

lbname = tkinter.Label(master = root ,text = "Name",bg = "green",width =60 )
lbname.grid(row = 2,column = 1,columnspan = 2)

lbaddress = tkinter.Label(master = root ,text = "address",bg = "green",width = 60)
lbaddress.grid(row = 3,column = 1,columnspan = 2)

lbemail = tkinter.Label(master = root ,text = "email",bg = "green",width = 60)
lbemail.grid(row = 4,column = 1,columnspan = 2)

lbcont_no = tkinter.Label(master = root ,text = "cont_no",bg = "green",width = 60)
lbcont_no.grid(row = 5,column = 1,columnspan = 2)
"""<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<LABELING END HERE >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"""

"""<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<ENTRY START FROM HERE >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"""
varid = tkinter.IntVar()
enid = tkinter.Entry(master = root ,text  = varid,width = 20)
enid.grid(row = 1 ,column = 2,columnspan = 2)

varname = tkinter.StringVar()
enname = tkinter.Entry(master = root ,text  = varname,width = 20)
enname.grid(row = 2 ,column = 2,columnspan = 2)

varaddress = tkinter.StringVar()
enaddress = tkinter.Entry(master = root ,text  = varaddress,width = 20)
enaddress.grid(row = 3,column = 2,columnspan = 2)

varemail = tkinter.StringVar()
enemail = tkinter.Entry(master = root ,text  = varemail,width = 20)
enemail.grid(row = 4 ,column = 2,columnspan = 2)

varcont_no = tkinter.IntVar()
encont_no = tkinter.Entry(master = root ,text  = varcont_no,width = 20)
encont_no.grid(row = 5 ,column = 2,columnspan = 2)
"""<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<ENTRYES END HERE>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"""

""" <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<BUTTONS START FROM HERE >>>>>>>>>>>>>>>>>>>>>>>>>>"""
btnadd = tkinter.Button(master = root ,text = "add",bg = "blue",width = 10,command = addcostumer_click)
btnadd.grid(row= 6,column = 1,columnspan = 2)

btnsearch = tkinter.Button(master = root,text = "search",bg = "blue",width = 10,command = searchcostumer_click)
btnsearch.grid(row= 6,column = 2,columnspan = 2)

btnmodify = tkinter.Button(master = root ,text = "modify",bg = "blue",width = 10,command = modifycostumer_click)
btnmodify.grid(row= 6,column = 3,columnspan = 1)

btnfist = tkinter.Button(master = root ,text = "fist",bg = "blue",width = 10,command = fistcostumer_click)
btnfist.grid(row= 7,column = 1,columnspan = 2)

btnnext = tkinter.Button(master = root ,text = "next",bg = "blue",width = 10,command = nextcostumer_click)
btnnext.grid(row= 7,column = 2,columnspan = 2)

btnpre = tkinter.Button(master = root ,text = "previous",bg = "blue",width = 10,command = previouscostumer_click)
btnpre.grid(row= 7,column = 3,columnspan = 1)

btndelete = tkinter.Button(master=root, text="delete",bg = "blue", width=10,command = deletecostumer_click)
btndelete.grid(row=8, column=1, columnspan=2)

btnsavecsv = tkinter.Button(master=root, text="f.csv",bg = "blue", width=10,command = savecostumercsv_click)
btnsavecsv.grid(row=8, column=2, columnspan=2)

btnsave = tkinter.Button(master = root ,text = "save",bg = "blue",width = 10,command = saveallcostuminfile_click)
btnsave.grid(row= 8,column = 3,columnspan = 1)

btnshowall = tkinter.Button(master = root ,text = "showall",bg = "blue",width = 10)#),command = showallcostumer_click)
btnshowall.grid(row= 9,column = 1,columnspan = 2)

btnlast = tkinter.Button(master = root ,text = "last",bg = "blue",width = 10,command = lastcostumer_click)
btnlast.grid(row= 9,column = 2,columnspan = 2)

btnload = tkinter.Button(master = root ,text = "load",bg = "blue",width = 10,command = loadcostumer_click)
btnload.grid(row= 9,column = 3,columnspan = 1)

btntbl = tkinter.Button(master = root ,text = "show in table",bg = "blue",width = 46,command  = showallcostumerintable_click )
btntbl.grid(row= 10,column = 2,columnspan = 3)
"""<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<BUTTONS CODEINFG ENND HERE >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> """
root.state("zoomed")
root.mainloop()