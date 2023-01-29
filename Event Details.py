import tkinter as tk


# add the following to the save button as a command and assign command=add_event
def add_event():
    editor= tk.Toplevel()
    editor=tk.Tk()
    editor.title("Calendar")
    editor.geometry("350x250")



    #Defining the save button function
    def save():
        date= editor_date.get()
        time= editor_time.get()
        title= editor_title.get()
        description= editor_description.get()
        
        #creating an instance of queries class
        queries=Queries("event_data_base.csv")
        
        # writing to csv file
        queries.write_file([date,time,title,description])
        


    #Defining Labels 
    lb_date=tk.Label(editor,text="Date").place(x=10,y=20)
    lb_time=tk.Label(editor,text="Time").place(x=10,y=40)
    lb_title=tk.Label(editor,text="Title").place(x=10,y=60)
    lb_desc=tk.Label(editor,text="Description").place(x=10,y=80)

     #Entry Statements
    editor_date=tk.Entry(editor,width=30)
    editor_date.place(x=100,y=20)

    editor_time=tk.Entry(editor,width=30)
    editor_time.place(x=100,y=40)

    editor_title=tk.Entry(editor,width=30)
    editor_title.place(x=100,y=60)

    editor_description=tk.Entry(editor,width=30)
    editor_description.place(x=100,y=80)




    #Creating the save button
    save_button=tk.Button(editor,text="SAVE",command = save).place(x=300,y=100)

    return_button=tk.Button(editor, text="Return",command=editor.destroy).place(x=10,y=100)

    editor.mainloop()