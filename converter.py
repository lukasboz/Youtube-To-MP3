# importing packages 
from pytubefix import YouTube, exceptions
import os 

class EmptyFolderPathError(Exception):
    def __init__(self, message):
        super().__init__(message)

class InvalidURLError(Exception):
    def __init__(self, message):
        super().__init__(message)

class FileAlreadyExistsError(Exception):
    def __init__(self, message):
        super().__init__(message)

vidTitle = ""

def convert(urlEntered, folderPath):
    global vidTitle
    try:

        if folderPath == "":
            raise EmptyFolderPathError("Folder path is empty")

        # url input from user 
        yt = YouTube(urlEntered)
        vidTitle = yt.title
        print(vidTitle)

        # extract only audio 
        video = yt.streams.filter(only_audio=True).first() 

        # download the file 
        out_file = video.download(output_path=folderPath) 

        # save the file 
        base, ext = os.path.splitext(out_file) 
        new_file = base + '.mp3'

        # check if this file exists already
        if os.path.exists(new_file):
            os.remove(new_file) #if the file already exists, remove it

        os.rename(out_file, new_file) #save the new file to downloads (essentially we overwrote the old file)

        # result of success 
        print(yt.title + " has been successfully downloaded.")

    except exceptions.RegexMatchError as err:
        raise InvalidURLError("URL is invalid")
    
def getVideoTitle(urlEntered):
    try:
        yt = YouTube(urlEntered)
        return yt.title
    except exceptions.RegexMatchError as err:
        raise InvalidURLError("URL is invalid")


