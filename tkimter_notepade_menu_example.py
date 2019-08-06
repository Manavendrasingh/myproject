import tkinter
import tkinter.filedialog
import  tkinter.messagebox
import os
import tkinter.font
import tkinter.colorchooser
""" file functions start from here  """
filename = None
zoom_value = 15#random value
zoomout_value = 10#random value
def newfile():
   global filename
   root.title(" untitled - notepad")#to change tatle when open new file
   filename = None#default value
   filearea.delete(1.0,tkinter.END)#to errase everthing from text when open new file


def openfile():
    global filename
    filename = tkinter.filedialog.askopenfilename(defaultextension = ".txt",filetypes = [('All Files',"*.*"),("Text Documents","*.txt")])#take path from which file is opened
    if filename == "":
        filename = None
    else :
        root.title(os.path.basename(filename)+ "-Notepad")#to give title as filename or path name
        filearea.delete(1.0,tkinter.END)#to errase everthing from text when open new file
        f = open(filename,"r")#to open file at rea mode
        filearea.insert(1.0,f.read())#to insert everthing from file into text 1.0 mean start to end
        f.close()

def savefile():
    global filename
    if filename == None:
        filename = tkinter.filedialog.asksaveasfilename(initialfile = 'Untitled.txt',defaultextension = ".txt",filetypes = [('All Files',"*.*"),("Text Documents","*.txt")])#to give path for  file to save
        f = open(filename, "w")#open file at write mode
        f.write(filearea.get(1.0, tkinter.END))
        f.close()
        root.title(os.path.basename(filename) + " - Notepad")#to change title
    else :
        #save the file
        f = open(filename, "w")
        f.write(filearea.get(1.0, tkinter.END))
        f.close()
        root.title(os.path.basename(filename) + " - Notepad")
def savefileas():
        # save as new file
        global filename
        filename = tkinter.filedialog.asksaveasfilename(initialfile= os.path.basename(filename) + ".txt", defaultextension=".txt",filetypes=[('All Files', "*.*"), ("Text Documents", "*.txt")])
        f = open(filename, "w")
        f.write(filearea.get(1.0, tkinter.END))
        f.close()
        root.title(os.path.basename(filename) + " - Notepad")
def printfile():
    pass
def quitapp():
     root.destroy()#to exit from notepad

""" file function end here """


"""edit function start from here """
def cutportion():
    filearea.event_generate("<<Cut>>")#to cut portion

def copyportion():
    filearea.event_generate("<<Copy>>")#to copy

def pasteportion():
    filearea.event_generate("<<Paste>>")#to past

def deleteportion():
    filearea.delete(tkinter.SEL_FIRST, tkinter.SEL_LAST)#to delete

def select_all():
        filearea.tag_add(tkinter.SEL,1.0,tkinter.END)
        filearea.mark_set(tkinter.INSERT, "1.0")
        filearea.see(tkinter.INSERT)
        #filearea.tag_add(tkinter.SEL_FIRST, tkinter.SEL_LAST)
        #filearea.mark_set(tkinter.INSERT, "1.0")
        #filearea.see(tkinter.INSERT)
        #print(filearea)


"""edit function end here"""


"""view function start from here"""
def zoomin():
    global zoom_value,zoomout_value
    myfont = tkinter.font.Font(size = zoom_value)
    filearea.config(font = myfont)
    zoom_value = zoom_value + 3
    zoomout_value = zoom_value


def zoomout():
    global zoomout_value
    if zoomout_value > 0:
        myfont = tkinter.font.Font(size = zoomout_value)
        filearea.config(font=myfont)
        zoomout_value = zoomout_value - 3
"""view function end here """

"""help function start from here"""

def about():
    tkinter.messagebox.showinfo("Notepad","   This notepade is developed  by MR.Manvendra Singh       ")
"""help function end here """

def colorset():
    (rgb, hx) = tkinter.colorchooser.askcolor()
    filearea.tag_add('color', 'sel.first', 'sel.last')
    filearea.tag_configure('color', foreground=hx)


def popupmenu_edit(e):
   try:
      editsubmenu.tk_popup(e.x_root, e.y_root,0)
   finally:
      editsubmenu.grab_release()


def popupmenu_file(e):
   try:
      filesubmenu.tk_popup(e.x_root, e.y_root,0)
   finally:
      filesubmenu.grab_release()


if __name__ =="__main__":
        root  = tkinter.Tk()
        root.title("MS Notepad")
        root.minsize(400,400)

        """ <<<<<<<<creation of Text area start from here>>>>>>>>> """

        filearea = tkinter.Text(master=root, font = "lucida 13")
        file = None
        filearea.pack( expand=True,fill =  'both')

        """ <<<<<<<<<<<<<<end of creation of text area>>>>>>>"""

        filearea.bind("<Button-3>", popupmenu_edit)#for popup of editmenu on right click

       # filearea.bind("<ButtonPress-1>", popupmenu_file)#for popup of file on left click
        #filearea.bind("<Control-Key-a>", select_all)
        #texxt area end here

        """<<<<<<<<<<<<<<<<scrollbar coding start from here>>>>>>>>>>>"""

        scroll = tkinter.Scrollbar(filearea)
        scroll.pack(side = 'right',fill = 'y')
        scroll.config(command = filearea.yview)
        filearea.config(yscrollcommand = scroll.set)

        """<<<<<<<<<<<<<scrollbar coding end here>>>>>>>>>>>>>>>>"""

        mainmenu = tkinter.Menu(master = root)#main menu
        """"<<<<<<<creation of filemenu start from here>>>>>>>>"""

        filesubmenu = tkinter.Menu(master = mainmenu)#filemenu
        filesubmenu.add_command(label = "New ",command = newfile)
        filesubmenu.add_command(label = "Open",command = openfile)
        filesubmenu.add_command(label = "Save",command = savefile)
        filesubmenu.add_command(label = "Save as",command = savefileas)
        filesubmenu.add_command(label = "Print.",command = printfile)
        filesubmenu.add_command(label = "Exit.",command = quitapp)

        """<<<<<<<<<<<<<creation if filemenu end here>>>>>>>>>>>>>"""


        """<<<<<<<<<<creation if editmenu start from here>>>>>>>>>"""

        editsubmenu = tkinter.Menu(master  = mainmenu)
        editsubmenu.add_command(label = "Cut",command = cutportion)
        editsubmenu.add_command(label = "Copy",command = copyportion)
        editsubmenu.add_command(label = "Paste",command = pasteportion)
        editsubmenu.add_command(label = "Delete",command = deleteportion)
        editsubmenu.add_command(label = "Select All",command = select_all)

        """<<<<<<<<<creation if editmenu end here>>>>>>>>>>>>>>>>>>"""

        formatesubmenu = tkinter.Menu(master  = mainmenu)
        fontsubmenu = tkinter.Menu(master = formatesubmenu)
        sizesubmenu = tkinter.Menu(master=  formatesubmenu)
        fontoptions = tkinter.font.families(root)
        for option in fontoptions:
            fontsubmenu.add_command(label = option,command = lambda  myfont = tkinter.font.Font(family= option , size=15): filearea.configure(font = myfont))
        formatesubmenu.add_cascade(label = "font...",menu = fontsubmenu)
        for value in range(1, 31):
            sizesubmenu.add_command(label= str(value),command=lambda  myfont = tkinter.font.Font(size= value):filearea.config(font = myfont))
        formatesubmenu.add_cascade(label = "size",menu = sizesubmenu)
        formatesubmenu.add_command(label="color", command=colorset)

        """<<<<<<<<<<creation if editmenu end here>>>>>>>>>>>>>>>>>"""

        """<<<<<<<<<creation if helpmenu start from here>>>>>>>>>>>"""

        helpsubmenu = tkinter.Menu(master  = mainmenu)
        #helpsubmenu.add_command(label = "View Help",command = viewhelp)
        #helpsubmenu.add_command(label = "Send Feedback",command = feedback)
        helpsubmenu.add_command(label = "About Notepad",command = about)

        """<<<<<<<<<<<creation if helpmenu end here>>>>>>>>>>>>>>"""

        """<<<<<<<<<<<<<creation if viewmenu start from here>>>>>>>>>>>"""
        viewsubmenu = tkinter.Menu(master  = mainmenu)
        viewsubmenu.add_command(label = "Zoom In",command = zoomin )
        viewsubmenu.add_command(label = "Zoom Out",command = zoomout)
        """<<<<<<<<<<<<<<creation if viewmenu end here>>>>>>>>>>>>>>>>>>>"""


        """<<<<<<<<<<<<<joining of all menu with mainmenu>>>>>>>>>>>>>"""
        mainmenu.add_cascade(label = "File",menu = filesubmenu)
        mainmenu.add_cascade(label = "   Edit",menu = editsubmenu )
        mainmenu.add_cascade(label = "      View",menu = viewsubmenu)
        mainmenu.add_cascade(label = "        Formate",menu = formatesubmenu)
        mainmenu.add_cascade(label = "          Help",menu = helpsubmenu)
        root.config(menu = mainmenu)


root.state("zoomed")
root.mainloop()
