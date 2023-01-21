# I Created an Automatic Folder Cleaner in Python
import os

def createIfNotExits(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)


def moveFile(foldername,files):
    for file in files:
        os.replace(file,f"{foldername}/{file}" )
    
if __name__ == "__main__":
    files = os.listdir()
    files.remove("python5.py")
    print(files)
    createIfNotExits('Images')
    createIfNotExits('video')
    createIfNotExits('Code')
    createIfNotExits('Others')

    imgExts = [".png",".jpg",".jpeg"]
    images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts]
    print(images)

    mediaExts= [".mp4",".mp3",".flv",".wmv"]
    medias = [file for file in files if os.path.splitext(file)[1].lower() in mediaExts]
    print(medias)

    docExts = [".html", ".log",".gitignore",".css",".js",".css"]
    doc = [file for file in files if os.path.splitext(file)[1].lower() in docExts]

    other =[]
    for file in files:
        ext = os.path.splitext(file)[1].lower()
        if (ext not in mediaExts) and (ext not in docExts) and (ext not in imgExts) and os.path.isfile(file):
            other.append(file)

    print(other)
    moveFile("Code", doc)
    moveFile("Image", images)
    moveFile("video", medias)
    moveFile("Others", other)