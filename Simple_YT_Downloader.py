import customtkinter as ctk
from pytube import YouTube
import os

#Main Window
main_window = ctk.CTk()
main_window.title("YT Downloader")
main_window.geometry("511x125")

#Functionality: All of my functions
def make_directories():
    os.mkdir("./audio_download")
    os.mkdir("./video_download")

def URL_data():
        try:    
            yt = YouTube(URL_Var.get())
            URL_Info.configure(text=(yt.title))
        except:
            URL_Info.configure(text=("Invalid URL"))

def Download_Video():
        try: 
            yt = YouTube(URL_Var.get())
            video = yt.streams.get_highest_resolution()
            video.download("./video_download")
            URL_Info.configure(text=("Download Successful"))
            
        except:
            URL_Info.configure(text=("Download Unsuccessful"))
def Download_Audio():
        try: 
            yt = YouTube(URL_Var.get())
            audio_name = yt.title 
            audio_name = audio_name + ".mp3"
            audio_stream = yt.streams.filter(only_audio=True).first()
            audio_stream.download(output_path = "./audio_download", filename=audio_name)
            URL_Info.configure(text=("Download Successful"))

        except:
            URL_Info.configure(text=("Download Unsuccessful"))

#Widgets; Labels, Buttons, Textboxes
#URL Label
URLlabel = ctk.CTkLabel(master=main_window,
                               text="Insert YT URL: ",
                               width=80,
                               height=35,
                               corner_radius=5,
                               #fg_color = ("lightblue"),
                               text_color = ("white"),
                               font = ("Serif", 17)
                               )
URLlabel.grid(row=0, column =0, pady=5)

#URL BAR
URL_Var = ctk.StringVar(main_window)

URL_Insert = ctk.CTkEntry(master=main_window,
                                placeholder_text="Enter YT URL",
                                textvariable=URL_Var,
                               width=360,
                               height=35,
                               corner_radius=10,
                               font = ("Serif", 17),
                               )
URL_Insert.place(x=145, y=5)

# URL INFO Text
URL_Info = ctk.CTkLabel(master=main_window,
                               text= "",
                               width=160,
                               height=25,
                               corner_radius=5,
                               text_color = ("white"),
                               font = ("Serif", 17)
                               )
URL_Info.place(x=165, y=88)

# Check URL Button
URL_Button = ctk.CTkButton(master=main_window,
                          text = "Search URL",
                          width=160,
                          height=35,
                          font = ("Serif", 17),
                          command = URL_data
)
URL_Button.grid(row=1, column=0, padx=5, sticky = "w")

# Download Video Button
Video_Button = ctk.CTkButton(master=main_window,
                          text = "Download Video",
                          width=160,
                          height=35,
                          font = ("Serif", 17),
                          command = Download_Video
)
Video_Button.grid(row=1, column=1, padx=5, sticky = "w")

# Download Audio Button
Audio_Button = ctk.CTkButton(master=main_window,
                          text = "Download Audio",
                          width=160,
                          height=35,
                          font = ("Serif", 17),
                          command = Download_Audio
)
Audio_Button.grid(row=1, column=2, padx=5, sticky = "w")

# Make directories Button /audio_download /video_download
make_directories = ctk.CTkButton(master=main_window,
                          text = "Create Directories",
                          width=160,
                          height=35,
                          font = ("Serif", 15),
                          command = make_directories
)
make_directories.grid(row=3, column=0, pady=5)


main_window.mainloop()
