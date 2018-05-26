#!/usr/bin/env python

"""This is a small script to demonstrate using Tk to show PIL Image objects.
The advantage of this over using Image.show() is that it will reuse the
same window, so you can show multiple images without opening a new
window for each image.

This will simply go through each file in the current directory and
try to display it. If the file is not an image then it will be skipped.
Click on the image display window to go to the next image.

Noah Spurrier 2007
"""

import os, sys
import tkinter
import re
from PIL import ImageTk, Image

def clickOnButton(event, imgPath):
    print(imgPath)
    selected = "Selected.opml"
    if len(sys.argv) > 3:
        selected = sys.argv[2]
    with open(selected, "a+") as txtfile:
        txtfile.write(imgPath + "\n")

def RclickOnButton(event, imgPath):
    print(imgPath)
    selected = "Selected.opml"
    if len(sys.argv) > 3:
        selected = sys.argv[2]
    with open("R"+ selected, "a+") as txtfile:
        txtfile.write(imgPath + "\n")

def MclickOnButton(event, imgPath):
    print(imgPath)
    selected = "Selected.opml"
    if len(sys.argv) > 3:
        selected = sys.argv[2]
    with open("M"+ selected, "a+") as txtfile:
        txtfile.write(imgPath + "\n")


def button_click_exit_mainloop (event):
    event.widget.quit() # this will cause mainloop to unblock.
    pass

def getImgList(path):
    imglist = []
    for files in os.listdir(path):

        # print(files)
        if re.search("(.*?\.jpe*g$)",files):
            matched = re.match("(.*?\.jpe*g$)",files)[0]
            imglist.append(matched)
        elif re.search("(.*?\.png$)",files):
            matched = re.match("(.*?\.png$)",files)[0]
            imglist.append(matched)
        else:
            continue
    return imglist



root = tkinter.Tk()
# root.bind("<Button>", button_click_exit_mainloop)
root.geometry('+%d+%d' % (100,100))
width = 904
height = 612
root.geometry('%dx%d' % (width, height))
imgHeight = 306
imgWidth = 226
# imgHeight = height/2
# imgWidth = width/4
inDirPath = r'C:\GalImgs\NewBabes'
outTxtPath = "scanned.opml"

if len(sys.argv) > 1:
    inDirPath = sys.argv[1]
    if len(sys.argv) > 2:
        outTxtPath = sys.argv[2]

inDirPath = inDirPath.rstrip("\\ ") + "\\"
atATime= 6
root.title(inDirPath)
# dirlist = os.listdir(inDirPath)
dirlist = getImgList(inDirPath)
old_label_image = None
for f in range(0,len(dirlist),atATime):

    try:
        # print(dirlist[f])
        with open(outTxtPath, "a+") as txtfile:
            if f > 0 or len(dirlist) < 2*atATime:
                for index in range(f-2*atATime,f-atATime,1):
                    if index > 0:
                        # print("writing index %d",index)
                        txtfile.write(inDirPath + dirlist[index] + "\n")

            i = f
            tkpi = ImageTk.PhotoImage(Image.open(inDirPath + dirlist[i]).resize((imgWidth, imgHeight ), Image.ANTIALIAS))
            label_image = tkinter.Button(root, image=tkpi)
            label_image.place(x=0,y=0,width=imgWidth,height=imgHeight)
            label_image.bind('<Button-1>', lambda e,index=inDirPath + dirlist[i]: clickOnButton(e,index))
            label_image.bind('<Button-2>', lambda e,index=inDirPath + dirlist[i]: MclickOnButton(e,index))
            label_image.bind('<Button-3>', lambda e,index=inDirPath + dirlist[i]: RclickOnButton(e,index))
            # print(inDirPath + dirlist[i])
            i = i+1
            if(i > len(dirlist)-1 ):
                i -= 1

            tkpi2 = ImageTk.PhotoImage(Image.open(inDirPath + dirlist[i]).resize((imgWidth, imgHeight ), Image.ANTIALIAS))
            label_image2 = tkinter.Button(root, image=tkpi2)
            label_image2.place(x=imgWidth,y=0,width=imgWidth,height=imgHeight)
            label_image2.bind('<Button-1>', lambda e,index=inDirPath + dirlist[i]: clickOnButton(e,index))
            label_image2.bind('<Button-2>', lambda e,index=inDirPath + dirlist[i]: MclickOnButton(e,index))
            label_image2.bind('<Button-3>', lambda e,index=inDirPath + dirlist[i]: RclickOnButton(e,index))

            # print(inDirPath + dirlist[i])
            i = i+1
            if (i > len(dirlist) - 1):
                i -= 1

            tkpi3 = ImageTk.PhotoImage(Image.open(inDirPath + dirlist[i]).resize((imgWidth, imgHeight ), Image.ANTIALIAS))
            label_image3 = tkinter.Button(root, image=tkpi3)
            label_image3.place(x=imgWidth*2,y=0,width=imgWidth,height=imgHeight)
            label_image3.bind('<Button-1>', lambda e,index=inDirPath + dirlist[i]: clickOnButton(e,index))
            label_image3.bind('<Button-2>', lambda e,index=inDirPath + dirlist[i]: MclickOnButton(e,index))
            label_image3.bind('<Button-3>', lambda e,index=inDirPath + dirlist[i]: RclickOnButton(e,index))

            # print(inDirPath + dirlist[i])
            i = i+1
            if (i > len(dirlist) - 1):
                i -= 1

            tkpi4 = ImageTk.PhotoImage(Image.open(inDirPath + dirlist[i]).resize((imgWidth, imgHeight ), Image.ANTIALIAS))
            label_image4 = tkinter.Button(root, image=tkpi4)
            label_image4.place(x=imgWidth*3,y=0,width=imgWidth,height=imgHeight)
            label_image4.bind('<Button-1>', lambda e,index=inDirPath + dirlist[i]: clickOnButton(e,index))
            label_image4.bind('<Button-2>', lambda e,index=inDirPath + dirlist[i]: MclickOnButton(e,index))
            label_image4.bind('<Button-3>', lambda e,index=inDirPath + dirlist[i]: RclickOnButton(e,index))

            # print(inDirPath + dirlist[i])
            i = i+1
            if (i > len(dirlist) - 1):
                i -= 1

            tkpi5 = ImageTk.PhotoImage(Image.open(inDirPath + dirlist[i]).resize((imgWidth, imgHeight ), Image.ANTIALIAS))
            label_image5 = tkinter.Button(root, image=tkpi5)
            label_image5.place(x=0,y=imgHeight,width=imgWidth,height=imgHeight)
            label_image5.bind('<Button-1>', lambda e,index=inDirPath + dirlist[i]: clickOnButton(e,index))
            label_image5.bind('<Button-2>', lambda e,index=inDirPath + dirlist[i]: MclickOnButton(e,index))
            label_image5.bind('<Button-3>', lambda e,index=inDirPath + dirlist[i]: RclickOnButton(e,index))

            # print(inDirPath + dirlist[i])
            i = i+1
            if (i > len(dirlist) - 1):
                i -= 1

            tkpi6 = ImageTk.PhotoImage(Image.open(inDirPath + dirlist[i]).resize((imgWidth, imgHeight ), Image.ANTIALIAS))
            label_image6 = tkinter.Button(root, image=tkpi6)
            label_image6.place(x=imgWidth,y=imgHeight,width=imgWidth,height=imgHeight)
            label_image6.bind('<Button-1>', lambda e,index=inDirPath + dirlist[i]: clickOnButton(e,index))
            label_image6.bind('<Button-2>', lambda e,index=inDirPath + dirlist[i]: MclickOnButton(e,index))
            label_image6.bind('<Button-3>', lambda e,index=inDirPath + dirlist[i]: RclickOnButton(e,index))

            # print(inDirPath + dirlist[i])
            i = i+1
            if (i > len(dirlist) - 1):
                i -= 1

                # image2 = Image.open(inDirPath + dirlist[f+1])
            # tkpi2 = ImageTk.PhotoImage(image2)
            # label_image2 = tkinter.Label(root, image=tkpi2)
            # label_image2.place(x=width/4,y=0,width=width/4,height=height/2)
            continueBtn = tkinter.Button(root,text=str(f+1)+"/"+str(len(dirlist)))
            continueBtn.place(x=imgWidth*2,y=imgHeight,width=imgWidth/2,height=imgHeight/2)
            continueBtn.bind("<Button>", button_click_exit_mainloop)
            quitBtn = tkinter.Button(root, text="Quit", command=root.destroy)
            quitBtn.place(x=imgWidth*2,y=3*imgHeight/2,width=imgWidth/2,height=imgHeight/2)




        if old_label_image is not None:
            old_label_image.destroy()
            old_label_image2.destroy()
            old_label_image3.destroy()
            old_label_image4.destroy()
            old_label_image5.destroy()
            old_label_image6.destroy()

        old_label_image = label_image
        old_label_image2 = label_image2
        old_label_image3 = label_image3
        old_label_image4 = label_image4
        old_label_image5 = label_image5
        old_label_image6 = label_image6
        root.mainloop() # wait until user clicks the window
        imgWidth = int(root.winfo_width()/4)
        imgHeight = int(root.winfo_height()/2)
    except OSError as e:

        # print(e.__str__())
        if "truncated" in e.__str__():
            f = f + 1


# root.destroy()
