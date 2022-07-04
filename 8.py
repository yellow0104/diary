


import datetime
import tkinter as tk
from tkinter import END, ttk
from tkinter import messagebox
from tkcalendar import *

root = tk.Tk()

root.title('calendar')
root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='calendar.png'))
root.geometry("600x400")
root.resizable(False, False)

def t_day_diary():
    def save():
        messagebox_request = messagebox.askquestion('today diary', '저장할까요?')
        if messagebox_request == 'yes':
            with open('diary_saves.txt', 'a', encoding='utf-8') as f:
                f.write(f"\n/{datetime.date.today()}/ : {diary.get(1.0, END)}")
            win.destroy()
        else:
            print('test')
    win = tk.Tk()
    win.geometry("300x400")
    win.title('today diary')
    diary = tk.Text(win, width=40, height=20)
    diary.grid(row=0, column=0)
    bt = tk.Button(win, text="저장하기",command=save)
    bt.grid(row=1, column=0)
    

    

    win.mainloop() 
def read_t_day_diary():
    new_win = tk.Tk()
    
    new_win.geometry("300x400")
    new_win.title('today diary')

    title = ttk.Label(new_win, text='오늘의 일기 불러오기')
    title.grid(column=0, row=0)
    
    combo_search = ttk.Combobox(new_win)
    

    with open('diary_saves.txt', 'r', encoding='utf-8') as f:
        diary_saves_variable = f.read()
        
        diary_saves_date = diary_saves_variable.split('/')
        del(diary_saves_date[0])
        print(diary_saves_date)

    roop = 0

    record_list = []

    for i in range(int(len(diary_saves_date)/2)):
        record_list.append(diary_saves_date[roop])
        roop += 2
    combo_search['value'] = record_list
    combo_search['state'] = 'readonly'
    
    combo_search.grid(column=0, row=1)        

    def find_diary():
        diary_textbox.delete('1.0', 'end')
        put = 0
        dict_saves_date = {}
        for i in range(int(len(diary_saves_date)/2)):
            dict_saves_date[diary_saves_date[put]] = diary_saves_date[put+1]
            put+=2

        print(dict_saves_date)
        diary_text = combo_search.get() + dict_saves_date[combo_search.get()]
        print(diary_text)
        
        diary_textbox.insert('1.0', diary_text)

        
        # dictionary_record_list = dict(diary_saves_date)

        

        # print(dictionary_record_list[combo_search.get()])

    combo_search_button = tk.Button(new_win, text='검색', command=find_diary)
    combo_search_button.grid(column=1, row=1)
   
    diary_textbox = tk.Text(new_win, width=30, height=15)
    diary_textbox.grid(column=0, row=2)
    

    new_win.mainloop()

bt = tk.Button(text="오늘의 일기 작성하기", command=t_day_diary)
bt.pack()

bt2 = tk.Button(text="오늘의 일기 불러오기", command=read_t_day_diary)
bt2.pack()

cal = Calendar(root, selectmode='day', year=2022, month=6, day = 12)
cal.pack(pady=20)

root.mainloop()