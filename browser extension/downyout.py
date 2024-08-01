from flask import Flask, request, jsonify
from pytube import YouTube
import threading

app = Flask(__name__)

def download_video(url):
    try:
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution()
        # Specify your download path or it will download to the current directory
        video.download()
        return True
    except Exception as e:
        print(f"Error downloading the video: {e}")
        return False

@app.route('/download', methods=['POST'])
def download():
    content = request.json
    url = content['url']
    # Run the download in a separate thread to prevent blocking
    threading.Thread(target=download_video, args=(url,)).start()
    return jsonify({"message": "Download started"}), 202

if __name__ == '__main__':
    app.run(debug=True, port=5000)

