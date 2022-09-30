
import pygame #used to create video games
import tkinter as tkr #used to develop GUI
from tkinter.filedialog import askdirectory #it permit to select dir
import os #it permits to interact with the operating system
music_player = tkr.Tk() 
music_player.title("Simple Music Player") 
music_player.geometry("750x500")
directory = askdirectory()
os.chdir(directory) #it permits to chenge the current dir
song_list = os.listdir() #it returns the list of files song
play_list = tkr.Listbox(music_player, font="Calibri 14 bold", bg="yellow", selectmode=tkr.SINGLE)
for item in song_list:
    pos = 0
    play_list.insert(pos, item)
    pos += 1

pygame.init()
pygame.mixer.init()

def play():
    pygame.mixer.music.load(play_list.get(tkr.ACTIVE))
    var.set(play_list.get(tkr.ACTIVE))
    pygame.mixer.music.play()
def stop():
    pygame.mixer.music.stop()
def pause():
    pygame.mixer.music.pause()
def unpause():
    pygame.mixer.music.unpause()

Button1 = tkr.Button(music_player, width=5, height=2, font="Algerian 12 bold", text="Play", command=play, bg="orange", fg="white")
Button2 = tkr.Button(music_player, width=5, height=2, font="Algerian 12 bold", text="Stop", command=stop, bg="blue", fg="white")
Button3 = tkr.Button(music_player, width=5, height=2, font="Algerian 12 bold", text="Pause", command=pause, bg="grey", fg="white")
Button4 = tkr.Button(music_player, width=5, height=2, font="Algerian 12 bold", text="Unpause", command=unpause, bg="green", fg="white")    



var = tkr.StringVar() 
song_title = tkr.Label(music_player, font="Algerian 12 bold", textvariable=var)

song_title.pack()
Button1.pack(fill="x")
Button2.pack(fill="x")
Button3.pack(fill="x")
Button4.pack(fill="x")
play_list.pack(fill="both", expand="yes")
music_player.mainloop()
