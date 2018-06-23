from tkinter import *
from tkinter import filedialog as fd
from pytube import YouTube
import tkinter.messagebox



def openDirectoryLocation():
    global filePath
    filename = fd.askdirectory()
    filePath=filename
    openDirectoryLocation.location=filename
    print(filename)
    changeLabel()


def downloadStart():
    print("Link is "+entry.get() +" and File Path is "+filePath+" and "+openDirectoryLocation.location)
    download(entry.get(),filePath)
    entry.delete(0,'end')


def download(link,path):
    you = YouTube(link)
    print("Downloading ...."+you.title+" Started ")
    try:
        mp4files = you.streams.filter(progressive=True, file_extension='mp4').order_by(
            'resolution').desc().first().download(path)
        tkinter.messagebox.showinfo("status","Sucessfully Downloaded "+you.title)
    except Exception as e:
        print(e)
        tkinter.messagebox.showinfo("status", "Error Occured while downloading "+you.title)

def changeLabel():
    fileLabel.update()
    fileLabel.configure(text=filePath)

def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func


root=Tk()



fileLocationLabel=Label(root,text="Select File Path")
fileLocationLabel.grid(row=0)
fileLocationButton=Button(root,text="File Path",command=combine_funcs(openDirectoryLocation,changeLabel))
fileLocationButton.grid(row=0,column=1)

linkLabel=Label(root,text="Youtube Link ")
linkLabel.grid(row=1)
entry=Entry(root,width=20)
entry.grid(row=1,column=1)
downloadButton=Button(root,text="download",command=downloadStart)
downloadButton.grid(row=1,column=2)

fileLabel=Label(root,text="current path")
fileLabel.grid(row=0,column=2)


root.mainloop()
