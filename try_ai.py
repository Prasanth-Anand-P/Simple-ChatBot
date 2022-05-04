from tkinter import *
from tkinter import messagebox
import pyttsx3
import random
from pygame import mixer as song

song.init()
sd = pyttsx3.init()
sd.setProperty("rate",150)
sd.setProperty("volume",2.0)
voices = sd.getProperty('voices')
sd.setProperty('voice', voices[0].id)


def greetings():
    return "Hi da mapla"

def joke():
    jk=["what do you call a security gaurd in a samsung showroom? Gauridan of the galaxy",
        """What’s the best thing about Switzerland?            I don’t know, but the flag is a big plus.""",
        """Hear about the new restaurant called Karma?         There’s no menu: You get what you deserve.""",
        "I am so poor. I can't even pay attention"]
    jkc = random.randint(0,3)
    return (jk[jkc])

def songs():
    song_list=["Elangaathu veesudhey.mp3","Kadhal Valarthen.mp3","Sangetha Megam.mp3"]
    sc = random.randint(0,2)
    return (song_list[sc])


def s(q):
    txt=e.get()
    txt2=txt.lower()
    print(txt2)
    val="\nYou:\n=>\t" + txt
    t.insert(END,val)
    if txt2 in ["hi","hello","hey"]:
        print("ghhfh")
        msg=greetings()
        ai_val= "\nBot\n=>\t"+msg
        t.insert(END,ai_val)
        sd.say(msg)
        sd.runAndWait()

    elif("joke" in txt2):
        msg=joke()
        ai_val= "\nBot\n=>\t"+msg
        t.insert(END,ai_val)
        sd.say(msg)
        sd.runAndWait()

    elif(("song" in txt2) or ("sing" in txt2)):
        msg=songs()
        ai_val= "\nBot\n=>\tSong Name: "+ msg + "\n=>\tEnter 's' to stop, 'p' to pause, 'r' to resume"
        t.insert(END,ai_val)
        song.music.load(msg)
        song.music.play()

    elif(txt2=="s"):
        song.music.stop()
    elif(txt2=="p"):
        song.music.pause()
    elif(txt2=="r" ):
        song.music.unpause()
        
        
        """
        song_list=["Elangaathu veesudhey","Kadhal Valarthen.mp3","Sangetha Megam.mp3"]
        sc = random.randint(0,2)
        return (song_list[sc])
        """
        
    
    else:
        messagebox.showerror("Message","Bot Can't understand")
    e.delete(0,END)



r = Tk()
r.attributes('-fullscreen', True)
r.config(bg="#2e332f")
#r.maxsize(964,660)
#Label(r,text="",width=-1).grid(row=0,column=0)
t=Text(r,bg="#2e332f",font=("Ink Free",20),fg="white",width=100,height=23)
t.grid(row=0,column=0,columnspan=3)
#Label(r,text="").grid(row=1,column=0)
e=Entry(r,width=37,fg="black",bg="white",font=("bold",49))
e.grid(row=1,column=0)
e.focus()

Button(r,text="Send",bg="red",font=("bold",31),command=s,width=8).grid(row=1,column=1)
r.bind('<Return>', s)


r.mainloop()

