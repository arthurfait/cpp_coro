#!/usr/bin/env python3

from tkinter import *
from tkinter import ttk, messagebox
from tkinter import filedialog
from tkinter import colorchooser

from ttkthemes import ThemedTk

# root = Tk()
root = ThemedTk(theme='clam')
root.option_add('*tearOff', FALSE)

menubar = Menu(root, background='#dcdad5')
menu_file = Menu(menubar)

menubar.add_cascade(menu=menu_file, label='File')
menu_file.add_command(label='New', command=lambda: print("new"))

menu_edit = Menu(menubar)
menubar.add_cascade(menu=menu_edit, label='Edit')

menu_edit.add_command(label="Paste", command=lambda: root.focus_get().event_generate("<<Paste>>"))
menu_edit.add_command(label="Find...", command=lambda: root.event_generate("<<OpenFindDialog>>"))


menu_help = Menu(menubar, name='help')
menubar.add_cascade(menu=menu_help, label='Help')
menu_help.add_command(label="?", command=lambda: messagebox.showinfo(message="This is tk tester!"))

root['menu'] = menubar


def launchFindDialog(*args):
    messagebox.showinfo(message="I hope you find what you're looking for!")

root.bind("<<OpenFindDialog>>", launchFindDialog)


# import os
# path = "".join([os.path.dirname(os.path.abspath(__file__)), '/awthemes-10.4.0'])
# root.tk.call('lappend', 'auto_path', path)
# root.tk.call('package', 'require', 'awclearlooks')
# root.tk.call('package', 'require', 'award')


# s = ttk.Style()
# s.theme_use('clam')
# s.theme_use('awclearlooks')


root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


frame_outer = ttk.Frame(root)
frame_outer.grid(sticky=(N, S, W, E))
frame_outer['padding'] = 5
frame_outer.columnconfigure(0, weight=1)
frame_outer.rowconfigure(0, weight=1)


notebook = ttk.Notebook(frame_outer)
notebook.grid(sticky=(N, S, W, E))

# style = ttk.Style()
# style.configure('Danger.TFrame', background='red', borderwidth=5, relief='raised')


frame = ttk.Frame(notebook)

# frame.grid(sticky=(N, S, W, E))

notebook.add(frame, text='Basic')

label = ttk.Label(frame, text="sample label").grid(row=0, column=0, sticky=(W, N))

padding = 5

frame['padding'] = padding

def handlePaddingInc(*args):
    global padding
    padding = padding + 5
    frame['padding'] = padding
    button['padding'] = padding


def handlePaddingDec(*args):
    global padding
    padding = padding - 5
    frame['padding'] = padding

reliefs = ['flat', 'raised', 'sunken', 'solid', 'ridge', 'groove']
reliefs_idx = 0

relief_size = 1

def handleRelief(*args):
    global reliefs_idx
    global reliefs
    rel = reliefs[reliefs_idx]
    frame['relief'] = rel
    labelReliefTxt.set(rel)
    reliefs_idx = reliefs_idx + 1
    if reliefs_idx >= len(reliefs):
        reliefs_idx = 0

def handleReliefSize():
    global relief_size
    relief_size = relief_size + 1
    frame['borderwidth'] = relief_size
    if relief_size > 10:
        relief_size = 1


frame['borderwidth'] = relief_size
frame['relief'] = 'sunken'

buttonPadding = ttk.Button(frame, text="padding +5", command=handlePaddingInc)
buttonPadding.grid(row=1, sticky=(N,W))

labelReliefTxt = StringVar()
labelRelief = ttk.Label(frame, textvariable=labelReliefTxt)
labelRelief.grid(row=2, sticky=(N,W))

buttonRelief = ttk.Button(frame, text="toggle relief", command=handleRelief)
buttonRelief.grid(row=3, sticky=(N,W))

buttonReliefSize = ttk.Button(frame, text="border width", command=handleReliefSize)
buttonReliefSize.grid(row=4, sticky=(N,W))

image = PhotoImage(file='alt/sample.png', height=480)
image_label = ttk.Label(frame, text='girl', compound='top')
image_label['image'] = image
image_label.grid(row=5, columnspan=2, sticky=(N,S,E,W))

def onCommand(*args):
    buttonOk['text'] = "oked"
    buttonOk.state(['pressed'])

buttonOk = ttk.Button(frame, default='active', text="Ok", command=onCommand)
buttonOk.grid(row=6, sticky=(N,W))
root.bind('<Return>', lambda e: buttonOk.invoke())

measure = StringVar(value='metric')

def metricChanged(*args):
    print("system {}".format(measure.get()))

check = ttk.Checkbutton(frame, text="use metric",
        command=metricChanged, variable=measure,
        onvalue='metric', offvalue='imperial')

check.grid(row=0, column=1)

frameRatio = ttk.Frame(frame)

def setBorder(frm):
    frm['borderwidth'] = 1
    frm['relief'] = 'sunken'

setBorder(frameRatio)

frameRatio.grid(row=1, column=1)

language = StringVar()
en = ttk.Radiobutton(frameRatio, text="English", variable=language, value='en')
ru = ttk.Radiobutton(frameRatio, text="Russian", variable=language, value='ru')
fr = ttk.Radiobutton(frameRatio, text="French", variable=language, value='fr')
ua = ttk.Radiobutton(frameRatio, text="Ukrainian", variable=language, value='ua')
en.grid(row=0, sticky=W)
ru.grid(row=1, sticky=W)
fr.grid(row=2, sticky=W)
ua.grid(row=3, sticky=W)


username = StringVar(value='your name')

def clearName():
    usernameEntry.delete(0, 'end')
    usernameEntry.insert(0,'your name')

frameUserName = ttk.Frame(frame)
setBorder(frameRatio)
frameUserName.grid(row=2, column=1,sticky=(W, N))

usernameEntry = ttk.Entry(frameUserName, textvariable=username)
usernameEntry.grid(row=0, column=0, sticky=W)

usernameButton = ttk.Button(frameUserName, text='Clear', command=clearName)
usernameButton.grid(row=0, column=1, sticky=E)

usernamelabel = ttk.Label(frameUserName, text='ent')
usernamelabel.grid(row=1, column=0, sticky=W)

password = StringVar()
userpasswd = ttk.Entry(frameUserName, textvariable=password, show='*')
userpasswd.grid(row=2, column=0, sticky=E)


def addPadding(frm):
    for child in frm.winfo_children():
        child.grid_configure(padx=2, pady=3)

addPadding(frameUserName)


def user_name_changed(*args):
    usernamelabel['text'] = username.get()
username.trace_add('write', user_name_changed)


import re
def check_num(newval):
    return re.match("^[0-9]*$", newval) is not None and len(newval) < 10

# magic? == >
check_num_wrapper = (root.register(check_num), "%P")

num = StringVar()
numEntry = ttk.Entry(frame, textvariable=num, validate='key', validatecommand=check_num_wrapper)
numEntry.grid(row=3, column=1, sticky=W)


countryvar = StringVar()
country = ttk.Combobox(frame, textvariable=countryvar)

country.grid(row=4, column=1, sticky=W)

def sel(*args):
    print("args {}".format(args))

country.bind('<<ComboboxSelected>>', sel)

country['values'] = ('USA', 'Canada', 'Australia', 'C1',
        'C2',
        'C3',
        'C4',
        'C5',
        'C6',
        'C7',
        'C8',
        'C9',
        )

addPadding(frame)


frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=2)

frame.rowconfigure(0, weight=10)
frame.rowconfigure(1, weight=10)
frame.rowconfigure(2, weight=10)
frame.rowconfigure(3, weight=10)
frame.rowconfigure(4, weight=10)
frame.rowconfigure(5, weight=1)
frame.rowconfigure(6, weight=10)


def clear_all(*args):
    frame.forget()

ttk.Button(frame, text='Clear All', command=clear_all).grid(row=6, column=1)

frame_more = ttk.Frame(notebook)
notebook.add(frame_more, text="more widgets")

print(notebook.select())

notebook.select(frame_more)

print(notebook.select())



## More widgets
variants = [ "message {}".format(i) for i in range(1,1100)]
variantsVar = StringVar(value=variants)
listBox = Listbox(frame_more, height=5, listvariable=variantsVar)
listBox.grid(row=0, column=0, sticky=(N, S, W, E))

listBox['selectmode'] = 'extended'

listBoxLabelVar = StringVar()
listBoxLabel = ttk.Label(frame_more, textvariable=listBoxLabelVar)
listBoxLabel.grid(row=0, column=2, padx=5, sticky=W)

def selectedDetails(selection):
    print(selection)
    if len(selection) > 0:
        listBoxLabelVar.set(variants[selection[0]])
        text['state'] = 'normal'
        text.insert('end', variants[selection[0]] + '\n')
        text['state'] = 'disabled'


listBox.bind("<<ListboxSelect>>", lambda e: selectedDetails(listBox.curselection()))
scroll = ttk.Scrollbar(frame_more, orient=VERTICAL, command=listBox.yview)
scroll.grid(column=1, row=0, sticky=(N, S))
listBox['yscrollcommand'] = scroll.set



frame_more.columnconfigure(0, weight=2)
frame_more.columnconfigure(1, weight=0)
frame_more.columnconfigure(2, weight=1)

frame_more.rowconfigure(0, weight=2)
frame_more.rowconfigure(1, weight=1)


text = Text(frame_more, width=80, height=42)
text.grid(row=1, column=0, columnspan=2, padx=0, pady=2, sticky=(N, S, W, E))

scrollText = ttk.Scrollbar(frame_more, orient=VERTICAL, command=text.yview)
scrollText.grid(column=2, row=1, sticky=(N, S))
text['yscrollcommand'] = scrollText.set
text['state'] = 'disabled'
# addPadding(frame_more)

def on_enable_edit(*args):
    text['state'] = enableEdit.get()

context_menu = Menu(text)
enableEdit = StringVar(value='dissabled')
context_menu.add_checkbutton(label="Enable edit", onvalue='normal', offvalue='disabled', variable=enableEdit, command=on_enable_edit)
text.bind('<3>', lambda e: context_menu.post(e.x_root, e.y_root))

scalett = ttk.Scale(frame_more, orient=HORIZONTAL, length=200, from_= 0.1, to=100.0)
scalett.grid(row=4, column=0, pady=30)

scale = Scale(frame_more, orient=HORIZONTAL, length=200, from_= 0.1, to=100.0)
scale.grid(row=4, column=1)

spinbox = Spinbox(frame_more, from_= 0, to = 20)
spinbox.grid(row=5, column=0)


spinboxttk = ttk.Spinbox(frame_more, from_= 0, to = 20)
spinboxttk.grid(row=5, column=1)


progressbart = ttk.Progressbar(frame_more, length=200, mode='indeterminate')
progressbart.grid(row=6, column=0, columnspan=2, sticky=(W, E))
progressbart.start()


styleProgressbartDeterminated = ttk.Style()

styleProgressbartDeterminated.configure('TProgressbar', background='blue', darkcolor='midnight blue', lightcolor='sky blue')

progressbartDeterminated = ttk.Progressbar(frame_more, length=200, mode='determinate')
progressbartDeterminated.grid(row=7, column=0, sticky=(W, E))




progressbartInc = ttk.Button(frame_more, text="Progress", command=lambda: progressbartDeterminated.step())
progressbartInc.grid(row=7, column=1, sticky=(W, E))


## Windows
window_frame = ttk.Frame(notebook)
notebook.add(window_frame, text="win")
# notebook.select(window_frame)

def testToplevel():
    t = Toplevel(root)
    t.title("Sub win")
    # t.geometry('480x640-50+50')
    t.attributes("-alpha", 0.5)

openbtn = ttk.Button(window_frame, text="test top level", command=lambda: testToplevel())
openbtn.grid(row=0, column=1, sticky=(W, E))


def open_file(*args):
    filename = filedialog.askopenfilename()
    print(filename)

file_open_btn = ttk.Button(window_frame, text="File..", command=open_file)
file_open_btn.grid(row=1, column=1, sticky=(W, E))

def save_file(*args):
    filename = filedialog.asksaveasfilename()
    print(filename)

file_save_btn = ttk.Button(window_frame, text="Save..", command=save_file)
file_save_btn.grid(row=2, column=1, sticky=(W, E))


def choose_color(*args):
    filename = colorchooser.askcolor()
    print(filename)

choose_color_btn = ttk.Button(window_frame, text="Choose color", command=choose_color)
choose_color_btn.grid(row=3, column=1, sticky=(W, E))

def font_changed(font):
    font_lbl['font'] = font

def choose_font(*args):
    root.tk.call('tk', 'fontchooser', 'configure', '-font', 'helvetica 21', '-command', root.register(font_changed))
    root.tk.call('tk', 'fontchooser', 'show')

font_btn = ttk.Button(window_frame, text="Choose font", command=choose_font)
font_btn.grid(row=4, column=1, sticky=(W, E))


font_lbl = ttk.Label(window_frame, text='Font', font='helvetica 21')
font_lbl.grid(row=4, column=2, sticky=(W, E))





addPadding(window_frame)

frame_outer.columnconfigure(0, weight=1)
frame_outer.rowconfigure(0, weight=1)

frame_outer.columnconfigure(1, weight=1)
frame_outer.rowconfigure(1, weight=1)

# Treeview
tree_frame = ttk.Frame(notebook)
notebook.add(tree_frame, text="tree")
notebook.select(tree_frame)

tree = ttk.Treeview(tree_frame, columns=('size'))
tree.grid()

tree.insert('', 'end', 'widgets', text="tour")
tree.insert('', 0, 'gallery', text="Apps")

id = tree.insert('', 'end', text="Tutorial")
print(id)

tree.insert('widgets', 'end', text="Canvas", tags=('ttk'))
tree.insert(id, 'end', text='Tree')

tree.move('widgets', 'gallery', 'end')


tree['columns'] = ('size', 'modified', 'owner')

tree.column('size', width=100, anchor='center')
tree.heading('size', text='Size')
tree.heading('modified', text='Modified')
tree.heading('owner', text='Owner')

many = tree.insert('', 'end', text='Listbox', values=('15KB', 'Yesterday', 'mark'))

def itemClicked(*args):
    print(tree.focus())
    print(args)

tree.insert('', 'end', text='button', tags=('ttk', 'simple'))
tree.tag_configure('ttk', background='yellow')
tree.tag_bind('ttk', '<1>', itemClicked)

print(tree.set(many))

## Theme
theme_frame = ttk.Frame(notebook)
notebook.add(theme_frame, text="theme")
# notebook.select(theme_frame)

themes = root.get_themes() + ['azure', 'sun-valley']
listboxThemeVar=StringVar(value=themes)
listboxTheme = Listbox(theme_frame, height=9, listvariable=listboxThemeVar)
listboxTheme.grid(row=0, column=0, columnspan=2, sticky=W, padx=2, pady=2)
listboxThemeScroll = ttk.Scrollbar(theme_frame, orient=VERTICAL, command=listboxTheme.yview)
listboxTheme['yscrollcommand'] = listboxThemeScroll.set
listboxThemeScroll.grid(row=0, column=2, sticky=(W, S, N))

class RdbendeTheme:
    def __init__(self, **kwargs) -> None:
        self.path = kwargs.get('path')
        self.name = kwargs.get('name')
        self.loaded = False
        self.load()

    def name(self) -> str:
        return self.name

    def load(self):
        if self.loaded == False:
            root.tk.call("source", self.path)
            self.loaded = True

    def set_theme(self, theme):
        currentAzureThemeVar.set(theme)
        root.tk.call("set_theme", theme)


class Azure(RdbendeTheme):
    def __init__(self) -> None:
        super().__init__(path="alt/Azure-ttk-theme-main/azure.tcl")


class SunValley(RdbendeTheme):
    def __init__(self) -> None:
        super().__init__(path="alt/Sun-Valley-ttk-theme-master/sun-valley.tcl")

rdbende_theme: RdbendeTheme = None

def ensure_rdbende_theme(name):
    global rdbende_theme
    print(name)
    if rdbende_theme is None:
        if name == 'azure':
            print('Azure!')
            rdbende_theme = Azure()
        else:
            rdbende_theme = SunValley()
    else:
        # sanity
        if rdbende_theme.name != name:
            messagebox.showwarning("theme not compatible!")


def set_theme(selection):
    if (len(selection)) == 1:
        theme = themes[selection[0]]
        print(theme)
        if theme == 'azure' or theme == 'sun-valley':
            ensure_rdbende_theme(theme)
            rdbende_theme.set_theme(currentAzureThemeVar.get())
        else:
            root.set_theme(theme)
        currentThemeVar.set(theme)

listboxTheme.bind('<<ListboxSelect>>', lambda e: set_theme(listboxTheme.curselection()))

currentThemeLabel = ttk.Label(theme_frame, text='Current theme: ')
currentThemeLabel.grid(row=1, column=0, sticky=E, padx=2, pady=2)

style = ttk.Style(root)
currentThemeVar = StringVar(value=style.theme_use())
currentThemeValueLabel = ttk.Label(theme_frame, textvariable=currentThemeVar)
currentThemeValueLabel.grid(row=1, column=1, sticky=W, padx=2, pady=2)

azure_themes = ['light', 'dark']
listBoxAzureThemeVar = StringVar(value=azure_themes)
listBoxAzureTheme = Listbox(theme_frame, height=2, listvariable=listBoxAzureThemeVar)
listBoxAzureTheme.grid(row=0, column=3, sticky=(W, E), pady=2)

def select_azure_theme(selection):
    if len(selection) > 0:
        current_theme = currentThemeVar.get()
        print(current_theme)
        if current_theme != 'azure' and current_theme != 'sun-valley':
            ifazure = messagebox.askyesno(message="Set Azure theme?")
            theme_name = ''
            if ifazure:
                theme_name = 'azure'
            else:
                theme_name = 'sun-valley'

            ensure_rdbende_theme(theme_name)
            currentThemeVar.set(theme_name)
        rdbende_theme.set_theme(azure_themes[selection[0]])



listBoxAzureTheme.bind('<<ListboxSelect>>', lambda e: select_azure_theme(listBoxAzureTheme.curselection()))

currentAzureThemeVar = StringVar(value='dark')
currentAzureThemeValueLabel = ttk.Label(theme_frame, textvariable=currentAzureThemeVar, borderwidth=1, relief='sunken')
currentAzureThemeValueLabel.grid(row=1, column=2, sticky=W, padx=2, pady=2)



# Menubar




root.mainloop()

