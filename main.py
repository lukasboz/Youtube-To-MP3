import customtkinter as ctk
import time
from converter import convert, InvalidURLError, EmptyFolderPathError


# variables
urlEntered = ""
folderPath = ""

def urlFieldEntered(self):
    global urlEntered
    urlEntered = urlField.get()
    urlField.delete(0, ctk.END)
    urlField.insert(0, "URL Entered.")

def fileSelectPressed():
    global folderPath

    folderPath = ctk.filedialog.askdirectory()  # Open the file explorer and get the selected folder path
    if folderPath:  # Check if a folder was selected
        print("Selected Folder:", folderPath)
    else:
        print("No folder selected")

def convertPressed():
    global urlErrorLabel
    global folderErrorLabel

    try:
        convert(urlEntered, folderPath)
    except InvalidURLError as error:
        print("invalid url error")
        urlErrorLabel.pack(padx=10, pady=(10, 10))
        root.after(3000, urlErrorLabel.pack_forget)
    except EmptyFolderPathError as error:
        print("invalid filepath error")
        folderErrorLabel.pack(padx=10, pady=(10, 10))
        root.after(3000, folderErrorLabel.pack_forget)


root = ctk.CTk()
root.geometry("750x500")
root.title("YouTube to MP3 - Lukas")

title_label = ctk.CTkLabel(root, text="Convert Your YouTube Video", font=ctk.CTkFont(size=26, weight="bold"))
title_label.pack(padx=10, pady=(40, 40))

urlField = ctk.CTkEntry(root, placeholder_text="Enter your URL", width=400)
urlField.pack(padx=20, pady=(40, 40))
urlField.bind("<Return>", urlFieldEntered)

buttonFrame = ctk.CTkFrame(root)
buttonFrame.pack(pady=20)

outputDestButton = ctk.CTkButton(buttonFrame, text="Select Output Destination", width=100, command=fileSelectPressed)
convert_button = ctk.CTkButton(buttonFrame, text="Convert", width=100, command=convertPressed)
outputDestButton.pack(side="left", padx=10, pady=20)
convert_button.pack(side="left", padx=10, pady=20)

folderErrorLabel = ctk.CTkLabel(root, text="No folder selected.", font=ctk.CTkFont(size=16, weight="bold"), text_color = "#FF0000")
urlErrorLabel = ctk.CTkLabel(root, text="Invalid URL entered.", font=ctk.CTkFont(size=16, weight="bold"), text_color = "#FF0000")


root.mainloop()