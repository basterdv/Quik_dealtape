from tkinter import *
from tkinter import ttk
from tkinter import filedialog

root = Tk()
root.title("METANIT.COM")
root.geometry("1550x600")


def click_button():
    text_label.config(text='fsksdflkjsdjlkfkl;sfl;kjsdklf')


# root.grid_rowconfigure(index=1, weight=1)
# root.grid_columnconfigure(index=0, weight=1)
# root.grid_columnconfigure(index=1, weight=2)

frame1 = ttk.LabelFrame(text='1', width=800, height=600)
frame1.grid(column=0, row=0, padx=5, pady=5)
frame2 = ttk.LabelFrame(text='2')
frame2.grid(column=1, row=0, padx=0, pady=6, ipadx=100, ipady=20, sticky=NE)

open_button = ttk.Button(frame2, text="Открыть файл", command=click_button)
open_button.grid(row=0, column=0, padx=10, pady=10)

btn2 = ttk.Button(frame2, text='jjsdjdsjsd')
btn2.grid(column=1, row=0)

text_label = ttk.Label(text="dsfdfdfgdfgdfgdfgdfgdfgsdf")
text_label.grid(column=1, row=0, sticky=W)

# text_editor = Text()
# text_editor.grid(column=0, columnspan=2, row=0)


# открываем файл в текстовое поле
# def open_file():
#     filepath = filedialog.askopenfilename(title='Выбор файла загрузки', filetypes=(
#         ('csv файлы', '*.csv'), ('txt файлы', '*.txt'), ('Все файлы', '*.*')))
#     if filepath != "":
#         with open(filepath, "r") as file:
#             text = file.read()
#             text_editor.delete("1.0", END)
#             text_editor.insert("1.0", text)
# # сохраняем текст из текстового поля в файл
# def save_file():
#     filepath = filedialog.asksaveasfilename()
#     if filepath != "":
#         text = text_editor.get("1.0", END)
#         with open(filepath, "w") as file:
#             file.write(text)


# open_button = ttk.Button(text="Открыть файл", command=open_file)
# open_button.grid(column=0, row=1, sticky=NSEW, padx=10)
#
# save_button = ttk.Button(text="Сохранить файл", command=save_file)
# save_button.grid(column=1, row=1, sticky=NSEW, padx=10)

root.mainloop()
