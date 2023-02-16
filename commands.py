import pickle
import time

def write():
    text = input(" admin/textedit > ")
    print("Saved file as text.txt")
    pickle.dump(text, open("text.txt","wb"))

def opentext():
    text = input(" admin/texteditor.gos > ")
    try:
        print(" opening file..")
        fromfile = pickle.load(open("text.txt", "rb"))
        print(fromfile)
    except FileNotFoundError:
        print("file doesnt exist")

def clock():
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print("Current time is " + current_time)

def help():
    print("""All system commands:
    write : makes a new .txt file (dont edit the file outside the os or it will go boom boom and commit kernel wallshart)
    opentext : open text.txt
    clock : shows current time
    shutdown : closes this commandline""")

def shutdown():
    print("Shutting down...")
    quit()