from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
import tkinter.messagebox
import events
import official


class Holidays:
    def __init__(self,root):
        self.root=root
        self.root.title("Holidays")
        self.root.geometry("400x540")
        self.root.iconbitmap("logo170.ico")
        self.root.resizable(0,0)


        holiday=StringVar()





        def on_enter1(e):
            but_show['background']="black"
            but_show['foreground']="cyan"
  
        def on_leave1(e):
            but_show['background']="SystemButtonFace"
            but_show['foreground']="SystemButtonText"

        def on_enter2(e):
            but_clear['background']="black"
            but_clear['foreground']="cyan"
  
        def on_leave2(e):
            but_clear['background']="SystemButtonFace"
            but_clear['foreground']="SystemButtonText"



        def show():
            if holiday.get()!="Select Holidays":
                if holiday.get()=="All India Event":
                    for date,name in sorted(events.custom_holidays.items()):
                        #print(date,name)
                        holidays_trees.insert('','end',values=(date,name))
                if holiday.get()=="Offical Holidays":
                    for date,name in sorted(official.custom_holidays.items()):
                        #print(date,name)
                        holidays_trees.insert('','end',values=(date,name))
            else:
                tkinter.messagebox.showerror("Error","Please Select Holidays")


        
        def clear():
            holiday.set("Select Holidays")
            holidays_trees.delete(*holidays_trees.get_children())






#=================frame=================================#
        
        mainframe=Frame(self.root,width=400,height=540,relief="ridge",bd=3)
        mainframe.place(x=0,y=0)

        firstframe=Frame(mainframe,width=394,height=180,relief="ridge",bd=3,bg="gray66")
        firstframe.place(x=0,y=0)

        secondframe=Frame(mainframe,width=394,height=354,relief="ridge",bd=3)
        secondframe.place(x=0,y=180)

#==========================================================================#

        holis=["All India Event","Offical Holidays"]
        holis_combo=Combobox(firstframe,values=holis,font=('arial',12),width=20,state="readonly",textvariable=holiday)
        holis_combo.set("Select Holidays")
        holis_combo.place(x=100,y=30)


        
        but_show=Button(firstframe,width=15,text="Show Holidays",font=('times new roman',12),cursor="hand2",command=show)
        but_show.place(x=30,y=100)
        but_show.bind("<Enter>",on_enter1)
        but_show.bind("<Leave>",on_leave1)

        but_clear=Button(firstframe,width=15,text="Clear",font=('times new roman',12),cursor="hand2",command=clear)
        but_clear.place(x=210,y=100)
        but_clear.bind("<Enter>",on_enter2)
        but_clear.bind("<Leave>",on_leave2)


#=======================================================================#


        scol=Scrollbar(secondframe,orient="vertical")
        scol.place(relx=1, rely=0, relheight=1, anchor='ne')

        holidays_trees=ttk.Treeview(secondframe,columns=("Date","Holiday Name"),height=16,yscrollcommand=scol.set)
        holidays_trees.heading("Date",text="Date")
        holidays_trees.heading("Holiday Name",text="Holiday Name")
        holidays_trees['show']="headings"
        holidays_trees.column("Date",width=125,minwidth=10)
        holidays_trees.column("Holiday Name",width=242,minwidth=40)
        holidays_trees.place(x=0,y=0)



if __name__ == "__main__":
    root=Tk()
    app=Holidays(root)
    root.mainloop()