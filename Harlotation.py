import os
import sys
import pickle


def getFileMeta(fileName, path):
    with open(path + "FileUrl.pkl", "rb") as inFile:
        fileMeta = pickle.load(inFile)
        # resultUrl = fileMeta[fileName]
    # import pdb;pdb.set_trace()
    if fileName in fileMeta:
        return fileMeta[fileName]
    else:
        return ""


def writeUrls(path):
    allFiles = os.listdir(path)
    for files in allFiles:
        # print(files)
        if ".jp" in files:
            # import pdb;pdb.set_trace()
            Url = getFileMeta(files, path + "\\..\\")
            print(Url)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        # batchGen("https://www.dogfartnetwork.com/tour/sites/WatchingMyMomGoBlack/raven_hart/?p=[1,10,1,4]&#pics")
        # extractMatchingLines("D:\Developed\Automation\inHaste\quicKlip.txt", "brazzer")
        writeUrls(r"D:\Developed\Automation\GalleryDownloader\NewBabes\www.foxhq.comGallery\inKoChodo")
        pass
    else:
        # print("hell")
        # import pdb;pdb.set_trace()
        try:
            writeUrls(sys.argv[1])
        except Exception as e:
            print(e)
