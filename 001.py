from tkinter import *
from tkinter import ttk

###########подключаемся к бд#############
import pymysql.cursors
con = pymysql.connect(host='localhost',
                      user='root',
                      password='111',
                      db='bdmain',
                      charset='utf8mb4',
                      cursorclass=pymysql.cursors.DictCursor)

##### Создание окна #######
peremennaia = Tk()
##### название окна #######
peremennaia.title("база данных")
##### размер окна #######
peremennaia.geometry("400x300")
##### иконка #######
peremennaia.iconbitmap('static/icon.ico')

##### Добавление вкладок #######
tab_control = ttk.Notebook(peremennaia)

# вкладка 1 #

vkladka1 = ttk.Frame(tab_control)
tab_control.add(vkladka1, text='добавление')

# текст вкладки 1 #
txt1 = Label(vkladka1, text='наименование')
txt1.grid(column=0, row=0)

txt2 = Label(vkladka1, text='описание')
txt2.grid(column=0, row=1)

txt3 = Label(vkladka1, text='цена')
txt3.grid(column=0, row=2)

txt4 = Label(vkladka1, text='количество')
txt4.grid(column=0, row=3)


# ввод текста вкладки 1 #
txt = Entry(vkladka1,width=20)
txt.grid(column=2, row=0)

txt = Entry(vkladka1,width=20)
txt.grid(column=2, row=1)

txt = Entry(vkladka1,width=20)
txt.grid(column=2, row=2)

# ввод количества вкладки 1 #
spin = Spinbox(vkladka1, from_=0, to=100, width=5)
spin.grid(column=2, row=3)


# кнопка внутри вкладки 1 #
# действие кнопки 1 #
def clicked():
    txt1.configure(text="действие кнопки")
    txt2.configure(text="действие кнопки")
    txt3.configure(text="действие кнопки")
    txt4.configure(text="действие кнопки")

# кнопка 1 #
btn1 = Button(vkladka1, text="загрузка данныйх", command=clicked)
btn1.grid(column=0, row=4, padx=5, pady=5)


# вкладка 2 #
tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text='поиск')
lbl2 = Label(tab2, text='Вкладка 2')
lbl2.grid(column=0, row=0)


# запуск вкладки #
tab_control.pack(expand=1, fill='both')



##### запуск окна #######
peremennaia.mainloop()


