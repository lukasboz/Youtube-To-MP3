import customtkinter as ctk
from converter import convert, InvalidURLError, EmptyFolderPathError, getVideoTitle

# variables and stuff
urlEntered = ""
folderPath = ""

def urlFieldEntered(self):
    try:
        global urlEntered
        global urlEnteredLabel
        global videoTitleLabel
        urlEntered = urlField.get()
        urlField.delete(0, ctk.END)
        urlEnteredLabel.pack_forget()
        videoTitleLabel.pack_forget()
        urlEnteredLabel = ctk.CTkLabel(videoInfoFrame, text="URL Entered: " + urlEntered, font=ctk.CTkFont(size=16, weight="bold"), text_color="#FFFFFF")
        videoTitleLabel = ctk.CTkLabel(videoInfoFrame, text="Video Title: " + getVideoTitle(urlEntered), font=ctk.CTkFont(size=16, weight="bold"), text_color="#FFFFFF")
    except InvalidURLError as error:
        print("invalid url error")
        messageLabel.configure(text="Invalid URL given.", text_color="#FF0000")
        messageLabel.pack(padx=10, pady=(10, 10))
        root.after(3000, messageLabel.pack_forget)
    finally:
        urlEnteredLabel.pack(padx=10, pady=(10, 10))
        videoTitleLabel.pack(padx=10, pady=(10, 10))
    

def fileSelectPressed():
    global folderPath

    folderPath = ctk.filedialog.askdirectory()  # Open the file explorer and get the selected folder path
    if folderPath:  # Check if a folder was selected
        print("Selected Folder:", folderPath)
    else:
        print("No folder selected")

def convertPressed():
    try:
        convert(urlEntered, folderPath)
    except InvalidURLError as error:
        print("invalid url error")
        messageLabel.configure(text="Invalid URL given.", text_color="#FF0000")
        messageLabel.pack(padx=10, pady=(10, 10))
        root.after(3000, messageLabel.pack_forget)
    except EmptyFolderPathError as error:
        print("invalid filepath error")
        messageLabel.configure(text="No folder selected.", text_color="#FF0000")
        messageLabel.pack(padx=10, pady=(10, 10))
        root.after(3000, messageLabel.pack_forget)
    else:
        print("successful conversion")
        messageLabel.configure(text="Conversion successful! Check your output folder for your file.", text_color="#00FF00")
        messageLabel.pack(padx=10, pady=(10, 10))
        root.after(3000, messageLabel.pack_forget)


root = ctk.CTk()
root.geometry("800x600")
root.title("YouTube to MP3 - Lukas")

title_label = ctk.CTkLabel(root, text="Convert Your YouTube Video", font=ctk.CTkFont(size=26, weight="bold"))
title_label.pack(padx=10, pady=(40, 40))

urlField = ctk.CTkEntry(root, placeholder_text="Enter your URL", width=400)
urlField.pack(padx=20, pady=(40, 40))
urlField.bind("<Return>", urlFieldEntered)

videoInfoFrame = ctk.CTkFrame(root)
videoInfoFrame.pack(pady=20)

urlEnteredLabel = ctk.CTkLabel(videoInfoFrame, text="URL Entered: (empty)", font=ctk.CTkFont(size=16, weight="bold"))
urlEnteredLabel.pack(padx=10, pady=(10, 10))
videoTitleLabel = ctk.CTkLabel(videoInfoFrame, text="Video Title: (empty)", font=ctk.CTkFont(size=16, weight="bold"))
videoTitleLabel.pack(padx=10, pady=(10, 10))

buttonFrame = ctk.CTkFrame(root)
buttonFrame.pack(pady=20)

outputDestButton = ctk.CTkButton(buttonFrame, text="Select Output Destination", width=100, command=fileSelectPressed)
convert_button = ctk.CTkButton(buttonFrame, text="Convert", width=100, command=convertPressed)
outputDestButton.pack(side="left", padx=10, pady=20)
convert_button.pack(side="left", padx=10, pady=20)

messageLabel = ctk.CTkLabel(root, font=ctk.CTkFont(size=16, weight="bold"))


root.mainloop()