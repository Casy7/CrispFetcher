import os
from sys import platform


if platform in ("linux", "linux2", "darwin"):
    os.system('python3 -m pip install eel')
    os.system('python3 -m pip install tk')
    
elif platform == "win32":
    os.system('python -m pip install eel')
    os.system('python -m pip install tk')


from tkinter.filedialog import askopenfilename
import tkinter as tk
from tkinter import ttk
from parser.crispfetcher import *

root = tk.Tk()
root.geometry("530x140")
root.title('CrispMerge: Выберите XML-файлы')
root.resizable(0, 0)

oldFile = tk.StringVar()
newFile = tk.StringVar()
err = tk.StringVar()


def eel_init():
    root.destroy()
    eel.init("web")  
    try:
        eel.start("editor.html", mode="custom")
    except:
        try:
            eel.start("editor.html", mode="firefox")
        except:
            eel.start("editor.html", mode="chrome")
    finally:
        pass

def open_old_xml_file():
    filename = askopenfilename()
    oldFile.set(filename)    
    print(filename)

def open_new_xml_file():
    filename = askopenfilename()
    newFile.set(filename)
    print(filename)



    

def start_web_interface():
    if not os.path.exists(oldFile.get()):
        err.set("Некорректный путь к страому XML")
        return None
    if not os.path.exists(newFile.get()):
        err.set("Некорректный путь к новому XML")
        return None
    # err_set()
    err.set("Запуск веб-приложения...")
    root.update()
    old_XML_file_content = ""
    with open(oldFile.get(), "r", encoding="UTF-8") as old_XML_file:
        old_XML_file_content = old_XML_file.read()
    
    new_XML_file_content = ""
    with open(newFile.get(), "r", encoding="UTF-8") as new_XML_file:
        new_XML_file_content = new_XML_file.read()
    
    xml_file.old_XML = old_XML_file_content
    xml_file.new_XML = new_XML_file_content

    xml_file.generate()

    eel_init()


def root_show():
    
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=6)

    root.bind('<Return>', start_web_interface)

    username_label = ttk.Label(root, text="Старый XML:")
    username_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

    username_entry = ttk.Entry(root, textvariable=oldFile)
    username_entry.grid(column=1, row=0, sticky=tk.EW, padx=5, pady=5)

    open_file_button = ttk.Button(root, text="📁", command=open_old_xml_file)
    open_file_button.grid(column=2, row=0, sticky=tk.E, padx=2, pady=5)

    password_label = ttk.Label(root, text="Новый XML:")
    password_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

    password_entry = ttk.Entry(root, textvariable=newFile)
    password_entry.grid(column=1, row=1, sticky=tk.EW, padx=5, pady=5)

    open_file_button = ttk.Button(root, text="📁", command=open_new_xml_file)
    open_file_button.grid(column=2, row=1, sticky=tk.E, padx=5, pady=5)

    password_label = ttk.Label(root, textvariable=err)
    password_label.grid(column=1, row=3, sticky=tk.W, padx=5, pady=5)

    login_button = ttk.Button(root, text="Закрыть", command=exit)
    login_button.grid(column=1, row=4, sticky=tk.E, padx=30, pady=5)

    login_button = ttk.Button(root, text="Выбрать", command=start_web_interface)
    login_button.grid(column=2, row=4, sticky=tk.E, padx=5, pady=5)
    root.mainloop()


root_show()


