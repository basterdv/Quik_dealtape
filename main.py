import itertools
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.messagebox import showerror, showwarning, showinfo, askyesno
import pandas as pd

root = Tk()
root.title("Программа по анализу ленты сделок")
root.geometry("1500x675")


# открываем файл в текстовое поле
def logger(log_index):
    listbox1.insert(0, log_index)


def open_file():
    filepath = filedialog.askopenfilename(title='Выбор файла загрузки', filetypes=(
        ('csv файлы', '*.csv'), ('txt файлы', '*.txt'),))  # ('Все файлы', '*.*')))
    logger(f'Загрузка файла: {filepath}')
    if filepath != "":
        try:
            data = pd.read_csv(filepath, sep=",", encoding='ANSI',
                               names=['key1', 'key2', 'key3', 'key4', 'key5', 'key6', 'key7', 'key8', 'key9', 'key10',
                                      'key11', 'key12', 'key13', 'key14', 'key15', 'key16'])

        except ValueError:
            showerror(title="Ошибка", message="Сообщение об ошибке")
            return None
        except FileNotFoundError:
            showerror(title='Ошибка', message='Файл не найден')
            return None

        # logger(filepath)
        # text_label.config(text=filepath)
        clear_data()
        combobox.set('')
        combobox.configure(values='', state='enabled')
        list_sec = []

        df = pd.DataFrame(data)
        df = df.drop(columns=['key4', 'key7', 'key10', 'key11', 'key12', 'key13', 'key14', 'key15'])

        df_row = df.to_numpy().tolist()
        # print(df_row)

        for row in df_row:
            # print(row[2])
            if row[7] == 'B':
                row[7] = 'Покупка'

            elif row[7] == 'S':
                row[7] = 'Продажа'

            else:
                row[7] = '-------'
                str_log = f'Что-то пошло не так, не могу индексировать направление сделки номер {row[0]}'
                logger(str_log)

            list_sec.append(row[2])
            tree.insert("", END, values=row)

        # удаляем повторы
        r = [a[0] for a in itertools.groupby(sorted(list_sec))]
        # print(sorted(r))

        combobox.configure(values=r)
        return None


# создаем блок для загруки данных из файла
frame1 = ttk.LabelFrame(text='Таблица обезличенных сделок', width=1000, height=800)
frame1.grid(column=0, row=0, padx=5, ipady=200, ipadx=220)

# создаем блок для управления
frame2 = ttk.LabelFrame(text='2', width=300, height=200)
frame2.grid(column=1, row=0, sticky=N, padx=10, ipady=50, ipadx=45)
# таблица для анализа
frame4 = ttk.LabelFrame(text='Расчёт',width=450,height=250)
frame4.grid(column=1,row=0,padx=0,pady=0,ipady=100, ipadx=190,sticky=S)

frame3 = ttk.LabelFrame(text='log frame', width=300, height=200)
frame3.grid(column=0, row=1, padx=5, sticky=W, ipadx=3, columnspan=3)

listbox1 = Listbox(frame3, width=180)
listbox1.pack(side='left')

label1 = ttk.Label(frame2, text='Выборка по инструменту:')
label1.grid(column=0, row=1)

label2 = ttk.Label(frame2, text='Выыбран инструмент - ')
label2.grid(column=0, row=2)

labe3 = ttk.Label(frame2, text='')
labe3.grid(column=1, row=2)


def combochoice(event):
    # получаем выделенный элемент
    selection = combobox.get()
    # print(selection)
    # label3["text"] = f"вы выбрали: {selection}"
    labe3.configure(text=selection)
    tree_filter(selection)
    test(selection)


def tree_filter(index):
    new_list = []
    for k in tree.get_children(""):
        if tree.set(k, 2) == index:
            row = tree.item(k)
            new_list.append(row['values'])

    clear_data()
    # print(df3)
    #print(df)
    # print(len(df[1]) - len(df[1].drop_duplicates()))
    combobox.configure(state=DISABLED)
    # count = 1
    # temp_row = ''
    for row in new_list:
        #     if temp_row != '':
        #         if row[1] == temp_row:
        #             count += 1
        #             print(f'{temp_row}- {count}')
        #         else:
        #             count = 1
        #             print(f'{temp_row}')
        #     temp_row = row[1]
        tree.insert("", END, values=row)


combobox = ttk.Combobox(frame2, values='', state='readonly')
combobox.grid(column=1, row=1)
combobox.bind("<<ComboboxSelected>>", combochoice)

open_button = ttk.Button(frame2, text="Открыть файл", command=open_file)
open_button.grid(column=0, row=0)

def analis():
    new_list = []
    for k in tree.get_children(""):
        row = tree.item(k)
        new_list.append(row['values'])


    df = pd.DataFrame(new_list, columns=['key1', 'key2', 'key3', 'key4', 'key5', 'key6', 'key7', 'key8'])
    # print(df)
    # subset1 = ['key1', 'key2', 'key3', 'key4', 'key5']
    subset2 = ['key2', 'key3', 'key4', 'key8']
    que = df.duplicated(subset=subset2, keep=False)
    #df1 = df[que].groupby(subset2)['key6'].sum()
    # df2 = df[~que].groupby(subset2)['key6'].sum()
    df1 = df.groupby(subset2)['key6'].sum().reset_index()
    print(df1)

    #print(df1)
    df_row = df1.to_numpy().tolist()

    for row in df1:
        #print(row)
        #     if temp_row != '':
        #         if row[1] == temp_row:
        #             count += 1
        #             print(f'{temp_row}- {count}')
        #         else:
        #             count = 1
        #             print(f'{temp_row}')
        #     temp_row = row[1]
        tree2.insert("", END, values=row)

def test(index):
    pass
    # for k in tree.get_children(""):
    #     if tree.set(k, 2) == index:
    #         print(tree.set(k, 2))


btn = ttk.Button(frame2, text='test', command=analis)
btn.grid(column=1, row=0)

text_label = ttk.Label(text="")
text_label.grid(column=1, row=0, sticky=W, padx=10, columnspan=50)

# определяем столбцы
columns = ('key1', 'key2', 'key3', 'key4', 'key5', 'key6', 'key7', 'key8',  )

tree = ttk.Treeview(frame1, columns=columns, show="headings")
tree.place(relheight=1, relwidth=1)

treescrolly = ttk.Scrollbar(frame1, orient="vertical", command=tree.yview)
treescrollx = ttk.Scrollbar(frame1, orient='horizontal', command=tree.xview)
tree.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set)
treescrolly.pack(side='right', fill='y')
treescrollx.pack(side='bottom', fill='x')

# определяем заголовки
tree.heading("key1", text="Номер операции", anchor=W)
tree.heading("key2", text="Время ", anchor=W)
tree.heading("key3", text="Инструмент", anchor=W)
tree.heading("key4", text="Тикер")
tree.heading("key5", text="Цена")
tree.heading("key6", text="Кол-во")
tree.heading("key7", text="Объём")
tree.heading("key8", text="Направление")


# настраиваем столбцы
tree.column("#1", stretch=NO, width=110)
tree.column("#2", stretch=NO, width=60)
tree.column("#3", stretch=NO, width=100)
tree.column("#4", stretch=NO, width=60)
tree.column("#5", stretch=NO, width=60)
tree.column("#6", stretch=NO, width=60)
tree.column("#7", stretch=NO, width=60)
tree.column("#8", stretch=NO, width=100)

# определяем столбцы для таблицы 2
columns2 = ('key1', 'key2', 'key3', 'key4', 'key5', )

tree2 = ttk.Treeview(frame4, columns=columns2, show="headings")
tree2.place(relheight=1, relwidth=1)

treescrolly2 = ttk.Scrollbar(frame4, orient="vertical", command=tree2.yview)
treescrollx2 = ttk.Scrollbar(frame4, orient='horizontal', command=tree2.xview)
tree2.configure(xscrollcommand=treescrollx2.set, yscrollcommand=treescrolly2.set)
treescrolly2.pack(side='right', fill='y')
treescrollx2.pack(side='bottom', fill='x')

# определяем заголовки
tree2.heading("key1", text="Время", anchor=W)
tree2.heading("key2", text="Инструмент ", anchor=W)
tree2.heading("key3", text="Тикер", anchor=W)
tree2.heading("key4", text="Направление")
tree2.heading("key5", text="Кол-во")

# настраиваем столбцы
tree2.column("#1", stretch=NO, width=110)
tree2.column("#2", stretch=NO, width=60)
tree2.column("#3", stretch=NO, width=100)
tree2.column("#4", stretch=NO, width=60)
tree2.column("#5", stretch=NO, width=60)


# ysb = ttk.Scrollbar(orient=tkinter.VERTICAL, command=tree.yview)


# # добавляем вертикальную прокрутку
# scrollbar = ttk.Scrollbar(orient=VERTICAL, command=tree.yview)
# tree.configure(yscroll=scrollbar.set)
# scrollbar.grid(row=0, column=1, sticky="ns")

# удаляем данные в таблице
def clear_data():
    tree.delete(*tree.get_children())
    # combobox.set('')
    # combobox.configure(values='')
def exit():
    choice = askyesno(title="Выход", message="Хотите закрыть приложение?")
    if choice:
        root.destroy()
root.protocol("WM_DELETE_WINDOW", exit)
root.mainloop()
