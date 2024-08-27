# importing packages 
from pytubefix import YouTube, exceptions
import os 

successfulConversion = False

def convert(urlEntered, folderPath):
    try:
        # url input from user 
        yt = YouTube(urlEntered)

        # extract only audio 
        video = yt.streams.filter(only_audio=True).first() 

        # download the file 
        out_file = video.download(output_path=folderPath) 

        # save the file 
        base, ext = os.path.splitext(out_file) 
        new_file = base + '.mp3'
        os.rename(out_file, new_file) 

        # result of success 
        print(yt.title + " has been successfully downloaded.")

        global successfulConversion
        successfulConversion = True
    except exceptions as err:
        print("shit")

