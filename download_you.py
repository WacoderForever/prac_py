import tkinter as tk
from tkinter import messagebox
from pytube import YouTube
import os

def download_video():
    video_url = url_entry.get()  # Get the url from the entry widget
    try:
        yt = YouTube(video_url)
        # You can add some logic here to choose streams or formats
        video = yt.streams.get_highest_resolution()
        #set output directory and filename
        output_dir="/home/wacoder/Downloads"
        filename=yt.title+".mp4"
        # Download the video to the current directory or a directory of your choice
        video.download(output_dir,filename)
        messagebox.showinfo("Success", "Download completed!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to download video: {e}")

# Create the main window
root = tk.Tk()
root.title("YouTube Video Downloader")

# Create a Label widget to ask for the video URL
url_label = tk.Label(root, text="Video URL:")
url_label.pack()

# Create an Entry widget to accept the Video URL
url_entry = tk.Entry(root, width=50)
url_entry.pack()

# Create a Button widget to start the download
download_button = tk.Button(root, text="Download", command=download_video)
download_button.pack()

# Start the GUI event loop
root.mainloop()
