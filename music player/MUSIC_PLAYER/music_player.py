from tkinter import *
from tkinter import filedialog
import os
from pygame import *
root=Tk()
root.geometry('1200x650')
root.resizable(0,0)
root.title("mp3 music player")
fleft = Frame(root, height=650, width=800,bd=10,relief=SUNKEN, bg='#cfcdcc')
fbottom=Frame(root, height=100, width=800,bg='#807878')
fbottom.place(x=10,y=550)
fleft.place(x=0,y=0)
fright=Frame(root, height=650, width=400,bd=10,relief=SUNKEN, bg="black")
fright.place(x=800,y=0)
#img=PhotoImage(file=)
#Label(fleft,image=img).place(x=0,y=0)
playlist=Listbox(root,selectmode=SINGLE,bg="#d6d3d2",fg="black",bd=10,height=35,relief=SUNKEN,width=60)
playlist.place(x=810,y=60)
Label(fright,text='Playlist...',font='helvetika 20 bold',fg='white',bg='#b0a9a7',padx=125,relief=SUNKEN,bd=5).place(x=0,y=0)

#os.chdir(r'C:\Users\A\Downloads\music')
songs=None
def play():
    cureentsong=playlist.get(ACTIVE)
    mixer.init()
    mixer.music.load(cureentsong)
    mixer.music.play()
def pase():
    mixer.music.pause()
def add():
     fn=filedialog.askdirectory()
     os.chdir(r"%s"%fn)
     songs=os.listdir()
     for s in songs:
        playlist.insert(END,s)
        

Button(fbottom,text='play',command=play,bg='white',font='Helvetika 12',padx=13).place(x=350,y=20)
Button(fbottom,text="pause",command=pase,bg='white',font='Helvetika 12').place(x=420,y=20)
Button(fbottom,text="add songs",command=add,bg='white',font='Helvetika 12').place(x=100,y=20)
root.mainloop()
