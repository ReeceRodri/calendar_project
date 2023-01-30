import tkinter as tk
from tkinter import END, ttk
from datetime  import date, datetime
from  calendar import monthrange
from statistics_page import statistics_page
from Queries import Queries

root = tk.Tk()
root.title("Calander")
root.geometry('500x400')

DATE = str(date.today()).split('-')

DAY = int(DATE[2])
MONTH = int(DATE[1])
YEAR = int(DATE[0])

current_window_date = [DAY, MONTH , YEAR]

def create_days_list(year, month):
    number_of_days = monthrange(year, month)[1]
    days_list = [i for i in range(1,number_of_days +1)]   
    return days_list

days_list = create_days_list(current_window_date[2], current_window_date[1])

month_list = ['January', 'February', 'March', 'April', 'May', 
            'June', 'July', 'August', 'September', 'October', 
            'November', 'December']

year_list = [i for i in range(1990,2100)]


def callback_day(selection):
    current_window_date[0] = selection
    print(current_window_date)
   

def callback_month(selection):
    current_window_date[1] = month_list.index(selection) + 1
    new_days_list = create_days_list(current_window_date[2], current_window_date[1])

    if current_window_date[0] not in new_days_list: 
        current_window_date[0] = new_days_list[-1]
        value_inside_days.set(current_window_date[0])
        
    day_optionmenue = tk.OptionMenu(date_frame, value_inside_days, *new_days_list,command=callback_day)
    day_optionmenue.place(relx=0, rely=0, relwidth= 0.25, relheight=1)
    print(current_window_date)




def callback_year(selection):
    current_window_date[2] = selection
    new_days_list = create_days_list(current_window_date[2], current_window_date[1])

    if current_window_date[0] not in new_days_list: 
        current_window_date[0] = new_days_list[-1]
        value_inside_days.set(current_window_date[0])
        
    day_optionmenue = tk.OptionMenu(date_frame, value_inside_days, *new_days_list,command=callback_day)
    day_optionmenue.place(relx=0, rely=0, relwidth= 0.25, relheight=1)



def scroll_date_right():
    
    if current_window_date[0] + 1 in create_days_list(current_window_date[2],current_window_date[1]):
        current_window_date[0] += 1

        value_inside_days.set(str(current_window_date[0]))
        new_days_list = create_days_list(current_window_date[2], current_window_date[1])
        day_optionmenue = tk.OptionMenu(date_frame, value_inside_days, *new_days_list,command=callback_day)
        day_optionmenue.place(relx=0, rely=0, relwidth= 0.25, relheight=1)
        
        value_inside_month.set(str(month_list[current_window_date[1]-1]))
        value_inside_year.set(str(current_window_date[2]))
            
    else: 
        if current_window_date[1] < 12:
            current_window_date[1] += 1
            current_window_date[0] = 0 
            scroll_date_right()
        else:
            current_window_date[2] += 1 
            current_window_date[1] = 1
            current_window_date[0] = 0
            scroll_date_right()
    
    

   
def scroll_date_left():
    if current_window_date[0] - 1 in create_days_list(current_window_date[2],current_window_date[1]):
        current_window_date[0] -= 1

        value_inside_days.set(str(current_window_date[0]))
        new_days_list = create_days_list(current_window_date[2], current_window_date[1])
        day_optionmenue = tk.OptionMenu(date_frame, value_inside_days, *new_days_list,command=callback_day)
        day_optionmenue.place(relx=0, rely=0, relwidth= 0.25, relheight=1)
       
        value_inside_month.set(str(month_list[current_window_date[1]-1]))
        value_inside_year.set(str(current_window_date[2]))
            
    else: 
        if current_window_date[1] > 1:
            current_window_date[1] -= 1
            current_window_date[0] = create_days_list(current_window_date[2],current_window_date[1])[-1] + 1
            scroll_date_left()
        else:
            current_window_date[2] -= 1 
            current_window_date[1] = 12
            current_window_date[0] = create_days_list(current_window_date[2],current_window_date[1])[-1] + 1
            scroll_date_left()
    

 

# add the following to the save button as a command and assign command=add_event
def add_event():
    editor= tk.Toplevel(root)
    editor.title("Calendar")
    editor.geometry("350x250")



    #Defining the save button function
    def save():
        date= editor_date.get()
        time= editor_time.get()
        title= editor_title.get()
        description= editor_description.get()
        
        #creating an instance of queries class
        queries=Queries()
        
        # writing to csv file
        queries.write_file([date,time,title,description])
        


    #Defining Labels 
    lb_date=tk.Label(editor,text="Date").place(x=10,y=20)
    lb_time=tk.Label(editor,text="Time").place(x=10,y=40)
    lb_title=tk.Label(editor,text="Title").place(x=10,y=60)
    lb_desc=tk.Label(editor,text="Description").place(x=10,y=80)

  
    # defining global statements to retrive data from main
    global value_inside_days 
    global value_inside_month
    global value_inside_year
    global editor_date
    global editor_time
    global editor_title
    global editor_description
    selected_date=[value_inside_days,value_inside_month,value_inside_year]

    
     
    #Entry Statements
    editor_time=tk.Entry(editor,width=30)
    editor_time.place(x=100,y=40)

    editor_title=tk.Entry(editor,width=30)
    editor_title.place(x=100,y=60)

    editor_description=tk.Entry(editor,width=30)
    editor_description.place(x=100,y=80)
    


    
 
    #Creating the save button
    save_button=tk.Button(editor,text="SAVE",command = save).place(x=300,y=100)

    return_button=tk.Button(editor, text="Return",command=editor.destroy).place(x=10,y=100)  
    
#Command to modify/edit data
def modify():
    add_event()
    #creating an instance of queries class
    queries=Queries("event_data_base.csv")
    
    found, column1, column2, column3 = queries.check_date(date)
    if found:
        editor_time.delete(0, END)
        editor_time.insert(0, column1)
        editor_title.delete(0, END)
        editor_title.insert(0, column2)
        editor_description.delete(0, END)
        editor_description.insert(0, column3)
    else:
        print("Date not found in the CSV file")

    








def create_event(frame):
    single_event_frame  = tk.Frame(frame , bg = 'black')
    single_event_frame.pack()


stat_button = tk.Button(root, text= 'st',bg = 'gray', fg = 'white', command = statistics_page)
stat_button.place(relx=0, rely=0, relwidth=0.05, relheight=0.05)

save_button = tk.Button(root, text= 'Add a task', bg = 'gray', fg = 'white', command = add_event)
save_button.place(relx=0.2, rely=0.85, relwidth=0.6, relheight=0.1)

forward_button = tk.Button(root, text= '>', bg = 'gray', fg = 'white', command= lambda: scroll_date_right())
forward_button.place(relx= 0.9, rely=0.87, relwidth=0.05, relheight= 0.05)

back_button = tk.Button(root, text= '<', bg = 'gray', fg = 'white', command= lambda: scroll_date_left())
back_button.place(relx=0.05, rely= 0.87, relwidth=0.05, relheight=0.05)


# Creating the event scrolling object 
event_frame = tk.Frame(root)
event_frame.place(relx = 0.15, rely= 0.2, relwidth= 0.7, relheight= 0.5)

# Create Canvas 
canvas = tk.Canvas(event_frame)
canvas.place(relx=0, rely= 0 , relwidth= 1, relheight= 1)

# Add a scrollbar to the Canvas
scrollbar = tk.Scrollbar(event_frame, orient= 'vertical', command= canvas.yview)
scrollbar.pack(side= 'right', fill= 'y')

# Configurate the canvas
canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

main_event_frame = tk.Frame(canvas)

canvas.create_window((0,0), window= main_event_frame, anchor='nw')

for i in range(10):
     tk.Button(main_event_frame, text= 'that is an event', bg = 'gray', fg = 'white').grid(row = i , column=0, pady = 5, padx = 10)


# Creating a date selecting onject
date_frame = tk.Frame(root, bg = '#80c1ff' )
date_frame.place(relx = 0.25, rely= 0.05, relwidth= 0.5, relheight= 0.1)


value_inside_days = tk.IntVar(date_frame)
value_inside_days.set(str(DAY))
day_optionmenue = tk.OptionMenu(date_frame, value_inside_days, *days_list,command=callback_day)
day_optionmenue.place(relx=0, rely=0, relwidth= 0.25, relheight=1)


value_inside_month = tk.IntVar(date_frame)
value_inside_month.set(month_list[MONTH - 1])
month_optionmenue = tk.OptionMenu(date_frame, value_inside_month, *month_list, command=callback_month)
month_optionmenue.place(relx=0.25, rely=0, relwidth= 0.35, relheight=1)


value_inside_year = tk.IntVar(date_frame)
value_inside_year.set(YEAR)
year_optionmenue = tk.OptionMenu(date_frame, value_inside_year, *year_list,command = callback_year)
year_optionmenue.place(relx=0.6, rely=0, relwidth= 0.4, relheight=1)
print(value_inside_days,value_inside_month,value_inside_year)


root.mainloop()