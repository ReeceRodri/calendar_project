import tkinter as tk
display_list = ['Week', 'Month', 'Year']
current_display = 0

def statistics_page():
    root = tk.Tk()
    
    root.geometry('700x450')


    def display_main_text(factor):
        global current_display
        
        if factor: 
            if current_display + 1 <= 2:
                current_display = current_display + 1 
                    
                main_display = tk.Label(root, text = display_list[current_display], bg = 'gray', fg = 'white')
                main_display.place(relx= 0.3 , rely= 0.9, relwidth=0.4, relheight= 0.05)
                    
        else :
                if current_display - 1 >= 0:
                    current_display -= 1
                    
                    main_display = tk.Label(root, text = display_list[current_display], bg = 'gray', fg = 'white')
                    main_display.place(relx= 0.3 , rely= 0.9, relwidth=0.4, relheight= 0.05)
                        
        

    line_chart_frame = tk.Frame(root, bg = '#80c1ff')
    line_chart_frame.place(relx=0.01, rely=0.01, relwidth= 0.98, relheight=0.42)

    bar_chart_frame = tk.Frame(root, bg = '#80c1ff')
    bar_chart_frame.place(relx=0.01 , rely= 0.45 , relwidth=0.485, relheight=0.42)

    pie_chart_frame = tk.Frame(root, bg = '#80c1ff')
    pie_chart_frame.place(relx=0.505 , rely= 0.45, relwidth=0.485, relheight=0.42)

    left_button = tk.Button(root,text = "<",bg = 'gray', fg = 'white', command = lambda: display_main_text(False))
    left_button.place(relx= 0.02 , rely= 0.9 , relwidth=0.05, relheight= 0.05)

    right_button = tk.Button(root,text = ">",bg = 'gray', fg = 'white',command = lambda: display_main_text(True))
    right_button.place(relx= 0.93 , rely= 0.9 , relwidth=0.05, relheight= 0.05)

    main_display = tk.Label(root, text = "Week", bg = 'gray', fg = 'white')
    main_display.place(relx= 0.3 , rely= 0.9, relwidth=0.4, relheight= 0.05)

        
    root.mainloop()
