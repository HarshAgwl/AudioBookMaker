import os
from tkinter import *
from tkinter import ttk
import subprocess



root = Tk()    
auds = StringVar()
img_d = StringVar()

def do():
    st = ""
    st2 = ""
    st2 = auds.get()
    print(st2)

    img_path = img_d.get()
    print(img_path)
    
    arr = os.listdir(st2)
    for item in arr:
        st += ("file \'" + item + "'" + "\n")

   
    f = open("audio-input-list.txt","w")
    f.write(st)
    f.close()
    proc = subprocess.Popen('ffmpeg -r 24 -i %s -f concat -safe 0 -i audio-input-list.txt -c:v libx264 -c:a aac -strict -2 -pix_fmt yuv420p -crf 23 -r 24 -y video-from-frames.mp4 ' % img_path, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    tmp = proc.stdout.read()
    print(tmp)


    

Label(root,text="Enter audio file(s) path: ").pack()
audio_dir = ttk.Entry(root,width=40,textvariable=auds)
audio_dir.pack()
Label(root,text="Enter image file full path (with file name): ").pack()
img_dir = ttk.Entry(root,width=40,textvariable=img_d)
img_dir.pack()
gen = Button(root,text="Generate",command=do)
gen.pack()
root.mainloop()



    
