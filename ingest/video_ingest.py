import os
from pytube import YouTube
import cv2
import tempfile

def process_youtube_video(youtube_url):
    yt = YouTube(youtube_url)
    stream = yt.streams.filter(file_extension="mp4").first()
    temp_video = tempfile.mktemp(suffix=".mp4")
    stream.download(filename=temp_video)
    # Extract frames every X seconds
    video_id = yt.video_id
    out_dir = f"data/samples/{video_id}/frames"
    os.makedirs(out_dir, exist_ok=True)
    vidcap = cv2.VideoCapture(temp_video)
    fps = int(vidcap.get(cv2.CAP_PROP_FPS))
    count = 0
    sec = 0
    while True:
        vidcap.set(cv2.CAP_PROP_POS_MSEC, sec*1000)
        success, image = vidcap.read()
        if not success:
            break
        cv2.imwrite(f"{out_dir}/frame{count:04d}.jpg", image)
        sec += 2  # 1 frame every 2 seconds
        count += 1
    # TODO: Extract transcript using YouTube API or STT
    # Save all frame paths and transcript to database
    return video_id
