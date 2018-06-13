#/usr/bin/env python2.7 -i
#-*- coding: utf-8 -*-
# PCAP FACTORY version 0.1.13 codename Kaley 
# Gorebox Networks Edition
# Licensed under GPLv2
# Copyright cbk914@riseup.net 2018

### IMPORTANT WARNING: WORK IN PROGRESS, NOT FINISHED, DON'T EXECUTE OR RUN.
### YOU ARE RESPONSIBLE FOR ANY DAMAGE PRODUCED BY THE EXECUTION OF THIS SCRIPT 
### ON ANY SYSTEM!!!

import tkMessageBox
import dpkt
import sys
import os
import scapy
import image

from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *
from tkFileDialog import *


# Variables

# External sources
CAPINFOS = "/usr/bin/capinfos"
DALTON = "/usr/local/bin/dalton"
FLOWSYNTH = "/usr/local/bin/flowsynth"
NETWORKMINER = "/opt/NetworkMiner_2-3/NetworkMiner.exe"
PCAPXRAY = "/opt/PcapXray/source/main.py"
SURICATA = "/opt/Suricata/_build/bin/blacksuricata"
TCPDUMP = "/usr/bin/tcpdump"
TCPREPLAY = "/usr/bin/tcpreplay"
WIRESHARK = "/usr/bin/wireshark"

# GUI

window = Tk()
window.title("Gorebox Networks ~ PCAP Factory")
window.geometry('800x600')
window.configure(background='black')
#imageFile = "kaley.jpg"
#window.im1 = image.open(imageFile)


# Console

console = Frame(window, height=300, width=580)
console.grid(row=1, column=8)
wid = console.winfo_id()
os.system('xterm -into %d -geometry 400x200 -sb &' % wid)

# Functions

#def OpenPCAP():
#    file_path = tkFileDialog.askopenfilename()

def openfile():
    file = filedialog.askopenfilename() 
    file

#def Openfile():
#
#    filename = askopenfilename(parent=root)
#    f = open(filename)
#    f.read()

def About():
    tkMessageBox.showinfo("You are all alone...","http://buscatelavida.com")

# Menu definition

menu = Menu(window)
filemenu = Menu(menu)
#window.config(menu=menu)
menu.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label='New')#, command=NewFile)
filemenu.add_command(label='Open...', command=openfile) 
filemenu.add_command(label='Save as...')#, command=SaveFileAs)
filemenu.add_command(label='Close')
filemenu.add_separator()
filemenu.add_command(label='Local Capture')
filemenu.add_command(label='Remote Capture')
filemenu.add_separator()
filemenu.add_command(label='Exit', command=window.quit)

editmenu = Menu(menu)
menu.add_cascade(label='Edit', menu=editmenu)
editmenu.add_command(label='Info')
editmenu.add_command(label='Replay')
editmenu.add_separator()
editmenu.add_command(label='Trim PCAP')
editmenu.add_command(label='Edit PCAP')
editmenu.add_command(label='Merge PCAP')

fuzzmenu = Menu(menu)
menu.add_cascade(label='Fuzzing', menu=fuzzmenu)
fuzzmenu.add_command(label='Wirefuzz')
fuzzmenu.add_command(label='AFL')

helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About', command=About)

window.config(menu=menu)

# Tools selector

lbl1 = Label(window, text="Tools")
lbl1.grid(column=5, row=0)
combo = Combobox(window)
combo['values'] = ("Capinfos","Dalton","Flowsynth","NetworkMiner","BlackSuricata","PcapXray","TCPdump","TCPReplay","Wireshark")
combo.current(4)
combo.grid(column=6, row=0)
#combo.get()

window.mainloop()

