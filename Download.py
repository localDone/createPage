import tkinter as tk

try:
    from pytube import YouTube
except Exception as e:
    print(e)

root = tk.Tk()
apps = []

debugmode = False

labelY = 110
labelX = 120


# Downloads the highest resolution video that has sound in it
def download_video():
    url = myEntry.get()

    if len(url) > 0:

        #adds label with link to download
        myLabel = tk.Label(root, text=url)
        myLabel.place(x=120, y=40)
        myLabel.place
        print(url)

        try:
            # prepares and prints available resolutions of video
            ytd = YouTube(url)
            print(ytd.streams.filter(adaptive=True).all)
            print(YouTube(url).streams.filter(resolution='360p').first())
            print(YouTube(url).streams.filter(resolution='480p').first())
            print(YouTube(url).streams.filter(resolution='720p').first())
            print(YouTube(url).streams.filter(resolution='1080p').first())
            # ytd = YouTube(url).streams.first().download('.\\test')

            # ytd = YouTube(url).streams.filter(resolution='480p').first().download('.\\test')

            highest_res = str(YouTube(url).streams.filter(resolution='1080p').first())
            high_res = str(YouTube(url).streams.filter(resolution='720p').first())
            medium_res = str(YouTube(url).streams.filter(resolution='480p').first())
            low_res = str(YouTube(url).streams.filter(resolution='360p').first())

            # Filters the video to get the best resolution available that has sound
            if 'None' not in highest_res and 'acodec' in highest_res:
                print("Downloading video at res of 1080p.")
                ytd = YouTube(url).streams.filter(resolution='1080p').first().download('.\\test')
            elif 'None' not in high_res and 'acodec' in high_res:
                print("Downloading video at res of 720p.")
                ytd = YouTube(url).streams.filter(resolution='720p').first().download('.\\test')
            elif 'None' not in medium_res and 'acodec' in medium_res:
                print("Downloading video at res of 480p.")
                ytd = YouTube(url).streams.filter(resolution='480p').first().download('.\\test')
            elif 'None' not in low_res and 'acodec' in low_res:
                print("Downloading video at res of 360p.")
                ytd = YouTube(url).streams.filter(resolution='360p').first().download('.\\test')
            else:
                print("Something went wrong when trying to find resolutions to download.")

            # Prints file destiny
            print(ytd)

        except Exception as e:
            print(e)
    else:
        myLabel = tk.Label(root, text="URL is empty, try again please.")
        myLabel.place(x=120, y=40)
        myLabel.place


# Only checks available resolutions
def check_resolutions():
    url = myEntry.get()

    if len(url) > 0:

        # Creates label with video link
        myLabel = tk.Label(root, text=url)
        myLabel.place(x=120, y=40)
        myLabel.place
        print(url)

        try:

            # Adds label
            check_label1 = tk.Label(root, text=str(YouTube(url).streams.filter(resolution='360p').first()))
            check_label2 = tk.Label(root, text=str(YouTube(url).streams.filter(resolution='480p').first()))
            check_label3 = tk.Label(root, text=str(YouTube(url).streams.filter(resolution='720p').first()))
            check_label4 = tk.Label(root, text=str(YouTube(url).streams.filter(resolution='1080p').first()))
            check_label1.place(x=120, y=130)
            check_label2.place(x=120, y=150)
            check_label3.place(x=120, y=170)
            check_label4.place(x=120, y=190)

        except Exception as e:
            print(e)
    else:
        myLabel = tk.Label(root, text="URL is empty, try again please.")
        myLabel.place(x=120, y=40)
        myLabel.place


def moveLabelDown():
    global labelY
    global labelX
    labelY += 10
    print(labelY)
    try:
        # Adds label
        change_label1 = tk.Label(root, text=str("w:{0} h:{1}".format(labelX, labelY)))
        change_label1.place(x=labelX, y=labelY)

    except Exception as e:
        print(e)


def moveLabelRight():
    global labelX
    global labelY
    labelX += 10
    print(labelX)
    try:
        # Adds label
        change_label1 = tk.Label(root, text=str("w:{0} h:{1}".format(labelX, labelY)))
        change_label1.place(x=labelX, y=labelY)

    except Exception as e:
        print(e)


def moveLabelUp():
    global labelY
    global labelX
    labelY -= 10
    print(labelY)
    try:
        # Adds label
        change_label1 = tk.Label(root, text=str("w:{0} h:{1}".format(labelX, labelY)))
        change_label1.place(x=labelX, y=labelY)

    except Exception as e:
        print(e)


def moveLabelLeft():
    global labelX
    global labelY
    labelX -= 10
    print(labelX)
    try:
        # Adds label
        change_label1 = tk.Label(root, text=str("w:{0} h:{1}".format(labelX, labelY)))
        change_label1.place(x=labelX, y=labelY)

    except Exception as e:
        print(e)


# Adds title to program
root.title('{-<DownLoad>-}')

# Creates canvas
canvas = tk.Canvas(root, height=250, width=700, bg="#263D42")
canvas.pack()

myEntry = tk.Entry(root, width=50)
myEntry.pack()

# Adds Button
myButton = tk.Button(root, text="Download Now", command=download_video)
myButton.pack()

# Adds Button
myButton_Check = tk.Button(root, text="Check available resolutions", command=check_resolutions)
myButton_Check.pack()

if debugmode:
    # tests label height
    myButton_Check1 = tk.Button(root, text="moveLabelDown", command=moveLabelDown)
    myButton_Check1.pack()

    # tests label height
    myButton_Check2 = tk.Button(root, text="moveLabelRight", command=moveLabelRight)
    myButton_Check2.pack()

    # tests label height
    myButton_Check3 = tk.Button(root, text="moveLabelUp", command=moveLabelUp)
    myButton_Check3.pack()

    # tests label height
    myButton_Check4 = tk.Button(root, text="moveLabelLeft", command=moveLabelLeft)
    myButton_Check4.pack()

# Adds Blank canvas
# frame = tk.Frame(root, bg="white")
# frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

# Adds label
label1 = tk.Label(root, text="Add Video URL:")
label1.place(x=110, y=255)

root.mainloop()
