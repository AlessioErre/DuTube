
#!/usr/bin/env python3


#Import the required Libraries
### Pytube ###
from pathlib import Path
from pytube import YouTube
import shutil
import os
import sys
import warnings

### TKinter ###
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# Import tkinter and Button Widget
from tkinter import Tk
from tkinter.ttk import Button
import subprocess

link = ""
path = os.path.expanduser("~/05-Script/DuTube/progetto-gui/")

def Dutube():
   link=0
   win= Tk()
   win.geometry("750x250")
   win.title("Dutube")

   def Esci():
      win.destroy()

   def Mp3GUI():
      def get_link():
         link= entry.get()
         #cmd= subprocess.call(["python3", path + "mp3.py", link])
         cmd= subprocess.call(["php", path + "Mp3.php", link])

         chiudi_finestra()

      def combinaF(*funcs):
        def combina(*args, **kwargs):
           for f in funcs:
              f(*args, **kwargs)
        return combina


      def chiudi_finestra():
         new.destroy()


      new= Toplevel(win)
      new.geometry("750x250")
      new.title("Win2")
      Label(new, text="DuTube", font=('Helvetica 17 bold')).pack(pady=30)

      canvas = Canvas(new, width=400, height=300, relief='raised')
      canvas.pack()

      label = Label(new, text='Converti Video In MP3')
      label.config(font=('helvetica', 14))
      canvas.create_window(200, 25, window=label)

      entry = Entry(new)
      canvas.create_window(205, 100, window=entry)
      Label(new, text= "Converti", font= ('Helvetica 17 bold')).pack(pady=30)
      #Button(new, text="Converti", command=lambda: combinaF(get_link, chiudi_sessione)).place(relx=0.50,  rely=0.95, anchor=S)
      btn= Button(new, text="Converti", command=get_link).place(relx=0.50,  rely=0.95, anchor=S)

       
      label2= Label(new, text=float(link)**0.5, font=('helvetica', 10, 'bold'))
      canvas2= Canvas(new, width=400, height=300, relief='raised')
      canvas2.create_window(200, 230, window=label2)
   ###END OF DEF###





   def WavGUI():
      def get_link():
         link= entry.get()
         #cmd= subprocess.call(["python3", path + "wav.py", link])
         cmd= subprocess.call(["php", path + "Wav.php", link])

         chiudi_finestra()

      def combinaF(*funcs):
        def combina(*args, **kwargs):
           for f in funcs:
              f(*args, **kwargs)
        return combina


      def chiudi_finestra():
         new.destroy()


      new= Toplevel(win)
      new.geometry("750x250")
      new.title("Win2")
      Label(new, text="DuTube", font=('Helvetica 17 bold')).pack(pady=30)

      canvas = Canvas(new, width=400, height=300, relief='raised')
      canvas.pack()

      label = Label(new, text='Converti Video In WAV')
      label.config(font=('helvetica', 14))
      canvas.create_window(200, 25, window=label)

      entry = Entry(new)
      canvas.create_window(205, 100, window=entry)
      Label(new, text= "Converti", font= ('Helvetica 17 bold')).pack(pady=30)
      #Button(new, text="Converti", command=lambda: combinaF(get_link, chiudi_sessione)).place(relx=0.50,  rely=0.95, anchor=S)
      btn= Button(new, text="Converti", command=get_link).place(relx=0.50,  rely=0.95, anchor=S)

       
      label2= Label(new, text=float(link)**0.5, font=('helvetica', 10, 'bold'))
      canvas2= Canvas(new, width=400, height=300, relief='raised')
      canvas2.create_window(200, 230, window=label2)
   ###END OF DEF###





   def Mp4GUI():
      def get_link():
         link= entry.get()
         #cmd= subprocess.call(["python3", path + "mp4.py", link])
         cmd= subprocess.call(["php", path + "Mp4.php", link])

         chiudi_finestra()

      def combinaF(*funcs):
        def combina(*args, **kwargs):
           for f in funcs:
              f(*args, **kwargs)
        return combina


      def chiudi_finestra():
         new.destroy()


      new= Toplevel(win)
      new.geometry("750x250")
      new.title("Win2")
      Label(new, text="DuTube", font=('Helvetica 17 bold')).pack(pady=30)

      canvas = Canvas(new, width=400, height=300, relief='raised')
      canvas.pack()

      label = Label(new, text='Converti Video In MP4')
      label.config(font=('helvetica', 14))
      canvas.create_window(200, 25, window=label)

      entry = Entry(new)
      canvas.create_window(205, 100, window=entry)
      Label(new, text= "Converti", font= ('Helvetica 17 bold')).pack(pady=30)
      #Button(new, text="Converti", command=lambda: combinaF(get_link, chiudi_sessione)).place(relx=0.50,  rely=0.95, anchor=S)
      btn= Button(new, text="Converti", command=get_link).place(relx=0.50,  rely=0.95, anchor=S)

       
      label2= Label(new, text=float(link)**0.5, font=('helvetica', 10, 'bold'))
      canvas2= Canvas(new, width=400, height=300, relief='raised')
      canvas2.create_window(200, 230, window=label2)
   ### END OF DEF ###



   def OggGUI():
      def get_link():
         link= entry.get()
         #cmd= subprocess.call(["python3", path + "ogg.py", link])
         cmd= subprocess.call(["php", path + "Ogg.php", link])

         chiudi_finestra()

      def combinaF(*funcs):
        def combina(*args, **kwargs):
           for f in funcs:
              f(*args, **kwargs)
        return combina


      def chiudi_finestra():
         new.destroy()


      new= Toplevel(win)
      new.geometry("750x250")
      new.title("Win2")
      Label(new, text="DuTube", font=('Helvetica 17 bold')).pack(pady=30)

      canvas = Canvas(new, width=400, height=300, relief='raised')
      canvas.pack()

      label = Label(new, text='Converti Video In OGG')
      label.config(font=('helvetica', 14))
      canvas.create_window(200, 25, window=label)

      entry = Entry(new)
      canvas.create_window(205, 100, window=entry)
      Label(new, text= "Converti", font= ('Helvetica 17 bold')).pack(pady=30)
      #Button(new, text="Converti", command=lambda: combinaF(get_link, chiudi_sessione)).place(relx=0.50,  rely=0.95, anchor=S)
      btn= Button(new, text="Converti", command=get_link).place(relx=0.50,  rely=0.95, anchor=S)

       
      label2= Label(new, text=float(link)**0.5, font=('helvetica', 10, 'bold'))
      canvas2= Canvas(new, width=400, height=300, relief='raised')
      canvas2.create_window(200, 230, window=label2)
   ###END OF DEF###





   def MovGUI():
      def get_link():
         link= entry.get()
         #cmd= subprocess.call(["python3", path + "mov.py", link])
         cmd= subprocess.call(["php", path + "Mov.php", link])

         chiudi_finestra()

      def combinaF(*funcs):
        def combina(*args, **kwargs):
           for f in funcs:
              f(*args, **kwargs)
        return combina


      def chiudi_finestra():
         new.destroy()


      new= Toplevel(win)
      new.geometry("750x250")
      new.title("Win2")
      Label(new, text="DuTube", font=('Helvetica 17 bold')).pack(pady=30)

      canvas = Canvas(new, width=400, height=300, relief='raised')
      canvas.pack()

      label = Label(new, text='Converti Video In MOV')
      label.config(font=('helvetica', 14))
      canvas.create_window(200, 25, window=label)

      entry = Entry(new)
      canvas.create_window(205, 100, window=entry)
      Label(new, text= "Converti", font= ('Helvetica 17 bold')).pack(pady=30)
      #Button(new, text="Converti", command=lambda: combinaF(get_link, chiudi_sessione)).place(relx=0.50,  rely=0.95, anchor=S)
      btn= Button(new, text="Converti", command=get_link).place(relx=0.50,  rely=0.95, anchor=S)

       
      label2= Label(new, text=float(link)**0.5, font=('helvetica', 10, 'bold'))
      canvas2= Canvas(new, width=400, height=300, relief='raised')
      canvas2.create_window(200, 230, window=label2)
   ###END OF DEF###





   Label(win, text= "Benvenuti su DuTube", font= ('Helvetica 17 bold')).pack(pady=30)
   Button(win, text="MP3", command=Mp3GUI).place(relx=0.4,  rely=0.5, anchor=NW)
   Button(win, text="WAV", command=WavGUI).place(relx=0.4,  rely=0.6, anchor=NW)
   Button(win, text="MP4", command=Mp4GUI).place(relx=0.5,  rely=0.5, anchor=NW)
   Button(win, text="OGG", command=OggGUI).place(relx=0.5,  rely=0.6, anchor=NW)
   #Button(win, text="MOV", command=MovGUI).place(relx=0.5,  rely=0.6, anchor=NW)

   Button(win, text="ESCI", command=Esci).place(relx=0.45,  rely=0.8)
   win.mainloop()
Dutube()

