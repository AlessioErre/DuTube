#!/usr/bin/env python3

from pathlib import Path
from pytube import YouTube
import shutil
import os
import sys
import warnings

path = os.path.expanduser("~/05-Script/DuTube/Downloads/")
dutube, link, formato = sys.argv

if len(sys.argv) < 2:
    yt = YouTube(link)
    yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-1].download(path)
    sys.exit()

yt = YouTube(link)
yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-1].download(path)

#os.system('ffmpeg -i *.mp4 -acodec mp3 new.mp3')

Format = os.system(formato)
print(Format)

dir = path
allfiles = os.listdir(dir)
files = [fname for fname in allfiles if fname.endswith('.mp4')]

filename = ', '.join(files)

if sys.argv[2] == 'mp3':
   sys.argv[2] = os.system('ffmpeg -i ' + path + '*.mp4 -acodec mp3 ' + path + 'new.mp3')
   tagliaExt = os.path.splitext(filename)
   file = tagliaExt[0]
   #print(file)

   dir = path
   allfiles = os.listdir(dir)
   files = [fname for fname in allfiles if fname.endswith('.mp4')]

   filename = ', '.join(files)

   tagliaExt = os.path.splitext(filename)
   file = tagliaExt[0]
   #print(file)

   shutil.copyfile(dir + "new.mp3", dir + file + '.mp3')
   os.remove(dir + 'new.mp3')
   os.remove(dir + filename)
   sys.exit()
   quit()

elif sys.argv[2] == 'wav':
   sys.argv[2] == os.system('ffmpeg -i ' + path + '*.mp4 -ac 2 -f wav ' + path + 'new.wav')
   tagliaExt = os.path.splitext(filename)
   file = tagliaExt[0]
   #print(file)

   dir = path
   allfiles = os.listdir(dir)
   files = [fname for fname in allfiles if fname.endswith('.mp4')]

   filename = ', '.join(files)

   tagliaExt = os.path.splitext(filename)
   file = tagliaExt[0]
   #print(file)

   shutil.copyfile(dir + "new.wav", dir + file + '.wav')
   os.remove(dir + 'new.wav')
   os.remove(dir + filename)
   sys.exit()
   quit()


 ####################################################################

#### VIDEO FORMAT ###

elif sys.argv[2] == 'mov':
   sys.argv[2] == os.system('ffmpeg -i ' + path + '*.mp4 -f mov ' + path + 'new.mov')
   tagliaExt = os.path.splitext(filename)
   file = tagliaExt[0]
   #print(file)

   dir = path
   allfiles = os.listdir(dir)
   files = [fname for fname in allfiles if fname.endswith('.mp4')]

   filename = ', '.join(files)

   tagliaExt = os.path.splitext(filename)
   file = tagliaExt[0]
   #print(file)

   shutil.copyfile(dir + "new.mov", dir + file + '.mov')
   os.remove(dir + 'new.mov')
   os.remove(dir + filename)
   sys.exit()
   quit()


elif sys.argv[2] == 'wmv':
   sys.argv[2] == os.system('ffmpeg -i *.mp4 -c:v wmv2 -b:v 1024k -c:a wmav2 -b:a 192k new.wmv')
   tagliaExt = os.path.splitext(filename)
   file = tagliaExt[0]
   #print(file)


   dir = path
   allfiles = os.listdir(dir)
   files = [fname for fname in allfiles if fname.endswith('.mp4')]

   filename = ', '.join(files)

   tagliaExt = os.path.splitext(filename)
   file = tagliaExt[0]
   #print(file)

   shutil.copyfile(dir + "new.wmv", dir + file + '.wmv')
   os.remove(dir + 'new.wmv')
   os.remove(dir + filename)
   sys.exit()
   quit()



else:
   sys.exit()
   quit()

