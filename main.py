# Author: Killmil Biratch
# link: https://killmiledc.github.io/htmls/Blogs/CSSQAS/20230204CSS.html
# First development date: 2023-02-04
# Python Interpreter version: 3.10

import ctypes
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

root = tk.Tk()
ctypes.windll.shcore.SetProcessDpiAwareness(1)
ScaleFactor = ctypes.windll.shcore.GetScaleFactorForDevice(0)
root.tk.call('tk', 'scaling', ScaleFactor/75)
root.withdraw()

Filepath = filedialog.askopenfilename()

suffix = '.css'
if suffix not in Filepath:
    messagebox.showinfo('Message', 'It is not a .css file!\r\nAll work is terminated.')
else:
    lines = open(Filepath).readlines()
    Fp = open(Filepath, 'w')
    for w in lines:
        Fp.write(w.replace('  ', ''))   # del 'Tab'
    Fp.close()
    lines = open(Filepath).readlines()
    Fp = open(Filepath, 'w')
    for w in lines:
        Fp.write(w.replace('    ', ''))   # del 'Tab'
    Fp.close()
    lines = open(Filepath).readlines()
    Fp = open(Filepath, 'w')
    for w in lines:
        Fp.write(w.strip('\r\n'))   # del '\r\n'
    Fp.close()
    lines = open(Filepath).readlines()
    Fp = open(Filepath, 'w')
    for w in lines:
        Fp.write(w.replace(';}', '}'))  # del ';' character at the end
    Fp.close()
    lines = open(Filepath).readlines()
    Fp = open(Filepath, 'w')
    for w in lines:
        Fp.write(w.strip('\r\n'))
    Fp.close()

    ''' This code is used to del ';' character at the end, 
    to be precise, delete the';' character of the last line of code in a code block. '''
    file = open(Filepath).read()
    Fp = open(Filepath, 'w')
    Fp.write(file.replace('{', '{\r\n'))
    Fp.close()
    file = open(Filepath).read()
    Fp = open(Filepath, 'w')
    Fp.write(file.replace(';', ';\r\n'))
    Fp.close()
    file = open(Filepath).read()
    Fp = open(Filepath, 'w')
    Fp.write(file.replace('*/', '*/\r\n'))
    Fp.close()
    file = open(Filepath).read()
    Fp = open(Filepath, 'w')
    Fp.write(file.replace('}', '\n}\r\n'))
    Fp.close()
    lines = open(Filepath).readlines()
    Fp = open(Filepath, 'w')
    for line in lines:
        if line == '\n':
            line = line.strip('\n')
        Fp.write(line)
    Fp.close()

    lines = open(Filepath).readlines()
    Fp = open(Filepath, 'w')
    for w in lines:
        Fp.write(w.lstrip())
    Fp.close()
    lines = open(Filepath).readlines()
    Fp = open(Filepath, 'w')
    for w in lines:
        Fp.write(w.rstrip(' '))
    Fp.close()

    messagebox.showinfo('Message', 'The work is done.')

# Code end
