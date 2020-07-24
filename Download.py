import tkinter as tk
try:
    from pytube import YouTube
except Exception as e:
    print(e)

root = tk.Tk()
apps = []

def myClick():
    url = myEntry.get()

    if len(url) > 0:
        myLabel = tk.Label(root, text=url)
        myLabel.place(x=120, y=40)
        myLabel.place
        print(url)
        try:
            ytd = YouTube(url)
            print(ytd.streams.filter(adaptive=True).all)
            print("Downloading video at res of 720p.")
            ytd = YouTube(url).streams.filter(resolution='720p').first().download('.\\test')
            print(ytd)
        except Exception as e:
            print(e)
    else:
        myLabel = tk.Label(root, text="URL is empty, try again please.")
        myLabel.place(x=120, y=40)
        myLabel.place


# Adds title to program
root.title('{-<DownLoad>-}')

# Creates canvas
canvas = tk.Canvas(root, height=250, width=700, bg="#263D42")
canvas.pack()

myEntry = tk.Entry(root, width=50)
myEntry.pack()

# Adds Button
myButton = tk.Button(root, text="Download Now", command=myClick)
myButton.pack()
# Adds Blank canvas
# frame = tk.Frame(root, bg="white")
# frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

# Adds label
label1 = tk.Label(root, text="Add Video URL:")
label1.place(x=120, y=20)

root.mainloop()