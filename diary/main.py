


import datetime
import tkinter as tk
from tkinter import END, Menu, ttk
from tkinter import messagebox
from tkcalendar import *

import babel.numbers
import keyboard


import os
import sys 
def resource_path(relative_path): #이미지, txt 파일 os exe
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)




def program():
    root = tk.Tk()  

    root.title('diary')
    root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file=resource_path('img/calendar.png')))
    root.resizable(False, False)
    
    
    def t_day_diary(): #쓰기
        def save():
            messagebox_request = messagebox.askquestion('today diary', '저장할까요?')
            if messagebox_request == 'yes':
                with open(resource_path('img\diary_saves.txt'), 'r', encoding='utf-8') as f:
                    diary_saves_variable = f.read()
            
                    diary_saves_date = diary_saves_variable.split('/')
                print(type(datetime.date.today()))
                print(diary_saves_date)
                if str(datetime.date.today()) in diary_saves_date:
                    print("여기까지 실행됨")
                    troop = 1
                    troop_int = 2
                    while troop:
                        
                        
                        print(f"{datetime.date.today()}({str(troop_int)})")
                        if f"{datetime.date.today()}({str(troop_int)})" in diary_saves_date:
                            troop_int += 1
                            print(troop_int)
                            continue
                        else:
                            print("여기까지 실행됨2")
                            troop = 0
                            with open(resource_path('img\diary_saves.txt'), 'a', encoding='utf-8') as f:
                                f.write(f"\n/{datetime.date.today()}({str(troop_int)})/ : {diary.get(1.0, END)}") #이어적기
                                messagebox.showinfo('today diary', '저장이 완료되었습니다.')
                            win.destroy()
                            program()
                else:
                    with open(resource_path('img\diary_saves.txt'), 'a', encoding='utf-8') as f:
                        f.write(f"\n/{datetime.date.today()}/ : {diary.get(1.0, END)}") #이어적기
                        messagebox.showinfo('today diary', '저장이 완료되었습니다')
                    win.destroy()
                    program()
                
            else:
                print('test')
        def back_h():
            win.destroy()
            program()
        win = tk.Tk()
        win.geometry("300x400")
        win.title('today diary')
        win.resizable(False, False)


        frame = tk.Frame(win)
        frame.grid(column=0,row=4)

        diary = tk.Text(win, width=42, height=20)
        diary.grid(row=0, column=0)
        bt = tk.Button(frame, text="저장하기",command=save)
        bt.grid(row=0, column=0)
        bt2 = tk.Button(frame, text="돌아가기",command=back_h)
        bt2.grid(row=0,column=1)

        
        

        
    
        root.destroy()
        win.mainloop() 
    def read_t_day_diary(): #불러오기
        root.destroy()
        new_win = tk.Tk()
        
        new_win.geometry("300x400")
        new_win.title('today diary')
        new_win.resizable(False, False)

        title = ttk.Label(new_win, text='오늘의 일기 불러오기')
        title.grid(column=0, row=0)

        readonly_title = ttk.Label(new_win, text='읽기전용입니다.')
        readonly_title.grid(column=0,row=3)
        combo_search = ttk.Combobox(new_win)
        

        with open(resource_path('img\diary_saves.txt'), 'r', encoding='utf-8') as f:
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
            diary_textbox.configure(state='normal')
            diary_textbox.delete('1.0', 'end')
            diary_textbox.configure(state='disabled')
            put = 0
            dict_saves_date = {}
            for i in range(int(len(diary_saves_date)/2)):
                dict_saves_date[diary_saves_date[put]] = diary_saves_date[put+1]
                put+=2

            print(dict_saves_date)
            diary_text = combo_search.get() + dict_saves_date[combo_search.get()]
            print(diary_text)
            diary_textbox.configure(state='normal')
            diary_textbox.insert('1.0', diary_text)
            diary_textbox.configure(state='disabled')
        def delete_diary():
            diary_date = combo_search.get()
            print(f"DIARY DATE={diary_date}")
            for i in diary_saves_date: 
                if str(i) == str(diary_date):
                    diary_index = diary_saves_date.index(i)

                    print(f"1.{diary_saves_date[diary_index]}")
                    print(f"2.{diary_saves_date[1]}")
                    print(f"3.{diary_index+1}")
                    print("-"*100)
                    print(diary_saves_date)
                    # diary_saves_date.pop(diary_index)
                    

                    with open(resource_path('img\diary_saves.txt'), 'w', encoding='utf-8') as f:
                        print(type(diary_saves_date))
                        print(type(diary_index))
                        diary_saves_date.pop(diary_index+1)
                        diary_saves_date.pop(diary_index)
                        diary_contents = "/".join(diary_saves_date)
                        print(f"/{diary_contents}")
                        f.write(f"/{diary_contents}")
                        diary_textbox.configure(state='normal')
                        diary_textbox.delete('1.0', 'end')
                        diary_textbox.insert('1.0', '일기가 삭제됨')
                        diary_textbox.configure(state='disabled')
                    pass 
            # dictionary_record_list = dict(diary_saves_date)

            

            # print(dictionary_record_list[combo_search.get()])
        def back_h():
            new_win.destroy()
            program()
            
        frame = tk.Frame(new_win)
        frame.grid(column=0,row=4)

        combo_search_button = tk.Button(frame, text='검색', command=find_diary)
        combo_search_button.grid(column=0,row=0)

        combo_del_button = tk.Button(frame, text='삭제', command=delete_diary)
        combo_del_button.grid(column=1,row=0)

        combo_back_button = tk.Button(frame, text='돌아가기',command=back_h)
        combo_back_button.grid(column=2,row=0)
        
    
        diary_textbox = tk.Text(new_win, width=42, height=15)
        diary_textbox.grid(column=0, row=2)
        diary_textbox.configure(state='disabled')
        

        new_win.mainloop()




    menubar = Menu(root)
    menu1 = Menu(menubar, tearoff=0)
    menu1.add_command(label='일기작성하기', command=t_day_diary)
    menu1.add_command(label='일기불러오기', command=read_t_day_diary)
    menubar.add_cascade(label='일기', menu=menu1)


    root.config(menu=menubar)

    root.config(background="white")


    bt_img_write = tk.PhotoImage(file=resource_path('img/bt_write.png'))
    bt_img_read = tk.PhotoImage(file=resource_path('img/bt_read.png'))



    bt = tk.Button(command=t_day_diary, image=bt_img_write, width=200, height=25, background="white")
    bt.grid(column=0, row=0)

    bt2 = tk.Button(command=read_t_day_diary,image=bt_img_read, width=200, height=25, background="white")
    bt2.grid(column=1, row=0)



    #calander



    preview = tk.Listbox(root, selectmode="single", height=10, width=25) #하나만선택 single, 여러개 extended
    roop = 0


    record_list = []

    with open(resource_path('img\diary_saves.txt'), 'r', encoding='utf-8') as f:
        diary_saves_variable = f.read()
            
        diary_saves_date = diary_saves_variable.split('/')
        print(f" log: {diary_saves_date[0]}")
        del(diary_saves_date[0])
        print(f"log2:{diary_saves_date}")

    for i in range(int(len(diary_saves_date)/2)):
        record_list.append(diary_saves_date[roop])
        roop += 2
        preview.insert(tk.END, record_list[0])
        record_list.pop(0)

    preview.grid(column=0, row=3)



    def test():
        # root = 0
        # contents = []
        # for i in diary_saves_date:
        #     root += 1
        #     if root % 2 == 0:
        #         contents.append(i)

        # select = preview.curselection()
        # print(contents[select[0]])
        print(diary_saves_date)

    #테스트용

    # bt_test = tk.Button(command=test, width=25, height=10, text="리스트값 확인하기")
    # bt_test.grid(column=3, row=0)

    #gui 에선 while 문금지
    # while 1:
    #     if keyboard.read_key() == "p":
    #         print(preview.size)
    #         continue


    now_date_time = datetime.datetime.now()
    cal = Calendar(root, selectmode='day', year=now_date_time.year, month=now_date_time.month, day = now_date_time.day)
    cal.grid(column=1, row=3, pady=20)

    root.mainloop()


program() #start