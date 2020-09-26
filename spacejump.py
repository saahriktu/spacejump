#!/usr/bin/python3
"""
Space Jump v0.3
Workspace switching GUI util
2020 (c) saahriktu
under GNU GPLv3
"""
import tkinter
import os
import sys

def gospace(event):
    """
    Go to workspace procedure
    """
    spacenum = wrkspcntr.get()
    iwsnum = int(spacenum) - 1
    os.system('/usr/bin/wmctrl -s ' + str(iwsnum))
    sys.exit()

root = tkinter.Tk()
root.title('Space Jump v0.3')
root.bind('<Return>', gospace)
ntrlbl = tkinter.Label(root, text='Workspace to jump', font=("Terminus", 28))
ntrlbl.pack()
wrkspcntr = tkinter.Entry(root, width=10, font=("Terminus", 28))
wrkspcntr.pack()
gobttn = tkinter.Button(root, text = 'Go', font=("Terminus", 28))
gobttn.pack()
gobttn.bind('<Button-1>', gospace)
wrkspcntr.focus()
root.mainloop()
