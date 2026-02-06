from pytube import YouTube

#enter youtube video url

url="https://www.youtube.com/watch?v=ur9mI623cz8"

#create youtube object with the URL

yt=YouTube(url)

#select highest resolution video

video=yt.streams.get_highest_resolution()

#set output directory and filename

output_dir="/home/wacoder/Downloads"

filename=yt.title+".mp4"

#Download the video

video.download(output_dir,filename)

print(f"Download complete: {filename}")