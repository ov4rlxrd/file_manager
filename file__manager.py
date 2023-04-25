import os
import shutil
from tkinter import *




window = Tk()
window.title('File Manager')
window.geometry('700x650')

def clicked():
    path = txt.get()
    path = path.replace('\\','/')
    files_dir = os.listdir(f'{path}/')
    print(files_dir)
    only_files = []
    for i in files_dir:
        if os.path.isfile(path+i):
            only_files.append(i)
    print(only_files)

    file_ext = {
        'pdf':'PDFs',
        'jpg':'Images',
        'png':'Images',
        'docx':'Docs',
        'DOCX':'Docs',
        'txt':'Text',
        'doc':'Docs',
        'xlsx':'Excel',
        'zip':'Archives',
        'ini':'Other',
        'exe':'EXE',
        'url':'Other',
        'lnk':'Other',
        'lsx':'Excel',
        'rar':'Archives',
        'odp':'Other',
        'ptx':'Presentation'
    }
    for file in only_files:
        # if os.path.exists(f'{path}/{}')
        if file[-4:] == 'DOCX' or file[-4:] == 'docx':
            if os.path.exists(f'{path}/{file_ext[file[-4:]]}'):
                shutil.move(f'{path}/{file}', f'{path}/{file_ext[file[-4:]]}/{file}')
            else:
                os.mkdir(f'{path}/{file_ext[file[-4:]]}')

        else:
            if os.path.exists(f'{path}/{file_ext[file[-3:].lower()]}'):
                shutil.move(f'{path}/{file.lower()}', f'{path}/{file_ext[file[-3:].lower()]}/{file.lower()}')
            else:
                os.mkdir(f'{path}/{file_ext[file[-3:].lower()]}')
                shutil.move(f'{path}/{file.lower()}', f'{path}/{file_ext[file[-3:].lower()]}/{file.lower()}')
        print(file[-4:])


lbl = Label(window, text="Введите абсолютный(полный) адрес той папки, где вам нужно распределить файлы\n, и нажмите кнопку распределения",font=("Arial Bold", 12))
lbl.pack(pady=50)
txt = Entry(window,width=10)
txt.pack(anchor='n',fill=X, padx=[140,140],pady=100)
btn = Button(window, text="Распределить!",command=clicked)
btn.pack()



window.mainloop()