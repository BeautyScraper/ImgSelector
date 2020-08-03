#!/usr/bin/env python

"""
"""

import os, sys
import tkinter
import re
import random
from locale import currency

from PIL import ImageTk, Image


def isComplete(imgPath):
    try:
        d = Image.open(imgPath)
        if not d.verify():
            return True
    except:
        print("problem")
        return False


def maintainAspectFillWindow(currentImage, height, width):
    imageOldHeight = currentImage.size[1]
    imageOldWidth = currentImage.size[0]
    # print(width)
    imageRatio = (imageOldHeight) / (imageOldWidth)
    windowRatio = (height / (width))
    if imageRatio > windowRatio:
        imgHeight = height
        imgWidth = int(imgHeight / imageRatio)
    else:
        imgWidth = int(width)
        imgHeight = int(imgWidth * imageRatio)
    return (imgWidth, imgHeight)


def clickOnButton(event, imgPath):
    print(imgPath)
    invert_op = getattr(event.widget, "title", None)
    if callable(invert_op):
        event.widget.title(imgPath.split("\\")[-1] + " uprooted")
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
    with open("R" + selected, "a+") as txtfile:
        txtfile.write(imgPath + "\n")


def Four5OnButton(event, imgPath):
    print(imgPath)
    selected = "Selected.opml"
    if len(sys.argv) > 3:
        selected = sys.argv[2]
    with open("45" + selected, "a+") as txtfile:
        txtfile.write(imgPath + "\n")


def ADOnButton(event, imgPath):
    print(imgPath)
    selected = "Selected.opml"
    if len(sys.argv) > 3:
        selected = sys.argv[2]
    with open("AD" + selected, "a+") as txtfile:
        txtfile.write(imgPath + "\n")


def previousPhoto(event, f, a):
    f[0] = f[0] - 2 * a
    print(f[0])
    button_click_exit_mainloop(event)

def HighJump(event, f, a):
    f[0] = f[0] + 10 * a
    print(f[0])
    button_click_exit_mainloop(event)


def MclickOnButton(event, imgPath):
    print(imgPath)
    selected = "Selected.opml"
    if len(sys.argv) > 3:
        selected = sys.argv[2]
    with open("M" + selected, "a+") as txtfile:
        txtfile.write(imgPath + "\n")


def button_click_exit_mainloop(event):
    event.widget.quit()  # this will cause mainloop to unblock.
    pass


def getImgList(path):
    imglist = []
    f = os.listdir(path)
    f.sort(key=lambda x: os.path.getmtime(os.path.join(path, x)))
    for files in f[::-1]:
        if len(imglist) > 1000:
            break
        # print(files)
        if re.search("(.*?\.jpe*g$)", files):
            matched = re.match("(.*?\.jpe*g$)", files)[0]
            imglist.append(matched)
        elif re.search("(.*?\.png$)", files):
            matched = re.match("(.*?\.png$)", files)[0]
            imglist.append(matched)
        else:
            continue
    return imglist


root = tkinter.Tk()
# root.bind("<Button>", button_click_exit_mainloop)
root.geometry('+%d+%d' % (100, 100))
width = int(1366 / 2)
height = 675
root.geometry('%dx%d+%d+%d' % (width, height + 20, 0, 0))
root.configure(background='white')
imgHeight = 306
imgWidth = 768
# imgHeight = height/2
# imgWidth = width/4
inDirPath = r'C:\Heaven\Haven\brothel\bhabhi aur bhabhi aur saali ne Mehtar se chudwaya sinisterBabes'
outTxtPath = "scanned.opml"

if len(sys.argv) > 1:
    inDirPath = sys.argv[1]
    if len(sys.argv) > 2:
        outTxtPath = sys.argv[2]

inDirPath = inDirPath.rstrip("\\ ") + "\\"
atATime = 2
root.title(inDirPath)
# dirlist = os.listdir(inDirPath)
dirlist = getImgList(inDirPath)
# random.shuffle(dirlist)
old_label_image = None
temp = [0]

for f in range(0, len(dirlist), atATime):
    f = temp[0]
    try:
        # print(dirlist[f])
        tkpiArray = []
        label_imageArray = []

        with open(outTxtPath, "a+") as txtfile:
            if f > 0 or len(dirlist) < 2 * atATime:
                for index in range(f - 2 * atATime, f - atATime, 1):
                    if index > 0:
                        # print("writing index %d",index)
                        txtfile.write(inDirPath + dirlist[index] + "\n")

            i = f
            maxY = 0
            pXfill = 0
            dim = [[0, 0], [width / 2, 0], [0, height / 2], [width / 2, height / 2]]

            for r in range(atATime):
                # currentImage = Image.open(inDirPath + dirlist[i])
                if not isComplete(inDirPath + dirlist[i]):
                    currentImage = Image.open(
                        r"F:\Paradise\stuff\Filtered\too hot\H090520_TulipJoshiTulipJoshi3 W4.jpg")
                else:
                    currentImage = Image.open(inDirPath + dirlist[i])
                # if currentImage.verify():
                #     print("Verifeid")
                if r == 0:
                    # print(width)
                    (imgWidth, imgHeight) = maintainAspectFillWindow(currentImage, int(height), int(width / 2))
                    dim[1][0] = imgWidth
                    dim[2][1] = imgHeight
                elif r == 1:
                    (imgWidth, imgHeight) = maintainAspectFillWindow(currentImage, int(height),
                                                                     int((width / 2) - dim[1][0] + width / 2))
                    dim[3][1] = imgHeight
                elif r == 2:
                    (imgWidth, imgHeight) = maintainAspectFillWindow(currentImage,
                                                                     int((height / 2) - dim[2][1] + height / 2),
                                                                     int(width / 2))
                    dim[3][0] = imgWidth
                else:
                    (imgWidth, imgHeight) = maintainAspectFillWindow(currentImage,
                                                                     int((height / 2) - dim[r][1] + height / 2),
                                                                     int(width - dim[r][0]))
                tkpi = ImageTk.PhotoImage(currentImage.resize((imgWidth, imgHeight), Image.ANTIALIAS))
                tkpiArray.append(tkpi)
                # print("imgH%dimgW%dX%dY%d" % (imgHeight,imgWidth,dim[r][0],dim[r][1]))
                label_image = tkinter.Button(root, image=tkpiArray[-1])

                label_image.place(x=dim[r][0], y=dim[r][1], width=imgWidth, height=imgHeight)
                # label_image.grid(row=2,column=0)
                if r == 0:
                    root.bind('<Left>', lambda e, index=inDirPath + dirlist[i]: clickOnButton(e, index))
                    root.bind('<p>', lambda e, index=inDirPath + dirlist[i]: MclickOnButton(e, index))
                    root.bind('1', lambda e, index=inDirPath + dirlist[i]: RclickOnButton(e, index))
                    root.bind('4', lambda e, index=inDirPath + dirlist[i]: Four5OnButton(e, index))
                    root.bind('<a>', lambda e, index=inDirPath + dirlist[i]: ADOnButton(e, index))
                    root.bind('<A>', lambda e, index=inDirPath + dirlist[i]: ADOnButton(e, index))
                    root.bind('<Control-Key-Left>', lambda e, index=inDirPath + dirlist[i]: ADOnButton(e, index))
                if r == 1:
                    root.bind('<Right>', lambda e, index=inDirPath + dirlist[i]: clickOnButton(e, index))
                    root.bind('<space>', lambda e, index=inDirPath + dirlist[i]: MclickOnButton(e, index))
                    root.bind('2', lambda e, index=inDirPath + dirlist[i]: RclickOnButton(e, index))
                    root.bind('5', lambda e, index=inDirPath + dirlist[i]: Four5OnButton(e, index))
                    root.bind('<d>', lambda e, index=inDirPath + dirlist[i]: ADOnButton(e, index))
                    root.bind('<D>', lambda e, index=inDirPath + dirlist[i]: ADOnButton(e, index))
                    root.bind('<Control-Key-Right>', lambda e, index=inDirPath + dirlist[i]: ADOnButton(e, index))

                label_image.bind('<Button-1>', lambda e, index=inDirPath + dirlist[i]: clickOnButton(e, index))
                label_image.bind('<Button-2>', lambda e, index=inDirPath + dirlist[i]: MclickOnButton(e, index))
                label_image.bind('<Button-3>', lambda e, index=inDirPath + dirlist[i]: RclickOnButton(e, index))
                label_imageArray.append(label_image)
                i += 1
                pXfill += imgWidth
                if maxY < imgHeight:
                    maxY = imgHeight
                # print(inDirPath + dirlist[i])
            if maxY == height:
                maxY -= 20
            continueBtn = tkinter.Button(root, text=str(f + 1) + "/" + str(len(dirlist)), bg="blue")
            continueBtn.place(x=0, y=height, width=width, height=20)
            continueBtn.bind("<Button>", button_click_exit_mainloop)
            root.bind("<Down>", button_click_exit_mainloop)
            continueBtn.bind("<Button-3>", lambda e, index=temp, a=atATime: previousPhoto(e, index, a))
            root.bind("<Up>", lambda e, index=temp, a=atATime: previousPhoto(e, index, a))
            root.bind("<Control-Key-Down>", lambda e, index=temp, a=atATime: HighJump(e, index, a))
            print("after event value is =" + str(temp[0]))
            print("value of f is" + str(f))
            root.title(dirlist[temp[0]]+"                                                           "+dirlist[temp[0]+1])
            # quitBtn = tkinter.Button(root, text="Quit", command=root.destroy)
            # quitBtn.place(x=imgWidth*2,y=3*imgHeight/2,width=imgWidth/2,height=imgHeight/2)

        if old_label_image is not None:
            old_label_image.destroy()
            # old_label_image2.destroy()
            # old_label_image3.destroy()
            # old_label_image4.destroy()
            # old_label_image5.destroy()
            # old_label_image6.destroy()

        old_label_image = label_image
        # old_label_image2 = label_image2
        # old_label_image3 = label_image3
        # old_label_image4 = label_image4
        # old_label_image5 = label_image5
        # old_label_image6 = label_image6
        root.mainloop()  # wait until user clicks the window
        width = int(root.winfo_width())
        height = int(root.winfo_height() - 20)
        temp[0] = temp[0] + atATime
        continueBtn.destroy()
        for b in label_imageArray:
            b.destroy()
    except OSError as e:

        # print(e.__str__())
        if "truncated" in e.__str__():
            f = f + 1

# root.destroy()
