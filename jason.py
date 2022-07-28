import tkinter as tk
from tkinter import *
import pandas as pd
# THEME LIBRARY
import ttkbootstrap as ttk
from ttkbootstrap import ( Button, Entry, Labelframe, Progressbar )
from ttkbootstrap.constants import *
import tkinter.filedialog as fd
import os

# ---------- FUNCTIONS -------------

perc_done = int()
glossary_length = int()

class jason:
    def __init__(self, file):
        txt_in = ""
        self.frame = pd.read_csv(file).set_index('Property')
        new_keys = []
        frame_dict = self.frame.to_dict()['Value']
        for key in frame_dict:
            new_key = "{{"+key+"}}"
            new_keys.append(new_key)
            global glossary_length
            glossary_length = glossary_length + 1
            # SANITY CHECK
            print("Added:",new_key)
        print("Glossary Length:",glossary_length)
        self.glossary = dict(zip(new_keys, list(frame_dict.values())))
        self.input = txt_in
        self.save_path = str()

    def reference(self):
        return self.frame
    
    def get(self,prop):
        return self.glossary[prop]

    def save(self,txt):
        self.input = txt
        return print('Updated Input')

    def txt(self):
        return print(self.input)

    def parse(self):
        self.out = ""+self.input
        current = 0
        for k,v in self.glossary.items():
            current = current + 1
            perc_done = current / self.frame.shape[0] * 100
            self.out = str(self.out).replace(str(k),str(v))
            progress['value'] = perc_done
            print("Percent Done: "+str(perc_done)+"%")
        # WORKING return self.out
        self.save_path = out_path+".j"
        f = open(self.save_path, 'w')
        f.write(self.out)

def select_csv():
    filetypes = (
        ('CSV', '*.csv'),
    )
    path = fd.askopenfilename(
        title='Open a file',
        initialdir='.',
        filetypes=filetypes)
    global j
    try:
        j = jason(path)
    except:
        return
    csv_path.set(path)
    if j.glossary.items():
        btn_input.configure(state="enabled")

def select_input():
    filetypes = (
        ('All Files', '*.*'),
    )
    global out_path
    out_path = fd.askopenfilename(
        title='Open a file',
        initialdir='.',
        filetypes=filetypes)
    content = open(out_path, 'r').read()
    j.save(content)
    input_path.set(out_path)
    if j.input:
        btn_run.configure(state="enabled")
    
def run():
    print(j.parse())

# ----------------------------------

window = ttk.Window(themename="darkly")
window.geometry("350x375")
window.title('JASON')
window.resizable(False, False)
colors = window.style.colors

# COLUMNS
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
# ROWS
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)
window.rowconfigure(2, weight=70)
window.rowconfigure(3, weight=1)
window.rowconfigure(4, weight=1)

input_path= tk.StringVar()
csv_path= tk.StringVar()

# WIDGETS
btn_csv = Button (window, bootstyle="success", text="Open CSV", command=select_csv)
path_csv = Entry (window, textvariable=csv_path, state="disabled")
btn_input = Button (window, bootstyle="success", text="Open Input", state="disabled", command=select_input)

path_input = Entry (window, textvariable=input_path, state="disabled")
logo = Label (text="JASON")
about_box = Labelframe (window, bootstyle="success", labelwidget=logo)
about_txt = Label (about_box, padx=5, pady=5,
text="""A tiny python utility for bulk find and 
replace in text files of all types.
Requires: CSV with columns [ Property, Value ]

Use {{Double Curly}} bindings to refer to your 
properties that you want JASON to replace with
the corresponding value.

Output will retain the same name with a .j before 
the extension.
""")
about_txt.place(x=0,y=0)
btn_run = Button (window, bootstyle="success", text="Run", state="disabled", command=run)
progress = Progressbar (bootstyle="success", mode="determinate", variable=perc_done)

# GRID
btn_csv.grid(row=0, column=0, padx=5, pady=5, sticky='WENS')
path_csv.grid(row=0, column=1, padx=5, pady=5, columnspan=2, sticky='WENS')

btn_input.grid(row=1, column=0, padx=5, pady=5, sticky='WENS')
path_input.grid(row=1, column=1, padx=5, pady=5, sticky='WENS')

about_box.grid(row=2, column=0, columnspan=2, padx=5, pady=10, sticky='WENS')

btn_run.grid(row=3, column=0, columnspan=2, sticky='WENS')
progress.grid(row=4, column=0, columnspan=2, sticky='WENS')

window.mainloop()